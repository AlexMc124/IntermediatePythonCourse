# Tuple : ordered, immuntable, allows duplicate elemensts
# each element seperated by a comma
mytuple = ("Max", 28, "Boston")
print(mytuple)

#also make a tuple from a list
# access using index
print(mytuple[0])
print(mytuple[1])
print(mytuple[2])
print(mytuple[-1])

# tuples are immutible and cannot be changed
for i in mytuple:
    print(i)

if "Max" in mytuple:
    print("Yes")
else:
    print("No")

# len - number of elemeents in tuple
print(len(mytuple))

# count - returns the number of times something appears
tup2 = ('a','p','p','l','e',)
print(tup2.count('p')) # will return 2

# tuple.index - the first occurence of element
print(tup2.index('p')) # will return 1

# can change a tuple to a list
mylist = list(mytuple)
print(mylist)
# and back again
mytupleagain = tuple(mylist)
print(mytupleagain)

# slicing
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:5]
print(type(b)) # b in this case will also be a tuple
# note will not return the last one
# can also use a step
b = a[2:10:2]
print(b)

# unpacking - assigning the tuple values to a variable names
name, age, city = mytuple
print(name)
print(age)
print(city)
# can unpack multiple with a star
mynumtup = (0, 1, 2, 3, 4)
i1, *i2, i3 = mynumtup
print(i1)
print(i2)
print(i3)


# tuples vs list - tuples can be more efficent using large data
import sys
mylist = [0, 1, 2, "hello", True]
mytuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(mylist), "bytes")
print(sys.getsizeof(mytuple), "bytes")
# tuple is 8 bytes less than list despite having same elements

import timeit
# statement , repeat number of times
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))
# tuple takes about half the time
