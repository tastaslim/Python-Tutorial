/* eslint-disable @typescript-eslint/no-unused-vars */
`Many client-specific interfaces are better than one general-purpose interface.
Which means that we should not write single interface, put everything inside it and let all classes
implement this, because ultimately class which don't need any specific feature they are forced to implement
those functions.
Because we don't want our client to dependent on those functions/properties which it does not need.
Ultimately they will be either throwing an error saying that method not implemented or something which is wastage
of code and memory and not productive`;
`Hence let only those classes implement an interface which are logically supposed to. For different types of
classes, define different interfaces`;
// interface General {
//   color: string;
//   sound: string;
// }

// class Apple implements General {
//   color: string;
//   sound: string;
// }
// class Cat implements General {
//   color: string;
//   sound: string;
// }
`See in above code Apple class doesn't need sound property but still we are using it inside Apple class because we are implementing
the interface.This is not good practice instead, we should create another interface like fruit for apple and animal for cat`;

interface Animals {
  color: string;
  sound: string;
}

interface Fruits {
  color: string;
}

class Apple implements Fruits {
  color: string;
}
class Cat implements Animals {
  color: string;
  sound: string;
}
