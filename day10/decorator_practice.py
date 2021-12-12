def my_decorator(my_func):
    def fun(item):
        print("Hello")
        my_func(item)
        print("World")

    return fun


@my_decorator
def function(item: str):
    print(item)


# function("Test")  # outputs
"""
Hello 
Test 
world
"""

# my_decorator(function)  # does the same job


# --- But what if we keep on changing number of parameters? We need to come again and again to modify
# my_decorator function. We don't want this, right. Do we have solution, think about it before looking at the
# answer

# Yes we do have a solution, remember we learnt *args and **kwargs. We can use those here.

"""
It's nothing but decorator pattern where we give function extra functionality. Basically we decorate a function.
We can pass any number of parameters.
"""


def some_background_function(your_function):
    def some_function(*args, **kwargs):
        your_function(*args, **kwargs)

    return some_function


@some_background_function
def your_fun(name: str, age: int, address: str):
    print(name, age, address)


your_fun("John", 35, "New York")
