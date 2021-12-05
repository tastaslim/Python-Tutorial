"""
    Generally, we use *args so that we can have variable number of parameters inside a function. args is of type tuple.
    Say you wan to write a function which works for any number of argument, you can use args there in case
    1.)*args (Non-Keyword Arguments)
    2.)**kwargs (Keyword Arguments)
"""


def summation(a, b, *args, **kwargs):
    sum = a+b
    print(type(args))
    print(type(kwargs))
    for i in args:
        sum += i
    return sum


print(summation(1, 2))  # works
print(summation(12, 13, 1, 1, 2, 3, 4))  # works
# print(summation(1))   gives error

"""
    **kwargs is of dict type. It is keyword arg, meaning we pass key value pair like we do in dict
    Note: Order must be: 
    Normal -> args ->kwargs
"""
