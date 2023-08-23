"""
 *************** Typescript *****************
 abstract class Shape {
   protected abstract findArea(...params: number[]): number;
 }

 class Circle extends Shape {
   private pi: number = 22 / 7;
   constructor() {
     super();
   }
   findArea(radius: number): number {
     return this.pi * radius * radius;
   }
 }

 class Rectangle extends Shape {
   constructor() {
     super();
   }
   findArea(length: number, breadth: number): number {
     return length * breadth;
   }
 }

 class Square extends Shape {
   constructor() {
     super();
   }
   findArea(side: number): number {
     return side * side;
   }
 }
 const circleData = new Circle();
 const sol1 = circleData.findArea(7);
 console.log(sol1);

 const rectangleData = new Rectangle();
 const sol2 = rectangleData.findArea(3, 6);
 console.log(sol2);

 const SquareData = new Square();
 const sol3 = SquareData.findArea(3);
 console.log(sol3);
"""

# *************** Python *****************
from enum import Enum

"""
We have to filter the specifications on the basis of various criteria.
"""

# Approach-1 : Bad one
"""
    class Size(Enum):
        SMALL = 1
        MEDIUM = 2
        LARGE = 3
    
    
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
    
    
    class Product:
        def __init__(self, name, color, size):
            self.name = name
            self.color = color
            self.size = size
    
    
    class Filter:
        def filter_by_color(self, items, color):
            for element in items:
                if element.color == color:
                    yield element
    
        def filter_by_size(self, items, size):
            for element in items:
                if element.size == size:
                    yield element
    
        def filter_by_size_and_color(self, items, size, color):
            for element in items:
                if element.size == size and element.color == color:
                    yield element
    
    
    if __name__ == '__main__':
        p1 = Product("T-shirt", Color.RED, Size.SMALL)
        p2 = Product("Cup", Color.GREEN, Size.MEDIUM)
        p3 = Product("Jeans", Color.BLUE, Size.LARGE)
        p4 = Product("Shoes", Color.RED, Size.LARGE)
        p5 = Product("Socks", Color.BLUE, Size.SMALL)
        p6 = Product("Trousers", Color.GREEN, Size.MEDIUM)
        products = [p1, p2, p3, p4, p5, p6]
        f = Filter()
        print("Filter by color:")
        for item in f.filter_by_color(products, Color.GREEN):
            print(f'{item.name} is green')
    
        print("Filter by size:")
        for item in f.filter_by_size(products, Size.LARGE):
            print(f'{item.name} is large')

"""


# You see we are violating the Open-Closed Principle. As every time a requirement comes, we are modifying our
# existing class to support that. And it keeps on growing as different requirements come. Now class will be bulky and
# hard to maintain. There will be higher chances of introducing bugs as we are changing the class content quite
# frequently running on Production. Say we want to filter on the basis of 10 criteria. We will have 2^10-1 cases.
# ##################################################################################################################
# Approach-2 : Good one

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class Specification:
    def follows(self, item):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def follows(self, item):
        return self.color == item.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def follows(self, item):
        return self.size == item.size


class ANDSpecification(Specification):
    def __init__(self, *specs):
        self.specs = specs

    def follows(self, item):
        return all(map(lambda spec: spec.follows(item), self.specs))


class ORSpecification(Specification):
    def __init__(self, *specs):
        self.specs = specs

    def follows(self, item):
        return any(map(lambda spec: spec.follows(item), self.specs))


class BetterFilter:
    @staticmethod
    def filter_items(items, spec):
        return list(filter(lambda item: spec.follows(item), items))


if __name__ == "__main__":
    p1 = Product('Apple', Color.RED, Size.MEDIUM)
    p2 = Product('Watermelon', Color.GREEN, Size.MEDIUM)
    p3 = Product('Sky', Color.BLUE, Size.LARGE)
    p4 = Product('Red Chilli', Color.RED, Size.SMALL)
    p5 = Product('Ladies finger', Color.GREEN, Size.SMALL)
    p6 = Product('Car', Color.RED, Size.MEDIUM)

    products = [p1, p2, p3, p4, p5, p6]
    s1 = SizeSpecification(Size.SMALL)
    c1 = ColorSpecification(Color.RED)
    b1 = BetterFilter()
    or1 = ORSpecification(s1, c1)
    ans1 = b1.filter_items(products, or1)
    for i in ans1:
        print(i.name)

"""
See the benefit of using above approach is that when in future any new requirement/specification comes, we don't need to 
modify our existing class, instead we will extend it and add the new requirement. In this way, there will be very minor 
chance of introducing new bugs in existing production code. 

What I mean is, say in future, a new specification comes and we need to filter on the basis of name which starts with 
some specific character/word. I will create a new specification class for it, extending my base specification class and 
put the follows functionality there.
"""


class NameSpecification(Specification):
    def __init__(self, name_con):
        self.name_con = name_con

    def follows(self, item):
        return item.name.startswith(self.name_con)


if __name__ == "__main__":
    p1 = Product('Apple', Color.RED, Size.MEDIUM)
    p2 = Product('Watermelon', Color.GREEN, Size.MEDIUM)
    p3 = Product('Aky', Color.BLUE, Size.LARGE)
    p4 = Product('Red Chilli', Color.RED, Size.SMALL)
    p5 = Product('Ladies finger', Color.GREEN, Size.SMALL)
    p6 = Product('Aar', Color.RED, Size.MEDIUM)

    products = [p1, p2, p3, p4, p5, p6]

    n1 = NameSpecification('A')
    b1 = BetterFilter()
    for product in b1.filter_items(products, n1):
        print(product.name)
