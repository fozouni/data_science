#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


a=pd.read_csv('C:\\Users\\Ali\\Desktop\\dataset session 7 Pandas nba.csv')
a


# In[ ]:


a.head()


# In[ ]:


a.tail(2)


# In[ ]:


a.tail(n=1)


# In[ ]:


a.head(n=1)


# In[ ]:


a.index


# In[ ]:


a.values


# In[ ]:


a.shape


# In[ ]:


a.dtypes


# In[ ]:


a.dtypes.value_counts()


# In[ ]:


a.columns


# In[ ]:


a.axes


# In[ ]:


a.info()


# In[ ]:




