# Decorators - Are used to modify the functionality of a function.
# Function and class decorators.

# FUNCTION DECORATOR - A DECORATOR IS A FUNCTION THAT TAKES ANOTHER FUNCTION AS AN ARGUEMENT
# @mydecorator
# def do_something():
#     pass


def start_end_decorator(func):
    
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper
        
@start_end_decorator
def print_name():
    print("Alex")

print_name()
# as can be seen the decorator is called on the function and the code in the decorator is executed.
# can also call the decorator using 
# print_name = start_end_decorator(print_name)

def print_other_name_decorator(func):
    def wrapper():
        print("This is decorator number 2")
        func()
        print("This is the end of decorator number 2")
        print("\n\n")
    return wrapper

@print_other_name_decorator
def print_name():
    print("Alex")

print_name()

# the wrapper must have the same variables as the function it is decorating.
# this can be fixed by adding args and kwargs to the wrapper function.


import functools 

def decorator2(func):
    
    @ functools.wraps(func) # this will preserve the information of the use function
    def wrapper(*args, **kwargs):
        print("This is decorator number 3")
        result = func(*args, **kwargs)
        print("This is the end of decorator number 3")
        return result
    return wrapper

@decorator2
def add5(x):
    return x + 5

result = add5(5)
print(result)

print(help(add5))
print(add5.__name__)
print(add5.__doc__)

# To make a repeat decorator that repeats the function a number of times.

def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet("Alex")


# NESTED DECORATORS 

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

# the decorators will be executed in the order they are written.
@debug
@decorator2
def say_hello(name):
    greeting = f"Hello {name}"
    print(greeting)
    return greeting

say_hello("Alex")

# CLASS DECORATOR

class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)



@CountCalls # keep track of how many times this has been executed
def say_hello():
    print("Hello")

say_hello()
say_hello()
say_hello()

# USE CASES OF DECORATORS 

# TIMING DECORATORS - used to check execution time of the code
# DEBUG DECORATORS - used to check the code
# CHECK DECORATOR - check if args will fit in the function
# LOGGING DECORATORS - used to log the function
# CACHE DECORATORS - used to cache the function results
# PERFORMANCE DECORATORS - used to check the performance of the function