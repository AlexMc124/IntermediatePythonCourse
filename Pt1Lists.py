# Lists: ordered - Mutable, allows duplicate elements

mylist = ['banana', 'cherry', 'apple']
print(mylist)

mylist2 = [5, True, "banana"]
print(mylist2)

for i in mylist:
    print(i)


# if with lists
if "banana" in mylist:
    print("yes")
else:
    print("no")

# len - get the length
print(len(mylist))

# append - add to the end
mylist.append(22)

# insert - add to specified index
mylist.insert(1, "pear")
print(mylist)

# pop - remove and return last entry
x = mylist.pop()
print(x)
print(mylist)

# REMOVE - remove a specific element
print(mylist.remove("banana"))

# reverse
a = mylist.sort()
print(a)

# sorted method
mylist = ['banana', 'cherry', 'apple']
print(mylist)
new_list = sorted(mylist)
print(new_list)

# make a new list
new_list = [0] * 5
print(new_list)

#slicing
new_list = [1,2,3,4,5,6]
print(new_list)
print(new_list[1:4])

#steps
new_list = [1,2,3,4,5,6]
print(new_list)
print(new_list[::1]) # one step
print(new_list[::2]) # two step
print(new_list[::-1]) # reversed easily

# copying
list_org = ['banana','cherry','apple']
list_cpy = list_org
list_cpy.append("lemon")
print(list_org)
print(list_cpy)
# lemon has been appended to both as both refer to the same variable


# list comprehension - making a new list that is a copy
a = [1,2,3,4,5,6]
b = [i*i for i in a]
print(a)
print(b)
# the syntax is expression then for loop over the original list