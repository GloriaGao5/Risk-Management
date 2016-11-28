# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 21:44:40 2016

@author: Duanhong
"""

import numpy as np
import scipy.stats as ss
import pandas as pd
import math 
import matplotlib.pyplot as plt
import datetime as dt


path = '~/Documents/Semester3/M5320/homework/HW10/Hw10.csv'
sto_AMD= pd.read_csv(path, header = 1)  

data1 = sto_AMD.values
AMD_close = list(data1[:,1])
sto_AMD.shape
##### formula VaR #########  

A_log_rtn = []
A_log_rtn_sq = []

for i in range(1 ,len(data1)-1):
    log_return = math.log( AMD_close[i]/AMD_close[i+1] )
    A_log_rtn.append(log_return)
    A_log_rtn_sq.append(log_return**2) 
    
def vol_and_mu(years):
    S0 = 10000000
    T = 5/252
    p = 0.99
    
    A_vol_years = []
    A_mu_years = []
    A_VaR_years = []
    A_ES_years =[]
    
##### GBM Formula VaR and ES #######    
    for i in range(len(data1) - 252*years):
        vol_years = np.std(A_log_rtn[i:i+252*years]) * np.sqrt(252)
        mu_years = np.mean(A_log_rtn[i:i+252*years])*252 + (vol_years**2)/2
        VaR_years = S0 - S0 * np.exp( vol_years * T**(0.5)* ss.norm.ppf(1-p) + (mu_years - pow(vol_years,2)/2)*T )
        ES_years = S0 * (1 - np.exp(mu_years *T)/(1-0.975) * ss.norm.cdf(ss.norm.ppf(1-0.975) - T**(0.5)*vol_years))
        
        A_vol_years.append(vol_years)
        A_mu_years.append(mu_years)
        A_VaR_years.append(VaR_years)
        A_ES_years.append(ES_years)
       
    return(A_vol_years, A_mu_years, A_VaR_years, A_ES_years)

A_vol_years = vol_and_mu(5)[0][1:252*10]
A_mu_years = vol_and_mu(5)[1][1:252*10]
A_VaR_5years = vol_and_mu(5)[2][1:252*10]

print(A_mu_years[0], A_vol_years[0], A_VaR_5years[0])
