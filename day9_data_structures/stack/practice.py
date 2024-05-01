"""
Determine if Brackets are Balanced.
A balanced set of brackets is one where the number and type of opening and closing brackets match and that is also properly
nested within the string of brackets.

Examples of Balanced Brackets#
{ }
{ } { }
( ( { [ ] } ) )

Examples of Unbalanced Brackets#
( ( )
{ { { ) } ]
[ ] [ ] ] ]
"""
from day9_data_structures.stack.stack1 import Stack2


def balanced(string: str) -> bool:
    string_length = len(string)
    if string_length == 0 or string_length == 1:
        return True
    s = Stack2()
    return False
