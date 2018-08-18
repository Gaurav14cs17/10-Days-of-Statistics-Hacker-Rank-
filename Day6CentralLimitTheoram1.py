'''
Created on May 29, 2018

@author:Gaurav'''
import math

def cmf(case,mean,std):
    z=(case-mean)/(std*(2**0.5))
    error=math.erf(z)
    return (1+error)*0.5

mean=49*205
std=7*15
case1=9800
result1=cmf(case1, mean, std) 
print(round(result1,4))