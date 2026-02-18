#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Date input

Y = int(input('year: '))
M = int(input('month: '))
D = float(input('day: '))

#Formula

JD = 367*Y -7*(Y+(M+9)//12)//4 - 3*((Y+(M-9)//7)//100 + 1)//4 + (275*M)//9 + D + 1721029-0.5

print(f'the Julian Date is {JD}')


# In[ ]:


#comparing two dates

print('DATE 1')
Y1 = int(input('year: '))
M1 = int(input('month: '))
D1 = float(input('day: '))

JD1 = 367*Y1 -7*(Y1+(M1+9)//12)//4 - 3*((Y1+(M1-9)//7)//100 + 1)//4 + (275*M1)//9 + D1 + 1721029-0.5

print('DATE 2')
Y2 = int(input('year: '))
M2 = int(input('month: '))
D2 = float(input('day: '))

JD2 = 367*Y2 -7*(Y2+(M2+9)//12)//4 - 3*((Y2+(M2-9)//7)//100 + 1)//4 + (275*M2)//9 + D2 + 1721029-0.5

dif = JD2 - JD1

print(f'the difference in dates is {dif} day(s)')

