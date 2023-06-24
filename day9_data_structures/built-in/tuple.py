"""
List is a heterogeneous collection of objects. It is immutable/ read only. You can reassign
value to whole tuple variable but can not change individual elements.
"""
tup1 = ()  # create empty tuple
tup2 = (1, 2, 3, 4, 5)  # create tuple with elements
print(tup1, tup2)
tup3 = tuple()  # create empty tuple
tup4 = tuple([1, 2, 3, 4, 5])  # create tuple with elements
print(tup3, tup4)

# tup1[0] = 11   Error, because tuple is immutable.

tup1 = (1, 2, 3, 4, 5)  # This will work because you are assigning a new tuple to the variable tup1.
