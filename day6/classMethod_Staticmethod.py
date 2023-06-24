from datetime import datetime

data = """
We can call class method and static method using both class and object. But note that these are properties of class not 
object. class method can change state of class because it refers to blueprint/class while static method can't change 
state of class.
1. Like self is used to refer to the current object. We use cls to refer to the class. With all class methods
it is must to pass cls as first argument.
2. cls in nothing but class, but since we have class keyword as reserved for another task, we use cls.
Sometimes people use this class method as an alternative to the constructor.

One thing to note is, in class method we use cls at least 1 time and in normal methods we use self at least 1 time. 
Hence if you have a use case where you are not using self and cls, probably it is a use case of static method. 
"""

print(data)  # We can print docstring


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f"{self.first} {self.last}"

    # Static method

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


employee1 = Employee('Taslim', 'Arif', 50000)
print(employee1.fullname())
print(employee1.is_workday(datetime(2020, 5, 9)))  # True

# Let's take a use-case where you pass employee as "Taslim-Arif-22" ==> First name, Last name, Age. Now what I want is
# I just need to pass this information to any method of class, and it shows information as First name Last name Age.

"""
All in all, we can do same thing using other ways, prefer whatever you like. But generally, we won't see
people using class methods or static methods.
"""


class Employee:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    # if we don't have this class method, then user needs to first parse the string and then pass information while
    # creating object, but now we have given them this flexibility to just pass string, we will parse it on our side
    # and return relevant information.

    def get_employee(self):
        return f"{self.first} {self.last} {self.age}"

    @classmethod
    def from_string(cls, employee):
        first, last, age = employee.split("-")
        return cls(first, last, age)

    @staticmethod
    def from_string1(employee):
        first, last, age = employee.split("-")
        return first, last, age


# Below are 2 ways to do the same thing. 1 we are using class method. 2nd we are parsing it our side and
# calling constructor.
employee1 = "John-Wick-29"
object1 = Employee.from_string(employee1)

first_val, last_val, age_val = employee1.split("-")
object2 = Employee(first_val, last_val, age_val)

print(object1.first, object1.last, object1.age)  # way 1 of printing
# print(Employee.getEmployee())  # Gives error because we can't call normal methods directly using Class name. We
# must create an instance of class and call this method.
