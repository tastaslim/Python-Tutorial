"""
    Generally, we use *args so that we can have variable number of parameters inside a function. args is of type tuple.
    Say you want to write a function which works for any number of argument, you can use args there in case
    1.)*args (Non-Keyword Arguments ==> tuple)
    2.)**kwargs (Keyword Arguments ==> dictionary)
"""


def summation(a, b, *args, **kwargs):
    add = a + b
    print(type(args))
    print(type(kwargs))
    for i in args:
        add += i
    return add


print(summation(1, 2))  # works
print(summation(12, 13, 1, 1, 2, 3, 4))  # works
# print(summation(1))   gives error

"""
    **kwargs is of linkedlist type. It is keyword arg, meaning we pass key value pair like we do in linkedlist
    Note: Below must be order of these types passed to function as parameter: 
    Normal -> args ->kwargs
    
    Meaning you can not pass **kwargs as parameter before *args or normal parameters. Same goes for
    *args as we can not pass it before normal parameters.
"""
