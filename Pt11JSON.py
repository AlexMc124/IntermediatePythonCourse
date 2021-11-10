# JSON - Java Script Object Notation
# Python comes with a JSON module that can be used to convert Python data structures to JSON and vice versa.
import json

# See Below the conversion of Python Data to Json
# Python data to JSON
# dict -> obj 
# list, tuple -> arr
# str -> string
# int, long, float -> number
# True, False -> true, false
# None -> null

# Python dict to json string
person = {"firstName": "Sam",
    "lastName": "Smith",
    "hobbies": ["dancing", "flying", "coding"],
    "age": 32, 
    "hasChildren": False,
    "titles": ["engineer", "programmer"]}

# to convert python dict to json string use json.dumps()
# NOTE - JSON dumps is not the same as json.dump()
# use indent to make the json string more readable
# use sort_keys to sort the keys in the json string, tuple
# use separators to change the default seperators
personJSON = json.dumps(person, indent=4, separators=(". ", " = "), sort_keys=True)
print(personJSON)

# put personJSON into a file
with open("person.json", "w") as f:
    json.dump(person, f, indent=4, sort_keys=True)

# use the json.loads() function
# this is known as deserialization
personJSON = '{"firstName": "Sam", "lastName": "Smith", "hobbies": ["dancing", "flying", "coding"], "age": 32, "hasChildren": false, "titles": ["engineer", "programmer"]}'
person = json.loads(personJSON)
print(type(person))

# load json object from example.json file
with open("example.json", "r") as f:
    data = json.load(f)
    print(type(data))
    print(data)


# find firstNames of children in example.json
with open("example.json", "r") as f:
    data = json.load(f)
    for child in data["children"]:
        print(child["firstName"])

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Sam", 32)

# check if object is instance of User class, if so return a dictionary with each of the instaces as key value pairs
def encode_user(o):
    if isinstance(o, User):
        return {'name' : o.name, 'age' : o.age, o.__class__.__name__ : True}
    else:
        raise TypeError(repr(o) + " is not JSON serializable")

# can also implement a custom encoder using JSONEncoder
from json import JSONEncoder
class UserEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name' : o.name, 'age' : o.age, o.__class__.__name__ : True}
        return json.JSONEncoder.default(self, o)



userJson = json.dumps(user, default=encode_user)
print(userJson)


userJson = json.dumps(user, cls=UserEncoder)
print(userJson)
userJson = UserEncoder().encode(user)
print(userJson)

user = json.loads(userJson)
print(user)

# write a decoder for User class
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

user = json.loads(userJson, object_hook=decode_user)
print(type(user))
print(user.name)