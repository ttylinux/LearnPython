#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class AnyIter(object):
    def __init__(self,data,safe=False):
        self.safe = safe
        self.iter = iter(data) #从对象data获取一个Iterator
		
    def __iter__(self):
        return self
		
    def __next__(self,howmany=1):
        retval = []
        for eachItem in range(howmany):
            try:
                retval.append(self.iter.__next__())
            except StopIteration:
                if self.safe:
                    break
                else:
                    raise
        return retval
		
#--------main----------------------
a = AnyIter(range(10))
oneIterator = iter(a) #从对象a中获取该对象的迭代器
for j in range(1,5):
    print(j,':',oneIterator.__next__(j)) #调用__next__(self,howmany=1) 
	                                     #迭代器oneIterator，每次返回的值是一个retval数组
										 #数组retval，是AnyIter.data数据集的一个迭代结果
										 #传入参数howmany，决定了返回的值的大小，该值不能大于AnyIter.data的大小
print('------------------------test--------------------')

b = AnyIter(range(5))
bIter = iter(b)
print(bIter.__next__(5))


print('-------------------test--------------------------')

#c = AnyIter(range(5))
#cIter = iter(c)
#print(bIter.__next__(6))

print('-------------------test--------------------------')

d = AnyIter(range(5),True) #设置safe参数为True，这样，在捕捉道异常StopIteration时，可以正常退出for循环，从而可以正常返回retval值。
                           #如果不设置，则会继续将异常往上抛，这样就不会执行return retval
dIter = iter(d)
print(dIter.__next__(6))