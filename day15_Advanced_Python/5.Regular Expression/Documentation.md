# Regular Expression #

- Regular expressions is basically a tiny language all their own that we can use inside Python and many other
  programming languages. We will often hear regular expressions referred to as “regex”, “regexp” or just “RE”. Some
  languages, such as Perl and Ruby, actually support regular expression syntax directly in the language itself. Python
  only supports them via a library that we need to import. The primary use for regular expressions is matching strings.
  We create the string matching rules using a regular expression, and then we apply it to a string to see if there are
  any matches.

- The regular expression “language” is actually pretty small, so we won't be able to use it for all our string matching
  needs. Besides that, while there are some tasks that we can use a regular expression for, it may end up so complicated
  that it becomes difficult to debug. In cases like that, we should just use Python. It should be noted that Python is
  an excellent language for text parsing on its own and can be used for anything we do with a regular expression.
  However, it may take a lot more code to do so and be slower than the regular expression because regular expressions
  are compiled down and executed in C.
- There are some characters that are reserved for regular expressions. These are known as metacharacters. The following
  is a complete list of the metacharacters that Python’s regular expression implementation supports:
- Time Complexity: O(N) for each test case, where N is the length of the given string.
- Auxiliary Space: O(1)
- **/i** means ignore case , **/g** means The "g" flag indicates that the regular expression should be tested against
  all possible matches in a string

```markdown
   **. ^ $ * + ? { } [ ] | ( )**
```

---

## Regular Expression CheatSheet ##

```text

1. Meta Characters
[]  ==>   A set of characters
\   ==> Signals a special sequence (can also be used to escape special characters)
.   ==> Any character (except newline character)
^   ==> Starts with
$   ==> Ends with
*   ==> Zero or more occurrences
+   ==> One or more occurrences
{}  ==> Exactly the specified number of occurrences
|   ==> Either or
()  ==> Capture and group
  
2. Special Sequences
\A ==> Returns a match if the specified characters are at the beginning of the string
\b ==> Returns a match where the specified characters are at the beginning or at the end of a word r"ain\b"
\B ==> Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
\d ==> Returns a match where the string contains digits (numbers from 0-9)
\D ==> Returns a match where the string DOES NOT contain digits
\s ==> Returns a match where the string contains a white space character
\S ==> Returns a match where the string DOES NOT contain a white space character
\w ==> Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
\W ==> Returns a match where the string DOES NOT contain any word characters
\Z ==> Returns a match if the specified characters are at the end of the string
```
