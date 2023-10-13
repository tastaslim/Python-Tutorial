def partitionPivot(arr: list[int], startIndex: int, endIndex: int) -> int:
    count = 0
    pivotIndex = startIndex
    for i in range(startIndex + 1, endIndex + 1):
        if arr[i] <= arr[pivotIndex]:
            count += 1

    temp = arr[pivotIndex]
    arr[pivotIndex] = arr[pivotIndex + count]
    arr[pivotIndex + count] = temp
    pivotIndex += count

    i, j = startIndex, endIndex
    while i < pivotIndex < j:
        # Because we want to make sure a\ll elements right to pivot are > the pivot element
        if arr[pivotIndex] >= arr[i]:
            i += 1
        elif arr[pivotIndex] < arr[j]:
            j -= 1
        else:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1
    return pivotIndex


def quickSort(arr: list[int], startIndex: int, endIndex: int):
    """
    Don't write main().
    Don't read input, it is passed as function argument.
    Change in the given array itself.
    Taking input and printing output is handled automatically.
    """
    if startIndex >= endIndex:
        return
    pivot = partitionPivot(arr, startIndex, endIndex)
    quickSort(arr, startIndex, pivot - 1)
    quickSort(arr, pivot + 1, endIndex)


if __name__ == "__main__":
    size = int(input("Enter the size of array: "))
    a = [int(input()) for i in range(size)]
    # a = [2, 13, 4, 1, 3, 6, 28]
    quickSort(a, 0, size - 1)
    print(a)
