# ExitStack #

I believe Python's ExitStack feature does not get the recognition it deserves. I think part of the reason for this is
documentation where formally ExitStack is described as just one of many available context managers for Python's with
statement. But ExitStack deserves far more prominent notice than that. This post will hopefully help with that.

- it's the best way to handle allocation and release of external resources in Python.

### The Problem ###

The main challenge with external resources is that you have to release them when you don't need them anymore and in
particular you must not forget to do so in all the alternate execution paths that may be entered in case of error
conditions.

- Most languages implement error conditions as "exceptions" that can be "caught" and handled (Python, Java, C++,
  Javascript). Typically, code that needs to acquire and release external resources then looks like this:

```python
def acquire_resource_one():
    return 'acquire resource one'


def acquire_resource_two():
    return 'acquire resource two'


def release_resource(resource):
    return f'release {resource}'


res1 = acquire_resource_one()
try:
    # do stuff with res1
    res2 = acquire_resource_two()
    try:
        ...  # do stuff with res1 and res2
    except Exception as e:
        raise e
    finally:
        release_resource(res2)
except Exception as e:
    raise e
finally:
    release_resource(res1)
```

**This approach has multiple big problems:**

- The cleanup code is far away from the allocation code.
- When the number of resources increases, indentation levels (multiple try, except/catch, finally) accumulate, making
  things hard to read.
- Managing a dynamic number of resources this way is impossible.
- There is a lot of code to write, and it's easy to forget to release a resource in one of the alternate execution
  paths. This is a problem because if you don't release a resource, you may end up with a resource leak. A resource leak
  is when you acquire a resource but never release it. This can lead to a variety of problems, including:
    - running out of resources (e.g. memory, file handles, database connections, etc.)
    - the resource being acquired by another process (e.g. a file lock)
    - the resource being acquired by another thread (e.g. a database connection)

---

## The Solution ##

### 1. Partial solution: use with keyword ###

In python, some of these issues can be alleviated by using the with statement

```python
from contextlib import contextmanager


def acquire_resource(resource_id):
    return f'acquire resource id {resource_id}'


def release_resource(resource):
    return f'release {resource}'


@contextmanager
def my_resource(id_):
    res = acquire_resource(id_)
    try:
        yield res
    finally:
        release_resource(res)


with my_resource('RES_ONE') as res1, my_resource('RES_TWO') as res2:
    pass
# do stuff with res1
# do stuff with res1 and res2

```

But again the code is far from being optimal as the number of resources increases, multiple commas and indentation will
come, and still won't work for dynamics resources (we have to know the number of resources in advance.)

### 2. The ExitStack solution ###

**defer** in **go programming** does the same thing but has some problems. read about
defer https://gobyexample.com/defer