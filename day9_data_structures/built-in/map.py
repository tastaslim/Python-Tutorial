def max_frequency(arr):
    dictionary = {}
    for item in arr:
        # Kind of Ternary operator in python.
        dictionary[item] = 1 if item not in dictionary else dictionary[item] + 1

    for key, value in dictionary.items():
        print(f"Key:{key} and Value:{value}")


max_frequency([1, 2, 3, 4, 1, 1, 2])


#
def pair_sum(arr, output):
    dictionary = dict()  # or {}
    for element in arr:
        dictionary[element] = dictionary[element] + 1 if element in dictionary else 1
    # for key, value in dictionary.items():
    #     print(key, output-key) if output-key in dictionary else print(end="")
    count = 0
    for key, value in dictionary.items():
        if output - key in dictionary and dictionary.get(output - key) > 0:
            count1, count2 = value, dictionary.get(output - key)
            count = count + count1 * count2 if output - key != key else int((count1 * (count1 - 1)) / 2)
            dictionary[key] = 0
            dictionary[output - key] = 0
    return count


def dict_operations():
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
    print(dictionary["Taslim"])
    # Instead we will use get("key") method, if key doesn't exist it says None.
    print(dictionary.get("Taslim"))

    """
    linkedlist() way
    """
    # dict1 = linkedlist("name"="Taslim") ==> Wrong, because keys will always be without any string or anything because those must be unique.
    dict1 = dict(name="Taslim")
    print(dict1)


def remove_duplicates(arr):
    s = set()
    for i in arr:
        s.add(i)
    ans = ""
    for i in s:
        ans += i
    print(ans)


def element_with_max_frequency(arr):
    dictionary = {}
    ans, max_value = "", 0
    for element in arr:
        dictionary[element] = dictionary[element] + \
                              1 if element in dictionary else 1
        if dictionary.get(element) > max_value:
            max_value = dictionary.get(element)
            ans = element
    return ans


def main():
    element_with_max_frequency([1, 2, 3, 1, 1, 2, 3, 1, 2])
    ans = pair_sum([1, 2, 2, 4, 0, 0], 4)
    print(ans)
    dict_operations()
    ans = element_with_max_frequency("Kolkata")
    print(ans)


main()
