"""
In python self keyword is like this which we use in CPP or Typescript. We define 
constructor in python using __init__() method and self keyword is used to refer to the current object.

_variable is used to define protected variable.
__variable is used to define private variable.
Any variable without above two notation is public.

Class is blueprint of an object. self keyword refers to class.
"""


class Employee():  # class Employee ==> both works
    # class object attribute
    __name = None

    def __init__(self, name, age, salary):
        self.__name = name  # private variable
        self._age = age  # protected variable
        self.salary = salary  # public variable
    # class Object method

    def getInformation(self):
        return self.__name, self._age, self.salary  # return tuple


employee1 = Employee("John", 25, 10000)
employee2 = Employee("Mary", 30, 20000)
print(employee1.getInformation())
print(employee2.getInformation())


# Profile share settings: What is use in a real life scenario.
# In SAAS apps what do we consider as Devices( Like we do have Insync applications for endpoint backup, Similarly do we consider VM/EC2 instances as Devices for SAAS)
# Config Server==> Code and flow( How do we recognize which service to call, API authentication and token generation)
# CPortal and SPotal in UI, and how do they interact with each other.
# DRST(Druva storage==> Kind of storage) library using AWS API or what and how it configures which data to send where)
# H+ uses bin packing algorithm do the scaling of nodes/buckets but which one(BEST, First, Next fit) and how do we optimize space usage.
# Like we do have
# 1. Online bin packing algorithm
# 2. Offline bin packing algorithm

"""
H+ checks in RDS(Database) if there is any running bucket or not. If there is any running bucket, it checks how do we fit our comming bin size input in it, if not possible, create new bucket/node.
"""
