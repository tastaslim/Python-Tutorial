class Queue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.arr = [0] * 100001

    #  Enqueue (add) element 'e' at the end of the queue.
    def enqueue(self, e: int) -> None:
        if self.rear >= 100001:
            return
        self.arr[self.rear] = e
        self.rear += 1

    #  Dequeue (retrieve) the element from the front of the queue.
    def dequeue(self) -> int:
        if self.front >= self.rear:
            return -1
        ans = self.arr[self.front]
        self.front += 1
        return ans


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())
    q.enqueue(3)
    print(q.dequeue())
