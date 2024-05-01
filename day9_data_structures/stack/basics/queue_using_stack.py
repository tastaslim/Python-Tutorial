from queue import LifoQueue

"""
1. Take two Stacks S1 and S2.
2. For each push operation perform:
 a. S1 -> S2 (Move all elements of S1 to S2 one by one)
 b. Push element to S1
 c. S2 -> S1 (Move all elements of S2 to S1 one by one)

3. For pop operation:
  Check top of S1 ==> S1.get()
 
"""


class QueueUsingTwoStack:
    def __init__(self):
        self.s1 = LifoQueue()
        self.s2 = LifoQueue()

    def pop(self) -> int:
        if self.s1.empty():
            return -1
        return self.s1.get()

    def push(self, element):
        while not self.s1.empty():
            self.s2.put(self.s1.get())
        self.s1.put(element)
        while not self.s2.empty():
            self.s1.put(self.s2.get())
