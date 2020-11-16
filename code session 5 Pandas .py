#!/usr/bin/env python
# coding: utf-8

# # استخراج مقادیرمختلف از اندیس ها

# In[11]:


import pandas as pd


# In[12]:


a=pd.read_excel("C:\\Users\\Ali\\Desktop\\dataset session 5 Pandas.xlsx")
a


# In[8]:


a=pd.read_excel("C:\\Users\\Ali\\Desktop\\dataset session 5 Pandas.xlsx",index_col="a")
a


# In[13]:


a=pd.read_excel("C:\\Users\\Ali\\Desktop\\dataset session 5 Pandas.xlsx",index_col="a",squeeze=True)
a


# In[14]:


a


# In[15]:


a[0]


# In[16]:


a[[0,2]]


# In[17]:


a["d"]


# In[18]:


a["e"]


# In[19]:


a[['d','f']]


# In[20]:


a["d":"l"]


# In[21]:


a["l":]


# In[22]:


a[:"f"]


# In[24]:


a[["q","f"]]


# In[25]:


a.reindex(index=["q","f"])


# In[26]:


a["d":"l":3]


# In[ ]:


a


# # استخراج مقادیر از اندیس های مرتب شده

# In[27]:


a.sort_index(inplace=True)


# In[28]:


a


# In[29]:


a.get(0)


# In[30]:


a.get('l')


# In[31]:


a.get([1,4])


# In[33]:


a.get(1000)


# In[34]:


a.get('y')


# In[35]:


a.get(['y','f'])


# In[36]:


a.get(['t','s'])


# In[39]:


a.get('t',default="Does not exist")


# In[40]:


a.get('q',default= "Does not exist")


# In[41]:


a.get('f',default= "Does not exist")


# In[42]:


a.get(key=['c','d','q'],default= "Does not exist")


# In[43]:


a.get(key=[0,1,3],default= "Does not exist")


# # روشهای ریاضی در سری 

# In[45]:


data=pd.read_csv("C:\\Users\\Ali\\Desktop\\dataset session 3 Pandas numeric.csv",squeeze=True)
data


# In[46]:


data.count()


# In[47]:


len(data)


# In[48]:


data.sum()


# In[49]:


data.mean()


# In[50]:


data.sum() / data.count()


# In[51]:


data.std()


# In[52]:


data.min()


# In[53]:


data.max()


# In[54]:


data.median()


# In[57]:


data.mode()


# In[58]:


data.describe()


# In[ ]:




