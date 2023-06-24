"""
Python supports all types of inheritance(Multiple, Multilevel, Single, Hybrid, Hierarchical).
Inheritance is nothing but inheriting features from parent class and use it according to needs.

"""


# Single Inheritance


class Parent:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f" Inside Parent1 {self.name} is running")


class Child(Parent):
    def __init__(self, name):
        super().__init__(name)

    def get_name(self):
        print(f"{self.name}")


child1 = Child("Rohan")
child1.run()
child1.get_name()


# Multilevel Inheritance

class Parent:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f" Inside Parent1 {self.name} is running")


class Child(Parent):
    def __init__(self, name):
        super().__init__(name)

    def run(self):
        print(f"Inside Child1 {self.name} is running")


class GrandChild(Child):
    def __init__(self, name):
        super().__init__(name)


"""
As usual hierarchy will go from child to parent. First it will search for function inside it's own blueprint, then 
parent blueprint and then grandparent blueprint and so on.
"""

grand = GrandChild("Rohan")
grand.run()


# -----------------------------------------

# Hybrid  Inheritance


class P1:
    def run(self):
        print("Inside P1")


class P2(P1):
    def run(self):
        print("Inside P2")


class P3:
    def run(self):
        print("Inside P3")


class P4(P1, P3):
    def action(self):
        print("My action P4 {}".format(self.run()))

    def run(self):
        print("Inside P4")


p4 = P4()
p4.run()
