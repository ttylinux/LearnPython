#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._width = value

s = Student()
s.width = 60
print('s.score =', s.width)
# ValueError: score must between 0 ~ 100!
s.width = 9999