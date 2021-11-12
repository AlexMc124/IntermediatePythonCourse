from threading import Thread, Lock, Queue
import time 

# make a global variable
database_value = 0

def increase(lock): # gives a lock obj 
    global database_value

    # aquire the lock 
    with lock:
        local_copy = database_value
        # processing 
        local_copy += 1
        time.sleep(0.1) 
        database_value = local_copy
        

if __name__ == '__main__':
    lock = Lock()
    # make a thread
    print('start value', database_value)
    
    # make thread 1 
    thread1 = Thread(target=increase, args=(lock,)) # both threads are attempting to access the same variable
    thread2 = Thread(target=increase, args=(lock,)) # this is a race condition when two try to m

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('end value', database_value)
    print('end main')

    # Value is 1 at end of thread as both threads are accessing the same variable, but failing.
    # to prevent this we use a lock object

# def square_numbers():
#     for i in range(100):
#         i * i


# if __name__ == "__main__":
#     threads = []
#     num_threads = 10
#     sleep(0.1)
    
#     # create threads 
#     for i in range(num_threads):
#         thread = Thread(target=square_numbers)
#         threads.append(thread)
    
#     # start threads
#     for thread in threads:
#         thread.start()
    
#     # join threads 
#     for thread in threads:
#         thread.join()

#     print("Done!")