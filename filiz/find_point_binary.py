# -*- coding: utf-8 -*-
"""
Created on Tue May  5 02:11:54 2020

@author: filiz.aksoy
"""


def find_binary(b):
    binary = []
    q = 1
    while (b>= 2):
        q = b//2
        r = b%2
        binary.append(r)
        b = q
    binary.append(q)
    return binary