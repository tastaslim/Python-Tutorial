"""
Leetcode 84. Largest Rectangle in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram/
"""

from queue import LifoQueue


def largestRectangleArea(arr: list[int]) -> int:
    n = len(arr)
    maxArea = 0

    # T(n) = O(n^2)
    # for i in range(n):
    #     tempArea = arr[i]
    #     j, k = i - 1, i + 1
    #     while j >= 0 and arr[j] >= arr[i]:
    #         tempArea += arr[i]
    #         j -= 1
    #     while k < n and arr[k] >= arr[i]:
    #         tempArea += arr[i]
    #         k += 1
    #
    #     maxArea = max(maxArea, tempArea)

    # T(n) ==> O(n)
    stack = LifoQueue()
    tempArr = []
    tempArr2 = []
    for i in range(n):
        count = 1
        while not stack.empty() and stack.queue[-1][0] >= arr[i]:
            element, countLeft = stack.get()
            count += countLeft
        tempArr.append((arr[i], count))
        stack.put((arr[i], count))

    stack2 = LifoQueue()
    for i in range(n - 1, -1, -1):
        count = 1
        while not stack2.empty() and stack2.queue[-1][0] >= arr[i]:
            element, countLeft = stack2.get()
            count += countLeft
        tempArr2.append((arr[i], count))
        stack2.put((arr[i], count))

    tempArr2 = list(reversed(tempArr2))
    for i in range(len(tempArr2)):
        element, count1 = tempArr[i]
        element, count2 = tempArr2[i]
        cnt = count1 + count2 - 1
        maxArea = max(maxArea, element * cnt)
    return maxArea


def largestAreaOfRectangleInMatrix(matrix: list[list[str]]) -> int:
    rows = len(matrix)
    columns = len(matrix[0])
    arr = [[int(element) for element in matrix[0]]]
    finalAns = largestRectangleArea(arr[0])
    for i in range(1, rows):
        tempArr = []
        for j in range(columns):
            if int(matrix[i][j]) == 0:
                tempArr.append(int(matrix[i][j]))
            else:
                tempArr.append(int(matrix[i][j]) + arr[i - 1][j])
        finalAns = max(finalAns, largestRectangleArea(tempArr))
        arr.append(tempArr)

    return finalAns


if __name__ == "__main__":
    print(largestRectangleArea([1, 0, 1, 1, 1, 1, 0, 1, 1]))
    # print(largestAreaOfRectangleInMatrix(
    #     [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
