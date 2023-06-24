class Test:
    def __init__(self, name: str, age: int) -> None:
        self.age, self.name = age, name

    def get_name(self) -> str:
        return self.name

    def get_age(self) -> int:
        return self.age

    def check_eligibility(self) -> str:
        if self.age > 18:
            return f"{self.name} is eligible for voting"
        return f"{self.name} is not eligible"
