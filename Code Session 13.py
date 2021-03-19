#!/usr/bin/env python
# coding: utf-8

# # Sort a DataFrame with the sort_values Method, 

# In[7]:


import pandas as pd


# In[8]:


data=pd.read_csv('dataset session 7 Pandas nba.csv')


# In[9]:


data.head(3)


# In[11]:


data.sort_values("Name",ascending=False)


# In[12]:


data.sort_values("Name",ascending=False)


# In[13]:


data.sort_values("Age",ascending=False)


# In[14]:


data.sort_values("Salary",ascending=False)


# In[15]:


data.sort_values("Salary",ascending=False,inplace=True)
data.head(3)


# In[16]:


data.sort_values("Salary").tail()


# In[17]:


data.sort_values("Salary",ascending=False)


# In[19]:


data.sort_values("Salary",ascending=False,na_position='first').tail()


# In[20]:


d = pd.read_csv('dataset session 7 Pandas nba.csv')
d.head(3)


# In[21]:


d.sort_values(['Team','Name'])


# In[22]:


d.sort_values(['Team','Name'],ascending=False)


# In[24]:


d.sort_values(['Team','Name'],ascending=[True,False],inplace=True)
d


# # Sort DataFrame Indexwith the sort_index Method

# In[25]:


d.sort_values(['Number','Salary','Name'],inplace=True)
d.tail(3)


# In[26]:


d.sort_index()


# In[27]:


d.sort_index(ascending=False,inplace=True)


# In[28]:


d.head(3)


# # 18. Rank Series Values with the rank Method

# In[29]:


nb=pd.read_csv('dataset session 7 Pandas nba.csv').dropna(how='all')
nb['Salary']=nb['Salary'].fillna(0).astype('int')
nb.head(3)


# In[30]:


nb['Salary rank']=nb['Salary'].rank(ascending=False).astype(int)
nb


# In[33]:


nb.sort_values(by='Salary',ascending=False)


# In[ ]:





# In[ ]:




