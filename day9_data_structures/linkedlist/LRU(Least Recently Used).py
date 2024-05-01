class DoublyLinkedList:
    def __init__(self, data: tuple, next_node=None, prev=None):
        self.data = data
        self.next = next_node
        self.prev = prev


class LRUCache:

    # Constructor for initializing the cache capacity with the given value.
    def __init__(self, cap: int):
        self.keyTracker = dict()
        self.size = cap
        self.head = DoublyLinkedList((0, 0))
        self.tail = DoublyLinkedList((0, 0))
        self.head.next = self.tail
        self.tail.prev = self.head
        self.counter = 0

    # Function to return value corresponding to the key.
    def get(self, key):
        if key not in self.keyTracker:
            return -1
        requiredNode = self.keyTracker[key]
        # print(requiredNode.data[1]) ==> To get value of node
        previousNode = requiredNode.prev
        nextNode = requiredNode.next
        previousNode.next = nextNode
        nextNode.prev = previousNode
        newNode = DoublyLinkedList(requiredNode.data)

        headNext = self.head.next
        self.head.next = newNode
        newNode.prev = self.head
        newNode.next = headNext
        headNext.prev = newNode
        del self.keyTracker[key]
        del requiredNode
        self.keyTracker[key] = newNode
        return newNode.data[1]

        # Function for storing key-value pair.

    def set(self, key, value):
        if self.size == 0:
            return "Size of cache must be greater than 0"
        if key not in self.keyTracker:
            if self.counter != self.size:
                newNode = DoublyLinkedList((key, value))
                nextNode = self.head.next
                self.head.next = newNode
                newNode.prev = self.head
                newNode.next = nextNode
                nextNode.prev = newNode
                self.keyTracker[key] = newNode
                self.counter += 1
            else:
                nodeToRemove = self.tail.prev
                previousNode = nodeToRemove.prev
                previousNode.next = self.tail
                self.tail.prev = previousNode
                del self.keyTracker[nodeToRemove.data[0]]
                del nodeToRemove

                newNode = DoublyLinkedList((key, value))
                nextNode = self.head.next
                self.head.next = newNode
                newNode.prev = self.head
                newNode.next = nextNode
                nextNode.prev = newNode
                self.keyTracker[key] = newNode

        else:
            currentNode = self.keyTracker[key]
            previousNode = currentNode.prev
            nextNode = currentNode.next
            previousNode.next = nextNode
            nextNode.prev = previousNode
            del self.keyTracker[key]
            del currentNode

            newNode = DoublyLinkedList((key, value))
            headNext = self.head.next
            self.head.next = newNode
            newNode.prev = self.head
            newNode.next = headNext
            headNext.prev = newNode
            self.keyTracker[key] = newNode


def print_node(head):
    temp = head
    while temp:
        print(temp.data)
        temp = temp.next


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        cap = int(input())  # capacity of the cache
        qry = int(input())  # number of queries
        a = list(map(str, input().strip().split()))  # parent child info in list

        lru = LRUCache(cap)

        i = 0
        q = 1
        while q <= qry:
            qtyp = a[i]

            if qtyp == 'SET':
                lru.set(int(a[i + 1]), int(a[i + 2]))
                i += 3
            elif qtyp == 'GET':
                print(lru.get(int(a[i + 1])), end=' ')
                i += 2
            q += 1
        print()
