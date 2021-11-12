# MULTIPROCESSES 
# CREATE 
# SHARE DATA 
# LOCKS TO PREVENT RACE CONDITIONS 
# PROCESS POOL TO MANAGE PROCESSES 
from multiprocessing import Process, Value, Array, Lock
import os 
import time

def add100(numbers, lock):
    for i in range(100):
        time.sleep(0.1)
        with lock:
            for i in range(len(numbers)):
                numbers[i] += 1 

if __name__ == "__main__":

    lock = Lock()
    shared_array = Array('d', [0.0,100.0,200.0])
    print(f'Value at beginning is {shared_array[:]}')
    num_processes = os.cpu_count()
    # sharing data between processes
    # share with a global variable
    # processes dont live in the same memory space so cant share data globally
    # for processes to share data they use a shared memory object
    # A value or an array 

    p1 = Process(target=add100, args=(shared_array,lock))
    p2 = Process(target=add100, args=(shared_array,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()  # returns Value at beginning is 0 // Value at end is 161 due to race conditions


    print(f'Value at end is {shared_array[:]}')
