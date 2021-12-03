# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 00:21:16 2021

@author: Shaker
"""

def jumpingOnClouds(c):
    jumps = 0
    i=0
    while i< len(c)-2:
        #print(i, c[i])
        if(c[i+1] == 0 and c[i+2] == 0):
            jumps +=1
            i +=2
        elif(c[i+1] == 0 and c[i+2] == 1):
            jumps +=1
            i +=1
        elif(c[i+1]==1 and c[i+2]==0):
            jumps +=1
            i +=2    
        #print(i)
    try:
        if c[i+1] == 0:
            jumps +=1
    except:
        pass
    # if(c[i+1]==0):
    #     jumps +=1
    return(jumps)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))
    #print(c)

    result = jumpingOnClouds(c)