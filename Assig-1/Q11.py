# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 18:48:13 2022

@author: nanir"""

"""
Suppose we want to estimate the average weight of an adult male in Mexico. 
We draw a random sample of 2,000 men from a population of 3,000,000 men and 
weigh them. We find that the average person in our sample weighs 200 pounds, 
and the standard deviation of the sample is 30 pounds. Calculate 94%,98%,96% 
confidence interval?
"""

from scipy.stats import t 
import numpy as np
import pandas as pd
m = 200 # Mean
s = 30 # Standard_deviation
n = 2000 # sample size
N = 3000000 # Population Size
dof = n-1 #Degree of freedom i.e. dof = samples numbers-1 
confidence = [0.94,0.98,0.96]

Z = [np.abs(t.ppf((1-confidence[i])/2,dof)) for i in range(len(confidence))] 
# Z-score fom scipy.stats
standard_error= (s/((2000)**0.5))*(((N-n)/(N-1))**0.5)
x=standard_error
confidence_Interval = [[m-Z[i]*x,m+Z[i]*x] for i in range(len(confidence))]
dic={'Confidence':confidence , 'Z_Scores': Z, 'Confidence_Interval':confidence_Interval}
df = pd.DataFrame(dic)
df.to_excel('E:\Assignments\BasicStatistics_Level_1\Q11.xlsx')