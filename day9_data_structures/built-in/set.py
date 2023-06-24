"""
Set is a collection of unique elements.
It is mutable, unordered and heterogeneous.
"""

set1 = set()  # create empty set
set2 = {1, 2, 3, 4, 5}  # create set with elements
set3 = set([1, 2, 3, 4, 5])  # create set with elements from list
print(set1, set2, set3)

# Add element to set
set1.add(1)
set1.add(2)
print(set1)

# Remove element from set
set1.remove(1)
print(set1)

# Union of two sets
set4 = set1.union(set2)
print(set4)

# Intersection of two sets
set5 = set1.intersection(set2)
print(set5)

# Difference of two sets
set6 = set1.difference(set2)
print(set6)

# Symmetric difference of two sets
set7 = set1.symmetric_difference(set2)
print(set7)

# Check if element is present in set
print(1 in set1)
print(1 in set2)

# Check if set is subset of another set
print(set1.issubset(set2))
print(set1.issubset(set4))

# Check if set is superset of another set
print(set4.issuperset(set1))
print(set4.issuperset(set2))

# Check if set is disjoint with another set

set8 = {1, 2, 3}
set9 = {4, 5, 6}
print(set8.isdisjoint(set9))

# Check if set is empty
print(set1.isdisjoint(set9))

#############################


# Set comprehension
set10 = {i for i in range(10)}
print(set10)

# Set comprehension with condition
set11 = {i for i in range(10) if i % 2 == 0}
print(set11)

######################
# Set operations
######################
# Union
set12 = {1, 2, 3, 4, 5}
set13 = {4, 5, 6, 7, 8}
print(set12 | set13)

# Intersection

print(set12 & set13)

# Difference
print(set12 - set13)

# Symmetric difference
print(set12 ^ set13)

# Set is mutable
set12.add(6)
print(set12)


# Given an array, find unique elements

def unique(arr):
    temp_set = set()
    for element in arr:
        temp_set.add(element)
    return temp_set
