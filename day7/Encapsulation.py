"""
Encapsulation means bundling methods and properties in a package. Here you can see, we are
bundling everything inside a blueprint(class) which many object can use.
"""


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_employee(self):
        return f"My name is {self.name}. I am {self.age} years old."


employee1 = Employee("John Wick", 40)
print(employee1.get_employee())
