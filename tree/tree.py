# class Queue:
#     arr, frontIndex, rearIndex = [], 0, -1
#
#     def front(self):
#         return self.arr[self.frontIndex].data
#
#     def push(self, data):
#         node = BinaryTree(data)
#         self.arr.append(node)
#         self.rearIndex += 1
#
#     def pop(self) -> None:
#         if self.frontIndex > self.rearIndex:
#             print("Underflow")
#             return
#         self.frontIndex += 1
#
#     def empty(self) -> bool:
#         if self.rearIndex == -1:
#             return True
#         return False
from collections import defaultdict

from queue.myQueue import Queue


class BinaryTree:
    def __init__(self, data, left=None, right=None) -> None:
        self.data, self.left, self.right = data, left, right


# def take_input():
#     value = int(input("Enter data: "))
#     root = None
#     while value != -1:
#         newNode = BinaryTree(value)


def print_tree(head):
    if not head:
        return
    print(head.data, end=" ")
    print_tree(head.left)
    print_tree(head.right)


def find_node(head, value):
    if not head:
        return head
    if head.data == value:
        return head
    find_node(head.left, value)
    find_node(head.right, value)


def level_wise(head):
    if not head:
        return
    q1 = Queue()
    q1.push(head)
    while q1:
        front1 = q1.front()
        q1.pop()
        print(front1.data)
        if front1.left:
            q1.push(front1.left)
        if front1.right:
            q1.push(front1.right)


mp = defaultdict(list)


# myIndex[someId].append(someVal)

def action(head, distance):
    if not head:
        return
    mp[distance].append(head.data)
    action(head.left, distance + 1)
    action(head.right, distance + 1)


root = BinaryTree(1)
l1 = BinaryTree(2)
r1 = BinaryTree(3)
l2 = BinaryTree(4)
r2 = BinaryTree(5)

root.left, root.right = l1, r1
l1.left, l1.right = l2, None
r1.left, r1.right = None, r2
r2.left, r2.right = None, None
# levelWise(root)

action(root, 0)
print(mp)
