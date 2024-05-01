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

    def getSize(self):
        return self.tailIndex

    def isEmpty(self):
        if not self.head:
            return True
        return False

    def push(self, data):
        newNode = Node(data)
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
        newHead = self.head.next
        del self.head
        self.head = newHead

    def getTop(self):
        if self.isEmpty():
            return -1
        return self.head.data


if __name__ == "__main__":
    s = StackUsingLinkedlist()
    s.push(1)
    s.push(2)
    print(s.getTop())
    s.pop()
    print(s.getTop())
    s.push(3)
    print(s.getTop())
    s.pop()
    print(s.getTop())
