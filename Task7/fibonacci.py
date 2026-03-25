#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Fibonacci:
    """Class for calculating Fibonacci sequence"""
    
    def __init__(self, N, M):
        self.N = N
        self.M = M
        
    def nterm(self):
        a = 0
        b = 1
        terms = [0,1]
        for i in range(self.N-2):
            c = a+b
            terms += [c]
            a = b
            b = c
        return terms
    
    def divmterm(self):
        nterms = self.nterm()
        terms2 = []
        for i in nterms:
            try:
                if i%self.M == 0:
                    terms2 += [i]
            except ZeroDivisionError:
                print("Cannot divide by zero.")
                break
        return terms2

test = Fibonacci(100,7)
print(test.nterm())
print(test.divmterm())

