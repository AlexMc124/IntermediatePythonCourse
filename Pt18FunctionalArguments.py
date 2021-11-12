# FUNCTIONAL ARGUMENTS
 # - The difference betetween arguements and parameters
    # parameters are variables that are defined and used in a function 
    # 
 # - Positional and Keyword arguments
 # - Default arguments
 # - Variable-Length arguements (*args and **kwargs)
 # - Container unpacking into function arguements
 # - Local and Global arguements
 # - Parameter passing (by value or by reference?)


# PARAMETERS AND ARGUEMENTS 
def name(name): # in this example, name is a parameter
    print(name) # name is a local variable

print("Alex") # when the function is called, the value of name "Alex" is an argument

# POSITIONAL AND KEYWORD ARGUMENTS

def foo(a, b , c): # a, b, c are parameters
    print(a, b, c)

foo(1, 2, 3) # 1, 2, 3 are positional arguments
foo(a = 1, b = 2, c = 3) # 1, 2, 3 are keyword arguments, the order of the keyword arguments is not important
foo(1, b=2, c=3) # A mix of both can be used

# DEFAULT ARGUMENTS
def foo(a, b , c, d=4): # a, b, c are parameters
    print(a, b, c, d)

foo(a = 1, b = 2, c = 3) # d doesn't have a value, so it defaults to 4

# VARIABLE LENGTH ARGUMENTS
def foo(a, b, *args, **kwargs): 
    # *args mean any number of positional arguements to the function - args is a tuple
    # *kwargs mean any number of key word arguements to the function - kwargs is a dictionary
    # the names arent important but convention is args and kwargs
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3, 4, 5, six=6, seven=7)


# key word only arguements
def foo(a, b, *, c, d): 
    # any parameter after the star are keyword only arguements so must be called as such 
    print(a, b, c, d)

foo(1, 2, c=3, d=4)

# UNPACKING ARGUMENTS 
def foo(a, b, c):
    print(a, b, c)

my_list = [0, 1, 2]
foo(*my_list) # unpacks the list into the function, this is matching a positional arguement
mydict = {'a': 0, 'b': 1, 'c': 2} # for a list the key must have the same name as the parameter
# for each the length of the variables must match the length of the parameters

# LOCAL VS GLOBAL VARIABLES 
def foo():
    global number
    x = number
    # number = 3 # this is a local variable that is different in the function
    # to modify we must use the global keyword
    number = 3
    print(x)

number = 0 
foo() # this will print the number inside the function but modifying it from inside the function will not affect the global variable
foo() # this means we will output 3 

# to modify a variable in a function we must use the global keyword

# PARAMETER PASSING
 # Mutable objects can be changed within a method, but the original object is not modified
 # immuatable cannot be changed within a methd but .

def foo(x):
    x = 5 # var is an integer and will make a local variable x that has nothing to do with the global variable var

var = 10
foo(var) # this will not modify the original variable
print(var) 

def foo(myList):
    myList.append(4) # myList is a list, a mutable data type and so will be modified by the function

myList = [1, 2, 3]
foo(myList) # this will modify the original variable
print(myList) 