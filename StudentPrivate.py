#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
		

    def getName(self):
        return self.__name

    def getScore(self):
        return self.__score
		
    def setName(self,name):
        self.__name = name
		
    def setScore(self,score):
        self.__score = score
		
		
    def print_score(self):
        print('%s: %s'%(self.__name,self.__score))
		