#!/usr/bin/env python
# coding: utf-8

# ## Logging on
# 
# Use Selenium to visit https://webapps1.chicago.gov/buildingrecords/ and accept the agreement.
# 
# > Think about when you use `.find_element_...` and when you use `.find_elementSSS_...`

# In[1]:


from selenium import webdriver


# In[2]:


driver = webdriver.Chrome()


# In[3]:


driver.get('https://webapps1.chicago.gov/buildingrecords/')


# In[4]:


driver.page_source


# In[5]:


driver.find_element_by_id("rbnAgreement1").click()


# In[6]:


submit_button = driver.find_element_by_xpath('//*[@id="submit"]')
submit_button.click()


# ## Searching
# 
# Search for **400 E 41ST ST**.

# In[7]:


textbox = driver.find_element_by_id("fullAddress")


# In[8]:


textbox.send_keys("400 E 41ST ST.")


# In[9]:


submit_button = driver.find_element_by_xpath('//*[@id="submit"]')


# In[10]:


submit_button.click()


# ## Saving tables with pandas
# 
# Use pandas to save a CSV of all **permits** to `Permits - 400 E 41ST ST.csv`. Note that there are **different sections of the page**, not just one long permits table.

# In[11]:


import pandas as pd


# In[12]:



tables = pd.read_html(driver.page_source)
tables[0]


# In[13]:


tables[0].to_csv(r'/Users/sheridanwall/Documents/Foundations/Permits_400_E_41ST_ST.csv', index = False)


# ## Saving tables the long way
# 
# Save a CSV of all DOB inspections to `Inspections - 400 E 41ST ST.csv`, but **you also need to save the URL to the inspection**. As a result, you won't be able to use pandas, you'll need to use a loop and create a list of dictionaries.
# 
# You can use Selenium (my recommendation) or you can feed the source to BeautifulSoup. You should have approximately 157 rows.
# 
# You'll probably need to find the table first, then the rows inside, then the cells inside of each row. You'll probably use lots of list indexing. I might recommend XPath for finding the table.
# 
# *Tip: If you get a "list index out of range" error, it's probably due to an issue involving `thead` vs `tbody` elements. What are they? What are they for? What's in them? There are a few ways to troubleshoot it.*

# In[14]:


items = driver.find_elements_by_id('resultstable_inspections')
for item in items:
    insp_table= item.find_elements_by_tag_name('tbody')
    for insp in insp_table:
        cells = insp.find_elements_by_tag_name('tr')
        for cell in cells:
            number = cell.find_elements_by_tag_name('td')[0].text
            print(number)
            date = cell.find_elements_by_tag_name('td')[1].text
            print(date)
            status = cell.find_elements_by_tag_name('td')[2].text
            print(status)
            description = cell.find_elements_by_tag_name('td')[3].text
            print(description)


# In[15]:


for item in items:
    urls = item.find_elements_by_tag_name('td')
    for url in urls:
        links = url.find_elements_by_tag_name('a')
        for link in links:
            print(link.get_attribute('href'))
        


# In[16]:


inspections = []
items = driver.find_elements_by_id('resultstable_inspections')
for item in items:
    insp_table= item.find_elements_by_tag_name('tbody')
    for insp in insp_table:
        cells = insp.find_elements_by_tag_name('tr')
        for cell in cells:
            inspection = {}
            inspection['number'] = cell.find_elements_by_tag_name('td')[0].text
            inspection['date'] = cell.find_elements_by_tag_name('td')[1].text
            inspection['status'] = cell.find_elements_by_tag_name('td')[2].text
            inspection['description'] = cell.find_elements_by_tag_name('td')[3].text
            links = cell.find_elements_by_tag_name('a')
            for link in links:
                inspection['urls'] = link.get_attribute('href')
            print(inspection)
            inspections.append(inspection)
                
            


# In[17]:


df = pd.DataFrame(inspections)
df.head()


# In[18]:


df.to_csv("Inspections_400_E41_ST.csv")


# ### Loopity loops
# 
# > If you used Selenium for the last question, copy the code and use it as a starting point for what we're about to do!
# 
# If you click the inspection number, it'll open up a new window that shows you details of the violations from that visit. Count the number of violations for each visit and save it in a new column called **num_violations**.
# 
# Save this file as `Inspections - 400 E 41ST ST - with counts.csv`.
# 
# Since it opens in a new window, we have to say "Hey Selenium, pay attention to that new window!" We do that with `driver.switch_to.window(driver.window_handles[-1])` (each window gets a `window_handle`, and we're just asking the driver to switch to the last one.). A rough sketch of what your code will look like is here:
# 
# ```python
# # Click the link that opens the new window
# 
# # Switch to the new window/tab
# driver.switch_to.window(driver.window_handles[-1])
# 
# # Do your scraping in here
# 
# # Close the new window/tab
# driver.close()
# 
# # Switch back to the original window/tab
# driver.switch_to.window(driver.window_handles[0])
# ```
# 
# You'll want to play around with them individually before you try it with the whole set - the ones that pass are very different pages than the ones with violations! There are a few ways to get the number of violations, some easier than others.

# In[21]:


for item in items:
    insp_table= item.find_elements_by_tag_name('tbody')
    for insp in insp_table:
        cells = insp.find_elements_by_tag_name('tr')
        for cell in cells:
            links = cell.find_elements_by_tag_name('a')
            for link in links:
                link.click()
                


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




