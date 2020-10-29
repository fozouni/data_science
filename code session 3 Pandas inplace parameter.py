#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd


# In[24]:


a=pd.read_csv('C:\\Users\\Ali\\Desktop\\INDEX.csv',usecols=['HP'],squeeze=True)
a.head(3)


# In[25]:


a.sort_index()


# In[30]:


a.sort_index(ascending=False,inplace=True)
a


# In[31]:


a=a.sort_index(ascending=False)
a


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




