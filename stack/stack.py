class Stack:
    arr = []
    index = 0

    def push(self, data) -> list:
        self.arr.append(data)
        self.index += 1
        return self.arr

    def pop(self) -> None:
        if not self.empty():
            self.arr.pop()
            self.index -= 1

    def top(self):
        return self.arr[self.index-1]

    def empty(self) -> bool:
        return self.index == 0

    def printStack(self) -> None:
        for element in self.arr:
            print(element, end=" ")


# s1 = Stack()
# s1.push(1)
# s1.push(2)
# s1.printStack()
# print()
