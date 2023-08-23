"""
Given a list of integers and a number k, find the kth the largest integer in the list. The integer will be stored in the
kth_max variable. For example, with a list of 7 integers, if k = 2, then kth_max will be equal to the second-largest integer
in the list. If k = 6, kth_max will equal the 6th largest integer.

Note: Array does not contain any duplicates
"""


# Better approach is to use heap
def k_largest(arr: list, k: int) -> int:
    if len(arr) == 0 or k >= len(arr):
        return -1
    new_arr = list(set(arr))
    new_arr.sort()
    print(new_arr)
    return new_arr[k - 1]


def main():
    array, index = [14, 22, 35, 40, 53, 66, 82], 2
    print(k_largest(array, index))


main()
