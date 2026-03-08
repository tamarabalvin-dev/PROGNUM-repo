#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from numpy import sin, cos, exp, pi
import scipy

inp = input('Input function: f(x) =')   #user input

def function(x):
#returns evaluated function from user input, in case of an error raises error message
    try:
        return np.ones_like(x) * eval(inp)   #np.ones_like(x) returns array for Monte Carlo method (needed when input is a scalar)
    except:
        raise NameError 

#quad() integration
try:
    integral1 = scipy.integrate.quad(function,0,pi)
except NameError:
    print(f'Invalid function, cannot perform integration using function quad().')   #prints error for a function the code cannot evaluate
else:
    print(f'Integration using the quad() function: {integral1[0]:.3f}')

#Monte Carlo integration
a = 0
b = pi
N = 100000   #customizable variables
x_array = np.random.uniform(a,b,N)   #values of x to "integrate"
try:
    integral2 = ((b-a)/N)*np.sum(function(x_array))   #Monte Carlo method
except NameError:
    print(f'Invalid function, cannot perform integration using Monte Carlo.')   #same as for the quad() method
else:
    print(f'Integration using Monte Carlo: {integral2:.3f}')


# In[ ]:




