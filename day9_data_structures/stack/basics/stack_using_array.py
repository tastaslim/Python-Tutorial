class Stack:
    def __init__(self, capacity: int):
        self.stackSize = capacity
        self.lastIndex = 0
        self.arr = [0] * capacity

    def push(self, num: int) -> None:
        if self.isFull():
            return
        self.arr[self.lastIndex] = num
        self.lastIndex += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        topElement = self.arr[self.lastIndex - 1]
        self.lastIndex -= 1
        return topElement

    def top(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.lastIndex - 1]

    def isEmpty(self) -> int:
        if self.lastIndex == 0:
            return 1
        return 0

    def isFull(self) -> int:
        if self.lastIndex == self.stackSize:
            return 1
        return 0
