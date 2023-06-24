"""
In python, we declare protected variable as _variableName. 
private variable as __variableName. All variables except above two types are public variables.
These are used for naming conventions only to tell developers as such we don't enforce this things like we used to do in C++ or
Java using private or protected keywords, but we just use it as convention and whole community follow it.
"""


class Cow:
    def __init__(self, age: int, name: str, eligible: bool) -> None:
        self.__age = age
        self._name = name
        self.isEligible = eligible

    def list_properties(self):
        return self.__age, self._name, self.isEligible


c1 = Cow(2, "Steve", True)
print(c1.list_properties())
print(c1.isEligible)
print(c1._name)  # Bad practice to access protected variable
# print(c1.__age)  This will throw error as we can't access private variable
