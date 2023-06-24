"""
Like map, it also takes two functions 2 parameters:
1. function
2. data

Based on the function it will apply filter on data and based on returned value (boolean) it will filter out.
Like in below example as we can see that our function is returning true only if item is even. Now say, I want to
apply this functionality to a particular data structure. I just need to use filter and pass function and data structure
as parameters.
"""


def print_even(item: int):
    return item % 2 == 0


lst = [1, 2, 3, 4, 5, 6]
ans = list(filter(print_even, lst))


# print(ans)


def print_user_above_18(user) -> bool:
    return user["age"] > 18


users = [
    {
        "name": "Taslim",
        "age": 22,
        "designated": "Software Engineer"
    },
    {
        "name": "Rohan",
        "age": 22,
        "designated": "Software Engineer"
    },
    {
        "name": "Arshi",
        "age": 8,
        "designated": "Student"
    }
]
ans1 = list(filter(print_user_above_18, users))
print(ans1)
