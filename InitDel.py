#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class InstCt(object):
    count = 0 # 类的一个静态变量

    def __init__(self):
        InstCt.count += 1

    def __del__(self):
        InstCt.count -= 1

    def howMany(self):
        return InstCt.count


def test():
    a = InstCt()
    b = InstCt()
    print(a.howMany(),'\n')
    del b
    del a
    print(InstCt.count)
