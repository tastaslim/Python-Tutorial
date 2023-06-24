"""
1. We declare methods/functions using def keyword in python. Methods can have a specific return type which we
   represent using ->data_type
2. Variables can also have type in python. We can declare it using :data_type
3. We can pass function as a parameter to another function. We can also return a function from a function.
4. We can pass variable number of arguments to a function using *args and **kwargs.
5. We can pass default values to a function's parameter. If we do not pass any value to that parameter, it will
   take default value.
6. Functions in Python work like variable. It means that when you create a function with some name, what python does is
   it assigns some memory to that variable object and say I am trying to copy that function into another variable object,
   new variable will point to that location. Now we delete function, what will happen is that we can still access
   contents of that location using new variable (See i told you: functions are like variable in Python).

"""


def add(a: int, b: int) -> int:
    return a + b


def function_inside_function(another_function, *args):
    return another_function(*args)


# def output(a, b) -> int:
#     return "name" # Gives error because return type of method must be an int.

def result():
    response = function_inside_function(add, 1, 2)
    print(response)


def default_value(a: int, b: int = 20):
    return a + b


if __name__ == '__main__':
    result()  # 3
    default_value(12)  # will return 32
    default_value(12, 13)  # will return 25
