#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import matplotlib.pyplot as mpp
import numpy 
import cmath 

ITERATIONS = 50

def mycos(x):
  value = 0
  multiplayr = 1 
  sign = 1
  for i in range(0, ITERATIONS):
    value += sign * (multiplayr / math.factorial(2 * i))
    sign *= -1 
    multiplayr *= x**2
  return value 


argumments = numpy.arange(0,50,0.1)
mpp.plot(argumments,[math.cos(a) for a in argumments])
mpp.plot(argumments, [mycos(a) for a in argumments])
mpp.show()


# In[ ]:




