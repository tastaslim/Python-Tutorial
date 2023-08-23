"""
A race condition occurs when two or more threads can access shared data, and they try to change it at the same time.
Because the thread scheduling algorithm can swap between threads at any time, you don't know the order in which the
threads will attempt to access the shared data. Therefore, the result of the change in data is dependent on the thread
scheduling algorithm, i.e. both threads are "racing" to access/change the data.
"""

from threading import Thread
from time import sleep

global_count = 0


def update(a: int):
    global global_count
    local_count = global_count
    local_count += a
    sleep(0.3)
    global_count = local_count


if __name__ == '__main__':
    # Both threads are trying to update the same variable global_count at the same time which will cause a race condition.
    # Meaning sometimes the value of global_count will be 1, and sometimes it will be 20 based on thread scheduling algorithm
    # because we don't know when we run this code at that time which thread will be in execution state.
    th1 = Thread(target=update, args=(1,))
    th2 = Thread(target=update, args=(20,))

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    print(global_count)
