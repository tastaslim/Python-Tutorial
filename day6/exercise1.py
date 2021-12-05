class Cat():
    catCollection = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.catCollection[name] = age

    def findOldestCat(self):
        oldestName, oldestAge = "", 0
        for name, age in self.catCollection.items():
            if oldestAge < age:
                oldestName, oldestAge = name, age
        return oldestName


cat1 = Cat("Tom", 2)
cat2 = Cat("Jerry", 13)
cat3 = Cat("Rahul", 4)

print(cat3.findOldestCat())
