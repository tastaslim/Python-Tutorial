"""
List is a heterogeneous collection of objects. It is mutable.
"""
lst = list()  # create empty list
list1 = []  # create empty list
list2 = [1, 2, 3, 4, 5]  # create list with elements
# create list with elements
list2.pop()  # remove element from last
list2.remove(1)  # Removes actual element

ans = list2[0:2]  # 1,2

name = ['John', 'Taslim', 'Amazon', 'Facebook']
name.index('Taslim')  # 1

ans2 = name[:-1]  # -1 is like last index ==> prints first to second last as end is exclusive
print(name[-1:])  # Facebook
print(name[0:4:2])  # John, Amazon ==> Last Parameter shows step jump
print(ans2)
list3 = [1, "c", 3, "Tame", 5, 6, 7, 8, True, 10.89]
for val in list3:
    print(val, end=" ")

list3.reverse()
print(list3)

"""
List unpacking
"""
a, b, c, *other = [1, 2, 3, 4, 5, 6, 7, 0]
print(a, b, c, other)


# Maximum and minimum elements in list


def max_min(arr):
    maximum = arr[0]
    minimum = arr[0]
    for element in arr:
        if element > maximum:
            maximum = element
        if element < minimum:
            minimum = element
    return maximum, minimum


# Pair output in sorted array. You will learn about methods in python later.
def pair_sum(arr, output):
    i, j, count = 0, len(arr) - 1, 0
    while i < j:

        if arr[i] + arr[j] == output:
            temp1, temp2 = arr[i + 1], arr[j - 1]
            count1, count2 = 1, 1
            while arr[i] == temp1:
                count1 += 1
                i += 1
            while arr[j] == temp2:
                count2 += 1
                j -= 1
            count = count + count1 * count2
            i, j = i + 1, j - 1
        elif arr[i] + arr[j] > output:
            j = j - 1

        else:
            i += 1
    return count


def kadane(arr):
    target, current = 0, 0
    for element in arr:
        current += element
        if current > target:
            target = current
        if current < 0:
            current = 0
    return target


#

def reverse_array(arr):
    # arr.reverse()
    # return arr
    i, j = 0, len(arr) - 1
    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i, j = i + 1, j - 1
    return arr


def sum_subarray(arr, output):
    i, j, current_sum = 0, 0, 0
    while i < len(arr) - 1 or j < len(arr) - 1:
        if current_sum == output:
            return i, j - 1
        elif current_sum > output:
            print("Greater")
            current_sum -= arr[i]
            i += 1
        else:
            print("Lesser")
            current_sum += arr[j]
            j += 1
    return -1, -1


def sort01(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        if arr[start] == 0:
            start += 1
        elif arr[end] == 1:
            end -= 1
        else:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    return arr


def list_operations(arr):
    print(len(arr))
    arr.reverse()
    print(arr)


def push_pop(arr):
    arr.append(1)  # Inserts element at last
    arr.append(2)
    arr.append(3)
    # Inserts element at given position. insert(position,element)
    arr.insert(0, 21)
    print(arr)
    arr.pop()
    print(arr)
    arr.remove(2)  # Deletes provided element
    print(arr)


def largest(arr):
    maxima = arr[0]
    for element in arr:
        maxima = max(element, maxima)
    return maxima


def second_largest(arr):
    maximum, second_max = 0, 0
    for element in arr:
        if element > maximum:
            second_max = maximum
            maximum = element
        elif element > second_max:
            second_max = element
    return second_max


#  Given that num2>=num1
def count_elements(arr, num1, num2):
    count = 0
    for element in arr:
        if num1 <= element <= num2:
            count += 1
    return count


# Alternate Consecutive output:  Basically question is to  find all even elements less than or equal to x
def count_happy_numbers(x):
    if x == 0:
        return 1
    answer = 0
    for i in range(0, x + 1):
        if i % 2 == 0:
            answer += 1
    return answer


def rearrange_digits(num):
    arr = []
    while num != 0:
        rem = num % 10
        arr.append(rem)
        num //= 10
    arr.reverse()
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                return False
    return True


def main():
    print(kadane([1, 2, 3, -4, 8, -1, 5, -3, -5, 2, -5]))
    print(pair_sum([1, 2, 2, 4, 5, 6, 7, 8], 6))
    print(max_min([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(reverse_array([1, 2, 3, 4, 5]))
    print(sum_subarray([1, 2, 4, 2, -4, -4, 5, 6], 6))
    print(sort01([1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1]))
    list_operations([1, 2, 3, 5, 2, 3, 4, 0, 4])
    push_pop([])
    print(rearrange_digits(431))


main()
