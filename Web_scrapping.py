#!/usr/bin/env python
# coding: utf-8

# In[15]:


# importing libraries
import pandas as pd


# In[16]:


url = "https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"


# Getting Table from the webpage

# In[47]:


dfs = pd.read_html(url)
for df in dfs:
    dataframe = df
    break

Dropping the rows that have Not assigned value of boroughs
And already checked that there are no missing values of the neighbourhood
# In[48]:


dataframe.set_index('Borough', inplace = True)
dataframe.drop('Not assigned',inplace = True)
dataframe.reset_index(inplace =True)
dataframe.head(12)


# In[ ]:




