#!/usr/bin/env python
# coding: utf-8

# # Select One Column from a DataFrame

# In[ ]:


import pandas as pd


# In[ ]:


nb=pd.read_csv('C:\\Users\\Ali\\Desktop\\dataset session 7 Pandas nba.csv')
nb.head(3)


# In[ ]:


nb.Name.head(3)


# In[ ]:


nb.Number


# In[ ]:


nb.Salary


# In[ ]:


nb.salary


# In[ ]:


nb.Number
nb.Salary
output=None


# In[ ]:


nb["Name"]


# In[ ]:


nb["Salary"]


# In[ ]:


type(nb["Name"])


# In[ ]:


nb["Name"].head(3)


# In[ ]:




