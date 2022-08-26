# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 21:55:53 2022

@author: marco
"""
# a="1000"
# b="111"
# a="1"
# b="1"
# a="1101"
# b="111"
a="11110011010110000010110"
b="1"

def solution(a,b):
    
    r=""
    aux=0
    la=len(a)
    lb=len(b)
    while lb!=la:
        
        if(la>lb):
            b="0"+b
            lb+=1
        elif(lb>la):
            a="0+a"
            la+=1
    for i in range(len(a)):
        s=int(a[-(i+1)])+int(b[-(i+1)])+aux
        
        if s==2:
            aux=1
            r="0"+r
        elif s==3:
            r="1"+r
            aux=1
        else:
            r="1"+r
            aux=0
        s=0
    if aux==1:
        r="1"+r
    return r
print(solution(a,b))


        
    