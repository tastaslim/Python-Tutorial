"""
Algorithm:

1. Start traversing the Prefix string from last
2. Keep pushing element into stack if it is not an operator
3. If it is an operator,
  a. Pop top and second top element.
  b. Create a new element like ==>  Operand1 Operand2 Operator
  c. Push it again to stack
4. Once traversal to Prefix string is done, return the top of stack which would be nothing but Postfix notation.
"""

from queue import LifoQueue


# Operand1 Operand2 Operator
def preToPost(s: str) -> str:
    stack = LifoQueue()
    for i in range(len(s) - 1, -1, -1):
        if s[i] not in ('*', '+', '-', '/', '^'):
            stack.put(s[i])
        else:
            top = stack.get()
            secondTop = stack.get()
            elementToInsertBack = top + secondTop + s[i]
            stack.put(elementToInsertBack)
    return stack.get()
