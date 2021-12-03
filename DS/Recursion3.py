# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 20:40:48 2021

@author: Shaker
"""

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
    

print(factorial(5))