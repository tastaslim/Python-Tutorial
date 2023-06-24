# arr = [1, 2, 3, 4, 5, 6, 7]


def multiply(items):
    return items * 2


"""
map() pure function takes 2 parameters:
1. function
2. data on which function to perform operations

After this it will return updated data without affecting actual value of passed inputs.
"""
lst = [1, 2, 3, 4]
new_ans = list(map(multiply, lst))
print(new_ans)
print(lst)
