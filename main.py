# # from threading import Thread
# # from fastapi import FastAPI
# # from pydantic import BaseModel
# #
# #
# # class Item(BaseModel):
# #     url: list[str]
# #
# #
# # app = FastAPI()
# #
# #
# # @app.post("/")
# # def download_images(item: Item):
# #     try:
# #         start_time = time()
# #
# #         def download_image(img_url):
# #             print(f"Downloading {img_url}")
# #             img_bytes = requests.get(img_url).content
# #             img_feature_id = img_url.split('/')[3]
# #             img_feature_id = f'{img_feature_id}.jpg'
# #             with open(f'photos/{img_feature_id}', 'wb') as img_file:
# #                 img_file.write(img_bytes)
# #                 print(f'{img_feature_id} was downloaded...')
# #
# #         img_urls = item.url
# #         threads = [Thread(target=download_image, args=[image]) for image in img_urls]
# #         for thread in threads:
# #             thread.start()
# #         print(f'Time taken: {time() - start_time}')
# #         return {"message": "Downloading the images"}
# #     except Exception as e:
# #         print(e)
# # from datetime import datetime
# # from typing import List
# # from enum import Enum, unique
# import sys
#
#
# # @unique
# # class Permission(Enum):
# #     MANAGE_SETTINGS = "Manage Settings"
# #     MANAGE_PROFILE = "Manage Profiles"
# #
# #
# # # def test(permissions: List[Permission]):
# # #     for ele in permissions:
# # #         print(ele.MANAGE_PROFILE)
# # #
# # #
# # # test([Permission.MANAGE_PROFILE])
# #
# #
# # arr = [
# #     {
# #         "org_id": 1,
# #         "feature_id": 1
# #     },
# #     {
# #         "org_id": 1,
# #         "feature_id": 100
# #     },
# #     {
# #         "org_id": 20,
# #         "feature_id": 1
# #     },
# #     {
# #         "org_id": 30,
# #         "feature_id": 1
# #     }
# # ]
#
# # ans = list(set(value for ele in arr for value in ele.values()))
# # print(ans.index(30))
#
# #
# # features = [1, 2, 3, 4]
# # org_id = 30
# # org_features = [
# #     {
# #         "org_id": 1,
# #         "feature_id": 1
# #     },
# #     {
# #         "org_id": 1,
# #         "feature_id": 100
# #     },
# #     {
# #         "org_id": 20,
# #         "feature_id": 1
# #     },
# #     {
# #         "org_id": 3,
# #         "feature_id": 2
# #     }
# # ]
# #
# # res = any(org_id == orgs['org_id'] and orgs['feature_id'] in features for orgs in org_features)
# #
# # for ele in org_features:
# #     ele["feature"] = "Data"
# #
# # print(org_features)
#
# def getFrequencies(v: list[int]) -> list[int]:
#     dictionary = {}
#     for element in v:
#         dictionary[element] = dictionary[element] + 1 if element in dictionary else 1
#
#     smallest, largest = sys.maxsize, v[0]
#     # maxValue = 0
#     # for key, value in dictionary.items():
#     #     if value > maxValue and key < largest:
#     #         largest = key
#     #         maxValue = value
#
#     maxValue = sys.maxsize
#     for key, value in dictionary.items():
#         if value <= maxValue:
#             smallest = key
#             maxValue = value
#     return [smallest]
#
#
# print(getFrequencies([3, 3, 2, 2, 5, 4]))
# # payload = {
# #     "name": "Taslim",
# #     "age": 24
# # }
# # state: dict = {}
# # test = {
# #     "id": 1,
# #     "userId": 2,
# #     "organizationId": 3
# # }
# #
# # print({**{
# #     "id": 1,
# #     "userId": 2,
# #     "organizationId": 3
# # }, **payload})
def traffic(n: int, m: int, vehicle: [int]) -> int:
    finalMax = 0
    for i in range(n):
        j = i
        tempMax, count = 0, 0
        while j < n and (count < m or vehicle[j] == 1):
            if vehicle[j] == 0:
                count += 1
            tempMax += 1
            j += 1
        i += 1
        finalMax = max(finalMax, tempMax)
    return finalMax


def findOnce(arr: list, n: int) -> int:
    startIndex, endIndex = 0, n - 1
    # Only 1 element is in array
    if startIndex == endIndex:
        return arr[startIndex]
    # Last element is the answer
    if arr[endIndex] != arr[endIndex - 1]:
        return arr[endIndex]
    # First element is the answer
    if arr[startIndex] != arr[startIndex + 1]:
        return arr[startIndex]

    while startIndex <= endIndex:
        mid = endIndex + (startIndex - endIndex) // 2
        if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]:
            return arr[mid]

        elif (mid % 2 != 0 and arr[mid] == arr[mid + 1]) or (mid % 2 == 0 and arr[mid] != arr[mid + 1]):
            endIndex = mid - 1

        elif (mid % 2 == 0 and arr[mid] == arr[mid + 1]) or (mid % 2 != 0 and arr[mid] != arr[mid + 1]):
            startIndex = mid + 1

    return -1


from math import sqrt


def sumOfAllDivisorsHelper(n: int) -> int:
    if n == 1:
        return n
    sumofDivisors = n
    sqrtNumber = int(sqrt(n))
    for i in range(1, sqrtNumber + 1):
        if n % i == 0:
            sumofDivisors += i
    return sumofDivisors


def sumOfAllDivisors(n: int) -> int:
    finalSum = 0
    for i in range(1, n + 1):
        finalSum += sumOfAllDivisorsHelper(i)
    return finalSum


if __name__ == "__main__":
    # size = int(input("Enter size: "))
    # swaps = int(input("Enter allowed swaps: "))
    # arr1 = [int(input()) for _ in range(size)]
    # arr = input().strip().split(" ")
    # print(findOnce(arr, 43))
    # print(traffic(size, swaps, arr1))
    n = int(input())
    print(sumOfAllDivisors(n))
