#!/usr/bin/env python3
# -*- coding: utf-8 -*-

weight = input('input your weight\(kg\):')
height = input('input your height\(m\):')

temp = float(height)*float(height)
bmi = float(weight)/float(temp)

if bmi>32:
    print('Very fat')
elif bmi>=28:
    print('fat')
elif bmi>=25:
    print('overload')
elif bmi >=18.5:
    print('normal')
else:
    print('lighter')