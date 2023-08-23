# my_list = [4, 7, 0, 3]
# my_iter = iter(my_list)  # create an iterator object from that iterable(list)
#
# # iterate through it using next(). next(obj) is same as obj.__next__()
# print(next(my_iter))  # Output: 4
# print(next(my_iter))  # Output: 7
# print(my_iter.__next__())  # Output: 0
# print(my_iter.__next__())  # Output: 3
# next(my_iter)  # This will raise error (StopIteration) as no items are left.
#
# # infinite loop
# iter_obj = iter(my_list)
# while True:
#     try:
#         # get the next item
#         element = next(iter_obj)
#         print(element)
#     except StopIteration:
#         # if StopIteration is raised, break from loop
#         break


#################   PRACTICE #################
"""
lst = [1, 2, 3, 4]
# next(itr) => Both are same

try:
    itr = lst.__iter__()  # itr(lst) => Both are same
    print(itr.__next__())
    print(itr.__next__())
    print(itr.__next__())
    print(itr.__next__())
except StopIteration:
    pass
"""


# lst = [1, 2, 3, 4]
# itr = lst.__iter__()  # itr(lst) => Both are same
# while True:
#     try:
#         print(next(itr))
#     except StopIteration:
#         break
#

class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        curr = self.start
        self.start += 1
        return curr


i = MyRange(1, 10)
#
# for i in MyRange(21, 10):
#     print(i)

# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
