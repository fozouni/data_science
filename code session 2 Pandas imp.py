#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=['c','k','d']


# In[2]:


sorted(a)


# In[3]:


import pandas as pd


# In[28]:


a=pd.read_csv('C:\\Users\\Ali\\Desktop\\weather.csv',usecols=['play'],squeeze=True)
b=pd.read_csv('C:\\Users\\Ali\\Desktop\\B.csv',usecols=['crim'],squeeze=True)
c=pd.read_csv('C:\\Users\\Ali\\Desktop\\Book1.csv',squeeze=True)
c


# In[6]:


a.values


# In[7]:


a.index


# In[8]:


b.index


# In[10]:


a.is_unique


# In[11]:


b.is_unique


# In[12]:


c.is_unique


# In[29]:


c


# # b.ndimتعداد بعد ها(تعداد ستونها) را مشخص میکند  

# In[17]:


a.ndim


# In[18]:


c.ndim


# In[19]:


a.shape


# # برای ابعاد بیشتر هم استفاده میشود shapeیعنی سری ما506 ردیف یا سطر دارد بوسیله یک ستون

# In[20]:


b.shape


# In[ ]:


# a.sizeتعداد عناصریا مقادیر سری


# In[21]:


a.size


# In[22]:


b.size


# # a.nameهمان سرتیتری که انتخاب کردم

# In[24]:


b.name


# In[ ]:


b


# # b.name='ali'اختصاص دادن نام جدید

# In[25]:


b.name='ali'
b


# ### more methods

# مرتب کردن مقادیر براساس حروف الفبا در سری

# In[33]:


b.sort_values()


# # فرقی نمیکند بصورت حروف الفبا مرتب میکند

# In[34]:


a.sort_values(ascending=True)


# In[26]:


c.sort_values(ascending=True)


# a.sort_values(ascending=False)معکوس حروف الفبا

# In[36]:


a.sort_values(ascending=False).head()


# In[37]:


a.sort_values(ascending=False).tail()


# In[38]:


b.sort_values()


# # or

# In[39]:


b.sort_values(ascending=True)


# # بصورت نزولیdescending

# In[40]:


b.sort_values(ascending=False)


# In[ ]:




