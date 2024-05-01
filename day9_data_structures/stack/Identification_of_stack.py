"""
How to identity whether the question can be solved using stack?

1. If it is an array question and looks good, there is high probability that it can be solved using stack.
2. If there is question which is being solved using two loops and inner loop is somehow dependent on outer loop,
that question can be solved efficiently using stack

These patterns:

for i in range(0, n):
   j ==> i to n
   j ==> 0 to i
   j ==> n to i
   j ==> i to 0

"""
