# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 19:04:56 2022

@author: marco
"""

# l=30
# tarifas=[3,5,7,10,13]
# l=15
# tarifas=[7,10,13,15,17]
# l=19
# tarifas=[10,20,30,40,50]
l=19
tarifas=[3,5,7,10,13]

def solution(l,tarifas):
    pre=200
    tipouber=["UberX","UberXL","UberPlus","UberBlack","UberSUV"]
    resultado=""
    
    costo=0
    for i,j in enumerate(tarifas):
        costo=j*l
       
        if costo>pre:
            resultado=tipouber[i-1]
            break
    return resultado
print("El tipo de Uber elegido es: "+solution(l,tarifas))
        
        
    