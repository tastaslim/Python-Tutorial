"""
  ********************** Open-Closed Principle: ************************
"""
"""
  The Open-Closed Principle requires that classes should be open for extension and closed to modification.
  Modification means changing the code of an existing class, and extension means adding new functionality.
  Meaning, While adding new features in our product, we should make sure that we don't touch/modify our previous
  production code which is already working because it might cause bugs in working code.
"""
"""Let's say, we have this Shape class which has a function to calculate painting cost which requires calculating 
area of Shape. In the beginning we had circular area only but say in the future, we want to paint areas of shape like 
Sphere, Cone, Cylinder and from pass of time different shape comes. Now we have to again and again change existing 
code( PaintingCost function) inside Shape class which can cause bugs and  hence problem in production as we are 
changing previous code again and again. This violates Open Closed Principal."""


class Shape:
    workerCost, electricity_cost = 0, 0

    def __init__(self):
        pass

    def painting_cost(self, radius: int) -> float:
        return 3.14 * radius * radius + self.workerCost + self.electricity_cost


"""
In Typescript:
class Shape {
    private workerCost;
    private electricityCost;
    constructor() { }
    
    public PaintingCost(radius: number): number {
        return 3.14 * radius * radius + this.workerCost + this.electricityCost;
    }
}
"""

"""
But in future what if shape required is Sphere, then we need to change our existing code because area of sphere is 
different from circle. So we need to change our existing code. We might add lots of switch cases to handle different 
shapes, pass various default parameters as different shape require different parameters to calculate area. But this is 
bad practice as we are changing our existing code every time required shape changes.

Hence to overcome this problem, what we can do is, instead of finding radius directly inside painting cost function, 
we can create another base class which contains a function to find area of any shape and let all child classes
( circle, sphere, square, rectangle) extend this base class for finding area by overriding base class are function.
"""
# //See part-2 for Implementation
