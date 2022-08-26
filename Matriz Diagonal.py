# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 21:01:47 2022

@author: marco
"""

#m=[[1,0,0],[0,5,0],[0,0,3]]
#m=[[1,0,0],[0,5,0],[1,0,3]]
#m=[[1,0,0],[0,23,0],[0,0,-2]]
m=[[53,21,23,81,92],[75,72,30,39,62],[85,2,75,94,97],[40,31,95,82,30],[16,44,27,55,24]]

flag=False
for i in range(len(m)):
    for j in range(len(m)):
        if i!=j:
            if m[i][j]!=0:
                flag=False
                break
            else:
                flag=True
print(flag)
                
            