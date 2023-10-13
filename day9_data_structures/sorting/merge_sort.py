"""
It is divide nad conquer algorithm. We divide array in two parts and try to sort the left part of array and right part
of array. Once sorted we merge the sorted array
T(n):
Best :  O(nlog(n))
Worst : O(nlog(n))
Average:  O(nlog(n))

S(n) => O(n)
"""


def mergeSortedArray(arr: [int], left: int, right: int) -> None:
    mid = right + (left - right) // 2
    tempArray = [0] * len(arr)
    start, k, secondHalfStart = left, 0, mid + 1
    while start <= mid and secondHalfStart <= right:
        if arr[start] > arr[secondHalfStart]:
            tempArray[k] = arr[secondHalfStart]
            secondHalfStart += 1
        elif arr[start] < arr[secondHalfStart]:
            tempArray[k] = arr[start]
            start += 1
        else:
            tempArray[k] = arr[start]
            k += 1
            tempArray[k] = arr[secondHalfStart]
            start += 1
            secondHalfStart += 1
        k += 1

    while start <= mid:
        tempArray[k] = arr[start]
        k += 1
        start += 1

    while secondHalfStart <= right:
        tempArray[k] = arr[secondHalfStart]
        secondHalfStart += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = tempArray[i - left]


def mergeSort(arr: [int], l: int, r: int):
    if l >= r:
        return
    mid = r + (l - r) // 2
    mergeSort(arr, l, mid)
    mergeSort(arr, mid + 1, r)
    mergeSortedArray(arr, l, r)


if __name__ == "__main__":
    size = int(input("Enter the size of array: "))
    a = [int(input()) for i in range(size)]
    # a = [2, 13, 4, 1, 3, 6, 28]
    mergeSort(a, 0, size - 1)
    print(a)
