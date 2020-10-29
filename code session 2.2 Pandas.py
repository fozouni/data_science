#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


a=[4,9,3]
sorted(a)


# In[3]:


b=['z','t','k']
sorted(b)


# In[4]:


s=pd.read_csv("C:\\Users\\Ali\\Desktop\\weather.csv",usecols=['outlook'],squeeze=True)
dict(s)


# In[5]:


len(s)


# In[6]:


b=pd.Series(a)
b


# In[7]:


sorted(b)


# In[8]:


len(b)


# In[9]:


b.sum()


# In[10]:


b.mean()


# In[11]:


b.product()


# In[12]:


## methodsها و attributes 
dir(s)


# In[13]:


# لیست مرتب شده از مقادیر سری را میدهد براساس حروف الفبا


# In[13]:


sorted(s)


# In[15]:


list(s)


# In[ ]:


# max(s)اولین عنصر وآخرین عنصر بر اساس حروف الفبا
min(s)


# In[16]:


max(s)


# In[17]:


min(s)


# In[ ]:




