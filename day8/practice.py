class Animal:
    def __init__(self):
        pass

    def sound(self) -> str:
        pass

    def color(self) -> str:
        pass

    def type(self) -> str:
        pass


class Cow(Animal):
    def sound(self) -> str:
        return "moo"

    def color(self) -> str:
        return "white"

    def type(self) -> str:
        return "Herbivores"


class Cat(Animal):
    def sound(self) -> str:
        return "Mew"

    def color(self) -> str:
        return "Black"

    def type(self) -> str:
        return "Omnivores"


class Test:
    def __init__(self, animal_instance: Animal) -> None:
        self.animal_instance = animal_instance

    def print_properties(self) -> None:
        print(f"{self.animal_instance.color()} {self.animal_instance.type()} {self.animal_instance.sound()}")


test = Test(Cow())
# print(Cat.__mro__)
test.print_properties()
