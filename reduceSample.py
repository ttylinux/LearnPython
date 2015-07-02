from functools import reduce



def mySum(x,y):
    return x+y

#reduce方法，接收一个二元函数，一个数据源
#然后，reduce不断对数据源中的每两个元素应用二元函数
#最后，获得一个结果。
#这是一个折叠的过程
result = reduce(mySum,[1,3,5,7])
print(result)

result = reduce(mySum,['a','b','c','d'])
print(result)