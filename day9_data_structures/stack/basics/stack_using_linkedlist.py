class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class StackUsingLinkedlist:
    # Write your code here
    def __init__(self):
        self.tailIndex = 0
        self.tail = None
        self.head = None
        self.prevNode = None

    def getSize(self):
        return self.tailIndex

    def isEmpty(self):
        if self.tailIndex == 0:
            return True
        return False

    def push(self, data):
        newNode = Node(data)
        self.prevNode = self.tail
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
        self.tailIndex += 1

    def pop(self):
        if self.isEmpty():
            return
        if self.prevNode:
            self.prevNode.next = None
            del self.tail

        self.tail = self.prevNode
        self.tailIndex -= 1

    def getTop(self):
        if self.isEmpty():
            return -1
        return self.tail.data
