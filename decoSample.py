def simple_decorator(decorator):
    '''This decorator can be used to turn simple functions
    into well-behaved decorators, so long as the decorators
    are fairly simple. If a decorator expects a function and
    returns a function (no descriptors), and if it doesn't
    modify function attributes or docstring, then it is
    eligible to use this. Simply apply @simple_decorator to
    your decorator and it will automatically preserve the
    docstring and function attributes of functions to which
    it is applied.'''
    def new_decorator(f):
        g = decorator(f)
        print('g = decorator(f)')
        g.__name__ = f.__name__
        g.__doc__ = f.__doc__
        g.__dict__.update(f.__dict__)
        return g
    # Now a few lines needed to make simple_decorator itself
    # be a well-behaved decorator.
    new_decorator.__name__ = decorator.__name__
    print('new_decorator.__name__ = decorator.__name__')
    new_decorator.__doc__ = decorator.__doc__
    new_decorator.__dict__.update(decorator.__dict__)
    return new_decorator

#
# Sample Use:
#

# my_simple_logging_decorator = simple_decorator(my_simple_logging_decorator)
@simple_decorator
def my_simple_logging_decorator(func):
    def you_will_never_see_this_name(*args, **kwargs):
        print('calling {}'.format(func.__name__)) 
        return func(*args, **kwargs)
    return you_will_never_see_this_name

# double = my_simple_logging_decorator(double)
# double = simple_decorator(my_simple_logging_decorator)(double) ---先执行simple_decorator的函数体
# double = new_decorator(double) ---然后执行new_decorator的函数体;该方法返回的是没有装饰的my_simple_logging_decorator(double)
# double = my_simple_logging_decorator(double)，这是没有装饰的my_simple_logging_decorator;执行you_will_never_see_this_name的函数体

@my_simple_logging_decorator   
def double(x):
    'Doubles a number.'
    print('Doubles a number.')
    return 2 * x

assert double.__name__ == 'double'
assert double.__doc__ == 'Doubles a number.'
print(double(155))



#输出结果:
#new_decorator.__name__ = decorator.__name__  ---这是simple_decorator的函数体
#g = decorator(f) ---这是new_decorator的函数体
#calling double ---这是you_will_never_see_this_name的函数体
#Doubles a number.---这是double的函数体
#310
