#!/usr/bin/env python
# coding: utf-8

# ## MISSION TO MARS
# #### by F. A. Barillas

# In[1]:


from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os
import pymongo


# #### NASA Mars News

# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# In[4]:


soup = BeautifulSoup(browser.html, 'html.parser')


# In[5]:


print(soup.prettify())


# In[6]:


slide = soup.select_one('ul.item_list li.slide')
slide


# In[7]:


news_title = slide.find('div',class_='content_title').get_text()


# In[8]:


news_title


# In[9]:


news_summary = slide.find('div',class_='article_teaser_body').get_text()


# In[10]:


news_summary


# ### Find Feature Image URL

# In[11]:


url2 = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url2)


# In[12]:


soup = BeautifulSoup(browser.html, 'html.parser')


# In[13]:


print(soup.prettify())


# In[14]:


images2 = soup.select("img", class_="headerimage")
href = images2[1]['src']


# In[15]:


href


# In[16]:


featured_image_url =('https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/' + href)
featured_image_url


# ### Find Hemisphere URLs

# In[17]:


mars_hemisphere_image_urls=[
    {"title": "Cerberus Hemisphere", "img_url":"https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"},
    {"title": "Schiaparelli Hemisphere", "img_url":"https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"},
    {"title": "Syrtis Major Hemisphere", "img_url":"https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"},
    {"title": "Valles Marineris Hemisphere", "img_url":"https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"}
    ]


# ### Scrapping Mars Data Table

# In[18]:


url3 = 'https://space-facts.com/mars/'
browser.visit(url3)


# In[19]:


soup = BeautifulSoup(browser.html, 'html.parser')


# In[20]:


print(soup.prettify())


# In[24]:


tables = soup.select("table", class_="tablepress tablepress-id-p-mars")
mars_table = tables[0]
mars_table


# #### Mongo DB

# In[26]:


conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)


# In[27]:


# Define Database and Collection
db = client.marsnews_db
collection = db.items


# In[28]:


# Dictionary to be inserted as a MongoDB document
post = {
    'title': news_title,
    'summary': news_summary,
    'feature_image': featured_image_url,
    'hemispheres':mars_hemisphere_image_urls
        }


# In[29]:


# Insert Posts into marsnews_db
collection.update({},post,upsert=True)


# In[30]:


articles = db.items.find()


# In[31]:


for article in articles:
    print(article)

