#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd


# In[15]:


a=pd.read_csv('C:\\Users\\Ali\\Desktop\\weather.csv',usecols=['play'],squeeze=True)
a


# In[16]:


a.index


# In[17]:


a.values


# In[18]:


a.dtype


# In[ ]:





# In[ ]:




