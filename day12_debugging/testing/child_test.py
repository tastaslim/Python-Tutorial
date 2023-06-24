from day12_debugging.testing.practice import Test


class ChildTest:
    def __init__(self, name: str, age: int):
        self.test = Test(name, age)

    def print_test(self) -> None:
        print(self.test.name, self.test.age)
