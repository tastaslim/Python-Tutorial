"""
reduce(fun,seq) function is used to apply a particular function passed in its argument to all the list elements
mentioned in the sequence passed along.This function is defined in “functools” module.

1. At first step, first two elements of sequence are picked and the result is obtained.
2. Next step is to apply the same function to the previously attained result and the number just succeeding the second
   element and the result is again stored.
3. This process continues till no more elements are left in the container.
4. The final returned result is returned and printed on console.
"""
from functools import reduce

lst = [1, 2, 3, 4]


def max_element(a: int, b: int) -> int:
    return a if a > b else b


def sum_element(a: int, b: int) -> int:
    return a + b


ans = reduce(max_element, lst)
print(ans)

ans1 = reduce(sum_element, lst)
print(ans1)
