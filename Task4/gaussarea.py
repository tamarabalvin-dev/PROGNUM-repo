#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np, matplotlib.pyplot as plt, scipy

def gauss(x, A, x0, sigma, z0):
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0

A = int(input('A = '))
x0 = int(input('x0 = '))
sigma = int(input('sigma = '))
z0 = int(input('z0 = '))
min_lim = int(input('Lower integration limit = '))
max_lim = int(input('Upper integration limit = '))

area = scipy.integrate.quad(gauss, min_lim, max_lim, args=(A,x0,sigma,z0))

x = np.linspace(-10,10,200)
y = gauss(x, A, x0, sigma, z0)

plt.scatter(x,y)
plt.fill_between(x, y, 0, color='seagreen', alpha=0.5, label=f'Integration area = {area[0]:.2f}')
plt.legend()
plt.show()

