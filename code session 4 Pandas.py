#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


a=pd.read_csv('C:\\Users\\Ali\\Desktop\\dataset session (1,2 ) Pandas  weather.csv',usecols=['play'],squeeze=True)
a.head(3)


# In[18]:


5 in a


# In[21]:


13 in a.index


# In[22]:


13 in a


# In[24]:


a.values
'yes' in a


# In[19]:


a.index


# In[25]:


"yes" in a.values


# In[8]:


a


# In[ ]:


3 in [3,6,9]


# In[ ]:


100 in [3,6,9]


# In[3]:


a[0]


# In[4]:


a[[0,8,9]]


# In[5]:


a[1:3]


# In[7]:


a[-3:]


# In[9]:


a[-1:]


# In[10]:


a[:3]


# In[16]:


a[-5:-1]


# In[ ]:





# In[ ]:




