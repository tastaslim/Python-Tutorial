## Iterators ##

- Iterators are objects that can be iterated upon. In this tutorial, you will learn how iterator works and how you can
  build your own iterator using __iter__ and __next__ methods.
- Iterators are everywhere in Python. They are elegantly implemented within for loops, comprehensions, generators etc.
  but are hidden in plain sight.

- Iterator in Python is simply an object that can be iterated upon. An object which will return data, one element at a
  time.

- Technically speaking, a Python iterator object must implement two special methods, __iter__() and __next__(),
  collectively called the iterator protocol.

- An object is called iterable if we can get an iterator from it. Most built-in containers in Python like: list, tuple,
  string etc. are iterables. The iter() function (which in turn calls the __iter__() method) returns an iterator from
  them.
- We use the next() function to manually iterate through all the items of an iterator. When we reach the end and there
  is no more data to be returned, it will raise the StopIteration Exception

```python
my_list = [4, 7, 0, 3]
my_iter = iter(my_list)  # get an iterator using iter()
# iterate through it using next(). next(obj) is same as obj.__next__()
print(next(my_iter))  # Output: 4
print(next(my_iter))  # Output: 7
print(my_iter.__next__())  # Output: 0
print(my_iter.__next__())  # Output: 3
next(my_iter)  # This will raise error (StopIteration) as no items are left.
```

- You see in python for loop, we don't need to call next() function explicitly. It is done internally by for loop. With
  the help of for loop, we can iterate over any iterable.

```python
my_list = [4, 7, 0, 3]
for element in my_list:
    print(element)  # element is iterator 
```

**Ironically, this for loop is implemented using Infinite while loop, iter() and next() function under the hood, and it
breaks the execution once we get StopIteration Exception.**

```python
my_list = [4, 7, 0, 3]
iter_obj = iter(my_list)  # create an iterator object from that iterable(list)

# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break
```

## Building Custom Iterators ##

```python
class CustomPower:
    def __init__(self, maxi=0):
        self.maxi = maxi

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.maxi:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


a = CustomPower(
    5)  # Here a does not hold all values, it just holds address of iterator object. To get all values, you can use next which
# will return next value on the fly.
print(a)  # address of object
print(next(a))  # Output: 1
print(next(a))  # Output: 2`

```

## Why iterators are useful? ##

Iterators are useful because they save resources. We don't have to store all the values in memory and process them
later. We can generate the values on the fly and process them as we go along. This is called lazy evaluation.
Theoretically, we can have an infinite items in finite memory.

