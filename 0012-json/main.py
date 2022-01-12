import json

person = {
    "name": "Orifjon Narkulov",
    "age": 35,
    "city": "Salt Lake City",
    "title":[
        "Software Engineer",
        "Search Expert",
        "DevOps"
    ]
}

personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

# save in a file
with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)


with open('person.json', 'r') as file:
    person2 = json.load(file)
    print(person2)

    