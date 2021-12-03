# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 18:16:46 2021

@author: Shaker
"""

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        divisors = []
        for i in range(n):
            if i==0:
                continue
            if n%i==0:
                divisors.append(i)
        return(sum(divisors)+n)


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)