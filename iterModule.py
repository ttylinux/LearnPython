#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import choice

class RandSeq(object):
    
    def __init__(self,seq):
        self.data = seq
		
    def __iter__(self):
        return self
	
    def __next__(self):
        return choice(self.data)
		
oneTuple = ('rock','paper','scissors')
#for eachItem in RandSeq(oneTuple):
#    print(eachItem)

one = RandSeq(oneTuple)
while True:
    try:
	    #使用next方法获得下一个值，调用的是one实例的__next__方法
	    print(next(one))
    except StopIteration:
	    #遇到StopIteration就退出循环
        break