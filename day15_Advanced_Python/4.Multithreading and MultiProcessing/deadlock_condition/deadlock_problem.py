"""
Deadlock problem is a situation where two or more threads are blocked forever, waiting for each other.
This is a problem because your program will never terminate as threads are waiting for each other to finish/ release the lock.
We will do a simple demo of deadlock problem using two functions. Both functions are trying to acquire two locks in different
order. So, one thread will acquire lock 1, and then it will wait for lock 2 to be released by the other thread. But the other
thread will acquire lock 2, and then it will wait for lock 1 to be released by the first thread.
"""
import time
from threading import Lock, Thread


class Projector:
    def __init__(self):
        self.lock = Lock()

    def acquire(self, name):
        print(f'{name} is acquiring the projector')
        self.lock.acquire()
        print(f'The projector is granted to {name}')

    def release(self, name):
        self.lock.release()
        print(f'{name} released the projector')


class Computer:
    def __init__(self):
        self.lock = Lock()

    def acquire(self, name):
        print(f'{name} is acquiring the computer')
        self.lock.acquire()
        print(f'The computer is granted to {name}')

    def release(self, name):
        self.lock.release()
        print(f'{name} released the computer')


def present(name, resource1, resource2):
    resource1.acquire(name)
    time.sleep(2)
    resource2.acquire(name)
    time.sleep(2)
    print('Completed the presentation')
    resource1.release(name)
    resource2.release(name)


if __name__ == '__main__':
    projector = Projector()
    computer = Computer()
    transactions = [["A", "B"], [projector, computer], [computer, projector]]
    th1 = Thread(target=present, args=(transactions[0][0], transactions[1][0], transactions[2][0]))
    th2 = Thread(target=present, args=(transactions[0][1], transactions[1][1], transactions[2][1]))

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    # or we can write below which is same as above
    # with ThreadPoolExecutor(max_workers=2) as executor:
    #     executor.map(present, *transactions)

    print('Done')
