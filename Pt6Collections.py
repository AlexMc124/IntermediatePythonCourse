# Collections : Counter, namedTuple, OrderedDict, defaultdict, deque
from collections import *

# stores elements as dict keys and counts as values
a = "aaabbbbccc"
my_counter = Counter(a)
print(my_counter.items())
print(my_counter.most_common(1)[0][0])  # arg is usd to determine the number of how many elements to return
print(list(my_counter.elements()))

# named tuple = namedtuple(CLASS, DIFFERENTFIELDS)
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)  # returns Point(x=1, y=-4)

# ordered dictionary = Regular dict but remembers the order items were inserted
#                       dictionary class now also rememebers the oreder since 3.7
#                          older python versions use this

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)  # Returns OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
# remembereing the oreder they were inserted
# Default Dict = similar to usual dict container but will have a default value if key hasnt been set,
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['a'])
print(d['c'])  # entering a key that doesnt exist will return a default value
# prevents raising a key error

# deque - double ended queue, used to add and remove from both ends
d = deque()
d.append(1)
d.append(2)
print(d)
d.appendleft(3)  # will add to the front
print(d)
d.pop()  # wil return and remove the last element
print(d)
d.extend([4, 5, 6]) # will add all elements to the right
print(d)
d.extendleft([4, 5, 6]) # will add all elements to the left
print(d)
d.rotate(1) # will rotate all elements to the right
print(d)
d.rotate(-1) # will rotate all elements to the left