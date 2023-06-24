from time import time


def my_decorator(my_function):
    def fun(item):
        print("Hello")
        my_func(item)
        print("World")
        my_function(item)

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


def performance(your_function):
    def some_function(*args, **kwargs):
        start = time()
        your_function(*args, **kwargs)
        end = time()
        print(f"It took {end - start} seconds to execute")

    return some_function


@performance
def func() -> None:
    for i in range(10000000):
        print(2)


# func()  # takes nearly 14 seconds to complete its execution
# print(args["string"])  # error because tuple indices must be int (args it tuple, kwargs is dictionary)

"""
Create an @authenticated decorator that only allows the function to run if user has 'valid' set to True:
"""


def authentication(your_function):
    def some_function(user):
        your_function(user) if user["valid"] else print(f"Invalid username {user['name']}.")

    return some_function


@authentication
def my_func(user) -> None:
    print(f"User information : {user}")


user1 = {
    'name': 'Sorna',
    'valid': True  # changing this will either run or not run the message_friends function.
}
my_func(user1)
