# Shallow vs Deep Copying 
 # use the copy module 

import copy

org = [0,1,2,3,4]
cpy = org 
cpy[0] = -10
print(org, cpy) # doesnt make an actual copy when the copy is changed the original is too 

# shallow - one level deep, only copies reference of the nested child objects 
# deep - makes a true copy 

org = [0,1,2,3,4]
cpy = copy.copy(org) 
cpy[0] = -10
print(org, cpy) # now both are different
#cpy = copy(org)
cpy = list(org)
cpy = org[:]
# all above do the same thing 

# Nested List
org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.deepcopy(org)
cpy[0][1] = -10
print(org, cpy)

# for lists, dicts and tuples we can use methods but can also use for custom objects 


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee


p1 = Person("John", 30)
p2 = p1
# in this example both are affected 
p2.age = 40
print(p1.age, p2.age)    

# use the copy module to prevent this
p1 = Person("John", 30)
p2 = copy.copy(p1)
p2.age = 40
print(p1.age, p2.age)   
# now the age of the two persons are different


# As well in this example both are affected
company = Company(p1, p2)
company_clone = copy.copy(company)
company_clone.boss.age = 56

print(company_clone.boss.age, company.boss.age)

# to prevent this we use deep copy 
company = Company(p1, p2)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 56

print(company_clone.boss.age, company.boss.age)