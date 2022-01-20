`The dependency inversion principle (DIP) has two parts:

1. High-level modules should not depend on low-level modules. Instead, both should depend on abstractions (interfaces)
2. Abstractions should not depend on details. Details (like concrete implementations) should depend on abstractions.`;
/* 
                                       High level Module
                                        /            \
                                       /              \
                                      /                \
                                Low Level Module     Low Level Module
                                    /                     \
                                   /                       \                 =======> Bad Code
                                  /                         \
                            Lower Level Module          Lower level Module
                                /                             \
                               /                               \
                              /                                 \
                        Lowest Level Module             Lowest Level Module
*/
/* 
Because in this case any change in other lower module will break our higher module.
*/

`DIP decouples high and low-level components and instead connects both to abstractions. High and low-level components
can still benefit from each other, but a change in one should not directly break the other.
The advantage of this part of DIP is that decoupled programs require less work to change. Webs of dependencies across your program
mean that a single change can affect many separate parts.
If you minimize dependencies, changes will be more localized and require less work to find all affected components.`;

// class MySQLConnection {
//   public connect() {
//     // handle the database connection
//     return 'Database connection';
//   }
// }                                                    ======> Bad Code

// class PasswordReminder {
//   private dbConnection;
//   constructor(dbConnection: MySQLConnection) {
//     this.dbConnection = dbConnection;
//   }
// }

`You see problem in above code. Each time when type of database changes, We need to modify our PasswordReminder class again and
again to make it work.
Instead what we could do is, define an Interface of type database and let all databases implement it. Inside PasswordReminder
pass variable of this database interface type, because in this way we are freely allowing PasswordReminder class to use any
database.`;
interface DatabaseConnection {
  dbConnection;
}

class MySql implements DatabaseConnection {
  dbConnection;
}
class PostgresSql implements DatabaseConnection {
  dbConnection;
}
class MongoDB implements DatabaseConnection {
  dbConnection;
}
class MsSql implements DatabaseConnection {
  dbConnection;
}
class DynamoDB implements DatabaseConnection {
  //Low Level Module
  dbConnection;
}

class PasswordReminder {
  //High Level Module
  private dbConnection;
  constructor(dbConnection: DatabaseConnection) {
    this.dbConnection = dbConnection;
  }
  getConnection(): string {
    return 'connection';
  }
}
const pass = new PasswordReminder(new MySql()); //            \
const pass2 = new PasswordReminder(new MongoDB()); //          \
const pass3 = new PasswordReminder(new DynamoDB()); //    You see beauty of this code. Now we can pass any database type.
const pass4 = new PasswordReminder(new PostgresSql()); //      /
const pass5 = new PasswordReminder(new MsSql()); //           /
pass.getConnection();
pass2.getConnection();
pass3.getConnection();
pass4.getConnection();
pass5.getConnection();

`Now Basically any change in MongoBD module won't break PassReminder class. Because technically our class is 
independent of type of database(High Level Module doesn't depend on Low level Module, instead they depend on Abstraction(Interface))`;

`The second part can be thought of as “the abstraction is not affected if the details are changed”. The abstraction is the
user-facing part of the program.
The details are the specific behind-the-scenes implementations that cause program behavior visible to the user. In a DIP program,
we could fully overhaul the behind-the-scenes implementation of how the program achieves its behavior without the user’s knowledge.
This process is known as refactoring.`;

`This means you won’t have to hard-code the interface to work solely with the current details (implementation). 
This keeps our code loosely coupled and allows us the flexibility to refactor our implementations later.`;
