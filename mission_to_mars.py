
def scrape():

    from splinter import Browser
    from bs4 import BeautifulSoup
    import pandas as pd
    from sqlalchemy import create_engine
    from pprint import pprint
    import time

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    title2=[]
    description=[]
    date=[]
    posting = soup.find('div', class_='image_and_description_container')
    title2.append(posting.find('div',class_='list_text').find('div',class_='content_title').text)
    description.append(posting.find('div',class_='list_text').find('div', class_='article_teaser_body').text.strip('\n'))
    date.append(posting.find('div',class_='list_text').find('div', class_='list_date').text)


    url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(1)
    browser.find_by_css('.fancybox').click()
    time.sleep(1)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    picture=soup.find('img', class_='fancybox-image')
    featured_image_url= "https://www.jpl.nasa.gov" + picture.get('src')


    url='https://twitter.com/marswxreport'
    browser.visit(url)
    time.sleep(3)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    texts= soup.find('article', class_= 'css-1dbjc4n r-1loqt21 r-16y2uox r-1wbh5a2 r-1udh08x r-1j3t67a r-o7ynqc r-6416eg')
    tweet= texts.find('div', class_='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0').find('span', class_='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0').text


    url='https://space-facts.com/mars/'
    browser.visit(url)
    time.sleep(1)
    #table=browser.find_by_id('tablepress-p-mars-no-2').value
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    table_html= str(soup.find('table', id='tablepress-p-mars-no-2'))
    #table_pd= pd.read_html(str(table_html))[0]


    url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    time.sleep(1)
    title=[]
    link=[]
    for i in range(4):
        browser.find_by_css('.thumb')[i].click()
        pic=soup.find('div','downloads' )
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')       
        pic=soup.find('div','downloads' ).find('ul').find('li').find('a')
        link.append(pic.get('href'))
        title.append(soup.find('h2', class_='title').text)
        browser.visit(url)

    browser.quit()

    final_dictionary={'article':[title2,description,date],'image_url': featured_image_url,'weather_tweet':tweet,'table_html_code':table_html,'basic_info':{"title":title,"link":link}}

    return(final_dictionary)
