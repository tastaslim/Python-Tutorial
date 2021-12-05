def elementWithMaxOccurrence(arr):
    dictionary = dict()
    for item in arr:
        # Kind of Ternary operator in python.
        dictionary[item] = dictionary[item]+1 if item in dictionary else 1

    for key, value in dictionary.items():
        print(f"Key:{key} and Value:{value}")


def pairSum(arr, sum):
    dictionary = dict()  # or {}
    for element in arr:
        dictionary[element] = dictionary[element] + \
            1 if element in dictionary else 1
    # for key, value in dictionary.items():
    #     print(key, sum-key) if sum-key in dictionary else print(end="")
    count = 0
    for key, value in dictionary.items():
        if sum-key in dictionary and dictionary.get(sum-key) > 0:
            count1, count2 = value, dictionary.get(sum-key)
            count = count+count1*count2 if sum - \
                key != key else int((count1*(count1-1))/2)
            dictionary[key] = 0
            dictionary[sum-key] = 0
    return count


def dictOperations():
    """
    Although below statement won't give you error but as soon as you get dictionary["Taslim"], you will get
    last updated value of key because previous one's will be gone from dictionary. Python handles it internally
    but C++ or Java gives error. 
    """
    dictionary = {
        "Taslim": 22,
        "Taslim": 21
    }
    # Don't use this way of accessing elements because if key does not exist it will throw any error.
    # print(dictionary["Taslim"])
    # Instead we will use get("key") method, if key doesn't exist it says None.
    print(dictionary.get("Taslim"))

    """
    dict() way
    """
    # dict1 = dict("name"="Taslim") ==> Wrong, because keys will always be without any string or anything because those must be unique.
    dict1 = dict(name="Taslim")


def removeDuplicates(str):
    s = set()
    for i in str:
        s.add(i)
    ans = ""
    for i in s:
        ans += i
    print(ans)


def findElementWithMaxOccurrence(str):
    dictionary = {}
    ans, max = "", 0
    for element in str:
        dictionary[element] = dictionary[element] + \
            1 if element in dictionary else 1
        if dictionary.get(element) > max:
            max = dictionary.get(element)
            ans = element
    return ans


def main():

    # elementWithMaxOccurrence([1, 2, 3, 1, 1, 2, 3, 1, 2])
    # ans = pairSum([1, 2, 2, 4, 0, 0], 4)
    # print(ans)
    # dictOperations()
    ans = findElementWithMaxOccurrence("kolkataattt")
    print(ans)


main()
