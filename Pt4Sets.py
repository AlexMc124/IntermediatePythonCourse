# Sets: unordered, mutable, no duplicates
myset = {1, 2, 3, 4, 5}
print(myset)
# the order is arbitrary and there are no duplicates
myset = set("Hello")
print(myset)
# the order is arbitrary and there are no duplicates

# add elements
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
myset.add(4)
print(myset)

# remove from the set
myset.remove(1)
print(myset)
# can also use the discard method
myset.discard(2)  # remove if the element is there if not then nothing happens
print(myset)
myset.pop()  # returns the rop and removes

myset = {1, 2, 3, 4}
print(myset)
# iterating over a set
for i in myset:
    print(i)
# logic on a set
if 4 in myset:
    print("In")
else:
    print("Not in")

# union and intersection
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}
# finding the union without duplication
u = odds.union(evens)
print(u)
# finding intersection, only elements found in both sets
i = odds.intersection(primes)
print(i)
# finding differents
a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
b = {1, 2, 3, 10, 11, 12}
# differents return elements in the first set but not the second
diff = a.difference(b)
print(diff)
# symetric differnece - returns a set with all elements in set a and b but not in both sets
symdiff = a.symmetric_difference(b)
print(symdiff)

# modifying
a.update(b)
print(a)  # without duplication elements are added
a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
b = {1, 2, 3, 10, 11, 12}
# intersection update method
a.intersection_update(b)
print(a)
a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
b = {1, 2, 3, 10, 11, 12}
a.difference_update(b)
print(a)
a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
b = {1, 2, 3, 10, 11, 12}
a.symmetric_difference_update(b)
print(a)

# super set and disjoin methods
a = {1, 2, 3, 4, 5, 6}
b = {1, 2, 3}
print(a.issubset(b))
print(b.issubset(a)) # ALL ELEMENTS OF SET A ARE FOUND IN SET B
print(a.issuperset(b)) # ALL ELEMENTS OF SET A ARE FOUND IN SET B
print(b.issuperset(a))
print(a.isdisjoint(b)) # if two sets are both completely different
c = {8, 9}
print(a.isdisjoint(c)) # will return true as both have no common elements

# similarly to lists and dictionaries - making a simple copy will ca
# make a true copy using .copy()

# frozen set = immutable version of a normal set - this is the notation
a = frozenset([1, 2, 3, 4])



