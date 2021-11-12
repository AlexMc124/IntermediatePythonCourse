from threading import Thread, Lock, current_thread
from queue import Queue
import time 

# A Queue is a data structure that stores data in a first in first out (FIFO) manner.
# a good example is a queue of people waiting to be served at a restaurant.

def worker(q, lock):
    while True:
        value = q.get()
        # processing 
        with lock:
            print(f"in {current_thread().name} got {value}")
            q.task_done()
        # q.task_done()
        # if ...:
        #     break


if __name__ == '__main__':
    
    # q = Queue()
    # q.put(1)
    # q.put(2)
    # q.put(3)
    

    # # 3, 2, 1 -> 
    # first = q.get() # this will get and remove the first item
    # print(first)
    # # 3, 2 -> 
    # # check if the queue is empty
    # print(q.empty())
    # # Threading 
    # # when complete processing call 
    # q.task_done()
    # q.join() # this will wait until all the tasks are doneand elements are processed

    q = Queue()
    lock = Lock()
    num_threads = 10
    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon = True # by default threads are not daemon threads.
        thread.start()

    for i in range(1, 21):
        q.put(i)
        q.join() # block the main thread until all the tasks are done.

    print('end main')

    # with a queue we can easily exchange the data with other threads. in a thread safe way 
    # no other thread can write the same time

