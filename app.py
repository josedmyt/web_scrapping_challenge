from flask import Flask, render_template, redirect
import pymongo

app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.mars_db
collection = db.info_scraped

@app.route("/")
def home():
    data= collection.find_one()

    return render_template("index.html", data=data)

@app.route("/scrape")
def scrape():
    import mission_to_mars
    post= mission_to_mars.scrape()
    db.info_scraped.drop()
    collection.update({},post,upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
