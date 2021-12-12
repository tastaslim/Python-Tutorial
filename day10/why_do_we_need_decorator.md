# Why do we need decorator? #

- Well there are unlimited use of decorator. You want to make a function static , class level, want to check how much
  time a function takes to execute, how much memory it takes etc. We can have decorators for these.
- At the end of the day, its upto you how do you like it to use. We have many built in decorators, and we can also
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