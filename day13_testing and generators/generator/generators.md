### yield vs return ###

The yield statement hauls the function and returns the value to the function caller and restart from where it is
left off. The yield statement can be called multiple times. While the return statement ends the execution of the
function and returns the value back to the caller.

# Generators in Python #

- There is a lot of work in building an iterator in Python. We have to implement a class with __iter__() and __next__()
  method, keep track of internal states, and raise StopIteration when there are no values to be returned.
- This is both lengthy and counterintuitive. Generator comes to the rescue in such situations.
- Python generators are a simple way of creating iterators. All the work we mentioned above are automatically handled by
  generators in Python.
- Simply speaking, a generator is a function that returns an object (iterator) which we can iterate over (one value at a
  time).
- It is fairly simple to create a generator in Python. It is as easy as defining a normal function, but with a yield
  statement instead of a return statement.
- If a function contains at least one yield statement (it may contain other yield or return statements), it becomes a
  generator function. Both yield and return will return some value from a function.
- The difference is that while a return statement terminates a function entirely, yield statement pauses the function
  saving all its states and later continues from there on successive calls.
- Once the function yields, the function is paused and the control is transferred to the caller.
- Local variables and their states are remembered between successive calls.
- Finally, when the function terminates, StopIteration exception is raised and handled automatically on further calls.

```python
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


a = rev_str("hello")
print(next(a))  # Output: o
print(next(a))  # Output: l
print(next(a))  # Output: l
print(next(a))  # Output: e
print(next(a))  # Output: h
next(a)  # This will raise error (StopIteration) as no items are left.

for char in a:
    print(char)  # Output: o l l e h
```

## Expression of generator ##

- A generator expression is more compact and faster than an equivalent list comprehension. It is as easy to create a
  generator as it is to create a list comprehension.
- The major difference between a list comprehension and a generator expression is that a list comprehension produces the
  entire list while the generator expression produces one item at a time.
- Generator expressions are surrounded by parentheses () instead of square brackets [].

```python
# square each term using list comprehension
my_list = [1, 3, 6, 10]
list_ = [x ** 2 for x in my_list]

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator = (x ** 2 for x in my_list)
```

## When to use generators ##

- Generators are best for calculating large/infinite sets of results as it is memory efficient and loads only one item
  at a time(e.g. reading a file line by line).
- When we want to pipe the output of one generator to another generator, we can use generator expressions.

```python
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        yield x


def square(nums):
    for num in nums:
        yield num ** 2


print(sum(square(fibonacci_numbers(10))))  # Output: 4895
```
