#!/usr/bin/env python
# coding: utf-8

# # .idxmax() and .idxmin() Methods

# In[1]:


import pandas as pd


# In[2]:


n=pd.read_csv('C:\\Users\\Ali\\Desktop\\dataset session 3 Pandas numeric.csv',squeeze=True)
n


# In[3]:


n.max()


# In[4]:


n.idxmax()


# In[5]:


n[3]


# In[6]:


n.min()


# In[7]:


n.idxmin()


# In[8]:


n[0]


# In[9]:


n[n.idxmin()]


# In[10]:


b=pd.read_excel('C:\\Users\\Ali\\Desktop\\dataset session 6 Pandas.xlsx',index_col="a",squeeze=True)
b


# In[11]:


b.min()


# In[12]:


b.max()


# In[13]:


b.idxmax()


# In[14]:


b.idxmin()


# In[15]:


b['f']


# In[16]:


b['l']


# In[17]:


b.value_counts()


# In[18]:


b.value_counts(ascending=True)


# In[19]:


b.value_counts().sum()


# In[20]:


b.count()


# In[21]:


b


# # The  .apply() Method

# In[22]:


def classify_performance(number):
    if number<300:
        return "ok"
    elif number >= 300 and number < 650:
        return "statisfactory"
    else:
        return "Incredible!"


# In[23]:


b.apply(classify_performance)


# In[25]:


b.apply(classify_performance).tail(3)


# In[26]:


b.apply(lambda c:c+1)


# # The .map() Method

# In[27]:


r=pd.read_excel('C:\\Users\\Ali\\Desktop\\dataset session 5 Pandas.xlsx',index_col="b",squeeze=True)
r


# In[28]:


b=pd.read_excel('C:\\Users\\Ali\\Desktop\\dataset session 6 Pandas.xlsx',index_col="a",squeeze=True)
b


# In[29]:


r.map(b)


# In[30]:


b.map(r)


# In[31]:


r=pd.read_excel('C:\\Users\\Ali\\Desktop\\dataset session 5 Pandas.xlsx',index_col="b",squeeze=True)
b=pd.read_excel('C:\\Users\\Ali\\Desktop\\dataset session 6 Pandas.xlsx',index_col="a",squeeze=True).to_dict()
b


# In[32]:


r


# In[33]:


r.map(b)


# In[ ]:




