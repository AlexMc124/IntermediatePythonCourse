# GENERATORS - Functions that return an Object that can be iterated over 
# Lazy, generates one at a time and only when needed
# better memory usage 

def my_generator():
    yield 1
    yield 2
    yield 3


# now make a generator object 
g = my_generator()

for i in g:
    print(i)

g = my_generator()
value = next(g) # the function will run until it hits the yield and then return the value
    # in this example, the value is 1 as yeild 1 is the first yield
print(value)

value = next(g) # the function will run until it hits the yield and then return the value
    # in this example, the value is 2 as yeild 2 is the second yield
print(value)

value = next(g) # the function will run until it hits the yield and then return the value
print(value)

g = my_generator()
# generators can also be used as inputs to other functions that take iterables
print(sum(g)) # this will sum all the values in the generator, though if we set 
               # the generator to be next only the last two values will be added

g = my_generator()
print(sorted(g)) # this will sort all the values in the generator

def countdown(num):
    print("starting")
    while num > 0:
        yield num
        num -= 1

cd = countdown(5)
# running this as is will not print anything
value = next(cd)
# the function will run until it reaches the first yeild statement and then return the value
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
# for each time the next is called the function runs again and waits at the yeild value 
#print(next(cd)) # running again will rasie an error and stop iteration (* have commented out so rest of program runs*)

# generators are very memory efficient when working with large data  
# eg a function that takes a number and returns a sequence with all the numbers up to that n

# this is the function without using a generator
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

print(firstn(5))
# all the numbers are stored in this list and so more memory is used

# this is the same function as above but using a generator
def firstngenerator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(firstngenerator(5))
from sys import getsizeof

print(sum(firstn(10))) # for this one the values are all saved in memory and summed
print(sum(firstngenerator(10))) # this one is more memory efficient as it doesn't store all the values in a list

print(getsizeof(firstn(10))) # for this one the values are all saved in memory and summed - 96 bytes for 10 values
print(getsizeof(firstngenerator(10))) # this one is more memory efficient as it doesn't store all the values in a list - 56 bytes for 10 values

print(getsizeof(firstn(1000000))) # for this one the values are all saved in memory and summed - 4348728 bytes for 1000000 values
print(getsizeof(firstngenerator(1000000))) # this one is more memory efficient as it doesn't store all the values in a list - 56 bytes for 1000000 values


# Good example of generators is Fibonacci numbers
def fibonacci(limit):
    # store the first two values
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)
for i in fib:
    print(i)

# GENERATOR EXPRESSIONS - Shortcut to implement a generator expression

my_generator = (i for i in range(10) if i % 2 == 0) # this will put all even elements in a generator object
for i in my_generator:
    print(i)

# similar to a list comprehension but uses different syntax
mylist = [i for i in range(10) if i % 2 == 0]
print(mylist)
print(getsizeof(my_generator)) # 56 bytes for 10000 values
print(getsizeof(mylist)) # 21516 bytes for 10000 values