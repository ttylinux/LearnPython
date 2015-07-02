
#闭包就是，一个内部函数，可以访问该内部函数所在函数的内容，除了自身的局部作用域之外的变量
#比如下述，内部函数incr，访问了所在函数的count。counter包含了incr函数，并且访问了counter所在变量count
#count是在counter作用域，不是在incr作用域.
def counter(start_at):
    count = start_at
    def incr():
        result=count+1
        return result
    return incr
	
	

count = counter(5)
print(count())
print(count())

count2 = counter(100)
print(count2())

#内部函数sum，并不进行计算。lazy_sum，返回一个闭包，该闭包包含了外部函数的参数，和自身的计算过程
#只有调用内部函数的时候，才进行计算
print('------------------------------')
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

	
f = lazy_sum(1,3,5,7,9)
print(f()) #调用内部函数，执行计算

