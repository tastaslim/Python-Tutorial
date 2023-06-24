"""
lru_cache(maxsize=n) function is used to cache last n entries.This function is defined in “functools” module.
"""
import time
from functools import lru_cache

lst = [1, 2, 3, 4]


@lru_cache(maxsize=3)
def some_work(a: int, b: int) -> int:
    time.sleep(4)
    return a + b


if __name__ == '__main__':
    print(some_work(12, 4))
    print("Calling again")
    print(some_work(12, 4))
