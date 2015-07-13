#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class OneClass(object):

    def __init__(self):
        self.__superprivate = 'superprivate'
        self._semiprivate = 'semiprivate'

		
		
		
		
#---------main------------------

one = OneClass()
#print(one.__superprivate)
print(one._semiprivate)