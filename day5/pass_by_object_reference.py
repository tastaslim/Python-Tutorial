"""
In Python there in nothing like pass by value or pass by reference like we learnt in C++ or Java.
Here we have something like pass by object reference.
1. If object is immutable then modified value is not visible outside of function but for mutable it is visible.
For people of C++ or Java(Just for reference):
(Mutable objects: will work like pass by reference)
(Immutable objects: will work like pass value)
"""


def process(article):  # You will see it in your ide(Pycharm etc. ) that it says parameter x is not used
    # because passed value article is integer which is immutable.
    article = 1222
    print(article, id(article))


"""
In below case what will happen is, for variable article inside function, a new object is created in memory
and new value is assigned to it.
"""
#
# a = 14
# print(a, id(a))  # Say 14 and 1111
# process(a)  # 1222 and 293939(say)
# print(a, id(a))  # 14 and 1111

"""
In below case, for variable arr no object will be created, instead same object will be used as list is a mutable object 
"""


def modify_list(arr):
    print(arr, id(arr))
    arr.append(12)
    print(arr, id(arr))


lst = [1, 2, 3]
print(lst, id(lst))
modify_list(lst)
print(lst, id(lst))
