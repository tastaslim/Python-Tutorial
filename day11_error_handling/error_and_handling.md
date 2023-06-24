# Error and Handling #

While writing code, it is common that we make mistakes and those mistakes result in error which can cause code crash or
something else. No programmer in the world is perfect and there is no one in the world who has never written a bug in
the code. But how do we handle these errors even though they occur so that python interpreter does not stop its
execution(System crash) and run rest of the code.

Well this is done via error handling in python. It is very important to handle error because we want to make sure that
even though our code throws an error, our program is not going to crash. We know our code interacts with outside world
too, so sometimes we don't get the result what we expect. Hence, we must make sure that we handle error and be ready for
worst case scenario.

---

### Some common errors in python ### 

TypeError SyntaxError ZeroDivisionError KeyError OutOfIndexError FileNotFoundError NameError etc.

- 5/0: ZeroDivisionError
- def hello() # SyntaxError as : is missing
-     print("hey)

- 1+'He' # TypeError as we can't add int to string
- di={1:3,2:5} print(di[12]) # KeyError as key doesn't exist
- print(x) # NameError as x not found

---

# finally # 

In python there is finally block which is executed no matter what happened with your block of code.

```python
def check():
    try:
        print(1 / 0)
    except ZeroDivisionError as err:
        print(err)
    finally:
        print("I will run irrespective of try and except")
```

# Raise an error #

In Python programming, exceptions are raised when errors occur at runtime. We can also manually raise exceptions using
the raise keyword. Generally, we use it when we want stop execution of program but showing our customized error.

```python
def take(item):
    try:
        print(20 / item)
    except ZeroDivisionError as err:
        raise ZeroDivisionError(f"Please enter number except 0: {err}")


take(0)
```