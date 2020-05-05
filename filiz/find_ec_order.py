# -*- coding: utf-8 -*-
"""
Created on Tue May  5 02:23:44 2020

@author: filiz.aksoy
"""
from find_point_binary import find_binary
from find_power_points import power
from find_sum_points import solution

def find_order(p, P, A, B):
    border1 = int(((p**(1/2))-1)**2) + 1
    border2 = int(((p**(1/2))+1)**2) + 1
    print("For the equation E : y^2 = x^3 + {}x + {} over Fp where p={} and the point P = {}".format(A,B,p,P))
    print("\tHasse-Weil bound is  {} <= I <=  {}".format(border1, border2))
    for a in range (border1, border2):
        sum_result=[]
        result_binary = find_binary(a)
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
            if (count_a == True):           
                if (len(sum_result) == 2):
                    order = a
                    break
            sum_result.pop()
            sum_result.pop()
            sum_result.append(new_x_y)
            
    print("\tThe order is {}".format(order))
    return(order)
    