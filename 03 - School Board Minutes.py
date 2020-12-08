#!/usr/bin/env python
# coding: utf-8

# # School Board Minutes
# 
# Scrape all of the school board minutes from http://www.mineral.k12.nv.us/pages/School_Board_Minutes
# 
# Save a CSV called `minutes.csv` with the date and the URL to the file. The date should be formatted as YYYY-MM-DD.
# 
# **Bonus:** Download the PDF files
# 
# **Bonus 2:** Use [PDF OCR X](https://solutions.weblite.ca/pdfocrx/index.php) on one of the PDF files and see if it can be converted into text successfully.
# 
# * **Hint:** If you're just looking for links, there are a lot of other links on that page! Can you look at the link to know whether it links or minutes or not? You'll want to use an "if" statement.
# * **Hint:** You could also filter out bad links later on using pandas instead of when scraping
# * **Hint:** If you get a weird error that you can't really figure out, you can always tell Python to just ignore it using `try` and `except`, like below. Python will try to do the stuff inside of 'try', but if it hits an error it will skip right out.
# * **Hint:** Remember the codes at http://strftime.org
# * **Hint:** If you have a date that you've parsed, you can use `.dt.strftime` to turn it into a specially-formatted string. You use the same codes (like %B etc) that you use for converting strings into dates.
# 
# ```python
# try:
#   blah blah your code
#   your code
#   your code
# except:
#   pass
# ```
# 
# * **Hint:** You can use `.apply` to download each pdf, or you can use one of a thousand other ways. It'd be good `.apply` practice though!

# In[66]:


from selenium import webdriver


# In[67]:


driver = webdriver.Chrome()


# In[68]:


driver.get("http://www.mineral.k12.nv.us/pages/School_Board_Minutes")


# In[69]:


links = driver.find_elements_by_tag_name('p')
for link in links:
    urls = link.find_elements_by_tag_name('a')
    for url in urls:
        try:
            pdf_link = url.get_attribute('href')
            if ".pdf" in pdf_link:
                print(pdf_link)
        except:
            print("NONE")

    


# In[77]:


minutes = []
items = driver.find_elements_by_tag_name('a')
for item in items:
    mins = {}
    try:
        pdf_link = item.get_attribute('href')
        if ".pdf" in pdf_link:
            mins['url'] = pdf_link
            mins['dates'] = item.text
            minutes.append(mins)
    except:
        pass
meeting_minutes = minutes[:-9]
meeting_minutes
        

    


# In[78]:


import pandas as pd


# In[92]:


df = pd.DataFrame(meeting_minutes)
df.head()


# In[93]:


df['dates'] = pd.to_datetime(df["dates"])


# In[94]:


df.head()


# In[96]:


df.to_csv("minutes.csv", index=False, header=True)


# In[100]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option('prefs',  {
    "plugins.always_open_pdf_externally": True
})
for urls in meeting_minutes:
    links = urls['url']
    driver = webdriver.Chrome(options=options)
    driver.get(links)


# In[ ]:




