- Let's say you have a duck company in which you show duck simulation. You provide features like swim and quack and
  below is your initial design which works fine

```markdown
             SuperClass (Duck) ==> (swim, quack functionality)
             /         /       |       \          \       \
            /         /        |        \          \       \
           /         /         |         \          \       \
          /         /          |          \          \       \
       DuckType1  DuckType2  DuckType3 DuckType4 DuckType5  DuckType6 ===> Sub classes inherits SuperClass Duck
```

Over the time due to competition in the industry, the company decided to introduce some new features to the application.
Now they want to show fly functionality too.

- As a OOPS developer, you thought it is pretty simple, just add a new function to SuperClass (Duck) called fly and let
  all subclasses inherit and implement it. But that seemed to be a blunder as you have given fly functionality to those
  ducks too which were not supposed to fly. (Obviously you can override that fly function in subclasses to say method
  not implemented but that is a bad way ). Imagine 1000s of new requirements keep on coming and limited to various
  different types of ducks, this will be a pain in the ass.
- So Inheritance is not going to solve our problem.

```markdown
                                   SuperClass (Duck) ==> (swim,quack,fly)
                                   /              \                \        
                                  /                \                \
                                 /                  \                \
                                /                    \                \
                               /                      \                \
                         DuckType1                DuckType2          DuckType3
```

