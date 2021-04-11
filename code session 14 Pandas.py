#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv('employees.csv')
df.head(3)


# In[3]:


df.info()


# In[4]:


df['Start Date']


# In[5]:


pd.to_datetime(df['Start Date'])


# In[6]:


df["Start Date"]=pd.to_datetime(df['Start Date'])


# In[7]:


df.head(3)


# In[8]:


df["Last Login Time"]


# In[9]:


pd.to_datetime(df["Last Login Time"])


# In[10]:


df["Last Login Time"]=pd.to_datetime(df["Last Login Time"])
df.head(3)


# In[11]:


df["Senior Management"].astype("bool")


# In[12]:


df["Senior Management"]=df["Senior Management"].astype("bool")
df.head(3)


# In[13]:


df["Gender"]=df["Gender"].astype("category")
df.head(3)


# In[15]:


df.info()


# In[16]:


df=pd.read_csv('employees.csv')
df["Start Date"]=pd.to_datetime(df["Start Date"])
df["Last Login Time"]=pd.to_datetime(df["Last Login Time"])
df["Senior Management"]=df["Senior Management"].astype("bool")
df["Gender"]=df["Gender"].astype("category")
df.head(3)


# In[17]:


df=pd.read_csv('employees.csv',parse_dates=["Start Date","Last Login Time"])
#df["Start Date"]=pd.to_datetime(df["Start Date"])
#df["Last Login Time"]=pd.to_datetime(df["Last Login Time"])
df["Senior Management"]=df["Senior Management"].astype("bool")
df["Gender"]=df["Gender"].astype("category")
df.head(3)


# In[ ]:




