#!/usr/bin/env python
# coding: utf-8

# # Filter DataFrame with More than One Condition (AND - &)

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("employees.csv",parse_dates=["Start Date","Last Login Time"])
df["Senior Management"]=df["Senior Management"].astype("bool")
df["Gender"]=df["Gender"].astype("category")
df.head(3)


# In[5]:


mask=df["Gender"] == "Male"
df[mask]


# In[6]:


df["Team"] == "Marketing"


# In[9]:


mask1 = df["Gender"] == "Male"
mask2 = df["Team"] == "Marketing"


# In[7]:


mask1 = df["Gender"] == "Male"
df[mask1]


# In[10]:


df [mask1 & mask2]


# # Filter DataFrame with More than One Condition (OR - )

# In[11]:


df=pd.read_csv("employees.csv",parse_dates=["Start Date","Last Login Time"])
df["Senior Management"]=df["Senior Management"].astype("bool")
df["Gender"]=df["Gender"].astype("category")
df.head(3)


# In[12]:


mask1 = df["Senior Management"]
mask2 = df["Start Date"] < "1990-01-01"


# In[13]:


df[mask1 | mask2]


# In[16]:


mask1 = df["First Name"] == "Robert"
mask2 = df["Team"] == "Client Services"
mask3 = df["Start Date"] > "2016-06-01"
df[(mask1 & mask2) | mask3]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




