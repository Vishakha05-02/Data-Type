#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#python data type---> Tuple---> immutable data type. we cannot change any itme of Tuple. 


# In[3]:


#Empty tuple
My_tuple = ()
type(My_tuple)


# In[5]:


My_tuple = ("apple", "banana", "cherry", "mango")
print(My_tuple)


# In[7]:


My_tuple[1]


# In[8]:


print(My_tuple[2])


# In[11]:


# negative index
My_tuple[-1]


# In[12]:


#Range of index
My_tuple[0:2]


# In[18]:


# change of tuple element will give error because it is immutable data type. we can change tuple into a list.

My_tuple = ("apple", "banana", "cherry", "mango")
y = list(My_tuple)
print(type(y))


# In[19]:


print(y)


# In[20]:


y[1] = "kiwi"

My_tuple = tuple(y)

print(My_tuple)


# In[15]:


#length of a tuple
len(My_tuple)


# In[21]:


#tuple with only one element
T = ("vishakha")
type(T)


# In[22]:


T = ("vishakha",)
type(T)


# In[23]:


#deleting tuple with del function
del My_tuple


# In[24]:


print(My_tuple)


# In[ ]:




