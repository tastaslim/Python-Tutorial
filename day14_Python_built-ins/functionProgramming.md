# Functional Programming #

We will use some inbuilt functions to work with data structures. It keeps our code DRY, memory efficient, easy to
understand, maintain and extend.

### Pure Functions ### 

A function is called pure function if it always returns the same result for same argument values, and it has no side
effects like modifying an argument (or global variable) or outputting something. The only result of calling a pure
function is the return value. Examples of pure functions are strlen(), pow(), sqrt() etc. Examples of impure functions
are printf(), rand(), time(), etc. We have pure functions such as map(), filter(), zip(), reduce() etc.

Although, it is impossible to have pure function everywhere in the code, but it is recommended to use whenever and
wherever possible.

In simple language, Pure functions will perform operations and return data based on that operation without affecting
anything like printing anything inside function etc.

---

Below is an example of pure functions Here we didn't change anything outside of world and passed input just return
different value based on requirement.

```python
def work(item):
    return item * item
```

Below is example of not pure functions

```python
def work(lst):
    for element in lst:
        element *= 2
    print(lst)  # Since we are printing meaning interacting with outer world
    return lst
```

```python
def work(lst):
    new_list = []
    for element in lst:
        new_list.append(element)
    return new_list  # Since we hve created new list and returned it.
```