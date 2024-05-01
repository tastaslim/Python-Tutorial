"""
Find nearest greater to left for an element
"""
from queue import LifoQueue


def nearestGreaterToLeft(arr: list[int], n: int) -> list[int]:
    #  T(n) ==> O(n^2), S(n) ==> O(1)
    # for i in range(n - 1, -1, -1):
    #     element = -1
    #     for j in range(i - 1, -1, -1):
    #         if arr[j] > arr[i]:
    #             element = arr[j]
    #             break
    #     arr[i] = element

    #  T(n) ==> O(n^2), S(n) ==> O(n)
    stack = LifoQueue()
    ans = []
    for i in range(n):
        while not stack.empty() and stack.queue[-1] <= arr[i]:
            stack.get()
        if stack.empty():
            ans.append(-1)
        else:
            ans.append(stack.queue[-1])
        stack.put(arr[i])
    return ans


if __name__ == "__main__":
    print(nearestGreaterToLeft([1, 2, 3], 3))
