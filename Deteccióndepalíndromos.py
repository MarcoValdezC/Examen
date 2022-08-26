# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 21:28:27 2022

@author: marco
"""
# precios=[110,95,70]
# notas=["10.0% mas alto","5.0% mas bajo", "mismo que en tienda"]
#x=5
# precios=[48,165]
# notas=["20.0% mas alto","10.0% mas bajo"]
# x=2
precios=[24.42,24.42,24.2424,85.23]
notas=["13.157% mas alto","13.157% mas bajo","mismo que en tienda","19.24% mas alto"]
x=0
def solution(precios,notas,x):
    
    aux=0
    for i in range(len(precios)):
    
        if "alto" in notas[i]:
            n=notas[i].split()[0].split("%")
            f=float(n[0])/100
            aux+=(precios[i]*f)/(1+f)
            
            
        elif"bajo" in notas[i]:
            n=notas[i].split()[0].split("%")
            f=float(n[0])/100
            aux-=(precios[i]*f)/(1-f)
        else:
            aux=aux
           

    if aux<=x:
        return True
    else:
        return False
print(solution(precios,notas,x))
