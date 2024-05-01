"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the
array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one
position.
Return the max sliding window.
Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""


def maxSlidingWindow(arr: list[int], n: int, k: int):
    # O(n^2) Brute force
    subArray = []
    for i in range(n):
        if n - i < k:
            break
        subArray.append(arr[i:i + k])

    finalMax = []
    for element in subArray:
        finalMax.append(max(element))
    return finalMax


if __name__ == "__main__":
    print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 8, 3))
