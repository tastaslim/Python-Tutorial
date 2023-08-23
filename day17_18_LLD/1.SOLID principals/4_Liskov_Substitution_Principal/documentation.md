# Liskov substitution principle (LSP) #

- The Liskov substitution principle (LSP) is a specific definition of a sub-typing relation created by
  Barbara Liskov and Jeannette Wing. The principle says that any class must be directly replaceable by any
  of its subclasses without error.`;

- In other words, each subclass must maintain all behavior from the base class along with any new behaviors unique to
  the subclass(**subclass must extend the behaviour of base class instead of narrowing it down**. Meaning
  whenever you see something like **method not implemented or property doesn't exist** for any subclass extending a base
  class, you should know that probably the base and child class ae not synced and a new type of base class is required
  for that respective child class.). The child
  class must be able to process all the same requests and complete all the
  same tasks as its parent class.

- In other ways you can say that for any child class inheriting base class, if we change child classes to access
  functionality of base class, it should not affect our users, because our concern is related to base class
  whose functionality ultimately every child class has to implement.
  Meaning that only similar types of child classes should inherit a particular type of base class, because
  in that case only, they will have similar common properties(of base class) along with their own unique property.

- Animal base class should only be inherited by animals like cat, dog, horse not by orange or mango because
  these are category of fruits and for them there should be a base fruit class.

- Generally, when developers violet LSP, they use if else statement or throws an error to disable that feature.
  Let's understand it with the help of an example in next section.
