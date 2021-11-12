# MULTIPROCESSES 
# CREATE 
# SHARE DATA 
# LOCKS TO PREVENT RACE CONDITIONS 
# PROCESS POOL TO MANAGE PROCESSES 
from multiprocessing import Process, Value, Array, Lock, Queue, Pool
import os 
import time

def cube(number):
    return number * number * number

if __name__ == "__main__":

    numbers = range(1, 11)
    pool = Pool()
    # pools use 4 import processes by default
    # map, apply, join, close
    # map returns a list of results
    # apply returns a single result
    # join waits for all processes to finish
    # close closes the pool

    result = pool.map(cube, numbers)
    print(result)  
    
    # will automatically create as many processes as there are cores on the machine and 
    # split the iterable as equal sized chunks.
    # this is all that needs to be written and the rest is automatic
    pool.close()
    pool.join()

    # pool.apply(cube, (10,))
    
    print("Done!")
    