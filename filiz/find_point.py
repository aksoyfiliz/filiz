# -*- coding: utf-8 -*-
"""
Created on Tue May  5 02:21:53 2020

@author: filiz.aksoy
"""


def find_point(c,p,A,B):
    result = []
    for x in range (p):
        for y in range (p-1):
            y_square = (y*y)%p
            f_x = (x**3 + A*x + B)%p
            if (y_square == f_x):
                result.append([x,y])
                c -= 1
                if (c==0):
                    return result
                    
    return result  