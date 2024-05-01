"""
Array arr of size n.
For each element in the array, check whether the immediate right element of the array is smaller or not.
If the next element is smaller, update the current index to that element. If not, then  -1. The last element does not
have any elements on its right.
"""
from typing import List


def immediateSmaller(arr: List[int]) -> None:
    n = len(arr)
    for i in range(0, n - 1):
        element = -1
        if arr[i] >= arr[i + 1]:
            element = arr[i + 1]
        arr[i] = element
    arr[n - 1] = -1
