#!/usr/bin/env python
# coding: utf-8

# # Check for Inclusion with the isin Method

# In[1]:


import pandas as pd


# In[7]:


df=pd.read_csv("employees.csv",parse_dates=["Start Date","Last Login Time"])
df["Senior Management"]=df["Senior Management"].astype("bool")
df["Gender"]=df["Gender"].astype("category")
df.head(3)


# In[10]:


mask1 = df["Team"]== "Legal"
mask2 = df["Team"]== "Sales"
mask3 = df["Team"]== "Product" 
df[mask1 | mask2 | mask3]


# In[11]:


df["Team"].isin(["Legal","Sales","Product"])


# In[12]:


mask = df["Team"].isin(["Legal","Sales","Product"])
df[mask]


# ### Check for Null and Present DataFrame Values with the isnull and notnull Methods

# In[ ]:




