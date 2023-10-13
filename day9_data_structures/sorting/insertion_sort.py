"""
Idea is to take an element and place it in correct position when array would be sorted. choose one index and go towards
left and keep swapping the elements till it is swappable, and you find the correct position of the element.

T(n):
Best : O(n) ==> If array is sorted
Worst : O(n^2)
Average: O(n^2)

"""


def insertionSort(arr: list[int], n: int) -> list[int]:
    for i in range(n):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:  # This loop won't run if array is already sorted
            temp = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = temp
            j -= 1
    return arr


def insertionSortHelper(arr: list[int], n: int, start: int, end: int) -> None:
    if start >= n:
        return
    while end > 0 and arr[end] < arr[end - 1]:
        temp = arr[end - 1]
        arr[end - 1] = arr[end]
        arr[end] = temp
        end = end - 1
    insertionSortHelper(arr, n, start + 1, start + 1)


def insertionSortRecursive(arr: list[int], n: int) -> None:
    insertionSortHelper(arr, n, 0, 0)


if __name__ == "__main__":
    size = int(input("Enter the size of array: "))
    a = [int(input()) for i in range(size)]
    # print(insertionSort(a, size))
    insertionSortRecursive(a, size)
    print(a)
