abstract class Shape {
  protected abstract findArea(...params: number[]): number;
}

class Circle extends Shape {
  private pi: number = 22 / 7;
  constructor() {
    super();
  }
  findArea(radius: number): number {
    return 2 * this.pi * radius;
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
