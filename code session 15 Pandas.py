#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df=pd.read_csv("employees.csv",parse_dates=["Start Date","Last Login Time"])
df["Senior Management"]=df["Senior Management"].astype("bool")
df["Gender"]=df["Gender"].astype("category")
df.head(5)


# In[4]:


df["Gender"] == "Male"


# In[5]:


df[df["Gender"] == "Male"]


# In[6]:


df["Team"] == "Finance"


# In[7]:


df[df["Team"] == "Finance"]


# In[8]:


mask = df["Team"] == "Finance"
df[mask]


# In[13]:


df["Senior Management"] == True


# In[12]:


df[df["Senior Management"]]


# In[16]:


df["Team"]!= "Marketing"


# In[17]:


mask = df["Team"]!= "Marketing"
df[mask]


# In[18]:


df["Salary"]


# In[19]:


df["Salary"] > 110000


# In[20]:


df[df["Salary"] > 110000]


# In[21]:


df["Bonus %"]


# In[22]:


df["Bonus %"] < 1.5


# In[23]:


df[df["Bonus %"] < 1.5]


# In[24]:


df["Start Date"]


# In[25]:


df["Start Date"] <= "1985-01-01"


# In[26]:


mask = df["Start Date"] <= "1985-01-01"
df[mask]


# In[ ]:




