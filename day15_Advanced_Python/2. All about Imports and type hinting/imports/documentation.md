# imports #

**The backslash (\) is Python’s line continuation character, which tells Python that this line of code
continues on the following line.**

```text
from os import path, walk, unlink, uname, \
            remove, rename
```

- You can import using multiple approaches.

```python
from sys import *  # Imports everything from sys
import sys  # Same as 2nd
import sys as system  # You can import a package as your preferred naming convention
from sys import getsizeof  # imports only gettrace from sys
from os import getenv, getcwd, getgid  # Multiple items from a module. However Python 

''  # Imports from the current directory

# Way to access
system.gettrace()
sys.gettrace()
gettrace()
getsizeof([1, 2])
getenv('')
getcwd()
getgid()
```

## Import Pitfalls ##

There are some very common import pitfalls that programmers fall into. We’ll go over the two most common here:

- **Circular imports** ==> when you create two modules that import each other, you’ll get an error(AttributeError). This
  is because Python does not know which module to import first. I’ve read about some hacky workarounds but in general
  you should just refactor your code to prevent this kind of thing from happening. To fix this, you can import the
  module at the bottom of the file, after the function definitions(But we will never doo that).

```text
# file1.py
import file2
def func1():
    file2.test2()
    
# file2.py
import file1
def func2():
    file1.test1()
```

- **Shadowed imports** ==>  When you import a module with the same name as a variable in your code, you’ll get an error
  (NameError). This is because Python will think you’re trying to access the variable instead of the module. To fix
  this, you can rename the module when you import it.

```text
import math
def func1():
    math = 5
    print(math)
```

