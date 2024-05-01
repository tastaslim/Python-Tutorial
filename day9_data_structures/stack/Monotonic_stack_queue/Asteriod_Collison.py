"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.



Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.


Constraints:

2 <= asteroids. length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0

"""
from queue import LifoQueue


# def asteroidCollision(arr: list[int]) -> list[int]:
#     n = len(arr)
#     indicesToRemove = set()
#     for i in range(n):
#         temp = arr[i]
#         if arr[i] >= 0:
#             for j in range(i + 1, n):
#                 if arr[j] < 0 and temp <= abs(arr[j]):
#                     if temp == abs(arr[j]) and j - 1 in indicesToRemove:
#                         break
#                     indicesToRemove.add(i)
#                     break
#                 temp = max(temp, arr[j])
#         else:
#             for j in range(i - 1, -1, -1):
#                 if arr[j] >= abs(temp):
#                     if temp == abs(arr[j]) and j - 1 in indicesToRemove:
#                         break
#                     indicesToRemove.add(i)
#                     break
#                 temp = min(temp, arr[j])
#     ans = [arr[i] for i in range(n) if i not in indicesToRemove]
#     return ans


def collidingAsteroids(arr: list[int]) -> list[int]:
    ps, ns = LifoQueue(), LifoQueue()
    setTracker = set()
    n = len(arr)
    for i in range(n):
        if arr[i] >= 0:
            ps.put(arr[i])
        else:
            while not ps.empty() and abs(arr[i]) >= ps.queue[-1]:
                top = ps.get()
                if top == abs(arr[i]):
                    setTracker.add(i)
                    break
            if not ps.empty():
                setTracker.add(i)

    for i in range(n - 1, -1, -1):
        if arr[i] < 0:
            ns.put(arr[i])
        else:
            while not ns.empty() and arr[i] >= abs(ns.queue[-1]):
                top = ns.get()
                if abs(top) == arr[i]:
                    setTracker.add(i)
                    break
            if not ns.empty():
                setTracker.add(i)
    ans = [arr[i] for i in range(n) if i not in setTracker]
    return ans


if __name__ == "__main__":
    print(collidingAsteroids([-2, 1, 1, -2]

                             ))
