my_list = [4, 7, 0, 3]
my_iter = iter(my_list)  # create an iterator object from that iterable(list)

# iterate through it using next(). next(obj) is same as obj.__next__()
print(next(my_iter))  # Output: 4
print(next(my_iter))  # Output: 7
print(my_iter.__next__())  # Output: 0
print(my_iter.__next__())  # Output: 3
next(my_iter)  # This will raise error (StopIteration) as no items are left.

# infinite loop
iter_obj = iter(my_list)
while True:
    try:
        # get the next item
        element = next(iter_obj)
        print(element)
    except StopIteration:
        # if StopIteration is raised, break from loop
        break


class CustomIterator:
    def __init__(self, lst=None):
        self.lst = lst
        self.lst_length = len(lst)
        self.first = 0

    def __iter__(self):
        # self.first = 0
        return self

    def __next__(self):
        if self.first < self.lst_length:
            ans = self.lst[self.first]
            self.first += 1
            return ans
        else:
            raise StopIteration


arr = [1, 2, 3, 4, 5]
a = CustomIterator(arr)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
