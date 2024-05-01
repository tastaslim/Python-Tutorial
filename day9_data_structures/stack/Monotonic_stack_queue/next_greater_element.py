"""
You are given an array 'arr' of size 'n'.
Print the Next Greater Element(NGE) for every element.
The Next Greater Element for an element 'x' is the first element on the right side of 'x' in the array, which is greater
 than 'x'. If no greater elements exist to the right of 'x', consider the next greater element as -1.
"""
from queue import LifoQueue
from typing import List


def nextGreaterElement(arr: List[int], n: int) -> List[int]:
    # for i in range(n):
    #     element = -1
    #     for j in range(i+1, n):
    #         if arr[j] > arr[i]:
    #             element = arr[j]
    #             break
    #     arr[i] = element
    # return arr
    stack = LifoQueue()
    ans = []
    for i in range(n - 1, -1, -1):
        element = -1
        if stack.empty():
            ans.append(element)
            stack.put(arr[i])
        else:
            while not stack.empty() and arr[i] >= stack.queue[-1]:
                stack.get()
            if not stack.empty():
                element = stack.queue[-1]
            ans.append(element)
            stack.put(arr[i])
    return list(reversed(ans))


"""
You are given a circular array 'arr' of size 'n'.
Print the Next Greater Element(NGE) for every element.
A circular array is an array in which we consider the first element is next of the last element. That is, the next 
element of 'a[n - 1]' is 'a[0]'.
The Next Greater Element for an element 'x' is the first element on the right side of 'x' in the array, which is greater
 than 'x'. If no greater elements exist to the right of 'x', consider the next greater element as -1.
"""


def nextGreaterElementInCircularArray(arr: List[int], n: int) -> List[int]:
    stack = LifoQueue()
    ans = []
    for i in range(2 * n - 1, -1, -1):
        element = -1
        i = i % n
        if stack.empty():
            ans.append(element)
            stack.put(arr[i])
        else:
            while not stack.empty() and arr[i] >= stack.queue[-1]:
                stack.get()
            if not stack.empty():
                element = stack.queue[-1]
            ans.append(element)
            stack.put(arr[i])
    ans = list(reversed(ans))
    return ans[0:n]


"""
You are given Q-queries, and for each query, you are given an index(0-based indexing).
Answer to each query is the number of the strictly greater elements to the right of the given index element.
You must return an array  of length ’N’, where ‘answer[i]’ is the answer to the ‘ith’ query.
"""


def countGreater(N: int, Q: int, arr: List[int], query: List[int]) -> List[int]:
    ans = []
    # T(N) ==> O(N) * O(Constant) ~ O(N)
    for i in range(Q):  # O(constant) as Q <= 100
        index = query[i]
        count = 0
        for j in range(index + 1, N):
            if arr[j] > arr[index]:
                count += 1
        ans.append(count)
    return ans


if __name__ == "__main__":
    print(nextGreaterElement([1, 2, 3], 3))
