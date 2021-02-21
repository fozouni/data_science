#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data=pd.read_csv('dataset session 7 Pandas nba.csv')
data.head(3)


# In[3]:


data.tail(3)


# In[4]:


data.dropna()


# In[5]:


data.dropna(how = "all")


# In[7]:


data


# In[8]:


data.dropna(how = "all",inplace=True)


# In[9]:


data.tail(3)


# In[10]:


data.dropna(axis=1)


# In[11]:


data.dropna(axis=1)


# In[12]:


data.dropna(axis="columns")


# In[13]:


data.head(3)


# In[14]:


data.dropna(subset=["Salary","College"])


# In[15]:


nb=data=pd.read_csv('dataset session 7 Pandas nba.csv')
nb.head(3)


# In[16]:


nb.fillna(0)


# In[17]:


nb["Salary"]


# In[18]:


nb["Salary"].fillna(0,inplace=True)


# In[19]:


nb.head()


# In[20]:


nb["College"]


# In[21]:


nb["College"].fillna("No College",inplace=True)


# In[22]:


nb


# In[23]:


n=pd.read_csv('dataset session 7 Pandas nba.csv').dropna(how="all")
n.head(3)


# In[24]:


n.tail(3)


# In[25]:


n["Salary"].fillna(0,inplace=True)


# In[28]:


n


# In[29]:


n["College"].fillna("None",inplace=True)


# In[30]:


n.head(6)


# In[31]:


n.dtypes


# In[32]:


n.info()


# In[35]:


n["Salary"]


# In[34]:


n["Salary"].astype("int")


# In[ ]:





# In[37]:


n["Salary"]=n["Salary"].astype("int")


# In[38]:


n.head(3)


# In[39]:


n.info()


# In[41]:


n["Number"].astype("int")


# In[42]:


n["Number"]=n["Number"].astype("int")


# In[43]:


n["Age"].astype("int")


# In[44]:


n["Age"]=n["Age"].astype("int")


# In[45]:


n["Age"].nunique()


# In[46]:


n["Position"].nunique()


# In[47]:


n["Position"].astype("category")


# In[48]:


n["Position"]=n["Position"].astype("category")


# In[49]:


n.info()


# In[50]:


n["Team"].astype("category")


# In[51]:


n["Team"]=n["Team"].astype("category")


# In[52]:


n.info()


# In[ ]:




