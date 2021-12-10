# class LinkedList:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next


# def takeInput():
#     data = int(input("Enter data: "))
#     head = None
#     tail = None
#     while data != -1:
#         newNode = LinkedList(data)
#         if not head:
#             head = newNode
#             tail = newNode
#         else:
#             tail.next = newNode
#             tail = tail.next
#         data = int(input("Enter data: "))
#     return head


# def findMeet(head):
#     if not head:
#         return head
#     slow, fast = head, head.next
#     while fast.next and fast and slow is not fast:
#         slow = slow.next
#         fast = fast.next.next
#     if not fast or not fast.next:
#         return None
#     slow, fast = head, fast.next
#     while slow is not fast:
#         slow = slow.next
#         fast = fast.next
#     return slow


# def findLengthOfLoop(head) -> int:
#     if not head:
#         return 0
#     slow, fast = head, head.next
#     count = 0
#     while fast.next and fast and slow is not fast:
#         slow = slow.next
#         fast = fast.next.next
#     if not fast or not fast.next:
#         return 0
#     nextPointer = slow.next
#     while nextPointer is not slow:
#         nextPointer = nextPointer.next
#         count += 1
#     return count+1


# def reverse(head):
#     if not head:
#         return head
#     prev, current, nextNode = head, None, None
#     while current:
#         nextNode = current.next
#         current.next = prev
#         prev = current
#         current = nextNode
#     head = prev
#     return head


# def FindReverseInK(head, k):
#     if not head:
#         return head
#     count = 0
#     while count < k-1 and head:
#         head = head.next
#         count += 1
#     nextNode = head.next
#     head.next = None
#     temp = reverse(head)
#     nextNode = FindReverseInK(nextNode, k)
#     if nextNode:
#         head.next = nextNode
#         head = temp
#     return head

#     # printData(head)
#     # print()
#     # value, pos = int(input("Enter value: ")), int(input("Enter position: "))
#     # head = insertNode(head, value, pos)
#     # print()
#     # printData(head)
#     # head = removeNode(head, pos)
#     # print()
#     # printData(head)


# def printData(head):
#     if not head:
#         return
#     print(head.data)
#     printData(head.next)


# head = LinkedList(1)
# first = LinkedList(2)
# second = LinkedList(3)
# third = LinkedList(4)
# fifth = LinkedList(5)
# sixth = LinkedList(6)
# head.next = first
# first.next = second
# second.next = third
# third.next = fifth
# fifth.next = sixth
# ans = FindReverseInK(head, 2)
# printData(ans)


class LinkedList:
    def __init__(self, data, pointer=None) -> None:
        self.data = data
        self.next = pointer


def take_input():
    value = int(input("Enter data: "))
    head, tail = None, None
    while value != -1:
        new_node = LinkedList(value)
        if not head:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = tail.next
        value = int(input("Enter data: "))
    return head


def print_node(root):
    if not root:
        return
    print(root.data)
    print_node(root.next)

#
# head1 = take_input()
# print_node(head1)
