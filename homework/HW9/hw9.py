# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 10:46:55 2016

@author: Duanhong
"""

import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

def survival_func(B):
    d = (np.log(10000000/B) + 0.15)/(0.2 * np.sqrt(5))
    y = 1 -  ss.norm.ppf(-d)
    return(y)

B = np.arange(0.0, 1e+8, 1)

plt.figure()
plt.plot(B, survival_func(B))
plt.title('Spot spread for lambda = 0.03') 
plt.show()
lines = plt.plot([1,1])