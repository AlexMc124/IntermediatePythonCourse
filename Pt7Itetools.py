# Itertools : product, permutations, combinations, accumulatem groupby, and infinite iterators
# baso used as a for loop with extra stuff 
from itertools import product, permutations, combinations, accumulate, groupby, combinations_with_replacement, count, \
    cycle, repeat
import operator

## NOTE, ALL OBJECTS MUST BE CONVERTED TO LIST BEFORE BEING PRINTED TO PREVENT THE
## PRINTING OF THE OBJECTS MEMORY LOCATION

a = [1, 2]
b = [3, 4]
# PRODUCT - Calculates the cartesian product of the entries
prod = product(a, b)
# the product will calucate the cartesian product of the two
print(list(prod))
# outputs [(1, 3), (1, 4), (2, 3), (2, 4)]
# can also define number of repitions
b = [3]
prod = product(a, b, repeat=2)
print(list(prod))
# outputs [(1, 3, 1, 3), (1, 3, 2, 3), (2, 3, 1, 3), (2, 3, 2, 3)]

# PERMUTATIONS - return all possible ordering of an input
a = [1, 2, 3]
perm = permutations(a)
print(list(perm))
# can also use the to define the length of the permutations
perm = permutations(a, 2)
print(list(perm))
# outputs [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# COMBINATIONS - returns all possible combinations with a specified length
a = [1, 2, 3, 4]
comb = combinations(a, 2)  # second arg is mandatory
print(list(comb))
# outputs [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)] n.b. no repititions

# COMBINATION WITH REPLACEMENTS - make an iterable
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))  # this one allows for numbers to be used more than once
# outputs [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]

# ACCUMULATE - makes an iter that returns acc sums or any other binary functions
a = [1, 2, 3, 4]
acc = accumulate(a)
print(a)
print(list(acc))  # each of the elements are added together eg 1+ 2 + 3 + 4
# can multiply too
acc = accumulate(a, func=operator.mul)
print(a)
print(list(acc))
# can compare the max too
acc = accumulate(a[::-1], func=max)  # note have reversed the order to demonstrate
print(a)
print(list(acc))
# can subtract too
acc = accumulate(a, func=operator.sub)
print(a)
print(list(acc))


# GROUPBY - returns keys and groups from an iterable
def smaller_than_3(a):
    return a < 3


a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)  # group this into other lists with the
# comparison smaller than 3
for key, value in group_obj:
    print(key, list(value))
# returns True [1, 2]
#         False [3, 4] - sorts them into if theyre smaller than 3 or not

group_obj = groupby(a, key=lambda x: x < 3)  # group this into other lists with the
# group by values that are smaller than 3
for key, value in group_obj:
    print(key, list(value))

# using an object - or a dictionary - sort into thos older and younger than 25
persons = [{'name': 'Alex', 'age': 25},
           {'name': 'Emily', 'age': 25},
           {'name': 'Tim', 'age': 27},
           {'name': 'Claire', 'age': 28}
           ]
group_obj = groupby(persons, key=lambda x: x['age'] > 25)
for key, value in group_obj:
    print(key, list(value))

# INFINITE ITERATORS
# count, cycle, repeat
for i in count(10):
    print(i)
    if i == 15:
        break
# will make an infinite loop that will start at 10 and add one for every repitition
a = [1, 2, 3, 4]
for i in cycle(a):
    print(i)
    break
# will cycle over and over until stop condition
for i in repeat(1, 4):
    print(i)
# will make an infinite loop printing 1, can be given a repeat condition to say hw many times it will be repeated