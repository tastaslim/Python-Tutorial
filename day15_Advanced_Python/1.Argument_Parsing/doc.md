Have you ever wondered how to process command line arguments in Python? Yeah, there’s a module for that. It’s called
argparse, which is a replacement for optparse.

# argparse #

Let's say you have written some functionality and someone else wants to use it. You can write a script that takes
command line arguments and passes them to your function. This is a great way to make your code more flexible and
reusable. Also, if someone makes mistake while calling your function in command line, you can show them the correct way
to call it.

```python
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("square", help="display a square of a given number", type=int)
    args = parser.parse_args()
    print(args.square ** 2)
```

The argparse module supports two types of arguments:

- **Positional** arguments
    - These are the arguments that are required and are passed in a specific order.
    - For example, in the above code, the first argument is the square of which number you want to find.
    - You can also pass a help message to the argument, which will be shown when the user passes `-h` or `--help` to the
      script.
- **Optional** arguments
    - These are the arguments that are optional and are passed with a flag(--), order does not matter in this case.

```python
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--square", help="display a square of a given number", type=int)
    args = parser.parse_args()
    print(args.square ** 2)
```

---

## What to do when options conflict? ##

What do you do if you have options that conflict with each other? A common example would be running your application in
verbose mode versus quiet mode. You can run it in either mode, but not both. How do we prevent the user from running it
that way though? It’s actually quite easy via the mutually_exclusive_group function. Let’s pretend that options x and y
cannot run at the same time and modify our code accordingly. You will note that we have to create a mutually exclusive
group. Then we add the options that need to be mutually exclusive to that group. The rest go into the regular parser
group

```python
import argparse


def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is where you might put example usage"
    )

    group = parser.add_mutually_exclusive_group()
    # Here x and y are added to mutually_exclusive_group because we don't want them to run at the same time. Rest of the
    # options are added to the parser.
    group.add_argument('-x', '--execute', action="store",
                       help='Help text for option X')
    group.add_argument('-y', help='Help text for option Y', default=False)

    parser.add_argument('-z', help='Help text for option Z', type=int)
    print(parser.parse_args())


if __name__ == '__main__':
    get_args()
```