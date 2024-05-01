"""
Algorithm:

1. Start traversing the Prefix string from last
2. Keep pushing element into stack if it is not an operator
3. If it is an operator,
  a. Pop top and second top element.
  b. Create a new element like ==>  '({top} {operator} {secondTop})'
  c. Push it again to stack
4. Once traversal to Prefix string is done, return the top of stack which would be nothing but Infix notation.
"""

from queue import LifoQueue


def prefixToInfix(prefix: str) -> str:
    stack = LifoQueue()
    for index in range(len(prefix) - 1, -1, -1):
        if prefix[index] in ('+', '-', '*', '/', '^'):
            # If there comes an operator in stack, there must be 2 operands in stack already otherwise it
            # is not a valid Infix notation
            operand1 = stack.get()
            operand2 = stack.get()
            finalElement = f'({operand1}{prefix[index]}{operand2})'
            stack.put(finalElement)
        else:
            stack.put(prefix[index])
    return stack.get()


if __name__ == "__main__":
    print(prefixToInfix("*-a/bc-/dkl"))
