# # def rev_str(my_str):
# #     length = len(my_str)
# #     for i in range(length - 1, -1, -1):
# #         yield my_str[i]
# #
# #
# # a = rev_str("hello")
# # print(next(a))  # Output: o
# # print(next(a))  # Output: l
# # print(next(a))  # Output: l
# # print(next(a))  # Output: e
# # print(next(a))  # Output: h
# # next(a)  # This will raise error (StopIteration) as no items are left.
# #
# # for char in a:
# #     print(char)
# #
# # # square each term using list comprehension
# # my_list = [1, 3, 6, 10]
# # list_ = [x ** 2 for x in my_list]
# #
# # # same thing can be done using a generator expression
# # # generator expressions are surrounded by parenthesis ()
# # generator = (x ** 2 for x in my_list)
# #
# #
# # def fibonacci_numbers(nums):
# #     x, y = 0, 1
# #     for _ in range(nums):
# #         x, y = y, x + y
# #         yield x
# #
# #
# # def square(nums):
# #     for num in nums:
# #         yield num ** 2
# #
# #
# # print(sum(square(fibonacci_numbers(10))))
#
# def my_range(start, end):
#     while start < end:
#         cur = start
#         start += 1
#         yield cur
#
#
# # for i in my_range(1, 10):
# #     print(i)
#
#
# def generator_test(num):
#     if num < 2:
#         yield num
#
#     print("Come here")
#
#
# print(generator_test(20))
from concurrent.futures import ThreadPoolExecutor

from requests import post

count = 0


def createUser(userData) -> None:
    global count

    def helper():
        global count
        endpoint = "https://graph.microsoft.com/v1.0/users"
        post(url=endpoint, data=userData, headers={
            "Authorization": "Bearer "
        })
        count += 1

    with ThreadPoolExecutor(max_workers=32) as executed:
        executed.map(helper, userData)
    print(f"Total {count} User created successfully")


if __name__ == "__main__":
    headers = {

    }
    for i in range(1000000):
        body = {
            "accountEnabled": True,
            "displayName": f"Entra Team{count}",
            "mailNickname": f"EntraId{count}",
            "userPrincipalName": f"EntraId{count}@druvainternal.onmicrosoft.com",
            "passwordProfile": {
                "forceChangePasswordNextSignIn": True,
                "password": "xWwvJ]6NMw+bWH-d"
            }
        }
        createUser(body)
