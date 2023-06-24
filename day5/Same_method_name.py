from multipledispatch import dispatch

"""
In python we can use methods with same name using dispatch module.
In Backend, Dispatcher creates an object which stores different implementation and on runtime, 
it selects the appropriate method as the type and number of parameters passed.
"""


# passing one parameter
@dispatch(int)
def product(first):
    result = first * first
    print(result)


# passing two parameters

@dispatch(int, int)
def product(first, second):
    result = first * second
    print(result)


"""
    By default we can't declare two function with same name and same parameter, because 
    ultimately latest one will be used and previous will be discarded. But using dispatch decorator we can do
    that. It is a bad practice to declare functions with same name, until it is 
    necessary to do that and you have no other option to go for.
"""


@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result)


# you can also pass data type of any value as per requirement


@dispatch(float, int, int)
def product(first, second, third):
    result = first * second * third
    print(result)


# product(2, 3)
product(4.2, 2, 3)
