# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 08:31:05 2022

@author: marco
"""

m=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

for i in range(len(m)):
    for j in range(len(m)):
        if i>j:
            aux=m[i][j]
            m[i][j]=m[j][i]
            m[j][i]=aux
print(m)

for r in range(len(m)):
    for f in range(int(len(m)/2)):
        aux2=m[r][f]
       
        
        m[r][f]=m[r][len(m)-(f+1)]
        m[r][len(m)-(f+1)]=aux2
print(m)