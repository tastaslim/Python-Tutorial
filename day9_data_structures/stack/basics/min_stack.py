from queue import LifoQueue
from sys import maxsize


class MinStack:

    def __init__(self):
        self.s = LifoQueue()
        self.minimum = maxsize

    def push(self, val: int) -> None:
        self.minimum = min(self.minimum, val)
        self.s.put((val, self.minimum))

    def pop(self) -> None:
        if not self.s.empty():
            self.s.get()

    def getMin(self) -> int:
        if self.s.empty():
            return -1
        return self.s.queue[-1][-1]

    def top(self) -> int:
        if not self.s.empty():
            return -1
        return self.s.queue[-1][0]


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        q = int(input())

        arr = [int(x) for x in input().split()]

        stk = MinStack()

        qi = 0
        qn = 1
        while qn <= q:
            qt = arr[qi]

            if qt == 1:
                stk.push(arr[qi + 1])
                qi += 2
            elif qt == 2:
                print(stk.pop(), end=' ')
                qi += 1
            else:
                print(stk.getMin(), end=' ')
                qi += 1
            qn += 1
        print()
