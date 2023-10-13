"""
The idea is to move the smallest element to the first. For each element at index i traverse the array from i to len(arr)
and find the smallest element in array and swap smallest with arr[i]

T(n):
Best : O(n^2)
Worst : O(n^2)
Average: O(n^2)
"""


def selectionSort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        smallest, smallest_index = arr[i], i
        for j in range(i + 1, len(arr)):
            if arr[j] < smallest:
                smallest = arr[j]
                smallest_index = j
        temp = arr[smallest_index]
        arr[smallest_index] = arr[i]
        arr[i] = temp
    return arr


if __name__ == "__main__":
    n = int(input("Enter the size of array: "))
    a = [int(input()) for i in range(n)]
    print(selectionSort(a))
