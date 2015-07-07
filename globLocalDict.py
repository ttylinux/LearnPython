def foo():
    print('\ncalling foo()...')
    aString = 'bar'
    anInt = 42
    print('foo()\' globals:',globals().keys())
    print('\nfoo()\' locals:',locals().keys()) #local key asString,anInt

print('__main__\'s globals:',globals().keys())
print('\n__main__\'s locals:',locals().keys)
foo()