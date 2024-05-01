"""
Find nearest smaller to left
4 5 2 10 8

Answer:
-1 4 -1 2 2
"""


def nearestSmallerToLeft(arr: list[int], n: int) -> list[int]:
    for i in range(n - 1, -1, -1):
        minimum = -1
        for j in range(i - 1, -1, -1):
            if arr[j] < arr[i]:
                minimum = arr[j]
                break
        arr[i] = minimum
    return arr

    # stack = LifoQueue()
    # ans = []
    # for i in range(n):
    #     count = 1
    #     while not stack.empty() and stack.queue[-1][0] > arr[i]:
    #         stack.get()
    #         count += 1
    #     ans.append(-1) if stack.empty() else ans.append(stack.queue[-1])
    #     stack.put((arr[i], i))
    # return ans


if __name__ == "__main__":
    print(nearestSmallerToLeft([1, 2, 3], 3))
