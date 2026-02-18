#!/usr/bin/env python
# coding: utf-8

# Answers for Week 1
# 
# * Name: Tamara Balvin
# * Username: tbalvin
# * Student s-number: S6217451
# * Group (AS1, etc.): AS1

# In[1]:


x = 22/7


# $$y=\frac{sin(x)}{x}$$

# In[4]:


pi = 22/7 # Processed on Jupyter Hub


# In[6]:


x=6
for i in range(5):
    x*=(5-i)
print(x)


# In[7]:


from scipy.constants import c, h
freq = 2.42e28
energy = h * c / freq
print(energy)


# In[2]:


from scipy.constants import G
m1 = 7.342e22
m2 = 5.9722e24
r = 385000600
force = G * m1 * m2 / (r**2)
print("force: ", force, 'N')


# In[11]:


from scipy.constants import G, pi, au
period = 365*24*60*60
total_mass = (4*(pi**2)*(au**3))/(G*(period**2))
print(total_mass)


# In[12]:


x1 = 10
x2 = 22/7
print(x1, end="")
print(x2, end="")

