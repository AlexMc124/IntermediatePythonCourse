# Lambda : single line functions defined with no name
# lambda args : expression- > returns the result
from functools import reduce

add10 = lambda x: x + 10
print(add10(5))


def add10_func(x):
    return x + 10


# both these do the same thing but one is more efficient

mult = lambda x, y: x * y
print(mult(4, 5))

# normally used when a func is used once or used for functions
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2Dsorted = sorted(points2D)
# returns
# [(1, 2), (15, 1), (5, -1), (10, 4)]
# [(5, -1), (15, 1), (1, 2), (10, 4)]
print(points2D)
print(points2Dsorted)

# this will sort by the x arg but can also give a rule to sort using y
points2Dsorted = sorted(points2D, key=lambda x: x[1])
print(points2D)
print(points2Dsorted)

# sort according to the sum of each
points2Dsorted = sorted(points2D, key=lambda x: x[1] + x[0])
print(points2Dsorted)

# MAP - transforms each element with a function
# map(func, seq)
a = [1, 2, 3, 4, 5]
b = map(lambda x: x * 2, a)
print(a)
print(list(b))
# printing a map object will not work, use list
# can also use list comprehension - but good for example of Map
c = [x * 2 for x in a]
print(c)

# FILTER - takes a finc and seq, returns true or false
#           will return for where the value is true
b = filter(lambda x: x % 2 == 0, a)
print(list(b))
# can also use list comprehensiongit c:
c = [x for x in a if x % 2 == 0]
print(c)

# REDUCE - takes func and seq - returns to all elements and returns a sinlg evalue
a = [1, 2, 3, 4, 5]
product_a = reduce(lambda x, y: x * y, a)
print(product_a)
