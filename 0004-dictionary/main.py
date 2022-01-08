# Dictionary: Key-Value pairs, Unordered, Mutable

# create
from typing import ValuesView


mydict = {"name": "Orifjon", "age": 35, "city": "SLC"}
print(mydict)

print(dict(name="Orifjon", age=35))

print(mydict["age"])

# insert element

mydict["email"] = "test@orifjon.com"
print(mydict)

mydict["email"] = "info@orifjon.com"  # overrides

# delete an element
del mydict["name"]
print(mydict)

mydict.pop("email")  # or mydict.popitem() to delete last element
print(mydict)

# if statement
if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict["last_name"])
except:
    print("last_name key is missing")


# loop
for key in mydict.keys():
    print(key)

for value in mydict.values():
    print(value)

for key, value in mydict.items():
    print(key, value)

# copy
mydict_cp = mydict.copy()
mydict_cp2 = dict(mydict)

# merge
dic1 = {"name": "Orifjon", "age": 35}
dic2 = {"name": "Max", "city": "SLC"}

dic1.update(dic2)
print(dic1)

# complex key
print({(3, 5): 15})
