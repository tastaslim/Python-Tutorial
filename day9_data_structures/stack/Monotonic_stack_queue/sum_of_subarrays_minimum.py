import sys
from queue import LifoQueue


def allSubArrays(N: int, arr: list[int]) -> list[list[int]]:
    subArrays = []
    for i in range(N):
        for j in range(i, N):
            tempArr = arr[i:j + 1]
            subArrays.append(tempArr)
    return subArrays


def minMaxDifference(arr: list[int]) -> int:
    mini, maxi = sys.maxsize, -sys.maxsize
    for element in arr:
        mini = min(mini, element)
        maxi = max(maxi, element)
    return maxi - mini


def nextSmallerToLeft(arr: list[int], n: int) -> list[int]:
    stack = LifoQueue()
    NSL = []
    for i in range(n):
        while not stack.empty() and arr[i] < stack.queue[-1][0]:
            stack.get()
        if stack.empty():
            NSL.append(-1)
        else:
            NSL.append(stack.queue[-1][-1])
        stack.put((arr[i], i))
    return NSL


def nextSmallerToRight(arr, n):
    stack = LifoQueue()
    NSR = []
    for i in range(n - 1, -1, -1):
        while not stack.empty() and arr[i] <= stack.queue[-1][0]:
            stack.get()
        if stack.empty():
            NSR.append(n)
        else:
            NSR.append(stack.queue[-1][-1])
        stack.put((arr[i], i))
    return list(reversed(NSR))


def sumSubarrayMins(N: int, arr: list[int]) -> int:
    mod = 100000007
    finalSum = 0

    # For maxSum, we can calculate nextGreaterToLeft(NGL) and nextGreaterToRight(NGR). Apply same formula then where
    # Replace NSR with NGR and NGR with NGL
    NSL = nextSmallerToLeft(arr, N)
    NSR = nextSmallerToRight(arr, N)

    for i in range(N):
        finalSum += ((i - NSR[i]) * (NSL[i] - i)) * arr[i]

    # subArrays = []
    # for i in range(N):
    #     for j in range(i, N):
    #         tempArr = arr[i:j+1]
    #         subArrays.append(tempArr)
    # for element in subArrays:
    #     finalSum += min(element)
    return finalSum % mod


if __name__ == "__main__":
    print(sumSubarrayMins(4, [5, 10, 5, 10]))
