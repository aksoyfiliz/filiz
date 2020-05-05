# -*- coding: utf-8 -*-
"""
Created on Tue May  5 02:08:03 2020

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