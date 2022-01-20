`The Liskov substitution principle (LSP) is a specific definition of a sub-typing relation created by 
Barbara Liskov and Jeannette Wing. The principle says that any class must be directly replaceable by any
of its subclasses without error.`;

`In other words, each subclass must maintain all behavior from the base class along with any new behaviors
unique to the subclass. The child class must be able to process all the same requests and complete all the
same tasks as its parent class.`;

`In other ways you can say that for any child class inheriting base class, if we change child classes to access
functionality of base class, it should not affect our users, because our concern is related to base class
 whose functionality ultimately every child class has to implement `;
`Meaning that only similar types of child classes should inherit a particular type of base class, because
in that case only, they will have similar common properties(of base class) along with their own unique property.`;

`Animal base class should only be inherited by animals like cat, dog, horse not by orange or mango because
these are category of fruits and for them there should be a base fruit class.`;

`Generally, when developers violet LSP, they use if else statement`;

`let's consider a rectangle class which has a method to find area`;
// class Rectangle {
//   findArea(length: number, breadth: number): number {
//     return length * breadth;
//   }
// }
/*
  Now in future there comes a demand to implement area functionality for square.
  Now as a developer you might be thinking that square is a rectangle, right. But do you think, we can use same
  function for square, 
  Technically, yes we can but either we need to write an if condition to check when rectangle is square
  (which violets Open Closed Principle) or we have to some set length=breadth. But the problem is
  square needs one parameter and rectangle needs two, then why a user is going to pass two parameters when one
  parameter does the job for him/her. Moreover it will be a wastage of memory.
*/
`Hence Rectangle can't be parent class of square. To solve this problem, what we could do is, create a base class which
contains findArea() method and let rectangle,square or any other class to implement findArea according to them.`;

abstract class Area {
  abstract findArea(...params: number[]): number;
}

class Square1 extends Area {
  findArea(side: number) {
    return side * side;
  }
}

class Rectangle1 extends Area {
  findArea(length: number, breadth: number): number {
    return length * breadth;
  }
}

const t: Area = new Square1();
t.findArea(8);
const t1: Area = new Rectangle1();
t1.findArea(2, 5);

`You see above code, we can findArea using variable of Area type using any child class`;
