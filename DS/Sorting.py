# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 20:42:38 2021

@author: Shaker
"""

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
sc = 0
i=0
while i <len(a)-1:
    if a[i]>a[i+1]:
        sc +=1
        a[i] = a[i+1]
    i +=1
#print(a)