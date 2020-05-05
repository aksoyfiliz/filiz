# -*- coding: utf-8 -*-
"""
Created on Tue May  5 02:29:49 2020

@author: filiz.aksoy
"""
from find_point_binary import find_binary
from find_power_points import power
from find_sum_points import solution

def find_muliplication(p,P,A,B, num):
    sum_result=[]
    result_binary = find_binary(num)
    b = len(result_binary)-1
    power_list = power(b,P, A, p)
    for i in range(len(result_binary)):
        if result_binary[i] == 1:
            sum_result.append(power_list[i])

    new_x_y = []       
    while len(sum_result) >= 2:
        p11 = sum_result[-1][0]
        p12 = sum_result[-1][1]
        p21 = sum_result[-2][0]
        p22 = sum_result[-2][1]
        new_x_y, count_a = solution(p11,p12,p21,p22,A,p)
        sum_result.pop()
        sum_result.pop()
        if (count_a == False):
            sum_result.append(new_x_y)
        
    return(sum_result)
    
find_muliplication(3409573,[0,64],723,4096,11)
