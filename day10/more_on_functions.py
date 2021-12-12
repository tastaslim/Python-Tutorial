"""
Functions can be passed inside a function in Python.
"""


def hello(func):
    func()


def greet():
    print("Welcome to python")


hello(greet)

"""
Functions in Python work like variable. It means that when you create a function with some name, what python does is
it assigns some memory to that variable object and say I am trying to copy that function into another variable object,
new variable will point to that location. Now we delete function, what will happen is that we can still access
contents of that location using new variable (See i told you: functions are like variable in Python).
"""


def hey():
    print("Hey there!")


ans = hey
print(ans())
print(hey())
del hey
# print(hey()) Gives error
print(ans())
