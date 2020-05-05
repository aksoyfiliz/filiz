# -*- coding: utf-8 -*-
"""
Created on Tue May  5 02:13:00 2020

@author: filiz.aksoy
"""

from find_sum_points import solution

def power(num,root, A, p):
    result = [root]
    for i in range(num):
        x1 = root[0]
        y1 = root[1]
        root, count_a = solution(x1, y1, x1, y1, A, p)
        result.append(root)
    return result

