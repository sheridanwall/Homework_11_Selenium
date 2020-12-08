#!/usr/bin/env python
# coding: utf-8

# # Rock and Mineral Clubs
# 
# Scrape all of the rock and mineral clubs listed at https://rocktumbler.com/blog/rock-and-mineral-clubs/ (but don't just cut and paste!)
# 
# Save a CSV called `rock-clubs.csv` with the name of the club, their URL, and the city they're located in.
# 
# **Bonus**: Add a column for the state. There are a few ways to do this, but knowing that `element.parent` goes 'up' one element might be helpful.
# 
# * _**Hint:** The name of the club and the city are both inside of td elements, and they aren't distinguishable by class. Instead you'll just want to ask for all of the tds and then just ask for the text from the first or second one._
# * _**Hint:** If you use BeautifulSoup, you can select elements by attributes other than class or id - instead of `doc.find_all({'class': 'cat'})` you can do things like `doc.find_all({'other_attribute': 'blah'})` (sorry for the awful example)._
# * _**Hint:** If you love `pd.read_html` you might also be interested in `pd.concat` and potentially `list()`. But you'll have to clean a little more!_

# In[45]:


import requests
from bs4 import BeautifulSoup


# In[46]:


rocks = "https://rocktumbler.com/blog/rock-and-mineral-clubs/"
raw_html = requests.get(rocks).content
doc = BeautifulSoup(raw_html, "html.parser")
print(doc.prettify())


# In[124]:


# Clubs
tables = doc.find_all('tr', bgcolor = "#FFFFFF")
for table in tables:
    cities = table.find_all('td')
    for city in cities:
        clubs = table.find_all('a')
        for club in clubs:
            print(club.text)


# In[48]:


# urls
tables = doc.find_all('td')
for table in tables:
    clubs = table.find_all('a')
    for club in clubs:
        print(club['href'])


# In[123]:


# City
tables = doc.find_all('tr', bgcolor = "#FFFFFF")
for table in tables:
    cities = table.find_all('td')
    print(cities[1].text)


# In[126]:


rock_clubs = []
tables = doc.find_all('tr', bgcolor = "#FFFFFF")
for table in tables:
    rocks = {}
    cities = table.find_all('td')
    rocks['city'] = cities[1].text
    for city in cities:
        clubs = table.find_all('a')
        for club in clubs:
            rocks['club_name'] = club.text
            rocks['url'] = club['href']
    print(rocks)
    rock_clubs.append(rocks)


# In[127]:


import pandas as pd


# In[129]:


df = pd.DataFrame(rock_clubs)
df.head()


# In[131]:


df.to_csv("rock-clubs.csv", index=False, header=True)


# In[ ]:




