def findSubarray(a, n):
    tempSum, maxSum, startIndex, endIndex, finalStartIndex, finalEndIndex = 0, 0, 0, 0, 0, 0
    windowLength = 0
    for i in range(n):
        tempSum += a[i]
        if tempSum < 0 or a[i] < 0:
            tempSum = 0
            startIndex, endIndex = i + 1, i + 1
            if tempSum < 0:
                finalStartIndex, finalEndIndex = i + 1, i + 1
        if tempSum >= maxSum:
            if windowLength <= (i - startIndex + 1):
                finalStartIndex = startIndex
                finalEndIndex = i
            maxSum = tempSum
            windowLength = i - startIndex + 1

    return a[finalStartIndex: finalEndIndex + 1]


def takeInput():
    n1 = int(input())
    if n1 == 0:
        return list(), n1
    arr1 = list(map(int, input().strip().split(" ")))

    return arr1, n1


# main
arr, n = takeInput()
print(findSubarray(arr, n))
