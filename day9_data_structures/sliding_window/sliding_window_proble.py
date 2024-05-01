"""
Given an array, find the sum of all sub arrays of size k.
arr = [9,2,13,14,5,6]
k = 3

output:
sub arrays
[9,2,13] ==> 24
[2,13,14] ==> 29
[13,14,5] ==> 32
[14,5,6] ==> 25

Ans = 24 + 29 + 32 + 25 = 110
"""

from queue import Queue


def subArraySum(arr: list[int], k: int) -> int:
    n = len(arr)
    tempSum = 0
    i, j = 0, 0
    finalSum = 0
    while j < n:
        tempSum += arr[j]
        if j - i + 1 == k:
            finalSum += tempSum
            tempSum -= arr[i]
            i += 1
        j += 1
    return finalSum


def maximumSumSubarray(arr: list[int], n: int, k: int) -> int:
    tempSum = 0
    i, j = 0, 0
    maxSum = 0
    while j < n:
        tempSum += arr[j]
        if j - i + 1 == k:
            maxSum = max(maxSum, tempSum)
            tempSum -= arr[i]
            i += 1
        j += 1
    return maxSum


def firstNegativeIntegerInWindowOfSizeK(arr: list[int], n: int, k: int) -> list[int]:
    i, j = 0, 0
    q = Queue()
    finalAns = []
    while j < n:
        if arr[j] < 0:
            q.put((arr[j], j))
        if j - i + 1 == k:
            if not q.empty():
                if q.queue[0][-1] != i:
                    finalAns.append(q.queue[0][0])
                else:
                    ele, index = q.get()
                    finalAns.append(ele)
            else:
                # If no negative element in window add 0
                finalAns.append(0)
            i += 1
        j += 1

    return finalAns


def lengthOfLongestSubstringWithUniqueCharacters(s: str) -> int:
    freqCount = [0] * 256
    i, j = 0, 0
    n = len(s)
    maxLength = 1
    while j < n:
        if freqCount[ord(s[j])] != 0:
            freqCount = [0] * 256
            maxLength = max(maxLength, j - i)
            i += 1
        freqCount[ord(s[i])] += 1
        j += 1
    return maxLength


if __name__ == "__main__":
    print(lengthOfLongestSubstringWithUniqueCharacters("pwwkew"))
    # print(subArraySum([9, 2, 13, 14, 5, 6], 3))
    # array = [-8, 2, 3, -6, 10]
    # print(firstNegativeIntegerInWindowOfSizeK(array, 5, 2))
