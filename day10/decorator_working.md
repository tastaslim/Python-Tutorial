# How does a decorator work? #

I have always discussed that a decorator is nothing but a function which adds extra functionality to the another
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