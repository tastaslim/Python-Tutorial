"""
Scope in python is like functional scope. Anything which is inside a function has a scope within that function
only. If you want to access the same global variable and play with it inside a function, you need to use the
global keyword.
We know we always prefer locals over globals, right? Similar is case with scope if two variables have the
same name, local one will be preferred for function. If there is only one variable with the name then obviously, we will
use that. 
"""

a = 10


def func():
    a = 20
    return a


print(a)  # uses global a 10
print(func())  # uses local a 20


def func2():
    global a
    a = 30
    return a


# Now value will be changed as we are using same global variable a inside function.
print(func2())  # 30
print(a)  # 30
a = 30


def outer_function():
    a = 10

    def inner_function():
        a = 20
        print(f"Inner a={a}")

    print(f"Outer a={a}")
    inner_function()


outer_function()
print(a)

"""
nonlocal keyword is used to access the global variable inside the function. Meaning any variable which is not global on file level but
if there is hierarchy of function, it is global for that hierarchy.
"""


def outer_function():
    a = 10

    def inner_function():
        # nonlocal keyword is used to access the global variable inside the function.
        nonlocal a
        a = 20
        print(f"Inner a={a}")

    inner_function()
    print(f"Outer a={a}")


outer_function()
print(a)
