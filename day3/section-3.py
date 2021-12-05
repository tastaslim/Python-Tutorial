"""[summary]
    Take input as a list and print sum of it's elements.
"""

lst = [int(i) for i in input().strip().split(" ")]
sum = 0
for element in lst:
    sum += element
print(sum)

for i in range(0, 10, 2):
    print(i)
