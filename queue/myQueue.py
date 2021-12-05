class Queue:
    arr, frontIndex, rearIndex = [], 0, -1

    def __init__(self) -> None:
        self.frontIndex = 0

    def front(self):
        if self.frontIndex > self.rearIndex:
            return "List is empty"
        return self.arr[self.frontIndex]

    def push(self, data):
        self.arr.append(data)
        self.rearIndex += 1

    def pop(self) -> None:
        if self.frontIndex > self.rearIndex:
            print("Underflow")
            return
        self.frontIndex += 1

    def empty(self) -> bool:
        if self.rearIndex == -1:
            return True
        return False
