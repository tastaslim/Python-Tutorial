
from linkedlist.linkedlist import takeInput


def reverseList(head):
    if not head:
        return head
    prev, current, nextNode = None, head, None
    while current:
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode
    head = prev
    return head


head = takeInput()
head = reverseList(head)
# printData(head)
