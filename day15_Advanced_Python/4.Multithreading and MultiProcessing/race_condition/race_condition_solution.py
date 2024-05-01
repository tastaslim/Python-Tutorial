"""
To Prevent race condition we can implement locking mechanism.
"""
from threading import Thread, Lock

global_count = 0


def update(a: int, lock: Lock):
    global global_count
    with lock:
        local_count = global_count
        local_count += a
        global_count = local_count

    # We can also use traditional way of try, except and finally block to implement locking mechanism.
    # try:
    #     print("Lock acquired")
    #     lock.acquire()  # Acquire lock before updating the variable to prevent race condition
    #     global global_count
    #     local_count = global_count
    #     local_count += a
    #     global_count = local_count
    # except Exception as e:
    #     print(e)
    #     raise e
    # finally:
    #     print('Lock released')
    #     lock.release()  # Once the thread is done with execution, it releases the lock so that other threads can acquire it.


if __name__ == '__main__':
    # Both threads are trying to update the same variable global_count at the same time which will cause a race condition.
    # To prevent this we will use locking mechanism which tells the program that only one thread can access the shared data
    # at a time and other threads have to wait until the first thread is done with the shared data.

    thread_lock = Lock()
    th1 = Thread(target=update, args=(1, thread_lock))
    th2 = Thread(target=update, args=(20, thread_lock))

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    print(global_count)  # Output: 21 always because only one thread can access the shared data at a time. Once first
    # thread is done with the shared data, the second thread can access it and final sum will be 1+20 = 21
