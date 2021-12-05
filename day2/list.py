"""
List is a heterogeneous collection of objects. It is mutable.
"""
# lst = list()  # create empty list
# list1 = []  # create empty list
# list2 = [1, 2, 3, 4, 5]  # create list with elements
# # create list with elements
# list3 = [1, "c", 3, "Tame", 5, 6, 7, 8, True, 10.89]
# for i in list3:
#     print(i, end=" ")

# list3.reverse()
# print(list3)

"""
List unpacking
"""
a, b, c, *other = [1, 2, 3, 4, 5, 6, 7, 0]
print(a, b, c, other)
# Maximum and minimum elements in list


def maxMin(arr):
    maximum = arr[0]
    minimum = arr[0]
    for element in arr:
        if(element > maximum):
            maximum = element
        if(element < minimum):
            minimum = element
    return maximum, minimum


# Pair sum in sorted array
def pairSum(arr, sum):
    i, j, count = 0, len(arr)-1, 0
    while i < j:

        if arr[i]+arr[j] == sum:
            temp1, temp2 = arr[i+1], arr[j-1]
            count1, count2 = 1, 1
            while arr[i] == temp1:
                count1 += 1
                i += 1
            while arr[j] == temp2:
                count2 += 1
                j -= 1
            count = count+count1*count2
            i, j = i+1, j-1
        elif arr[i]+arr[j] > sum:
            j = j-1

        else:
            i += 1
    return count


def Kadane(arr):
    target, current = 0, 0
    for element in arr:
        current += element
        if current > target:
            target = current
        if current < 0:
            current = 0
    return target


#

def ReverseArray(arr):
    # arr.reverse()
    # return arr
    i, j = 0, len(arr)-1
    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i, j = i+1, j-1
    return arr


def sumSubarray(arr, sum):
    i, j, currentSum = 0, 0, 0
    while i < len(arr)-1 or j < len(arr)-1:
        if currentSum == sum:
            return i, j-1
        elif currentSum > sum:
            print("Greater")
            currentSum -= arr[i]
            i += 1
        else:
            print("Lesser")
            currentSum += arr[j]
            j += 1
    return -1, -1


def sort01(arr):
    start, end = 0, len(arr)-1
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


def listOperations(arr):
    print(len(arr))
    arr.reverse()
    print(arr)


def pushPop(arr):
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


def main():
    # print(Kadane([1, 2, 3, -4, 8, -1, 5, -3, -5, 2, -5]))
    # print(pairSum([1, 2, 2, 4, 5, 6, 7, 8], 6))
    # print(maxMin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    # print(ReverseArray([1, 2, 3, 4, 5]))
    # print(sumSubarray([1, 2, 4, 2, -4, -4, 5, 6], 6))
    # print(sort01([1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1]))
    # listOperations([1, 2, 3, 5, 2, 3, 4, 0, 4])
    pushPop([])


main()
