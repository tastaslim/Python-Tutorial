"""[summary] is vs ==
== checks for only value part.
is checks for everything(value,location in memory is same, same data type ), hence it is always recommended to use is while working with difference types of data
and comparision between them
"""
print(10 == 10.0)  # Prints true because ultimately value is same and integer is sub type of float in python.
print([] == [])  # true
print('' == 1)  # false
print('' == 0)  # false
print("" == '')  # true
print("1" == 1)  # False because these are two different values. If python wants to compare it, it will convert one of them wrt to other's instance
# and will check it(Say on basis of ASCII or something)

print(True == 1)  # Strange it gives true because
print(True == 2)  # gives false
print((1, 2, 3) == [1, 2, 3])
"""
Because Boolean in Python is a subtype of integers. From the documentation:
Boolean values are the two constant objects False and True. They are used to represent truth values
(although other values can also be considered false or true). In numeric contexts(for example when used as 
the argument to an arithmetic operator), they behave like the integers 0 and 1, respectively. 
The built-in function bool() can be used to cast any value to a Boolean, if the value can be interpreted as 
a truth value(see section Truth Value Testing above
"""

print([] is [])  # false because their memory location is different
print(10 is 10.0)  # false
print(True is 1)  # false
print(1 is 1)  # True
