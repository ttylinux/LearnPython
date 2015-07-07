#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import types
import classSample
def isAFunction(fn):
    if type(fn)==types.FunctionType:
        print('It is a function.')
    else:
        print('It is not a function.')
	
def isADog(dog):
    if isinstance(dog,Dog):
        print('It is a dog')
    else:
        print('It is not a dog')
