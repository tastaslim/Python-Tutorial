""" Docstrings are very useful for writing comments. By default, Python ignores it but
if you want to print it you can use functionName.__doc__
"""


def test():
    """
    Tangle is a good angle.
    """
    print()


print(test.__doc__)  # docstring inside function

print(test.__name__)  # name of function
