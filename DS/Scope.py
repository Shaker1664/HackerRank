# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 12:30:33 2021

@author: Shaker
"""

class Difference:
    def __init__(self, a):
        self.__elements = a
    maximumDifference = 0
    def computeDifference(self):
#        i=0
        s = sorted(self.__elements)
        l = len(s)
        f = s[0]
        ls = s[l-1]
        self.maximumDifference = abs(f-ls)
        return self.maximumDifference
            
	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)