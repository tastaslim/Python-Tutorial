# Functions in Python #

- Functions in Python work like variable. It means that when you create a function with some name, what python does is
  it assigns some memory to that variable object and say I am trying to copy that function into another variable object,
  new variable will point to that location. Now we delete function, what will happen is that we can still access
  contents of that location using new variable (See I told you: functions are like variable in Python).

```python
a = 1
print(a)
del a


# print(a)  # error as a is deleted


def hello():
    return "Hello"


new_variable = hello
print(new_variable)  # Gives memory location
print(new_variable())  # hello

del hello
# print(hello())  # error 
print(new_variable())  # hello
```

---

- Functions can be pass inside a function in Python.

```python
def hello(func):
    func()


def greet():
    print("Welcome to python")


hello(greet)
```

---

# Higher order functions #

- A higher order function(HOF) is any function which either accepts a function as parameter or returns a function or
  both.

```python
def higher_order_function(another_function):  # higher order function
    another_function()


def some_function():
    return "hey"


def higher_order_function2():  # higher order function
    return some_function()
```

---

One question which might be striking in your mind, why are we learning functions here? It's because decorators gives
extra functionality to functions. Say We want our function to have a special functionality, we can add a decorators with
it.

Like in case of a class. We make a function as static using @staticmethod decorator.

```python
class Test:
    def __init__(self) -> None:
        pass

    @staticmethod  # decorator
    def static_function():
        print("Static method")

    @classmethod  # decorator
    def class_method(cls):
        print(cls.__name__)
```

---

Decorator starts with a @. **@decorators_name**. Decorator is nothing but a function which is used to add extra
functionality to a function.

## Why do we need decorator? ##

- Well there are unlimited use of decorator. You want to make a function static , class level, want to check how much
  time a function takes to execute, how much memory it takes etc. We can have decorators for these.
- At the end of the day, it's up to you how do you like it to use. We have many built in decorators, and we can also
  create our own.

```python
# Let's say I want to find the time taken by a function to complete its execution.
import time


def performance(your_function):
    def some_function(*args, **kwargs):
        start = time.time()
        your_function(args, kwargs)
        end = time.time()
        print(end - start)

    return some_function


@performance
def func(name: str, age: int) -> None:
    print(name, age)
```

# How does a decorator work? #

I have already discussed that a decorator is nothing but a function which adds extra functionality to the another
function. It's like you have some functionality in the background, all you are doing is passing your function as
parameter to the special function running in background. So now what happens is when special function runs, it will show
all of its functionality along with functionality of your function. One more thing is that decorators are higher order
function.

```python
def background_function(your_function):
    def some_function():
        print("background functionality")
        your_function()
        print("Other tasks")

    return some_function


@background_function
def fun():
    print("hello")


fun()
# Outputs 
"""
background functionality
hello
Other tasks
"""
```

---

### Something came into your mind seeing above code ###

"""
See basically what we are doing above is :
We are passing our function as parameter to background function
"""

```python
def background_function(your_function):
    def some_function():
        print("background functionality")
        your_function()
        print("Other tasks")

    return some_function


def fun():
    print("hello")


background_function(fun)
```