"""
Basically, we perform operations on data structure while creating these. In one line
"""
# Here we are multiplying by 2 in each element of list.

# ans = [int(x) * 2 for x in input().strip().split(" ")]
# print(ans)

"""
Find square root of elements in list
"""

# ans1 = [math.sqrt(int(x)) for x in input().strip().split(" ")]
# print(ans1)

# ans3 = [x for x in input().strip().split(" ") if int(x) % 2 == 0]  # Print only even elements
# print(ans3)

# ---- SET comprehension ----------------------

ans4 = {x for x in input().strip().split(" ")}  # basically an unordered set
print(ans4)
