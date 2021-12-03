# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 18:57:34 2021

@author: Shaker
"""

def countX(ar, x): 
    return ar.count(x)

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    uar = list(set(ar))
    counts = []
    pairs =[]
    for x in uar:
        c = countX(ar, x)
        counts.append(c)
    for c in counts:
        p = int(c/2)
        pairs.append(p)
    return sum(pairs)        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)