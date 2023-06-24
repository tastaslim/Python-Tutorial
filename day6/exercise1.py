class Cat:
    catCollection = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.catCollection[name] = age

    def find_oldest_cat(self):
        oldest_name, oldest_age = "", 0
        for name, age in self.catCollection.items():
            if oldest_age < age:
                oldest_name, oldest_age = name, age
        return oldest_name


cat1 = Cat("Tom", 2)
cat2 = Cat("Jerry", 13)
cat3 = Cat("Rahul", 4)

print(cat3.find_oldest_cat())
