#!/usr/bin/env python


#装饰器，使用函数作为输入参数，这个保证，原有的函数功能存在；然后，再添加新的功能。
def myname(fn):
    def wrappedFunc():
        print('myname-Do some decorator')
        fn()
        print('This is in myname_wrappedfunc')
    return wrappedFunc
	

#装饰器
def myage(age):
    def real_decorator(fn):
        def wrappedFunc():
            print('myage-Do some decorator')
            print('Your age:',age)
            fn()
            print('This is in myage_wrappedfunc')
        return wrappedFunc
    return real_decorator

	

#使用装饰器之后，效果等同于 peter = myname(peter),得到一个新的函数。
@myname	
def peter():
    print('This is peter')

#效果等同于 John = myage(25)(John)，也就是John = real_decorator(John)
#那么，在定义带参数的装饰器的时候，就要返回一个函数(real_decorator)来接收John参数
@myage(25)
def John():
    print('This is John')
	
	
#效果等同于myname(myage(25)(Jack))
#先得到经过myage修饰的新函数Jack_age,然后，该函数，再被myname修饰
#输出结果是:
#myname-Do some decorator
# 调用Jack_age()函数
#This is myname_wrappedfunc
@myname
@myage(25)
def Jack():
    print('I am Jack')
	
#func define



peter()
print('-----------------Decorator with param------------------')
John()
print('----------------- More Decorator with param------------------')
Jack()
