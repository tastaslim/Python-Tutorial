"""
#1 Capitalize all the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
"""


def capi(item: str) -> str:
    return item.upper()


my_pets = ['sisi', 'bibi', 'titi', 'carla']
ans = list(map(capi, my_pets))
# print(ans)

"""
#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
"""

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]


def sort_element(a, b):
    return a > b


ans2 = list(zip(my_numbers, sorted(my_numbers)))
ans3 = list(zip(my_strings, sorted(my_strings)))
# print(ans2, ans3)

"""
#3 Filter the scores that pass over 50%
"""


def filter_score(score):
    return score > 50


ans4 = list(filter(filter_score, [1, 34, 56, 87, 45, 42, 85]))
print(ans4)
