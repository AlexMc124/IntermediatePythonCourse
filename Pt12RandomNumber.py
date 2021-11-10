# In this we will look at 
# RANDOM - pysdo random 
# SECRETS - crypto strong
# NUMPY - 

import random

#called pysdo random because the numbers are reproducable
a = random.random() # will print a random number between 0 and 1
print(a)
a = random.uniform(1,10) # will print a random float between 1 and 10
print(a)
a = random.randint(1,10) # will print a random number between 1 and 10
print(a)
a = random.randrange(1,10) # will print a random number between 1 and 10 but never pick 10
print(a)
a = random.normalvariate(0, 1) # will print a random number with a mean of 0 and a standard deviation of 1
print(a)

# differnt functions to work with sequences
mylist = list("ABCDEFGH")
a = random.choice(mylist) # will print a random element from the list
print(a)
a = random.sample(mylist, 2) # will print a list of 2 random elements from the list
print(a)
a = random.choices(mylist, k=3) # will choose randomly but can choose same element twice
print(a)
a = random.shuffle(mylist) # will shuffle the list randomly 
# can be reproduced with random seed 


# SEEDS 
random.seed(1) # will set the seed to 1
print(random.random())
print(random.randint(1,10))
random.seed(1) # will use the same seed and pick the same values using the same operations
print(random.random())
print(random.randint(1,10))
# just label ur seeds youll be fine
# dont use them for security purposes

# SECRETS 
import secrets
# use for passwords and security tokens
# diadvantage is takes longer but generate a true random number
print(secrets.randbelow(10)) # produce a random number between 0 and 10
print(secrets.randbits(4)) # produce a random number with 4 bits
print(secrets.token_hex(4)) # produce a random hexadecimal number with 4 characters
print(secrets.choice(mylist)) # produce a random element from the list

# NUMPY 
import numpy as np

a = np.random.rand(3) # will produce an 1d array with 3 random float elements
print(a)
print(type(a))
a = np.random.rand(3, 3) # will produce an 1d array with 3 random float elements
print(a)
print(type(a))
a = np.random.randint(0, 10, (3,4))
print(a) # will produce an 2d array with 3 rows and 4 columns with random int elements
# can also use a random shuffle method
np.random.shuffle(a)
print(a) # Note - will only shuffle the first dimension