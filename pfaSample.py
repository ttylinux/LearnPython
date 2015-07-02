from functools import partial


print(int('11',base=10))
print(int('11', base=8))

#偏函数，使用现有的函数，对现有函数的默认参数进行定制,固定，获得一个新的函数
baseTwo = partial(int,base=2)
print(baseTwo('11'))

