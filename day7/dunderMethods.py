"""
__ methods are called as dunder/magic methods. Dunder means two underscores (__)
We can modify these methods according to our need, but it is not recommended unless it is mandatory.

1. Remember we had __init__() method which behaves as constructor(Java, C++ etc.) This is dunder
method. See, now say you want to create your own list class which will have all the functionalities of inbuilt list
along with some extra functionalities of your own. you can do that as well as you can overwrite some functionalities
of inbuilt class.
"""

name = "My name is Khan"
print(name.__len__())  # Similar to len(name).


class SuperList(list):
    def __init__(self):
        super().__init__()

    def __len__(self):
        return 1000

    @staticmethod
    def __pop__() -> int:
        return 100


s1 = SuperList()
print(len(s1))
s1.append(1)
s1.append(2)
ans = s1.pop()
print(ans)
print(s1)
print(s1.__len__())  # 1000 as we have overridden len method of inbuilt list class.
