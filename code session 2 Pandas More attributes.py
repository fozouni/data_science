#!/usr/bin/env python
# coding: utf-8

# In[2]:


a=['c','k','d']


# In[3]:


sorted(a)


# In[4]:


import pandas as pd


# In[39]:


a=pd.read_csv('C:\\Users\\Ali\\Desktop\\weather.csv',usecols=['play'],squeeze=True)
b=pd.read_csv('C:\\Users\\Ali\\Desktop\\B.csv',usecols=['crim'],squeeze=True)
c=pd.read_csv('C:\\Users\\Ali\\Desktop\\Book1.csv',squeeze=True)
a


# In[8]:


a.values
b.values


# In[9]:


a.index


# In[10]:


b.index


# In[18]:


a.is_unique


# In[19]:


b.is_unique


# In[28]:


c.is_unique


# In[ ]:


# a.ndim


# # b.ndimتعداد بعد ها(تعداد ستونها) را مشخص میکند  

# In[31]:


c.ndim


# In[32]:


a.shape


# # برای ابعاد بیشتر هم استفاده میشود shapeیعنی سری ما506 ردیف یا سطر دارد بوسیله یک ستون

# In[37]:


b.shape


# In[43]:


# a.sizeتعداد عناصریا مقادیر سری


# In[41]:


a.size


# In[42]:


b.size


# # a.nameهمان سرتیتری که انتخاب کردم

# In[48]:


b.name


# In[49]:


b


# # b.name='ali'اختصاص دادن نام جدید

# In[51]:


b.name='ali'
b


# ### more methods

# مرتب کردن مقادیر براساس حروف الفبا در سری

# In[55]:


a.sort_values().head()


# # فرقی نمیکند بصورت حروف الفبا مرتب میکند

# In[56]:


a.sort_values(ascending=True)


# a.sort_values(ascending=False)معکوس حروف الفبا

# In[59]:


a.sort_values(ascending=False)


# In[60]:


a.sort_values(ascending=False).tail()


# In[61]:


b.sort_values()


# # or

# In[62]:


b.sort_values(ascending=True)


# # بصورت نزولیdescending

# In[65]:


b.sort_values(ascending=False)


# In[ ]:




