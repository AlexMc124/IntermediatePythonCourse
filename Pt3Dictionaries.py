# Dictionary: Key-Value pairs, unordered, Mutable
mydict = {"name": "Alex", "age": 24, "city": "Leicester"}
print(mydict)

# can also be made with python function
mydict = dict(name="Alex", age=24, city="Leicester")
print(mydict)

# access values
value = mydict['name']
print(value)

# appending and updating
mydict["email"] = "alex@xyz.com"
print(mydict)

# deletion
del mydict['name']
print(mydict)
mydict.popitem()
print(mydict)

# checking values
mydict = dict(name="Alex", age=24, city="Leicester")
if "name" in mydict:
    print(mydict["name"])
else:
    print("error")

# looping
for key in mydict:
    print(key)
for key in mydict.keys():
    print(key)
for value in mydict.values():
    print(value)
for key, value in mydict.items():
    print(key, value)

# similarly to lists modifying a copy will modify the original - use the built in copy function
# merging
mydict = dict(name="Alex", age=24, email="alex@xyz.com")
mydict2 = dict(name="Tim", age=28, city="Manchester")

mydict.update(mydict2)
print(mydict)
# the values for keys that exist in both were updated but
# for the keys that exist only in one the original value is kept
# anything can be used as a key, but not a list
mydict = {3:9, 6:36, 9:81}
mydict = {(8, 7), 15}
