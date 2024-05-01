"""
We will take 2 queues to implement a stack and follow below steps:
1. Add x to Q2
2. Move all elements of Q1 to Q2 element by element
3. Swap(Q1, Q2)
4. To get top element just call get on Q1
"""
from queue import Queue

q = Queue()


class StackUsingTwoQueue:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.lastIndex = 0

    # O(1)
    def pop(self):
        if self.lastIndex == 0:
            return "Queue is empty"
        self.lastIndex -= 1
        return self.q1.get()

    # O(n)
    def push(self, element):
        self.q2.put(element)
        while not self.q1.empty():
            self.q2.put(self.q1.get())
        while not self.q2.empty():
            self.q1.put(self.q2.get())


class StackUsingSingleQueue:
    def __init__(self):
        self.q = Queue()
        self.lastIndex = 0

    # O(1)
    def pop(self):
        if self.lastIndex == 0:
            return "Queue is empty"
        self.lastIndex -= 1
        return self.q.get()

    # O(n)
    def push(self, element):
        self.q.put(element)
        self.lastIndex += 1
        count = self.lastIndex
        while count != 1:
            self.q.put(self.q.get())
            count -= 1


if __name__ == "__main__":
    # s = StackUsingTwoQueue()
    s = StackUsingSingleQueue()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
