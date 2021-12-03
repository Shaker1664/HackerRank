# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 21:58:42 2021

@author: Shaker
"""

def countingValleys(steps, path):
    # Write your code here
    count = 0
    counter = 0
    for x in path:
        if x == 'U':
            count += 1
        if x == 'D':
            count -=1
        print(count, x)
        if count == 0 and x == 'U':
            counter +=1
        
    return(str(counter))


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)