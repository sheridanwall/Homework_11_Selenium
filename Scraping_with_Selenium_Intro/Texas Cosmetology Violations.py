#!/usr/bin/env python
# coding: utf-8

# # Texas Cosmetologist Violations
# 
# Texas has a system for [searching for license violations](https://www.tdlr.texas.gov/cimsfo/fosearch.asp). You're going to search for cosmetologists!

# ## Setup: Import what you'll need to scrape the page
# 
# We'll be using Selenium for this, *not* BeautifulSoup and requests.

# In[1]:


from selenium import webdriver


# In[2]:


driver = webdriver.Chrome()


# In[3]:


driver.get("https://www.tdlr.texas.gov/cimsfo/fosearch.asp")


# In[4]:


driver.page_source


# ## Starting your search
# 
# Starting from [here](https://www.tdlr.texas.gov/cimsfo/fosearch.asp), search for **cosmetologist violations** for people with the last name **Nguyen**.

# In[5]:


driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/section/div/div/table/tbody/tr/td/form/table/tbody/tr[3]/td/select/option[10]").click()


# In[6]:


textbox = driver.find_element_by_xpath('//*[@id="pht_lnm"]')


# In[7]:


textbox.send_keys("NGUYEN")


# In[8]:


submit_button = driver.find_element_by_xpath('//*[@id="dat-menu"]/div/div[2]/div[1]/div/section/div/div/table/tbody/tr/td/form/table/tbody/tr[18]/td/input[1]')


# In[9]:


submit_button.click()


# In[ ]:





# ## Scraping
# 
# Once you are on the results page, do this.

# ### Loop through each result and print the entire row
# 
# Okay wait, that's a heck of a lot. Use `[:10]` to only do the first ten (`listname[:10]` gives you the first ten).

# In[10]:


import pandas as pd


# In[11]:


driver.page_source


# In[12]:


tables = pd.read_html(driver.page_source)


# In[13]:


nguyen = tables[0]


# In[14]:


nguyen[:10]
    


# ### Loop through each result and print each person's name
# 
# You'll get an error because the first one doesn't have a name. How do you make that not happen?! If you want to ignore an error, you use code like this:
# 
# ```python
# try:
#    # try to do something
# except:
#    # Instead of stopping on an error, it'll jump down here instead
#    print("It didn't work')
# ```
# 
# It should help you out. If you don't want to print anything, you can type `pass` instead of the `print` statement. Most people use `pass`, but it's also nice to print out debug statements so you know when/where it's running into errors.
# 
# **Why doesn't the first one have a name?**

# In[15]:


for names in tables:
    try:
        print(names['Name and Location'])
    except:
        pass


# In[16]:


names = driver.find_elements_by_tag_name("tr")
for name in names:
    try:
        full_name = name.find_elements_by_class_name("results_text")[0]
        print(full_name.text)
    except:
        print("None")

    
    
#     try:
#         print(names)
#     except:
#         pass


# In[17]:


# for names in name:
#     print(names.find_element_by_class_name("results_text")[0]


# In[18]:


# https://stackoverflow.com/questions/24795198/get-all-child-elements
# print(driver.find_elements_by_css_selector("*")[10].text)


# ## Loop through each result, printing each violation description ("Basis for order")
# 
# > - *Tip: You'll get an error even if you're ALMOST right - which row is causing the problem?*
# > - *Tip: You can get the HTML of something by doing `.get_attribute('innerHTML')` - it might help you diagnose your issue.*
# > - *Tip: Or I guess you could just skip the one with the problem...*

# In[19]:


# for violation in tables:
#     try:
#         print(violation['Basis for Order'])
#     except:
#         pass


# In[20]:


violations = driver.find_elements_by_tag_name("tr")
for violation in violations:
    try:
        order_basis = violation.find_elements_by_tag_name("td")[2]
        print(order_basis.text)
    except:
        pass
    


# ## Loop through each result, printing the complaint number
# 
# - TIP: Think about the order of the elements

# In[21]:


complaints = driver.find_elements_by_tag_name("tr")
for complaint in complaints:
    try:
        complaint_number = complaint.find_elements_by_class_name("results_text")[5]
        print(complaint_number.text)
    except:
        print("None")


# ## Saving the results
# 
# ### Loop through each result to create a list of dictionaries
# 
# Each dictionary must contain
# 
# - Person's name
# - Violation description
# - Violation number
# - License Numbers
# - Zip Code
# - County
# - City
# 
# Create a new dictionary for each result (except the header).
# 
# > *Tip: If you want to ask for the "next sibling," you can't use `find_next_sibling` in Selenium, you need to use `element.find_element_by_xpath("following-sibling::div")` to find the next div, or `element.find_element_by_xpath("following-sibling::*")` to find the next anything.

# In[31]:


items = driver.find_elements_by_tag_name("tr")

rows = []
for item in items:
    row = {}
    try:
        row['name'] = item.find_elements_by_class_name("results_text")[0].text
    except:
        pass
    try:
        row['violations'] = item.find_elements_by_tag_name("td")[2].text
    except:
        pass
    try:
        row['complaint'] = item.find_elements_by_class_name("results_text")[5].text
    except:
        pass
    try:
        row['license'] = item.find_elements_by_class_name("results_text")[4].text
    except:
        pass
    try:
        row['zipcode'] = item.find_elements_by_class_name("results_text")[3].text
    except:
        pass
    try:
        row['county'] = item.find_elements_by_class_name("results_text")[2].text
    except:
        pass
    try:
        row['city'] = item.find_elements_by_class_name("results_text")[1].text
    except:
        pass
    print(row)
    rows.append(row)
    print('--------')
    
    
    


# ### Save that to a CSV
# 
# - Tip: Use `pd.DataFrame` to create a dataframe, and then save it to a CSV.

# In[43]:


df = pd.DataFrame(rows)
df.head()


# In[45]:


df.to_csv("nguyen_licenses1.csv", index=False, header=True)


# ### Open the CSV file and examine the first few. Make sure you didn't save an extra weird unnamed column.

# In[46]:


df=pd.read_csv("nguyen_licenses1.csv")
df.head()


# ## Let's do this an easier way
# 
# Use Selenium and `pd.read_html` to get the table as a dataframe.

# In[1]:


df2 = pd.read_html(driver.page_source)


# In[ ]:





# In[ ]:




