#!usr/bin/env python

output = '<int %r id=%#0x  val = %d>'
w = x = y = z = 1


#__closure__的含义None or a tuple of cells that contain bindings for the function’s free variables.
#函数定义
def f1():
    x = y = z = 2

def f2():
    y = z = 3
    def f3():
        z = 4
        print(w)
        print(x)
        print(y)
        print(z)
		
    clo = f3.__closure__
    if clo:
        print('f3 closure vars:',[str(c) for c in clo])#

    else:
        print('no f3 closure vars')

    f3() #在f2中调用f3

    clo = f2.__closure__
    if clo:
        print('f2 closure vars:',[str(c) for c in clo]) 
    else:
        print('no f2 closure vars')


#函数定义

		
f2() #执行f2
clo = f2.__closure__
if clo:
    print('f2 closure vars:',[str(c) for c in clo])
else:
    print('no f2 closure vars')

clo = f1.__closure__
if clo:
    print('f1 closure vars:',[str(c) for c in clo])
else:
    print('no f1 closure vars')

f1() #执行f1