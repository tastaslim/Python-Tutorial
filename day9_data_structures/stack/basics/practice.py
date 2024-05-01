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

from queue import LifoQueue


def isValidParenthesis(s: str) -> bool:
    tempStack = LifoQueue()
    if len(s) <= 1:
        return True
    for element in s:
        if element in ('{', '[', '('):
            tempStack.put(element)
        else:

            if element == ']':
                if not tempStack.empty() and tempStack.queue[-1] == '[':
                    tempStack.get()
                else:
                    tempStack.put(element)
            elif element == '}':
                if not tempStack.empty() and tempStack.queue[-1] == '{':
                    tempStack.get()
                else:
                    tempStack.put(element)
            elif element == ')':
                if not tempStack.empty() and tempStack.queue[-1] == '(':
                    tempStack.get()
                else:
                    tempStack.put(element)
    return tempStack.empty()


if __name__ == "__main__":
    inputString = "[()]{}{[()()]()}"
    print(isValidParenthesis(inputString))
