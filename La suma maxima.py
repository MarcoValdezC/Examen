# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 19:27:44 2022

@author: marco
"""
#l=[-1,2,1,3,-2]
#l=[,2,3]
#l=[51,41,3,30,32]
l=[53,36,35,85,46]


def solution(l):
    aux=1
    re=[]
    for j in range(len(l)):
        val_max=0
        val=0
        for i in range(len(l)-j):
            
            val=sum(l[i:i+aux])
            
            if val>val_max:
                val_max=val
                r=i
        re.append(r)
        aux+=1
    return re
print(solution(l))
    
    
    
    
    
