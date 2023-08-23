# Context Managers #

Python came out with a special new keyword several years ago in Python 2.5 that is known as the **with** statement. This
new keyword allows a developer to create context managers. But wait! What’s a context manager? They are handy constructs
that allow you to set something up and tear something down automatically. For example, you might want to open a file,
write a bunch of stuff to it and then close it. This is probably the classic example of a context manager. In fact,
Python creates one automatically for you when you open a file using the with statement:

----

- By default, the mode in which file is opened using open function is read ==> 'r'.
  Other common values are 'w' for writing (truncating the file if it already exists), 'x' for creating and writing to a
  new file, and 'a' for appending (which on some Unix systems, means that all writes append to the end of the file
  regardless of the current seek position).
- In text mode, if encoding is not specified the encoding used is platform dependent: **locale.getpreferredencoding(
  False)**
  is called to get the current locale encoding. (For reading and writing raw bytes use binary
  mode and leave encoding unspecified.)

```python
# w represents the mode in which file is opened using open function. 
with open('path', 'w') as f_obj:  # open is also a context manager in python
    f_obj.write('some_data')
```

## The with statement ##

- The with statement is used to wrap the execution of a block with methods defined by a context manager. This allows
  common try...except...finally usage patterns to be encapsulated for convenient reuse.

The execution of the with statement with one “item” proceeds as follows:

1. The context expression (the expression given in the with_item) is evaluated to obtain a context manager.
2. The context manager __exit__() is loaded for later use.
3. The context manager __enter__() method is invoked.
4. If a target was included in the with statement, the return value from __enter__() is assigned to it. The with
   statement guarantees that if **__enter__()** method returns without an error, then **__exit__()** will always be
   called. Thus, if an error occurs during the assignment to the target list, it will be treated the same as an error
   occurring within the suite would be. See step 6 below.
5. The suite is executed.
6. The context manager’s __exit__() method is invoked. If an exception caused the suite to be exited, its type, value,
   and traceback are passed as arguments to __exit__(). Otherwise, three None arguments are supplied.
   If the suite was exited due to an exception, and the return value from the __exit__() method was false, the exception
   is reraised. **If the return value was true from __exit__() function, the exception is suppressed, and execution
   continues with the statement following the with statement**.
   If the suite was exited for any reason other than an exception, the return value from __exit__() is ignored, and
   execution proceeds at the normal location for the kind of exit that was taken.

Let' see 6. with code.

```python
class Taslim:
    def __init__(self, path):
        """Constructor"""
        self.path = path

    def __enter__(self):
        """
        Open the file
        """
        print('enter')
        self.conn = open(self.path, 'w')
        return self.conn

    def __exit__(self, error_type, error_value, error_traceback):
        """
        Close the file
        """
        print('exit')
        self.conn.close()
        # return True  # as return value from __exit__() is true below raised ValueError is suppressed/ignored. Hence, be 
        # very careful while returning True from __exit__() method. You can return true for specific error types to ignore those.

        if error_type is ValueError:
            print('ValueError is suppressed')
            return True


with Taslim('a.txt') as f_obj:
    print('middle')
    f_obj.write('some_data')
    raise ValueError('some error')

# output:
# enter
# middle
# exit

```

---

With more than one item, the context managers are processed as if multiple with statements were nested:

```text
with A() as a, B() as b:
    suite

is equivalent to
with A() as a:
    with B() as b:
        suite
```

In the demo, I will show you how to create a context manager using the with statement.

---

# contextlib #

Python 2.5 not only added the with statement, but it also added the contextlib module. This allows us to create a
context manager using contextlib’s contextmanager function as a decorator. **contextlib** decorator is a function that
implements __enter__ and __exit__ methods for you under the hood.

Let’s try creating a context manager that opens and closes a file after all:

```python
from contextlib import contextmanager


@contextmanager
def open_file(path, mode):
    print("Enter method called")
    f_obj = ''
    try:
        f_obj = open(path, f'{mode}')
        yield f_obj
    except OSError:
        print("We had an error!")
    finally:
        print('Closing file')
        f_obj.close()
    print("Exit method called")


def do_the_stuff(path, mode):
    with open_file(f'{path}', f'{mode}') as f_obj1:
        f_obj1.write('some_data')
```

---

**Best thing about a context manager is that we can also use it as a decorator.**

```python
import time
from contextlib import ContextDecorator


class Taslim(ContextDecorator):
    def __init__(self):
        """Constructor"""
        self.start = None

    def __enter__(self):
        """
        Start timer
        """
        print('enter')
        self.start = time.time()
        return self.start

    def __exit__(self, error_type, error_value, error_traceback):
        """
        Close the file
        """
        print('exit')
        print(f'Time taken: {time.time() - self.start}')
        # return True  # as return value from __exit__() is true below raised ValueError is suppressed/ignored. Hence, be
        # very careful while returning True from __exit__() method. You can return true for specific error types to ignore those.

        if error_type is ValueError:
            print('ValueError is suppressed')
            return True


def do_the_stuff():
    with Taslim() as _:
        print('middle')
        time.sleep(2)


@Taslim()
def do_the_stuff2():
    print('middle')
    time.sleep(2)


do_the_stuff2()  # Using context manager as a decorator
do_the_stuff()  # Using with keyword
```

## Contextlib and Its Classes ##

There are multiple classes of contextlib. Let’s talk about them one by one.

- contextlib.suppress(*exceptions)
- contextlib.redirect_stdout / redirect_stderr

### contextlib.suppress(*exceptions) ###

Another handy little tool is the **suppress** class which was added in Python 3.4. The idea behind this context manager
utility is that it can suppress any number of exceptions. Let’s see how it works:

```python
from contextlib import suppress

with suppress(FileNotFoundError):
    with open('not_found_file.txt') as f:
        f.write('some_data')
```

### contextlib.redirect_stdout / contextlib.redirect_stderr ###

Sometimes we want to redirect the output of a function to a file or a string. We can do this using the
**redirect_stdout** context managers. **redirect_stderr** is similar to **redirect_stdout** but for errors. Let’s see
how it works:

```python
from contextlib import redirect_stdout

path = 'text.txt'
with open(path, 'w') as obj:
    with redirect_stdout(obj):
        help(redirect_stdout)
```


