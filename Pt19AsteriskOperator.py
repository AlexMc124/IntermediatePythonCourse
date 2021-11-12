# ASTERISK OPERATOR * * * 
 # Multiplication
 # Creation of lists with multiple elements
 # Args Kwargs
 # Unpacking Lists and Tuples
 # Unpacting Containers

print(3 * 2)
print(3**2)
print("Sorted")

# Creating lists with multiple repeating elements
zeros = [0] * 10
print(zeros)
zerosandones = [0, 1] * 10
print(zerosandones)
# also a tuple 
zeros = (0,) * 10
print(zeros)
zerosandones = (0, 1) * 10
print(zerosandones)
letters = ['a', 'b', 'c'] * 3
print(letters)

# ARGS AND KWARGS 
def foo(x, y, z, *args, **kwargs):
    print(x, y, z)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

print(foo(1,2,3,(4,5,6), {'a':1, 'b':2}))


# Unpacking List elements with the asterisk operator 
def foo(a, b , c):
    print(a, b, c)

mylist = [1, 2, 3]
foo(*mylist)
# the only rule is the number of elements in the list must match the number of parameters

mydict = {'a':1, 'b':2, 'c':3}
foo(**mydict) #  the length of the dict must match the number of parameters
# the keys must also m

*beginning, last = mylist #  will unpack all elements apart from the last into a list then keep the last as a seperate number
print(beginning)
print(last)


beginning, *last = mylist #  will unpack all elements apart from the first into a list then keep the last as a seperate number
print(beginning)
print(last)

beginning, *middle, last = mylist #  will unpack all elements apart from the first into a list then keep the last as a seperate number
print(beginning)
print(middle)
print(last)
# BASICALLY THE THING IS THE ONE WITH THE ASTERISK ON IT IS THE LIST

mytuple = (1, 2, 3)
mylist = [4, 5, 6]
myset = {7, 8, 9}

newlist = [*mytuple, *mylist, *myset]
print(newlist) # will make a new large list - works with sets too

dicta, dictb = {'a':1, 'b':2}, {'c':3, 'd':4}
newdict = {**dicta, **dictb}
print(newdict) # will make a new large dict
