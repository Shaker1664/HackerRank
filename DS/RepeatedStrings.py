# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 18:05:21 2021

@author: Shaker
"""

def repeatedString(s, n):
    c = s.count("a")
    i= (n // len(s))
    j =s[:n % len(s)].count("a")
    # while i < n:
    #     if s[i] == 'a':
    #         count +=1
    #     i+=1
    return (c*i+j)

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)