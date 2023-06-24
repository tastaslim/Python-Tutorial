"""
lambda function is used for those functions that are used only once in the code. Since they are
used only once, we don't need to name them.
That is why lambda functions are called as anonymous functions.

===  lambda element:operation on element
"""
from functools import reduce

lst = [71, 29, 83, 94, 45, 39]
ans = list(map(lambda it: it * 2, lst))
# print(ans)

ans2 = reduce(lambda x, y: x + y, lst)
# print(ans2)

ans3 = list(filter(lambda x: x > 50, lst))
# print(ans3)
"""
Sort a list of tuples based on second value
"""
question = [(1, 5), (14, 2), (9, 9), (12, -1)]

# ans4 = sorted(question, key=lambda x: x[1])
# print(ans4)

# question.sort(key=lambda x: x[1])
# print(question)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def function(x):
    return x if x % 2 == 0 else None


print(list(map(function, arr)))
