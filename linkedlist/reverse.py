from linkedlist.linkedlist import take_input


def reverse_list(head):
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


head = take_input()
head = reverse_list(head)
# printData(head)
