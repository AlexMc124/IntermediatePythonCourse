# Strings : ordered, immutable, text representation
my_string = "Hello World"
print(my_string)

# substrings
char = my_string[0:5] # the final character is excluded
print(char) # cannot access a character and change it using this method, strings are immutable
print(my_string[::2])

# can concat using +
name = "Alex"
print(my_string + " " + name)

# iterate
for i in my_string:
    print(i)

# logic
if "e" in name:
    print("Yes")
else:
    print("No")

# remove the whitespace using .strip()
# convert to upper using .upper()
# convert to lower using .lower()
# check if starts with using .startswith(x)
# check if ends with using .endswith(x)
# find index of char or substr using .find(x) - if it doesnt find retuns -1
# count number of occurences of a letter .count(x)
# replace(x, y) - replace x with y will return a new string, does nothing if

# lists and strings
my_string = "How are you doing"
my_list = my_string.split()
print(my_list) # splits using each space, can also use delimiter argument
# to str from list
new_string = ' '.join(my_list)
print(new_string)


# forming a string %, .format() and f-strings
var = "Tom"
my_string = "the variable is %s using the old method" % var
print(my_string)
# not to be used with a number use %d, for floats use %.2f where the .2 is the number of decimal places and f is the float
my_string = "the variable is {} using the format method".format(var)
print(my_string)
# finally with f strings
my_string = f"the variable is {var} with an f string"
print(my_string)