# -*- coding: utf-8 -*-
"""
Created on Tue May  5 02:04:57 2020

@author: filiz.aksoy
"""



def factors(a):
    factors = []
    if a%2 == 0 :
        factors.append(2)
    for i in range(3,a//2,2):
        if(a%i == 0):
            factors.append(i)
    return factors
