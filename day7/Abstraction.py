"""
Abstraction means, hiding unnecessary information from user. As you can see when we bundle our blueprint(class)
Users will only be able to see methods exposed by class/not actual implementation of methods. 
They are just concerned to use it.
"""


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_employee(self):
        return f"My name is {self.name}. I am {self.age} years old."


employee1 = Employee("John Wick", 40)
print(employee1.get_employee())
