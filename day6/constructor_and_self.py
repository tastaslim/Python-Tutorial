"""
In python self keyword is like this which we use in CPP or Typescript. We define 
constructor in python using __init__() method and self keyword is used to refer to the current object.

_variable is used to define protected variable.
__variable is used to define private variable.
Any variable without above two notation is public.

Class is blueprint of an object. self keyword refers to class.
"""


class Employee:  # class Employee() ==> both works
    # class object attribute
    __name = None

    def __init__(self, name, age, salary):
        self.__name = name  # private variable
        self._age = age  # protected variable
        self.salary = salary  # public variable

    # class Object method

    def get_information(self):
        return self.__name, self._age, self.salary  # return tuple


employee1 = Employee("John", 25, 10000)
employee2 = Employee("Mary", 30, 20000)
print(employee1.get_information())
print(employee2.get_information())
