#!/usr/bin/env python
# coding: utf-8

# # North Korean News
# 
# Scrape the North Korean news agency http://kcna.kp
# 
# Save a CSV called `nk-news.csv`. This file should include:
# 
# * The **article headline**
# * The value of **`onclick`** (they don't have normal links)
# * The **article ID** (for example, the article ID for `fn_showArticle("AR0125885", "", "NT00", "L")` is `AR0125885`
# 
# The last part is easiest using pandas. Be sure you don't save the index!
# 
# * _**Tip:** If you're using requests+BeautifulSoup, you can always look at response.text to see if the page looks like what you think it looks like_
# * _**Tip:** Check your URL to make sure it is what you think it should be!_
# * _**Tip:** Does it look different if you scrape with BeautifulSoup compared to if you scrape it with Selenium?_
# * _**Tip:** For the last part, how do you pull out part of a string from a longer string?_
# * _**Tip:** `expand=False` is helpful if you want to assign a single new column when extracting_
# * _**Tip:** `(` and `)` mean something special in regular expressions, so you have to say "no really seriously I mean `(`" by using `\(` instead_
# * _**Tip:** if your `.*` is taking up too much stuff, you can try `.*?` instead, which instead of "take as much as possible" it means "take only as much as needed"_

# In[10]:


from selenium import webdriver


# In[11]:


driver = webdriver.Chrome()


# In[12]:


driver.get("http://kcna.kp")


# In[13]:


headlines = driver.find_elements_by_class_name("titlebet")
for headline in headlines:
    print(headline.text)


# In[14]:


clicks = driver.find_elements_by_tag_name('strong')
for click in clicks:
    links = click.find_elements_by_tag_name('a')
    for link in links:
        print(link.get_attribute('onclick'))


# In[23]:



news = []

titles = driver.find_elements_by_class_name("titlebet")
for title in titles:
    articles = {}
    try:
        articles['urls'] = title.get_attribute('onclick')
        articles['headline'] = title.text
    except:
        pass
    print(articles)
    news.append(articles)

    


# In[36]:


import pandas as pd

df= pd.DataFrame(news)
df.head(30)


# In[44]:


article_id = df.urls.str.extract(r"([A-Z]+\d\d\d\d\d\d\d)")
df['article_id'] = article_id
df.head()


# In[45]:


df.to_csv("nk-news.csv", index=False, header=True)


# In[ ]:




