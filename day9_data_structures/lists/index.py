"""
A Python technique called list comprehension is used to iterate over the initial array.
With list comprehension, checking a condition and appending to the new list can all be done in one line.
The code for it starts and ends with a '[' and ends with a ']'. The basic syntax is:

newList = [expression(i) for i in oldList if filter(i)]
"""

# T(n) - Time Complexity
# S(n) - Space Complexity

"""
Challenge 1: Remove Even Integers from List
Given a list of size n, remove all even integers from it. Implement this solution in Python and see if it runs without an error.
"""


def remove_even_element(arr: list) -> list:
    # if len(arr) == 0:
    #     return arr
    # new_arr = []
    # for element in arr:
    #     if element % 2 != 0:
    #         new_arr.append(element)
    # arr = new_arr
    # return arr

    # More pythonic way
    return [element for element in arr if element % 2 != 0]


"""
Challenge 2: Merge Two Sorted Lists
Given two sorted lists, merge them into one list which should also be sorted. Implement the solution in Python 
and see if your code runs successfully!
"""


def merge_two_sorted_list(arr1: list, arr2: list) -> list:
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1
    """
    # With extra space of O(m+n)
    # Time Complexity (TC): O(m+n)
    final_arr, i, j = [], 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            final_arr.append(arr2[j])
            j += 1
        elif arr1[i] < arr2[j]:
            final_arr.append(arr1[i])
            i += 1
        else:
            final_arr.append(arr1[i])
            i += 1
            # j += 1  # UnComment it out if you don't want to duplicate elements

    while i < len(arr1):
        final_arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        final_arr.append(arr2[j])
        j += 1
    return final_arr
    """

    # By merging two lists ==> Still extra space of o(m)
    # Time Complexity (TC): O(m(n+m))
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            arr1.insert(i, arr2[j])
            j += 1
        else:
            i += 1

    while j < len(arr2):
        arr1.append(arr2[j])
        j += 1
    return arr1


"""
Challenge 3: Find Two Numbers that Add up to "k"
Given a list and a number "k", find two numbers from the list that sum to "k".
"""


def two_sum(arr: list, k: int) -> None:
    # Brute force -> T(n) = O(n^2), S(n) = O(1)
    """
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            if arr[i] + arr[j] == k:
                print({arr[i], arr[j]})
    """

    # Using sorting ==> T(n) = O(n*log(n)), S(n) = O(1)
    # 1,2,3,4,4,5,5,5,6,7,8,8,8,9,10  |  k=9
    """
    arr.sort()
    i, j = 0, len(arr) - 1
    while i < j:
        if arr[i] + arr[j] > k:
            j -= 1
        elif arr[i] + arr[j] < k:
            i += 1
        else:
            ki, kj = 1, 1
            while arr[i] == arr[i + 1] and i < j:
                ki += 1
                i += 1
            while arr[j] == arr[j - 1] and i < j:
                kj += 1
                j -= 1
            i += 1
            j -= 1
            m = 0
            while m < ki * kj:
                print({arr[i - 1], arr[j + 1]})
                m += 1
    """

    # Using Hashing ==> T(n) = O(n), S(n) = O(n)
    dictionary = {}
    for element in arr:
        if element in dictionary:
            dictionary[element] += 1
        else:
            dictionary[element] = 1
    for pair in dictionary:
        if dictionary.get(k - pair) and dictionary.get(
                k - pair) > 0:  # dictionary.get(k - pair) gives None if not found, hence we can not directly compare it with 0
            m = 0
            while m < dictionary.get(pair) * dictionary.get(k - pair):
                print({pair, k - pair})
                m += 1
            dictionary.__setitem__(pair, 0)
            dictionary.__setitem__(k - pair, 0)


"""
Challenge 4: List of Products of all Elements
Given a list, modify it so that each index stores the product of all elements in the list except the element at the index itself.
"""


def list_of_products(arr: list) -> list:
    # Brute force ==> T(n) = O(n^2), S(n) = O(n)
    """
    new_arr = []
    for i in range(0, len(arr)):
        prod = 1
        for j in range(0, len(arr)):
            if i != j:
                prod *= arr[j]
        new_arr.append(prod)
    return new_arr
    """

    # Using product ===> T(n)=O(n), S(n)=O(1) [0,1,2,3,4,5]

    prod, count_zero = 1, 0
    for element in arr:
        if count_zero >= 1 or element != 0:
            prod *= element
        elif element == 0:
            count_zero += 1

    for i in range(0, len(arr)):
        if count_zero > 0:
            if count_zero == 1:
                if arr[i] == 0:
                    arr[i] = prod
                else:
                    arr[i] = 0
            else:
                arr[i] = prod
        else:
            arr[i] = prod // arr[i]

    return arr


"""
Challenge 5: Find Minimum Value in List
Given a list of size n, can you find the minimum value in the list? Implement your solution in Python and see if your 
output matches the expected output.
"""


def find_minimum(arr: list) -> int:
    # T(n) = O(n) and S(n) = O(1)
    if len(arr) == 0:
        return -1
    min_value = arr[0]
    for element in arr:
        if element < min_value:
            min_value = element
    return min_value


"""
Challenge 6: Find Maximum Value in List
Given a list of size n, can you find the maximum value in the list? Implement your solution in Python and see if your 
output matches the expected output.
"""


def find_maximum(arr: list) -> int:
    # T(n) = O(n) and S(n) = O(1)
    if len(arr) == 0:
        return -1
    max_value = arr[0]
    for element in arr:
        if element > max_value:
            max_value = element
    return max_value


"""
Challenge 7: Find Second Maximum Value in List
Given a list of size n, can you find the second maximum value in the list? Implement your solution in Python and see if your 
output matches the expected output.
"""


def find_second_maximum(arr: list) -> int:
    # T(n) = O(n) and S(n) = O(1)
    if len(arr) == 0:
        return -1
    max_value, second_max_value = arr[0], -1
    for element in arr:
        if element > max_value:
            second_max_value = max_value
            max_value = element
        elif element > second_max_value and element != max_value:  # handle duplicates entries
            second_max_value = element
    return second_max_value


"""
Challenge 8: First Non-Repeating Integer in a list
Given a list, find the first integer which is unique in the list. Unique means the number does not repeat and appears 
only once in the whole list. Implement your solution in Python and see if it runs correctly!
"""


def first_non_repeating_number(arr: list) -> int:
    ans = -1
    if len(arr) == 0:
        return ans
    # Wrong approach which people often think of: Using sorting ==> T(n) = O(nlog(n)), S(n)=O(1) But this will not work
    # as order matters here, and sorting it, we have violated it.
    """
        arr.sort()
        for i in range(0, len(arr) - 1):
            if arr[i] != arr[i + 1]:
                ans = arr[i]
                return ans
        return ans
    """
    # Using Brute force ==> T(n) = O(n^2) and S(n)=O(1)
    """
    for i in range(0, len(arr)):
        count = 0
        for j in range(i, len(arr)):
            if arr[i] == arr[j]:
                count += 1
        if count == 0:
            return arr[i]
    return ans
    """
    # Using hashing ==> T(n) = O(n), S(n)=O(n)
    dictionary = {}
    for element in arr:
        if dictionary.get(element):
            dictionary[element] += 1
        else:
            dictionary[element] = 1
    for element in arr:
        if dictionary.get(element) == 1:
            return element
    return ans


"""
Challenge 9: Right Rotate List
Given a list, can you rotate its elements by one index from right to left k times? Implement your solution in Python and see if 
your code runs successfully!
"""


def reverse_helper(arr, k, arr_length):
    i, j = 0, k - 1
    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1
    i, j = k, arr_length - 1
    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1
    return arr


def right_rotate(arr, k):
    arr_length = len(arr)
    if k == 0 or arr_length == 0:  # Handle length 0 or k =0 cases
        return arr
    k %= arr_length
    """
    # T(n)=O(n), S(n)=O(1)
    arr.reverse()
    return reverse_helper(arr, k, arr_length)
    """

    # The pythonic way : Look at how awesome python is
    return arr[-k:] + arr[:-k]


"""
Challenge 10: Rearrange Positive & Negative Values
Given a list, can you rearrange its elements in such a way that the negative elements appear at one end and positive 
elements appear at the other? Solve this problem in Python and see if your code runs correctly!
Since zero is neither positive or negative, but we will treat zero as a positive integer for this challenge! So, 
zero will be placed at the right.
"""


def rearrange_numbers(arr: list) -> list:
    if len(arr) == 0:
        return arr

    # T(n) = O(n), S(n)=O(n)
    """
    new_arr = []
    for element in arr:
        if element < 0:
            new_arr.append(element)
    for element in arr:
        if element > 0:
            new_arr.append(element)
    return new_arr
    """

    # T(n) = O(n), S(n)=O(1)
    """
    i, j = 0, len(arr) - 1
    while i < j:
        if arr[i] < 0:
            i += 1
        elif arr[j] >= 0:
            j -= 1
        elif arr[i] >= 0 and arr[j] < 0:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j -= 1
            i += 1
    return arr
    """

    # Pythonic way
    return [element for element in arr if element < 0] + [element for element in arr if element >= 0]


def swap(arr: list, i: int, j: int):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


"""
Challenge 11: Rearrange Sorted List in Max/Min Form
Arrange elements in such a way that the maximum element appears at first position, then minimum at second, then second 
maximum at third and second minimum at fourth and so on.
"""


def rearrange_max_min(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    """
    new_arr = []
    i, j = 0, len(arr) - 1
    while i < j:
        new_arr.append(arr[j])
        new_arr.append(arr[i])
        i += 1
        j -= 1
    return new_arr
    """

    """
    Using this modular formula: 
    
    arr[i] = arr[i] + (arr[max_i/min_i] % me) * me 
    me = max_element_in_original_array + 1
    ( arr[max_i] and max_i-=1 ) if i is even number 
    ( arr[min_i] and min_i+=1 ) if i is odd number.
    
    Idea is to form a new array which gives actual array if we perform modulo of each element in modified array
    with 'me' and gives required answer while dividing elements with 'me'. But this solution only works on sorted and non negative elements.
    """
    min_i, max_i = 0, len(arr) - 1
    me = find_maximum(arr) + 1
    for i in range(0, len(arr)):
        if i % 2 == 0:
            temp_max = arr[max_i]
            max_i -= 1
        else:
            temp_max = arr[min_i]
            min_i += 1
        arr[i] += temp_max % me * me
    for i in range(0, len(arr)):
        arr[i] //= me
    return arr


print(rearrange_max_min([1, 2, 3]))
"""
Challenge 12: Maximum Sum Sublist
Given an array, find the contiguous sublist with the largest sum.
"""


def max_sum_contiguous(arr: list) -> int:
    ans = 0
    if len(arr) == 0:
        return ans
    # Brute force ==> T(n)=O(n^2), S(n)=O(n) ==> Works only when there are no negative elements
    """
    for i in range(0, len(arr)):
        temp = arr[i]
        for j in range(i + 1, len(arr)):
            temp += arr[j]
        if temp > ans:
            ans = temp
    return ans
    """
    # Brute force ==> T(n)=O(n^2), S(n)=O(n)

    """
    for i in range(0, len(arr)):
        temp, m, index = arr[i], 0, 0
        if temp > 0:
            m += temp
        for j in range(i + 1, len(arr)):
            temp += arr[j]
            if temp > m:
                m = temp
        if m > ans:
            ans = m
    return ans
    """

    # Using Kadane's Algorithm ==> T(n)= O(n), S(n)=O(1)
    temp, i, j = 0, 0, 0
    while j < len(arr):
        temp += arr[j]
        if temp > ans:
            ans = temp
        if temp < 0:
            temp = 0
        j += 1
    return ans
