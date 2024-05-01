# # # # from threading import Thread
# # # # from fastapi import FastAPI
# # # # from pydantic import BaseModel
# # # #
# # # #
# # # # class Item(BaseModel):
# # # #     url: list[str]
# # # #
# # # #
# # # # app = FastAPI()
# # # #
# # # #
# # # # @app.post("/")
# # # # def download_images(item: Item):
# # # #     try:
# # # #         start_time = time()
# # # #
# # # #         def download_image(img_url):
# # # #             print(f"Downloading {img_url}")
# # # #             img_bytes = requests.get(img_url).content
# # # #             img_feature_id = img_url.split('/')[3]
# # # #             img_feature_id = f'{img_feature_id}.jpg'
# # # #             with open(f'photos/{img_feature_id}', 'wb') as img_file:
# # # #                 img_file.write(img_bytes)
# # # #                 print(f'{img_feature_id} was downloaded...')
# # # #
# # # #         img_urls = item.url
# # # #         threads = [Thread(target=download_image, args=[image]) for image in img_urls]
# # # #         for thread in threads:
# # # #             thread.start()
# # # #         print(f'Time taken: {time() - start_time}')
# # # #         return {"message": "Downloading the images"}
# # # #     except Exception as e:
# # # #         print(e)
# # # # from datetime import datetime
# # # # from typing import List
# # # # from enum import Enum, unique
# # # import sys
# # #
# # #
# # # # @unique
# # # # class Permission(Enum):
# # # #     MANAGE_SETTINGS = "Manage Settings"
# # # #     MANAGE_PROFILE = "Manage Profiles"
# # # #
# # # #
# # # # # def test(permissions: List[Permission]):
# # # # #     for ele in permissions:
# # # # #         print(ele.MANAGE_PROFILE)
# # # # #
# # # # #
# # # # # test([Permission.MANAGE_PROFILE])
# # # #
# # # #
# # # # arr = [
# # # #     {
# # # #         "org_id": 1,
# # # #         "feature_id": 1
# # # #     },
# # # #     {
# # # #         "org_id": 1,
# # # #         "feature_id": 100
# # # #     },
# # # #     {
# # # #         "org_id": 20,
# # # #         "feature_id": 1
# # # #     },
# # # #     {
# # # #         "org_id": 30,
# # # #         "feature_id": 1
# # # #     }
# # # # ]
# # #
# # # # ans = list(set(value for ele in arr for value in ele.values()))
# # # # print(ans.index(30))
# # #
# # # #
# # # # features = [1, 2, 3, 4]
# # # # org_id = 30
# # # # org_features = [
# # # #     {
# # # #         "org_id": 1,
# # # #         "feature_id": 1
# # # #     },
# # # #     {
# # # #         "org_id": 1,
# # # #         "feature_id": 100
# # # #     },
# # # #     {
# # # #         "org_id": 20,
# # # #         "feature_id": 1
# # # #     },
# # # #     {
# # # #         "org_id": 3,
# # # #         "feature_id": 2
# # # #     }
# # # # ]
# # # #
# # # # res = any(org_id == orgs['org_id'] and orgs['feature_id'] in features for orgs in org_features)
# # # #
# # # # for ele in org_features:
# # # #     ele["feature"] = "Data"
# # # #
# # # # print(org_features)
# # #
# # # def getFrequencies(v: list[int]) -> list[int]:
# # #     dictionary = {}
# # #     for element in v:
# # #         dictionary[element] = dictionary[element] + 1 if element in dictionary else 1
# # #
# # #     smallest, largest = sys.maxsize, v[0]
# # #     # maxValue = 0
# # #     # for key, value in dictionary.items():
# # #     #     if value > maxValue and key < largest:
# # #     #         largest = key
# # #     #         maxValue = value
# # #
# # #     maxValue = sys.maxsize
# # #     for key, value in dictionary.items():
# # #         if value <= maxValue:
# # #             smallest = key
# # #             maxValue = value
# # #     return [smallest]
# # #
# # #
# # # print(getFrequencies([3, 3, 2, 2, 5, 4]))
# # # # payload = {
# # # #     "name": "Taslim",
# # # #     "age": 24
# # # # }
# # # # state: dict = {}
# # # # test = {
# # # #     "id": 1,
# # # #     "userId": 2,
# # # #     "organizationId": 3
# # # # }
# # # #
# # # # print({**{
# # # #     "id": 1,
# # # #     "userId": 2,
# # # #     "organizationId": 3
# # # # }, **payload})
# # import sys
# #
# #
# # def traffic(n: int, m: int, vehicle: [int]) -> int:
# #     finalMax = 0
# #     for i in range(n):
# #         j = i
# #         tempMax, count = 0, 0
# #         while j < n and (count < m or vehicle[j] == 1):
# #             if vehicle[j] == 0:
# #                 count += 1
# #             tempMax += 1
# #             j += 1
# #         i += 1
# #         finalMax = max(finalMax, tempMax)
# #     return finalMax
# #
# #
# # def findOnce(arr: list, n: int) -> int:
# #     startIndex, endIndex = 0, n - 1
# #     # Only 1 element is in array
# #     if startIndex == endIndex:
# #         return arr[startIndex]
# #     # Last element is the answer
# #     if arr[endIndex] != arr[endIndex - 1]:
# #         return arr[endIndex]
# #     # First element is the answer
# #     if arr[startIndex] != arr[startIndex + 1]:
# #         return arr[startIndex]
# #
# #     while startIndex <= endIndex:
# #         mid = endIndex + (startIndex - endIndex) // 2
# #         if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]:
# #             return arr[mid]
# #
# #         elif (mid % 2 != 0 and arr[mid] == arr[mid + 1]) or (mid % 2 == 0 and arr[mid] != arr[mid + 1]):
# #             endIndex = mid - 1
# #
# #         elif (mid % 2 == 0 and arr[mid] == arr[mid + 1]) or (mid % 2 != 0 and arr[mid] != arr[mid + 1]):
# #             startIndex = mid + 1
# #
# #     return -1
# #
# #
# # from math import sqrt
# #
# #
# # def sumOfAllDivisorsHelper(n: int) -> int:
# #     if n == 1:
# #         return n
# #     sumofDivisors = n
# #     sqrtNumber = int(sqrt(n))
# #     for i in range(1, sqrtNumber + 1):
# #         if n % i == 0:
# #             sumofDivisors += i
# #     return sumofDivisors
# #
# #
# # def sumOfAllDivisors(n: int) -> int:
# #     finalSum = 0
# #     for i in range(1, n + 1):
# #         finalSum += sumOfAllDivisorsHelper(i)
# #     return finalSum
# #
# #
# # def decimalToBinary(n: int) -> str:
# #     finalAns = ""
# #     count = 0
# #     while n > 0:
# #         rem = str(n % 2)
# #         finalAns += rem
# #         n = n // 2
# #         count += 1
# #
# #     return finalAns + "".join(['0'] * (32 - count))
# #
# #
# # def reverseBits(n):
# #     finalSum = 0
# #     binary = decimalToBinary(n)
# #     j = 31
# #     pos = 0
# #     while j >= 0:
# #         finalSum += pow(2, pos) * int(binary[j])
# #         j -= 1
# #         pos += 1
# #     return finalSum
# #
# #
# # def arrSum(arr: [int], i: int) -> int:
# #     finalSum = 0
# #     for ele in arr:
# #         finalSum += ele // i
# #     return finalSum
# #
# #
# # def smallestDivisor(arr: [int], limit: int) -> int:
# #     i = 1
# #     tempSum = sys.maxsize
# #     finalNum = 1
# #     while tempSum > limit:
# #         tempSum = arrSum(arr, i)
# #         finalNum = i
# #         i += 1
# #     return finalNum
# #
# #
# # # if __name__ == "__main__":
# # # size = int(input("Enter size: "))
# # # swaps = int(input("Enter allowed swaps: "))
# # # arr1 = [int(input()) for _ in range(size)]
# # # arr = input().strip().split(" ")
# # # print(findOnce(arr, 43))
# # # print(traffic(size, swaps, arr1))
# # # n = int(input())
# # # print(sumOfAllDivisors(n))
# # # print(reverseBits(1))
# # # print(smallestDivisor([1, 2, 3, 4, 5], 8))
# #
# #
# # def group():
# #     from itertools import groupby
# #     a = [
# #         {
# #             "id": 1,
# #             "name": "Tas"
# #         },
# #         {
# #             "id": 1,
# #             "name": "Ram"
# #         },
# #         {
# #             "id": 2,
# #             "name": "Tas"
# #         }
# #     ]
# #     ans = groupby(a, lambda x: x.get("id"))
# #     for key, value in ans:
# #         print(key, list(ans))
# #
# #
# # group()
#
# from concurrent.futures import ThreadPoolExecutor
#
#
# class ThreadPoolManager:
#     _thread_pool = None
#
#     @classmethod
#     def get_thread_pool(cls):
#         if cls._thread_pool is None:
#             # You can adjust the `max_workers` parameter based on your needs
#             cls._thread_pool = ThreadPoolExecutor(max_workers=128)
#         return cls._thread_pool
#
#     @classmethod
#     def shutdown_thread_pool(cls):
#         if cls._thread_pool:
#             cls._thread_pool.shutdown()
#             cls._thread_pool = None
#
#
# # Example usage in a class
# class SomeClass:
#     def __init__(self):
#         self.thread_pool = ThreadPoolManager.get_thread_pool()
#
#     def some_method(self):
#         # Use the thread pool in this method
#         result = self.thread_pool.submit(self.some_task, "Hello, World!")
#         print(result.result())
#
#     def some_task(self, message):
#         return f"Task completed with message: {message}"
#
#
# # Example usage in another class
# class AnotherClass:
#     def __init__(self):
#         self.thread_pool = ThreadPoolManager.get_thread_pool()
#
#     def another_method(self):
#         # Use the thread pool in this method
#         result = self.thread_pool.submit(self.another_task, 42)
#         print(result.result())
#
#     def another_task(self, value):
#         return f"Task completed with value: {value}"
#
#
# # Example to shut down the thread pool when done
# ThreadPoolManager.shutdown_thread_pool()

import pytest


def listRecords(objectName: str, queryParams: dict = None):
    return f"To be mocked for {objectName} with {queryParams}"


class A:
    @staticmethod
    def add(objectName, queryParams):
        return listRecords(objectName, queryParams)


class B:
    @staticmethod
    def add(objectName, queryParams):
        return listRecords(objectName, queryParams)


class C:
    @staticmethod
    def add(objectName, queryParams):
        return listRecords(objectName, queryParams)


test_params = [
    (A(), 2, 3, 5),  # Instance of ClassA, input parameters, expected output
    (A(), -1, 1, 0),
    (B(), 5, 5, 10),  # Instance of ClassB, input parameters, expected output
    (C(), -10, 10, 0),
]


# Define the test function
@pytest.mark.parametrize("obj, a, b, expected", test_params)
def test_add_method(obj, a, b, expected):
    assert obj.add(a, b) == expected


import unittest
from unittest.mock import patch


# Example classes with methods making API calls


class ClassA:
    def method_a(self):
        # Simulate API call
        return "Response from API in ClassA"


class ClassB:
    def method_b(self):
        # Simulate API call
        return "Response from API in ClassB"


# Example class to test


class MyClass:
    def __init__(self, class_a, class_b):
        self.class_a = class_a
        self.class_b = class_b

    def do_something(self):
        response_a = self.class_a.method_a()
        response_b = self.class_b.method_b()
        return response_a, response_b


# Test case class


class TestMyClass(unittest.TestCase):
    @patch.object(ClassA, 'method_a')
    @patch.object(ClassB, 'method_b')
    def test_do_something(self, mock_method_b, mock_method_a):
        # Define test cases with input data
        test_cases = [
            {"response_a": "Mocked response A", "response_b": "Mocked response B"},
            {"response_a": "Another mocked response A", "response_b": "Another mocked response B"}
        ]

        for case in test_cases:
            # Set up mock return values
            mock_method_a.return_value = case['response_a']
            mock_method_b.return_value = case['response_b']

            # Instantiate MyClass with mocked dependencies
            my_class = MyClass(ClassA(), ClassB())

            # Call the method under test
            response_a, response_b = my_class.do_something()

            # Assert expected behavior
            self.assertEqual(response_a, case['response_a'])
            self.assertEqual(response_b, case['response_b'])


if __name__ == '__main__':
    unittest.main()
