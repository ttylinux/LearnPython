#-*-coding:utf-8-*-

import math


def quadratic(a,b,c):
    one = not isinstance(a,(int,float))
    two = not isinstance(b,(int,float))
    three = not isinstance(c,(int,float))
    if one|two|three:
	    raise TypeError('bad operand type!!')
    else:
        sqrtValue = math.sqrt(b*b - 4*a*c)
        valueOne = (-b+sqrtValue)/(2*a)
        valueTwo = (-b-sqrtValue)/(2*a)
        return valueTwo,valueOne
		

print(quadratic(2,3,1))
