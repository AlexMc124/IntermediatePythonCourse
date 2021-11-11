# THREADS VS MULTIPROCESSING 
 # Can run code in parallel to run faster
 # what is the difference between threads and multiprocessing?
 # adv and disadv of both
 # threads are limited by the number of cores on the machine
 # useful modules

# DIFFERENCE OF A PROCESS AND A THREAD

# PROCESSES - *A process is an instance of a program* 
 # + Takes advantage of multiple cores : can execute code in paralell
 # + Seperate memory space -> Memory is shared between processes
 # + Great for CPU-bound processing : if there are large data, expensive computation can be done on multiple CPUs
 # + New process is started independently from other processes 
 # + Processes are interuptable and killable
 # + One GIL for each process -> avoid GIL limitation
 #  * FYI - A GIL is a global interpreter lock * 

 # - Heavyweight : takes more memory and time to create
 # - Starting a process is slower than starting a thread
 # - More memory used
 # - IPC (inter process communication) is more complex


# THREAD - * an entity within a process that can be scheduled for execution (also known as lightweight process) *
 # a process can spawn multiple threads

 # + All threads within a process share the same memory space
 # + Lightweight : takes less memory and time to create
 # + Starting a thread is faster than starting a process
 # + Great for I/O-bound tasks : Input/Output program can use time for slow devices
 
 # - Threading is limited by GIL: Only one thread at a time : no paralell computation in Multi threading
 # - No effect for CPU-bound tasks 
 # - Not interuptable / killable : need to be careful with memory leaks
 # - Careful with race conditions : occurs when two or more threads want to modify the same variable at the same time, causing bugs/ crashes 

# GIL - Global Interpreter Lock
 # controversial in the python community
 # Needed as in C-Python there is Memoryu management that is not thread safe

 # Avoid the GIL:
    # - Use Multiprocessing
    # - Use a differentm free0threaded Python implementation (Jython, IronPython)
    # - Use Python as a wrapper for third party libraries (C/C++) -> numpy, scipy, matplotlib, ...

from multiprocessing import Process, Queue
from threading import Thread
import os
import time

def square_numbers():
    for i in range(100):
        i*i
        time.sleep(0.1)

processes = []
num_processes = os.cpu_count()
print(f"Number of processes: {num_processes}")

# create processes 
for i in range(num_processes):
    p = Process(target=square_numbers) # target is a callable function that is executed in the new process // # args is the function arguments
    processes.append(p)

# start processes 
for p in processes:
    p.start()

# join processes 
for p in processes:
    p.join()
    # this means want to wait for process to finish before continuing and blocking the main thread

print('end main processes - this will only be printed when processes are done')


threads = []
num_threads = 10

# create Thread 
for i in range(num_threads):
    t = Thread(target=square_numbers) # target is a callable function that is executed in the new process // # args is the function arguments
    threads.append(p)

# start processes 
for t in threads:
    t.start()

# join processes 
for t in threads:
    t.join()
    # this means want to wait for Thread to finish before continuing and blocking the main thread

print('end main thread - this will only be printed when processes are done')