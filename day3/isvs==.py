"""[@summary] is vs == == checks for only value part. is checks for everything(value,location in memory is same,
same data type ), hence it is always recommended to use is while working with difference types of data and comparison
between them.

If you know Javascript, you can consider is as ===
"""
print(10 == 10.0)  # Prints true because ultimately value is same and integer is subtype of float in python.
print([] == [])  # True
print('' == 1)  # False
print('' == 0)  # False
print("" == '')  # True
print(
    "1" == 1)  # False because these are two different values. If python wants to compare it, it will convert one of
# these wrt to other's instance and will check it(Say on basis of ASCII or something)

print(True == 1)  # Strange it gives True
print(True is 2)  # False
print((1, 2, 3) == [1, 2, 3])  # False
print([1, 2, 3] == [1, 2, 3])  # True
"""
Because Boolean in Python is a subtype of integers. From the documentation:
Boolean values are the two constant objects False and True. They are used to represent truth values
(although other values can also be considered false or true). In numeric contexts(for example when used as 
the argument to an arithmetic operator), they behave like the integers 0 and 1, respectively. 
The built-in function bool() can be used to cast any value to a Boolean, if the value can be interpreted as 
a truth value(see section Truth Value Testing above
"""

print([] is [])  # False because their memory location is different
print(10 is 10.0)  # False
print(True is 1)  # False
print(1 is 1)  # True
print([1, 2, 3] is [1, 2, 3])  # False because their memory location is different
