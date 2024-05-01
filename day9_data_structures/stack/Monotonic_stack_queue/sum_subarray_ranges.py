from queue import LifoQueue
from typing import List


def nextGreaterToLeft(n: int, nums: List[int]) -> List[int]:
    stack = LifoQueue()
    NGL = []
    for i in range(n):
        while not stack.empty() and nums[i] >= stack.queue[-1][0]:
            stack.get()
        if stack.empty():
            NGL.append(-1)
        else:
            NGL.append(stack.queue[-1][-1])
        stack.put((nums[i], i))
    return NGL


def nextGreaterToRight(n: int, nums: List[int]) -> List[int]:
    stack = LifoQueue()
    NGR = []
    for i in range(n - 1, -1, -1):
        while not stack.empty() and nums[i] > stack.queue[-1][0]:
            stack.get()
        if stack.empty():
            NGR.append(n)
        else:
            NGR.append(stack.queue[-1][-1])
        stack.put((nums[i], i))
    return list(reversed(NGR))


def nextSmallerToLeft(n: int, nums: List[int]) -> List[int]:
    stack = LifoQueue()
    NSL = []
    for i in range(n):
        while not stack.empty() and nums[i] <= stack.queue[-1][0]:
            stack.get()
        if stack.empty():
            NSL.append(-1)
        else:
            NSL.append(stack.queue[-1][-1])
        stack.put((nums[i], i))
    return NSL


def nextSmallerToRight(n: int, nums: List[int]) -> List[int]:
    stack = LifoQueue()
    NSR = []
    for i in range(n - 1, -1, -1):
        while not stack.empty() and nums[i] < stack.queue[-1][0]:
            stack.get()
        if stack.empty():
            NSR.append(n)
        else:
            NSR.append(stack.queue[-1][-1])
        stack.put((nums[i], i))
    return list(reversed(NSR))


def subArrayRanges(nums: List[int]) -> int:
    n = len(nums)
    finalSum = 0
    NSL = nextSmallerToLeft(n, nums)
    NSR = nextSmallerToRight(n, nums)
    NGL = nextGreaterToLeft(n, nums)
    NGR = nextGreaterToRight(n, nums)

    for i in range(n):
        maxi = ((NGR[i] - i) * (i - NGL[i])) * nums[i]
        mini = ((NSR[i] - i) * (i - NSL[i])) * nums[i]
        finalSum = finalSum + maxi - mini
    return finalSum
