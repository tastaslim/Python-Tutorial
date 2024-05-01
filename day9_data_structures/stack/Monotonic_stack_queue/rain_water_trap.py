from typing import List


def getTrappedWater(arr: List[int], n: int) -> int:
    finalAns = 0
    buildingWidth = 1

    # T(n) = O(n^2), S(n) = O(1)
    # left, right = 0, n - 1
    # for i in range(n):
    #     j = i - 1
    #     k = i + 1
    #     nextGreaterInLeft, nextGreaterInRight = arr[i], arr[i]
    #     while j >= 0:
    #         if arr[j] > nextGreaterInLeft:
    #             nextGreaterInLeft = arr[j]
    #         j -= 1
    #     while k < n:
    #         if arr[k] > nextGreaterInRight:
    #             nextGreaterInRight = arr[k]
    #         k += 1
    #     finalAns += (min(nextGreaterInLeft, nextGreaterInRight) - arr[i]) * buildingWidth

    # T(n) = O(n), S(n) = O(n)
    # if n == 0 or n == 1:
    #     return finalAns
    #
    # prefixArr = [arr[0]] * n
    # suffixArr = [arr[n - 1]] * n
    # for i in range(1, n):
    #     prefixArr[i] = max(arr[i], prefixArr[i - 1])
    #
    # for i in range(n - 2, -1, -1):
    #     suffixArr[i] = max(arr[i], suffixArr[i + 1])
    #
    # for i in range(n):
    #     finalAns += (min(prefixArr[i], suffixArr[i]) - arr[i]) * buildingWidth

    # T(n) = O(n), S(n) = O(1)
    start, end = 0, n - 1
    leftGreater, rightGreater = arr[start], arr[end]
    while start <= end:
        if arr[start] <= arr[end]:
            if arr[start] > leftGreater:
                leftGreater = arr[start]
            else:
                finalAns += (leftGreater - arr[start]) * buildingWidth
            start += 1
        else:
            if arr[end] > rightGreater:
                rightGreater = arr[end]
            else:
                finalAns += (rightGreater - arr[end]) * buildingWidth
            end -= 1
    return finalAns


if __name__ == "__main__":
    print(getTrappedWater([2, 1, 1, 4], 4))
