

#*args被解释为一个tuple，元组
def foo(*args):
    for item in args:
        print(item)

#**kwargs被解释为一个键值对key-value中的Key
def bar(**kwargs):
    for key in kwargs:
        print(key,kwargs[key])
	

#解包参数列表,*l
#unpack argument lists	
def test(one,two):
    print(one,two)

list = ['one','two']
test(*list) #解包参数列表
print('------------------------')



foo(1,2,45)
print('------------------------')
foo('a','b','def')
print('------------------------')
bar(name='peter',age=25)
print('------------------------')
bar(country='China',city='SH')
print('-----------------------')

