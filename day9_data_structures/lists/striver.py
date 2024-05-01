"""
Largest Element in an array
"""

from sys import maxsize

arr = [41, 25, 3, 478, 2, 98, 45, 6]
arr2 = [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0,
        1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0,
        0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1,
        0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1,
        1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1,
        1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0,
        1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0,
        0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1,
        0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1,
        0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0,
        0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0,
        0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1,
        0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0,
        0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1,
        0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1,
        0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0,
        1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1,
        0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1,
        1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0,
        0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1,
        0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0,
        0, 1, 1, 1]


def largest_element(int_arr: list[int]) -> int:
    largest = - maxsize
    for element in int_arr:
        if element > largest:
            largest = element
    return largest


def second_largest_element(int_arr: list[int]) -> int:
    largest, sec_largest = -maxsize, -maxsize
    for element in int_arr:
        if element > largest:
            sec_largest = largest
            largest = element
        elif element > sec_largest:
            sec_largest = element
    return sec_largest


def traffic(n: int, m: int, vehicle: [int]) -> int:
    final_count = 0
    for i in range(n):
        temp_count, j, count = 0, i, m
        while j < n:
            if vehicle[j] == 1:
                temp_count += 1
            elif count > 0:
                temp_count += 1
                count -= 1
            elif count <= 0:
                temp_count = 0
            j += 1
        final_count = max(final_count, temp_count)
    return final_count


def print_fibonacci(n: int) -> int:
    arr = [0] * (n + 1)
    arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr[n]


def getPairsCount(arr1, k):
    dic = {}
    count = 0
    for element in arr1:
        if element not in dic:
            dic[element] = 1
        else:
            dic[element] += 1

    for key, val in dic.copy().items():
        remainderCount = dic[k - key] if k - key in dic else 0
        if key == k - key:
            count += (dic[key] * (dic[key] - 1)) // 2
        else:
            count += remainderCount * dic[key]
        dic[k - key] = 0
        dic[key] = 0

    return count


"""
Dutch National Glag Algorithm:

we take 3 pointers (3 pointer approach):
low, mid, high

All the elements b/w

1. 0  to  low-1
2. low to mid - 1
3. high +1  to n-1

should be sorted.

Only range b/w mid to high is unsorted. 

We can take mid as pointer and based on the value of mid (0, 1 oe 2)
we need to make decision and increase mid so that above 3 condition follows. Once mid > high, at that time, array 
of 0, 1 and 2s will already be sorted.
"""


def sort012(arr1: list[int], n: int) -> list[int]:
    low, mid, high = 0, 0, n - 1
    while mid <= high:
        if arr1[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            mid += 1
            low += 1
        if arr1[mid] == 1:
            mid += 1
        if arr1[mid] == 2:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
    return arr1


"""
Moore's Voting Algorithm:

Take first element as majority element and
Traverse the array, keep on increasing th count if first element otherwise decrease, once the count is 0
again, change the majority element as ith index element and keep on doing same. If we reach last and there is an element
for which the count is > 0, that can be our majority element and no one else.

Now to verify whether that element is majority element, traverse the array again nd count the occurrence.
"""


def majorityElement(v: list[int]) -> int:
    # length = len(v)
    # dic = {}
    # for element in v:
    #     if element not in dic:
    #         dic[element] = 1
    #     else:
    #         dic[element] += 1

    # for key, val in dic.items():
    #     if val > length//2:
    #         return key
    # return -1

    majority_element = v[0]
    count = 0
    for element in v:
        if element == majority_element:
            count += 1
        else:
            count -= 1

        if count == 0:
            majority_element = element
            count = 1

    count = 0
    for element in v:
        if element == majority_element:
            count += 1
    return majority_element if count > len(v) // 2 else -1


def longestSubarrayWithSumK(a: [int], k: int) -> int:
    # T(n) ==> O(n^2) and S(n) ==> O(1)
    maxCount = 0
    # for i in range(len(a)):
    #     tempSum = 0
    #     count = 0
    #     for j in range(i, len(a)):
    #         tempSum += a[j]
    #         count += 1
    #         if tempSum >= k:
    #             if tempSum == k:
    #                 maxCount = max(maxCount, count)
    #             if j != len(a) - 1 and a[j + 1] != 0:
    #                 tempSum = 0
    #                 break
    return maxCount


def rotateMatrix(mat: list[list[int]]):
    # find the transpose of matrix and then reverse the matrix
    # Transpose meaning, swap columns with rows
    col = len(mat[0]) - 1
    for i in range(len(mat)):
        for j in range(i + 1, col + 1):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    for i in range(len(mat)):
        j = 0
        k = col
        while j < k:
            mat[i][j], mat[i][k] = mat[i][k], mat[i][j]
            j += 1
            k -= 1
    return mat


def longestSuccessiveElements(arr: list[int]) -> int:
    if len(arr) == 1:
        return 1
    # count, tempCount = 1, 1
    # arr.sort()
    # for i in range(1, len(arr)):
    #     if arr[i] - arr[i - 1] == 1:
    #         tempCount += 1
    #     elif arr[i] != arr[i + 1]:
    #         tempCount = 1
    #     count = max(count, tempCount)
    # return count

    s = set()
    for element in arr:
        s.add(element)

    count = 0
    for val in s:
        if val - 1 not in s:
            tempCount = 1
            check = val + 1
            while check in s:
                tempCount += 1
                check += 1
            count = max(count, tempCount)
    return count


def majorityElementSecond(nums: list[int]) -> list[int]:
    dic = {}
    ans = []
    countFirst, countSecond = 0, 0
    firstElement, secondElement = 0, 0
    counter = 0
    for element in nums:
        if element not in dic:
            if counter == 2:
                dic[firstElement] -= 1
                dic[secondElement] -= 1
                if dic[firstElement] == 0:
                    del dic[firstElement]
                    counter -= 1
                    countFirst = 0
                else:
                    dic[firstElement] += 1

                if dic[secondElement] == 0:
                    del dic[secondElement]
                    counter -= 1
                    countSecond = 0
                else:
                    dic[secondElement] += 1

            if countFirst != 0 and countSecond == 0:
                secondElement = element
                countSecond += 1
            elif countFirst == 0:
                firstElement = element
                countFirst += 1
            if len(dic) != 2:
                dic[element] = 1
                counter += 1
        else:
            if element == firstElement:
                countFirst += 1
            if element == secondElement:
                countSecond += 1
            dic[element] += 1

    values = list(dic.keys())
    if len(values) == 0:
        return []

    counterOfFirst, counterOfSecond = 0, 0
    isFirst = values[0]
    for element in values:
        for k in nums:
            if k == element:
                if isFirst == k:
                    counterOfFirst += 1
                else:
                    counterOfSecond += 1

    length = len(nums)
    if counterOfFirst > length // 3:
        ans.append(isFirst)
    if counterOfSecond > length // 3:
        ans.append(values[1])
    return ans


def alternateNumbers(a: list[int]) -> list[int]:
    # S(n) => O(n) + O(n)
    # positiveArray = []
    # negativeArray = []
    # for element in a:
    #     if element >= 0:
    #         positiveArray.append(element)
    #     else:
    #         negativeArray.append(element)
    # i, j, k = 0, 0, 0
    # isEven = True
    # while i < len(positiveArray) and j < len(negativeArray):
    #     if isEven:
    #         a[k] = positiveArray[i]
    #         i += 1
    #         isEven = False
    #     else:
    #         a[k] = negativeArray[j]
    #         j += 1
    #         isEven = True
    #     k += 1

    # while i < len(positiveArray):
    #     a[k] = positiveArray[i]
    #     i += 1
    #     k += 1

    # while j < len(negativeArray):
    #     a[k] = negativeArray[j]
    #     j += 1
    #     k += 1
    # return a

    tempArr = [0] * (len(a))
    positiveIndex = 0
    negativeIndex = 1

    for element in a:
        if element >= 0:
            tempArr[positiveIndex] = element
            positiveIndex += 2
        else:
            tempArr[negativeIndex] = element
            negativeIndex += 2
    return tempArr


"""
Algorithm has 4 steps to follow:
1. take peakElement as arr[n-1]. Traverse arr from n-2 to 0 till you get arr[i] < peakElement. That would be our 
dipPointElement and dipPointIndex = i
2. Once dipElement is found, now Traverse from dipPointIndex + 1 to n-1 and find the nextGreaterElement for
arr[dipPointIndex]
3. Swap arr[dipPointIndex] with nextGreaterElement.
4. Sort the subarray from [dipPointIndex + 1, n-1]
"""


def nextGreaterPermutation(A: list[int]) -> list[int]:
    n = len(A)
    dipPointIndex = -1
    lastElement = A[n - 1]
    for i in range(n - 2, -1, -1):
        if A[i] >= lastElement:
            lastElement = A[i]
        else:
            dipPointIndex = i
            break
    if dipPointIndex == -1:
        A.reverse()
        return A

    nextGreaterElement = maxsize
    nextGreaterIndex = -1
    dipPointElement = A[dipPointIndex]

    for i in range(dipPointIndex + 1, n):
        if dipPointElement < A[i] < nextGreaterElement:
            nextGreaterElement = A[i]
            nextGreaterIndex = i
    A[nextGreaterIndex], A[dipPointIndex] = A[dipPointIndex], A[nextGreaterIndex]
    A[dipPointIndex + 1:] = sorted(A[dipPointIndex + 1:])
    return A


def takeInput():
    n1 = int(input())
    if n1 == 0:
        return list(), n1
    arr1 = list(map(int, input().strip().split(" ")))

    return arr1, n1


# main

if __name__ == "__main__":
    # arr, n = takeInput()
    # print(nextGreaterPermutation([1, 3, 2]))
    # print(alternateNumbers([1, 2, -3, -1, -2, -5]))
    # print(majorityElementSecond([4, 1, 3, 1, 3, 3, 1, 2, 3, 2, 4, 2, 1, 4, 4, 4, 4, 4]))
    # print(rotateMatrix([[10, 8, 7],
    #                     [2, 10, 5],
    #                     [6, 7, 6]]
    #                    ))
    arr = list(map(int, input().strip().split(" ")))
    print(longestSuccessiveElements(arr))
    # print(largest_element(arr))
    # print(second_largest_element([1, 1, 1]))
    # print(print_fibonacci(8))
    # print(traffic(9, 2, [1, 0, 0, 0, 1, 1, 1, 1, 1]))
    # getPairsCount(
    #     [49, 50, 48, 24, 99, 51, 33, 39, 29, 83, 74, 72, 22, 46, 40, 51, 67, 37, 78, 76, 26, 28, 76, 25, 10, 65, 64, 47,
    #      34, 88, 26, 49, 86, 73, 73, 36, 75, 5, 26, 4, 39, 99, 27, 12, 97, 67, 63, 15, 3, 92, 90], 50)
