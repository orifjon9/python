# Tuple: ordered, immutable, allows duplicate items

# create
mytuple = ("Orifjon", 35, "Narkulov")
print(mytuple)

mytuple2 = tuple(["Iowa", "Colorado", "Utah"])
print(mytuple2)

# get a single element
print(mytuple[-1])
print(mytuple2[1])

# cant change value

# loop
for x in mytuple2:
    print(x)

# check statement
if "Utah" in mytuple2:
    print("yes")
else:
    print("no")

# length
print(len(mytuple2))

# identify elements in

ab = ("a", "b", "c", "a", "d", "e", "f")

# count of 'a' element in the tuple
print(ab.count("a"))

# a location of the asking element
print(ab.index("f"))

# convert to list
print(list(ab))

# get elements with start and stop
# start:stop - both element positions
print(ab[1:5])

# if you dont spesify a start then starts from beginning
print(ab[:7])

# if you dont spesify a stop then it until the end
print(ab[4:])

# step index
print(ab[::1])
print(ab[::2])
print(ab[::-1])  # reverse


address = "Iowa", 1000, "Fairfield"

state, street_number, city = address
print(state)
print(street_number)
print(city)

i1, *i2, i3 = ab
print(i1)
print(i2)
print(i3)
