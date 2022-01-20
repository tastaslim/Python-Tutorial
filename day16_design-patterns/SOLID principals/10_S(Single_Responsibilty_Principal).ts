/* eslint-disable @typescript-eslint/no-unused-vars */
/*
 ********************** Single Responsibility Principal *****************************
 */
`
  It states that a class should do one thing and therefore it should have only a single reason to change.
  Meaning in a class there should be tasks related to one thing.
  Let's say we have a class named book which contains methods to list all books, get specific book, create book,
  get authors,rename author or book, delete book.
  Now we have another method inside book class which has logic to organize and print collection of books/authors.
  This will violate Single Responsibility Principal because class has two logics, one information of things and other
  to show information. It shouldn't be like this.
  Instead to organize or print collection of books/authors, we should write another class( say PrintBook).
`;
/*
// Below code violets Single responsibility principal because it does two different things
   1. Operations related to book and author information.
   2. Logic to show/display author/book information
class Book {
  private id: number;
  private name: string;
  private authorName: string;
  constructor(id: number, name: string, authorName: string) {
    this.id = id;
    this.name = name;
    this.authorName = authorName;
  }
  public getBookInformation() {
    return { id: this.id, name: this.name, authorName: this.authorName };
  }
  public getAuthorName(name){
     .
     .
     .
  }

  public deleteBook(id){
    .
    .
    .
  }
  public printAuthorAndBook(id): void {
    console.log(`Book print logic for Id:${id}`);
  }
}
*/

// How to overcome above problem? ----> Create another class which contains logic to print/display book/author information.
class Book {
  private id: number;
  private name: string;
  private authorName: string;
  constructor(id: number, name: string, authorName: string) {
    this.id = id;
    this.name = name;
    this.authorName = authorName;
  }
  public getBookInformation() {
    return { id: this.id, name: this.name, authorName: this.authorName };
  }
  public getAuthorName(name) {
    console.log(`Author Name:${name}`);
  }

  public deleteBook(id) {
    console.log(`Book deleted successfully with Id:${id}`);
  }
}

class PrintBook {
  public printAuthorAndBook(id): void {
    console.log(`Book print logic for Id:${id}`);
  }
}
