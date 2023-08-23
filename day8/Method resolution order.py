# class A:
#     num = 10
#
#
# class B:
#     num1 = 20
#
#
# class C(B, A):
#     def __init__(self):
#         pass
#
#
# c = C()
# print(c.num)
"""
Tell order of MRO
"""


class X:
    pass
    # name = "X"


class Y:
    pass
    # name = "Y"


class Z:
    # name = "Z"
    pass


class A(X, Y):
    # name = "A"
    pass


class B(Y, Z):
    pass
    # name = "B"


class M(B, A, Z):
    pass
    # name = "M"


"""Output is quite confusing, right? Because it is showing us hierarchy in such way because Python uses DFS(Depth 
First Search) to handle hybrid inheritance that is why we are getting such output. Good thing is that you have a way 
to find out how your code flow will be using __mro__ dunder method. See MRO.svg file and do a DFS from M to up. You 
will get your answer. Although we learnt this but make sure never ever write this type of code because it is bad code 
and becomes very complex."""

print(M.__mro__)
