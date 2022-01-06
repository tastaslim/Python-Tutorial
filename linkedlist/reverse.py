class LinkedList:
    def __init__(self, val, pointer=None) -> None:
        self.val = val
        self.next = pointer


def take_input():
    value = int(input("Enter data: "))
    root, tail = None, None
    while value != -1:
        new_node = LinkedList(value)
        if not root:
            root = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = tail.next
        value = int(input("Enter data: "))
    return root


def print_node(root):
    if not root:
        return
    print(root.val, end=" ")
    print_node(root.next)


def reverse_list(root):
    if not root:
        return root
    prev, current, next_node = None, root, None
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    root = prev
    return root


def next_larger_nodes(head):
    if not head:
        return head
    head = reverse_list(head)
    # print_node(head)
    max_val = head.val
    head.val = 0
    temp = head.next
    while temp:
        if max_val > temp.val:
            temp.val = max_val
        else:
            max_val = temp.val
            temp.val = 0
        temp = temp.next
    head = reverse_list(head)
    return head


r = take_input()
r = next_larger_nodes(r)
print_node(r)
#
# def insert_element(root, data, pos):
#     if not root or pos < 1:
#         return root
#     new_node = LinkedList(data)
#     if pos == 1:
#         new_node.next = root
#         root = new_node
#         return root
#     count, temp, prev = 0, root, None
#     while count < pos and temp:
#         count += 1
#         prev = temp
#         temp = temp.next
#
#     prev.next = new_node
#     new_node.next = temp
#     return root
#
#
# def middle_node(root):
#     if not root:
#         return root
#     slow, fast = root, root
#     while fast and fast.next:
#         slow, fast = slow.next, fast.next.next
#     return slow
#
#
# def delete_node(root, pos):
#     if not root or pos < 0:
#         return root
#     if pos == 0:
#         root = root.next
#         return root
#     temp, prev, count = root, None, 0
#     while count < pos - 1 and temp:
#         count += 1
#         prev = temp
#         temp = temp.next
#     if temp:
#         prev.next = temp.next
#     return root
#
#
# class MyHashSet:
#     root, tail = None, None
#
#     def __init__(self):
#         pass
#
#     def add(self, key: int) -> None:
#         new_node = LinkedList(key)
#         if not self.root:
#             self.root = new_node
#             self.tail = new_node
#             print(self.root.data, end=" ")
#         else:
#             self.tail.next = new_node
#             self.tail = self.tail.next
#             print(self.tail.data, end=" ")
#
#     def remove(self, key: int) -> None:
#         if not self.root:
#             return
#         if self.root.data == key:
#             self.root = self.root.next
#             return
#         temp, prev = self.root, None
#         while temp:
#             prev = temp
#             temp = temp.next
#             if temp.data == key:
#                 prev.next = temp.next
#         if temp:
#             prev.next = temp.next
#         temp = self.root
#         while temp:
#             print(temp.data, end=" ")
#             temp = temp.next
#
#     def contains(self, key: int) -> bool:
#         temp = self.root
#         while temp:
#             if temp.data == key:
#                 return True
#             temp = temp.next
#         return False
#
#     def print_node(self) -> None:
#         if not self.root:
#             return
#         temp = self.root
#         while temp:
#             print(temp.data)
#             temp = temp.next
#
#         # Your MyHashSet object will be instantiated and called as such:
#
#
# obj = MyHashSet()
# obj.add(1)
# obj.add(2)
# obj.add(3)
# obj.add(4)
# obj.add(5)
# obj.remove(1)
#
# class LinkedList2:
#     def __init__(self, key, value, next1=None):
#         self.key = key
#         self.value = value
#         self.next1 = next1
#
#     def print_node(self, head):
#         if not head:
#             return
#         print(head.val, end=" ")
#         self.print_node(head.next)
#
#     # def reverse_list(self, head):
#     #     if not head:
#     #         return head
#     #     prev, current, next_node = None, head, None
#     #     while current:
#     #         next_node = current.next
#     #         current.next = prev
#     #         prev = current
#     #         current = next_node
#     #     head = prev
#     #     return head
#
#     def next_larger_nodes(self, head):
#         if not head:
#             return head
#         head = self.reverse_list(head)
#         # self.print_node(head)
#         max_val = head.val
#         head.val = 0
#         temp = head.next
#         while temp:
#             if max_val > temp.val:
#                 temp.val = max_val
#             else:
#                 max_val = temp.val
#                 temp.val = 0
#             temp = temp.next
#         head = self.reverse_list(head)
#         return head

#
# class MyHashMap:
#     head, tail = None, None
#
#     def __init__(self):
#         pass
#
#     def put(self, key: int, value: int) -> None:
#         temp = self.head
#         while temp:
#             if temp.key == key:
#                 temp.value = value
#                 return
#             temp = temp.next1
#
#         new_node = LinkedList2(key, value)
#         if not self.head:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = self.tail.next1
#
#     def get(self, key: int) -> int:
#         temp = self.head
#         while temp:
#             if temp.key == key:
#                 return temp.value
#             temp = temp.next1
#         return -1
#
#     def remove(self, key: int) -> None:
#         if not self.head:
#             return
#         temp, prev = self.head, None
#         if temp.key == key:
#             self.head = self.head.next1
#             return
#         while temp and temp.key != key:
#             prev = temp
#             temp = temp.next
#         if temp:
#             prev.next1 = temp.next1


# ["MyHashMap","remove","get","put","put","put","get","put","put","put","put"]
# [[],[14],[4],[7,3],[11,1],[12,1],[7],[1,19],[0,3],[1,8],[2,6]]

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(1, 123)
# obj.put(2, 234)
# obj.put(3, 738)
# param_3 = obj.get(1)
# print(param_3)
# obj.put(1, 12)
# param_2 = obj.get(1)
# print(param_2)
# obj.remove(1)
# param_3 = obj.get(1)
# print(param_3)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#   self.next = next
# 5 3 4 7 2
# 0 5 5 0 7


# obj.remove(key)
# print_node(LinkedList(2))
# param_3 = obj.contains(1)
# print(param_3)
# head = take_input()
# element, position = [int(i) for i in input().strip().split(" ")]
# head = insert_element(head, element, position)
# head = reverse_list(head)
# pos = int(input("Enter position to delete node"))
# head = delete_node(head, pos)
# print_node(head)
