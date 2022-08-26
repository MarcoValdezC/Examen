# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 23:33:59 2022

@author: marco
"""

#m=[[1,1,1],[1,0,1],[1,1,1]]
#m=[[0,2],[0,4]]
m=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
x=[]
y=[]
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j]==0:
            x.append(i)
            y.append(j)
for r in range(len(x)):
    for t in range(len((m[0]))):
        m[x[r]][t]=0

for e in range(len(y)):
    for w in range(len((m))):
        m[w][y[e]]=0
print(m)
        

