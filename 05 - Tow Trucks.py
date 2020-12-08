#!/usr/bin/env python
# coding: utf-8

# # Texas Tow Trucks (`.apply` and `requests`)
# 
# We're going to scrape some [tow trucks in Texas](https://www.tdlr.texas.gov/tools_search/).

# ## Import your imports

# In[1]:


from selenium import webdriver


# In[2]:


driver = webdriver.Chrome()


# In[41]:


driver.get("https://www.tdlr.texas.gov/tools_search/")


# ## Search for the TLDR Number `006565540C`, and scrape the information on that company
# 
# Using [license information system](https://www.tdlr.texas.gov/tools_search/), find information about the tow truck number above, displaying the
# 
# - The business name
# - Owner/operator
# - Phone number
# - License status (Active, Expired, Etc)
# - Physical address
# 
# If you can't figure a 'nice' way to locate something, your two last options might be:
# 
# - **Find a "parent" element, then dig inside**
# - **Find all of a type of element** (like we did with `td` before) and get the `[0]`, `[1]`, `[2]`, etc
# - **XPath** (inspect an element, Copy > Copy XPath)
# 
# These kinds of techniques tend to break when you're on other result pages, but... maybe not! You won't know until you try.
# 
# > - *TIP: When you use xpath, you CANNOT use double quotes or Python will get confused. Use single quotes.*
# > - *TIP: You can clean your data up if you want to, or leave it dirty to clean later*
# > - *TIP: The address part can be tough, but you have a few options. You can use a combination of `.split` and list slicing to clean it now, or clean it later in the dataframe with regular expressions. Or other options, too, probably*

# In[42]:


textbox = driver.find_element_by_xpath("/html/body/div/div[1]/div/div/form/table/tbody/tr[5]/td[1]/input[2]")


# In[40]:


textbox.send_keys("006565540C")


# In[6]:


submit = driver.find_element_by_xpath("/htmlbody/div/div[1]/div/div/form/table/tbody/tr[10]/td/center/button/b")


# In[7]:


submit.click()


# In[8]:


trucks = driver.find_elements_by_tag_name('td')
company = trucks[6]
company_name = company.text
print(company_name)


# In[9]:


owner_name = trucks[8]
owner = owner_name.text
print(owner)


# In[10]:


number = trucks[10]
phone_number = number.text
print(phone_number)


# In[34]:


status = trucks[13].text
print(status)


# In[33]:


print(trucks[15].text)


# # Adapt this to work inside of a single cell
# 
# Double-check that it works. You want it to print out all of the details.

# In[ ]:





# # Using .apply to find data about SEVERAL tow truck companies
# 
# The file `trucks-subset.csv` has information about the trucks, we'll use it to find the pages to scrape.
# 
# ### Open up `trucks-subset.csv` and save it into a dataframe

# In[36]:


import pandas as pd
df2 = pd.read_csv("trucks-subset.csv")


# In[37]:


df2.head()


# ## Go through each row of the dataset, displaying the URL you will need to scrape for the information on that row
# 
# You don't have to actually use the search form for each of these - look at the URL you're on, it has the number in it!
# 
# For example, one URL might look like `https://www.tdlr.texas.gov/tools_search/mccs_display.asp?mcrnumber=006565540C`.
# 
# - *TIP: Use .apply and a function*
# - *TIP: You'll need to build this URL from pieces*
# - *TIP: You probably don't want to `print` unless you're going to fix it for the next question 
# - *TIP: pandas won't showing you the entire url! Run `pd.set_option('display.max_colwidth', None)` to display aaaalll of the text in a cell*

# In[ ]:





# In[ ]:





# In[ ]:





# ### Save this URL into a new column of your dataframe, called `url`
# 
# - *TIP: Use a function and `.apply`*
# - *TIP: Be sure to use `return`*

# In[ ]:





# ## Go through each row of the dataset, printing out information about each tow truck company.
# 
# Now will be **scraping** inside of your function.
# 
# - The business name
# - Owner/operator
# - Phone number
# - License status (Active, Expired, Etc)
# - Physical address
# 
# Just print it out for now.
# 
# - *TIP: use .apply*
# - *TIP: You'll be using the code you wrote before, but converted into a function*
# - *TIP: Remember how the TDLR Number is in the URL? You don't need to do the form submission if you don't want!*
# - *TIP: Make sure you adjust any variables so you don't scrape the same page again and again*

# In[ ]:





# In[ ]:





# ## Scrape the following information for each row of the dataset, and save it into new columns in your dataframe.
# 
# - The business name
# - Owner/operator
# - Phone number
# - License status (Active, Expired, Etc)
# - Physical address
# 
# It's basically what we did before, but using the function a little differently.
# 
# - *TIP: Same as above, but you'll be returning a `pd.Series` and the `.apply` line is going to be a lot longer*
# - *TIP: Save it to a new dataframe!*
# - *TIP: Make sure you change your `df` variable names correctly if you're cutting and pasting - there are a few so it can get tricky*

# In[ ]:





# In[ ]:





# In[ ]:





# ### Save your dataframe as a CSV named `tow-trucks-extended.csv`

# In[ ]:





# ### Re-open your dataframe to confirm you didn't save any extra weird columns

# In[ ]:





# ## Process the entire `tow-trucks.csv` file
# 
# We just did it on a short subset so far. Now try it on all of the tow trucks. **Save as the same filename as before**

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




