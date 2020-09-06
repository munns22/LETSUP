#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT 1

# In[1]:


#LIST
#Q1)
lst=['ram',12.5,22,'a']
print(lst)


# In[2]:


print(lst[3])


# In[3]:


lst.append('mrunal')


# In[4]:


print(lst)


# In[5]:


lst.insert(2,123)


# In[6]:


print(lst)


# In[7]:


lst1=[1,4,6]
lst.extend(lst1)
print(lst)


# In[11]:


lst2=[1,2,4,5,6,5,6,5,7,5,8,4,9]
print(lst2.count(5))


# In[12]:


print(len(lst2))


# In[13]:


#DICT
#Q2)
dct={'name':'Mrunal','phno':'123456789'}
print(dct)


# In[15]:


dct.pop('name')
print(dct)


# In[16]:


dct1={'name':'ram',"address":"pune","phno":"123456"}
x=dct1.copy()
print(x)


# In[17]:


dct1.get('address')


# In[18]:


dct.clear()


# In[19]:


print(dct)


# In[21]:


dct1.update({'nickname':'shyna'})
print(dct1)


# In[22]:


#SET
#Q3)
fruits = {"apple", "banana", "cherry"}

fruits.add("orange")

print(fruits)


# In[24]:


x = fruits.copy()

print(x)


# In[25]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)


# In[26]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)


# In[27]:


fruits = {"apple", "banana", "cherry"}

fruits.clear()

print(fruits)


# In[28]:


#TUPLE
#Q4)
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)


# In[29]:


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)


# In[30]:


#strings
#Q5)
txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)


# In[33]:




x = txt.casefold()

print(x)


# In[35]:


txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)


# In[36]:


txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)


# In[37]:


txt = "banana"

x = txt.center(20)

print(x)


# In[ ]:




