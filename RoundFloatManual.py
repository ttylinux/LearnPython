#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class RoundFloatManual(object):
    def __init__(self,val):
        assert isinstance(val,float), 'Value must be a float.'
        self.value = round(val,2)
    def __str__(self):
        return str(self.value)
    __repr__ = __str__ # __repr__方法使用__str__的实现