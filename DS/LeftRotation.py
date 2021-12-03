# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 13:24:41 2021

@author: Shaker
"""

def rotLeft(a, d):
    # last = a[:d]
    # rest = a[d:]
    # left  = [*rest, *last]    
    # return (left)
    return a[d:] + a[:d]    
        
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)