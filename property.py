#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ScreenOne(object):

		
    @property
    def width(self):
        return self._width   
    
    @width.setter
    def width(self,value):
        if(value < 0):
            raise ValueError('value is not valid') 
        self._width = value
			




