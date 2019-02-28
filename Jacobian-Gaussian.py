# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 11:23:52 2019

@author: 耿浩
"""


def iteration(p_0,q_0):
    q = 1+(1/2)*p_0
    p = 10 - q_0
    print(p,q)
    return p,q

i=0
p_0,q_0=4,1
while i<6:
    p,q=iteration(p_0,q_0)
    q_0,p_0=q,p
    i =i+1 
    


