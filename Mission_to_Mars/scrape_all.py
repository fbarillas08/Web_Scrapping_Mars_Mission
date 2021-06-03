#!/usr/bin/env python
# coding: utf-8

# ## MISSION TO MARS
# #### by F. A. Barillas

from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os
import pymongo

# #### NASA Mars News

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=True)

url = 'https://mars.nasa.gov/news/'
browser.visit(url)

soup = BeautifulSoup(browser.html, 'html.parser')

print(soup.prettify())

slide = soup.select_one('ul.item_list li.slide')
slide

news_title = slide.find('div',class_='content_title').get_text()

news_summary = slide.find('div',class_='article_teaser_body').get_text()

# ### Find Feature Image URL

url2 = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url2)

soup = BeautifulSoup(browser.html, 'html.parser')

print(soup.prettify())

images2 = soup.select("img", class_="headerimage")
href = images2[1]['src']

featured_image_url =('https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/' + href)
featured_image_url


# ### Find Hemisphere URLs

mars_hemisphere_image_urls=[
    {"title": "Cerberus Hemisphere", "img_url":"https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url":"https://astrogeology.usgs.gov/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url":"https://astrogeology.usgs.gov/cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg"},
    {"title": "Valles Marineris Hemisphere", "img_url":"https://astrogeology.usgs.gov/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg"}
    ]

# ### Scrapping Mars Data Table

url3 = 'https://space-facts.com/mars/'
browser.visit(url3)

soup = BeautifulSoup(browser.html, 'html.parser')

print(soup.prettify())

tables = soup.select("table", class_="tablepress tablepress-id-p-mars")
mars_table = tables[0]
mars_table

# #### Mongo DB

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define Database and Collection
db = client.marsnews_db
collection = db.items

# Dictionary to be inserted as a MongoDB document
post = {
    'title': news_title,
    'summary': news_summary,
    'feature_image': featured_image_url,
    'hemispheres':mars_hemisphere_image_urls
        }

# Insert Posts into marsnews_db
collection.update({},post,upsert=True)

articles = db.items.find()


