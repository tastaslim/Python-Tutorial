- In python, when you execute a code/script, python interpreter will first execute the code inside all imported
  files/modules which we don't want all the time, because we want to execute only required piece of code of import
  files not all and that too when we want.

---

In Short:

- **if __name__ == '__main__'** Allows You to Execute Code When the File Runs as a Script, but Not When It’s Imported as
  a Module. Let's understand it with the help of an example. You can remember it as C++ (int main() function), but in
  reality, in python this is not something special from where code execution starts, it is just a conditional check.
- __name__ returns filename when it is imported in another file but if you execute same file where if __name__ == '_
  _main__' is written it will return __main__ which is why inside file the conditional statement is true and hence piece
  of code is executed but not in other files.
- The below image is useful but confusing and don't think if __name_ == '__main__' is from where execution starts in
  python like int main() function in c++.
  ![Python](./namemain.webp)
  file1.py

```python
def test(a: int, b: int) -> int:
    return a + b


print(test(1, 2))
```

file2.py

```python
import file1


def test2(a: int, b: int) -> int:
    return a * b


print(
    test2(2,
          3))  # this will print 3 and 6 which is weired right? Because as we discussed python interpreter will first 
# execute the content of file1 and ultimately print(test(1, 2)) will be executed resulting to 3. 
```

---
Let's see how if __name__ == '__main__' helps us to solve this issue.

file1.py

```python
def test(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    print(test(1, 2))
```

file2.py

```python
import file1


def test2(a: int, b: int) -> int:
    return a * b


print(test2(6,
            7))  # Now only 42 will be printed. Again Python interpreter will execute the code of file1.py but this time 
# since the execution is inside the __main__, it will check whether __name__ == '__main__' or not. As we discussed 
# for imported files __name__ returns filename hence condition will be files and print(test(1,2)) will not get executed.
```

# When Should You Avoid the Name-Main Idiom? #

Now that you’ve learned when to use the name-main idiom, it’s time to find out when it’s not the best idea to use it.
You may be surprised to learn that in many cases, there are better options than nesting your code under if __name__ == "
__main__" in Python.

Sometimes, developers use the name-main idiom to add test runs to a script that combines code functionality and tests in
the same file:

# adder.py

```python
import unittest


def add(a: int, b: int) -> int:
    return a + b


class TestAdder(unittest.TestCase):
    def test_add_adds_two_numbers(self):
        self.assertEqual(add(1, 2), 3)


if __name__ == "__main__":
    unittest.main()
```

With this setup, you can run tests against your code when you execute it as a script:
$ python adder.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s
OK

Because you ran the file as a script, __name__ was equal to "__main__", the conditional expression returned True, and
Python called unittest.main(). The tiny test suite ran, and your test succeeded. At the same time, you did not create
any unexpected code execution when importing your code as a module:

> > >
>>> import adder
> > > adder.add(1, 2)
> > > 3
> > > It’s still possible to import the module and use the function that you’ve defined there. The unit test won’t run
> > > unless
> > > you execute the module in the top-level code environment.

While this works for small files, it’s generally not considered good practice. It’s not advised to mix tests and code in
the same file. Instead, write your tests in a separate file. Following this advice generally makes for a more organized
code base. This approach also removes any overhead, such as the need to import unittest in your main script file.

Another reason that some programmers use the name-main idiom is to include a demonstration of what their code can do:

# echo_demo.py

```python

def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    echoed_text = ""
    for i in range(repetitions, 0, -1):
        echoed_text += f"{text[-i:]}\n"
    return f"{echoed_text.lower()}."


if __name__ == "__main__":
    print('Example call: echo("HELLO", repetitions=2)', end=f"\n{'-' * 42}\n")
    print(echo("HELLO", repetitions=2))

```

You may find such demo code executions in the name-main idiom, but there are arguably much better ways to demonstrate
how to use your program. You can write detailed docstrings with example runs that can double as doctests, and you can
compose proper documentation for your project.

The previous two examples cover two common suboptimal use cases of the name-main idiom. There are other scenarios
when it’s best to avoid the name-main idiom in Python:
