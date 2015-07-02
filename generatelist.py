
L = ['Hello','World',18,'Apple',None]
NewL = [s.lower() for s in L if isinstance(s,str)]
print(NewL)