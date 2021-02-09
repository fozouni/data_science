#!/usr/bin/env python
# coding: utf-8

#  Add New Column to DataFrame

# In[1]:


import pandas as pd


# In[2]:


data=pd.read_csv('dataset session 7 Pandas nba.csv')
data.head()


# In[3]:


data['Name']


# In[4]:


data["sport"]="Basketball"


# In[5]:


data.head()


# In[9]:


data["league"]="National Basketball Association"


# In[10]:


data.head(3)


# In[11]:


data=pd.read_csv('dataset session 7 Pandas nba.csv')
data.head()


# In[12]:


data.insert(0,column="sport",value = "Basketball")
data.head(3)


# In[13]:


data.insert(2,column="league",value="National Basketball Association")
data.head(3)


# In[14]:


nb=pd.read_csv('dataset session 7 Pandas nba.csv')
nb.head(3)


# In[15]:


nb['Age']


# In[16]:


nb['Age'].add(5)


# In[17]:


nb['Age']+5


# In[19]:


nb['Salary'].sub(5000000)


# In[20]:


nb['Salary']-5000000


# In[21]:


nb["Weight"].mul(0.453592)


# In[22]:


nb["Weight"]*0.453592


# In[23]:


nb["Weight in kilograms"]=nb["Weight"]*0.453592


# In[24]:


nb.head(3)


# In[25]:


nb["Salary"].div(1000000)


# In[26]:


nb["Salary in Million"]=nb["Salary"]/1000000


# In[27]:


nb.head(3)


# In[28]:


data=pd.read_csv('dataset session 7 Pandas nba.csv')
data.head()


# In[29]:


data["Team"]


# In[31]:


data["Team"].value_counts()


# In[32]:


data["Position"].value_counts()


# In[33]:


data["Weight"].value_counts()


# In[34]:


data["Weight"].value_counts().tail(3)


# In[35]:


data["Salary"].value_counts()


# In[ ]:




