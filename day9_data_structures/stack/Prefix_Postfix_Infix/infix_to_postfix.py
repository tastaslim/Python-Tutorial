"""
Algorithm:

1. Take a map of operators and put values in BODMAS order ==> precedence = {'-': 1, '+': 1, '*': 2, '/': 2, '^': 3}
2. Traverse Infix string and if element:
   a. Not an operator or bracket, append element to output
   b. If element == '(' ==> push into stack
   c. If element == ')' ==> Keep popping the elements from stack and append to output till stack top is '(' but don't
   append ' (' into output.
   d. If operator ==> Keep popping elements from stack and appending to output till the top of stack has less precedence
    than the current element
"""
from queue import LifoQueue

"""
Time Complexity: O(N)
Space Complexity: O(N) for using the stack
"""


def infixToPostfix(exp: str) -> str:
    precedence = {'-': 1, '+': 1, '*': 2, '/': 2, '^': 3}
    ans = ""
    s = LifoQueue()
    for element in exp:
        if element not in ('*', '/', '+', '-', ')', '(', '^'):
            ans += element
        else:
            if element == '(':
                s.put(element)
            elif element == ')':
                while s.queue[-1] != '(':
                    ans += s.get()
                s.get()
            else:
                while not s.empty() and s.queue[-1] in precedence and precedence[element] <= precedence[s.queue[-1]]:
                    ans += s.get()
                s.put(element)
    while not s.empty():
        ans += s.get()
    return ans


if __name__ == "__main__":
    print(infixToPostfix("3^(1+1)"))
