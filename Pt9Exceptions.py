# Errors and Exceptions

# SYNTAX ERROR - when the parser detects a syntactically incorrect statement
# eg1) a = 5 print(5)
# eg 2.) print(5))

# TYPE ERROR - Trying to add a string and an int

# IMPORT ERROR - Trying to import a module that doesnt exist

# NAME ERROR - Trying to use a variable that doesnt exist

# FILE ERROR - Trying to use a file that doesnt exist, is in the wrong place

# VALUE ERROR - The right type but the wrong value
# a = [1, 2, 3]
# a.remove(4) - 4 is not in the list so

# INDEX ERROR - Trying to access an index that isnt real
# my_dict = {'name' : 'Alex'}
# my_dict['age']

# RAISING AN EXCEPTION - use the raise keyword
x = 5
if x < 0:
    raise Exception('x should be positive')

# can also use ASSERT statement - will throw error if not true
x = 1
assert (x >= 0), 'x is not positive'

# ERRORS and EXEPTIONS
try:
    a = 5 / 1
    b = 10 + a
except Exception as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally:  # good for cleanup operations - > always runs
    print("program finished, cleaning up...")


# if you know the specific errors use them

# MAKE OWN ERRORS

class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

# this is already valid


def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value is too high")
    if x < 5:
        raise ValueTooSmallError('value is too small : ', x)
try:
    test_value(1)
except ValueTooSmallError as e:
    print(e.message, e.value)
except ValueTooHighError as e:
    print(e)  # message is printed but program will continue to run
