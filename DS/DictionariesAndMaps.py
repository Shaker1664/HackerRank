# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 19:54:48 2021

@author: Shaker
"""

n = int(input())

Dict = {}
k = []
for i in range(n):
    name, number = input().split()
    Dict[name] = number


#taking unknown number of inputs
while True:
    try:
        inp = input()
        k.append(inp)
    except EOFError:
        break
       

#print(len(k))
    
for x in k:
     if Dict.get(x):
         print(x+"="+Dict[x])
     else:
         print("Not found")
    