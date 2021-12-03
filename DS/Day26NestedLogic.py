# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 21:30:12 2021

@author: Shaker
"""
from datetime import date

def fines(dateReturned, dueDate):
    fines = 0
    rday, rmonth, ryear = map(int, dateReturned.split(' '))
    returnDate = date(ryear, rmonth, rday)
    dday, dmonth, dyear = map(int, dueDate.split(' '))
    dueD = date(dyear, dmonth, dday)
    
    diff = returnDate - dueD
    if diff.days > 0:
        if rmonth == dmonth and ryear == dyear:
            fines = 15 * diff.days
            return fines
        if rmonth > dmonth and ryear == dyear:
            fines = 500 * (rmonth - dmonth)
            return fines
        if ryear > dyear:
            return 10000
    else:
        return fines
    
    
    
print("Enter return date: ")
returndate = input()
print("Enter due date:")
duedate = input()
#print(fines('03 06 2021', '05 05 2021'))
print(fines(returndate, duedate))

# date = input("Enter date in DD MM YYYY YYYY-MM-DD format")
# year, month, day = map(int, date.split(' '))