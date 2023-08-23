# Single Responsibility Principal #

It states that a class should do one thing, and therefore it should have a single reason to change.
Meaning in a class there should be tasks related to one thing.
Let's say we have a class named book which contains methods to list all books, get specific book, create book,
get authors,rename author or book, delete book.
Now we have another method inside book class which has logic to organize and print collection of books/authors.
This will violate Single Responsibility Principal because class has two logics, one information of things and other
to show information. It shouldn't be like this.
Instead, to organize or print collection of books/authors, we should write another class( say PrintBook).

## How Does it help us ##

How does this principle help us to build better software? Let's see a few of its benefits:
Testing – A class with one responsibility will have far fewer test cases.
Lower coupling – Less functionality in a single class will have fewer dependencies.
Organization – Smaller, well-organized classes are easier to search than monolithic ones.
Reusability – Classes with a single responsibility are more likely to be reused.
Readability – Classes that do one thing are easier to read than classes that do many things.

---

```typescript
/* 
Below code violets Single responsibility principal because it does two different things:
1. Operations related to book and author information.
2. Logic to show / display author / book information.
*/

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
        return {id: this.id, name: this.name, authorName: this.authorName};
    }

    public getAuthorName(name) {
        return this.authorName;
    }

    public deleteBook(id) {
        // delete book
    }


    public printAuthorAndBook(id): void {
        console.log(`Book print logic for Id:${id}`);
    }
}
```

**How to overcome above problem? ----> Create another class which contains logic to print/display book/author
information**

```typescript
class Book {
    private readonly id: number;
    private readonly name: string;
    private readonly authorName: string;

    constructor(id: number, name: string, authorName: string) {
        this.id = id;
        this.name = name;
        this.authorName = authorName;
    }

    public getBookInformation() {
        return {id: this.id, name: this.name, authorName: this.authorName};
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

```

## Summary ##

Another example:
Let's say you have a class which has responsibility to store the name, author and text associated to books.
But now you could think, what is benefit of CRUD operations when we can't display book information to User.
So what you did, you added another function to same class which has responsibility to display book information to user
on various platforms. You thought, this is great, but you violated Single Responsibility Principal.
Because say there are two teams working on same project, one team is responsible to store book information and
other team is responsible to display book information. They will be changing same class again and again, which might
lead to incompatible module and can cause merge conflicts.
Any issue in display feature will not affect CRUD operations too, which should not be the case.

## Take away ##

So what is the takeaway from this principal?
The Class should have only one reason to change. We should not add all the logic inside single class, like CRUD
operations, Data persistence, etc. Instead, we should create another class which contains logic to store/display book
information.
