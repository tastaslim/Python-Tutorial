from collections import deque

lst = [1, 2, 3, 4, 5, 6, 7, 8]
q1 = deque(lst)
# print(len(q1))
"""
Deque (Doubly Ended Queue) in Python is implemented using the module “collections“. Deque is preferred over list in the 
cases where we need quicker append and pop operations from both the ends of container, as deque provides an O(1) time 
complexity for append and pop operations as compared to list which provides O(n) time complexity.
"""
# Append element at first
q1.appendleft(9)
# print(q1)
# append element at last
q1.append(10)
# print(q1)
# Remove element from first
q1.popleft()
# print(q1)
# remove element from last
q1.pop()
# print(q1)

"""
Count frequencies of an element in the dequeue 
"""
# element = int(input("Enter element to count: "))
# ans = q1.count(element)  # O(n) operation
# print(ans)

"""
Reverse q dequeue 
"""
# print(q1)
# q1.reverse()
# print(q1)

"""
Rotate a dequeue by given number of times
"""
# print(q1)
# q1.rotate(2)  # O(n) operation
# print(q1)

# q2 = q1.copy()
# print(q2)
"""
Insert element at position x
q1.insert(position, element)

Remove element
"""
q1.insert(2, 94)
print(q1)

q1.remove(4)  # Removes first occurrence of element. Raises ValueError if the value is not present.
print(q1)

print(q1.index(94))  # return first index of value. Raises ValueError if the value is not present.
