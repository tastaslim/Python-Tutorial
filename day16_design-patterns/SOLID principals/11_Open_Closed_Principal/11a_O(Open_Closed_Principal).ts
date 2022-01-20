/* eslint-disable @typescript-eslint/no-unused-vars */
const pi = 22 / 7;
/*
 ************************************** Open Closed Principal ****************************************
 */
`
 The Open-Closed Principle requires that classes should be open for extension and closed to modification.
 Modification means changing the code of an existing class, and extension means adding new functionality.
 Meaning, While adding new features in our product, we should make sure that we don't touch/modify our previous
 production code which is already working because it might cause bugs in working code.
`;
/*
  Let's say, we have this Shape class which has a function to calculate painting cost which requires 
  calculating area of Shape. In the begging we had circular area only but say
  in future, we want to paint areas of shape like Sphere, cone, cylinder and from pass of time different shape comes.
  Now we have to again and again change existing code( PaintingCost function) inside Shape class which can cause bugs and  hence 
  problem in production as we are changing previous code again and again.
  This violates Open Closed Principal.
*/
class Shape1 {
  private workerCost;
  private electricityCost;
  public PaintingCost(radius: number): number {
    return 2 * pi * radius + this.workerCost + this.electricityCost;
  }
}
`But in future what if shape required is Sphere, then we need to change our existing code because radius of sphere is different 
from circle`;

`Hence to overcome this problem, what we can do is, instead of finding radius directly inside painting cost function, we can create another
base class which contains a function to find area of any shape and let all child classes( circle, sphere, square, rectangle) extend this base
class for finding area.
`;
//See 11b_O_Implementation
