from random import randint
from random import randint as ri

def odd(n):
    return n % 2
	
	
	
allNums = []
for eachNum in range(9):
    allNums.append(randint(1,99))

#display orignal data	
print('allNums:',allNums)

#use generator to filter data
result=(item for item in allNums if odd(item))
for item in result:
    print(item)
print('---------------------')

# use filter method 
resultFilter = filter(odd,allNums)
for item in resultFilter:
    print(item)
print('-----------------------')	



#use lambda to subsititue odd function
resultFilter = filter(lambda n:n%2,allNums)
for item in resultFilter:
    print(item)

	

	
print('----------------------')	
print('Use list comp to generate allNums')	
#use list comprehensions to generate allNums
#result=(item for item in allNums if odd(item))
result = (item for item in [ri(1,99) for i in range(9)] if item % 2)
for item in result:
    print(item)