#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running...')
		
class Dog(Animal):
    def run(self):
        print('Dog is running..')
		
	
class Cat(Animal):
    def run(self):
        print('Cat is running...')
		
		
def run_twice(animal):
    if isinstance(animal,Animal):
        animal.run()
    else:
        print('param type is incoreect,please make sure the param type is Animal')
    
def run_test(animal):
    animal.run()
	
class ClassLikeAnimal(object):
    def run(self):
        print('ClassLikeAnimal is doing something')
		
