# Functions in Python #

- Functions in Python work like variable. It means that when you create a function with some name, what python does is
  it assigns some memory to that variable object and say I am trying to copy that function into another variable object,
  new variable will point to that location. Now we delete function, what will happen is that we can still access
  contents of that location using new variable (See I told you: functions are like variable in Python).

```python 
   """
   Let's see for variable first 
   """
   a=1
   b=a
   del a
   print(a)  # error 
   print(b) # 1
   
   """ 
   Now let's see function
   """
   def hello():
       return "Hello"
   new_variable=hello 
   print(new_variable) # Gives memory location
   print(new_variable()) # hello
   
   del hello 
   print(hello()) # error 
   print(new_variable()) # hello
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

- A higher order function(HOF) is any function which either accepts a function as parameter or returns a function.

```python
def higher_order_function(another_function):  # higher order function
    another_function()


def some_function():
    return "hey"


def higher_order_function2():  # higher order function
    return some_function()
```

---

None question which might be striking in your mind, why are we learning functions here? It's because decorators gives
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