# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 00:51:27 2021

@author: Shaker
"""

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#MyBook class implementing Book class
class MyBook(Book):
    def __init__(self, title, author, price):
        self.title=title
        self.author=author
        self.price = price
    def display(self):
        print('Title: ' + title )
        print('Author: ' + author )
        print('Price: ' + str(price) )
title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()