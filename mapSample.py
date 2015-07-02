
#map对数据源中的每个列表应用函数lambda，得到一个新的列表
result = map(lambda x,y,z: x+y+z,'abc','def','ghk')
for  item in result:
    print(item)
	
	
def add(x):
    return x+2
	
result = map(add,[1,3,5])
for item in result:
    print(item)

