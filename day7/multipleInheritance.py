class Parent1:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f" Inside Parent1 {self.name} is running")


class Parent2:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f" Inside Parent2 {self.name} is running")


class Child(Parent2, Parent1):
    def __init__(self, name):
        super().__init__(name)


"""
In case of multiple inheritance in python. If both parent classes have same method name, then 
while inheriting them by child, the class which comes first, it's method is executed when we call that method using
child class object.
"""
child1 = Child("Andrew")
child1.run()  # Parent2 run() method will be called, since Parent2 class is first one in the
# inheritance in line no. 17
