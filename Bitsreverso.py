# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 17:55:50 2022

@author: marco
"""
n=86782
binario=""
while (n>0):
    if(n%2==0):
        binario="0"+binario
        
    else:
        binario="1"+binario
    n=int(n/2)
o=0
print(binario)
for i in range(len(binario)):
    o+=int(binario[i])*(2**i)
  
print(o)
    

