# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 11:30:35 2022

@author: marco
"""

from math import gcd

def solution(n):
    r = 0        
    for i in range(1, n + 1):
        if gcd(n, i) == 1:
            r += 1
    return r
n=49
print(solution(69))