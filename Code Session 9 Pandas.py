#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pd.read_excel('data.xlsx')


# In[3]:


b=pd.read_excel('data.xlsx',index_col='Date')
b


# In[4]:


a=pd.Series([1,2,3])
a.sum()


# In[5]:


b.sum()


# In[6]:


b.sum(axis='index')


# In[7]:


b.sum(axis=0)


# In[8]:


b.sum(axis=1)


# In[9]:


b.sum(axis='columns')


# In[ ]:




