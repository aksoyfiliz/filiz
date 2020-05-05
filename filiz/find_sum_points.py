# -*- coding: utf-8 -*-
"""
Created on Tue May  5 02:09:24 2020

@author: filiz.aksoy
"""
def gcd_EE(a,b):
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a
    
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r-q*r
        old_s, s = s, old_s-q*s
        old_t, t = t, old_t-q*t
        
    return old_r, old_s, old_t

def extended_euclidian(n,p):
    gcd, x, y = gcd_EE(n,p)
    assert (n*x + p*y) %p == gcd
    
    if gcd !=1:
        raise ValueError("{} has no multiplicative inverse modulo {}".format(n,p))
        
    else: 
        return x%p

def solution(x1,y1,x2,y2,A,p):
    x_y_result = []
    count_a = False    
    if(x1 != x2):
        k = (y2-y1)
        l = (x2-x1)
        t = extended_euclidian(l,p)
        m = (k*t)%p
        x_result = (m*m-x1-x2)%p
        y_result = (m*(x1-x_result)-y1)%p
    elif(y1 != y2):
        x_result, y_result = "I", "I"
        count_a = True
    elif(y1 != 0):
        f = extended_euclidian(2*y1,p)
        m = ((3*(x1**2)+A)*f)%p
        x_result = ((m*m)-(2*x1))%p
        y_result = (m*(x1-x_result)-y1)%p
    else:
        x_result, y_result = "I", "I"
        count_a = True
    x_y_result.append(x_result)
    x_y_result.append(y_result)
        
    return x_y_result, count_a
