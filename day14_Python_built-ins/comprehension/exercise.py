"""
Given a list of elements, find all elements which occur more than once in the list.
"""

lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'a', 'c', 'h', 'd', 'r', 'c', 'b', 'b', 'b']


def find_duplicates(elements: list) -> list:
    ans = []
    for element in elements:
        if elements.count(element) > 1 and ans.count(element) == 0:
            ans.append(element)
    return ans


# final_result = find_duplicates(arr)
# print(final_result)

# can we do above task in much cleaner way using comprehensions
final_result = list(set([element for element in lst if lst.count(element) > 1]))
print(final_result)
