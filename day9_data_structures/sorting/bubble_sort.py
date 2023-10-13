"""
The idea is to move the maximum element to last. For each element at index i traverse the array from 0 to i-1
and compare each element with arr[i], if arr[i] > element then swap elements. This way the subarray from i to len(arr) -1
will always be in sorted order.

T(n):
Best : O(n) ==> If array is sorted
Worst : O(n^2)
Average: O(n^2)
"""


def bubbleSort(arr: list[int], n: int) -> list[int]:
    for i in range(n - 1, 0, -1):
        isSortedArray = True
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                isSortedArray = False
        if isSortedArray:
            break
    return arr


def bubbleSortRecursive(arr: list[int], n: int) -> list[int]:
    if n == 0:
        return arr
    isSortedArray = True
    for j in range(0, n - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
            isSortedArray = False
    if isSortedArray:
        return arr
    return bubbleSortRecursive(arr, n - 1)


if __name__ == "__main__":
    size = int(input("Enter the size of array: "))
    a = [int(input()) for i in range(size)]
    print(bubbleSortRecursive(a, size))
