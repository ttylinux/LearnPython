#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Time60(object):
    'Time60 - track hours and minute'
	
    def __init__(self,hr,min):
        'Time60 constructor - takes hours and minutes'
        self.hr = hr
        self.min = min
		
    def __str__(self):
        'Time60 -string representation'
        return '%d:%d' % (self.hr,self.min)

    __repr__ = __str__
	
    def __add__(self,other):
        'Time60 0 overloading the addition operator'
        return self.__class__(self.hr+other.hr,self.min+other.min)

    def __iadd__(self,other):
        'Time60 - overloading in-place addition'
        self.hr += other.hr
        self.min += other.min
        return self
		
print('-------------------------------------')
one = Time60(10,35)
print(one)		
print('-------------------------------------')

today = Time60(12,10)
other = today+one
print('one+today :',other)
print('id of \'one+today\':',id(other))
print('-------------------------------------')

print('today:',today)
print('id of today:',id(today))
print('-------------------------------------')

today += one
print('today+= one:',today)
print('id of today:',id(today))
print('-------------------------------------')
