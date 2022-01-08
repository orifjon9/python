# Sets: unordered, muttable, no duplicates

# create
mysets = {1, 2, 3, 1, 2}
print(mysets)

mysets = set([5, 6, 7, 8, 9, 0, 1, 2, 1])
print(mysets)

print(set("Hello"))  # {'o', 'H', 'l', 'e'}

# add elements
mysets.add(10)
mysets.add(11)
mysets.add(1)
print(mysets)

# remove
mysets.remove(1)
mysets.pop()  # removes the first element
print(mysets)

# loop
for i in mysets:
    print(i)

# if check
if 10 in mysets:
    print("yes")

# union
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

# union
u = odds.union(evens)
print(u)

# inter section elements
i = odds.intersection(primes)
print(i)

# difference
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

print(setA.difference(setB))  # takes setA elements not in setB
print(setB.difference(setA))  # takes setB elements that are not in setA
# takes elemens that are not in both sets
print(setA.symmetric_difference(setB))


# update
# setA.update(setA) # unions elemens
# setA.difference_update(setB) # removes all elements that contains setB
setA.symmetric_difference_update(setB)  # removes all elements on both sets

# calculate
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
print(setB.issubset(setA))  # setB all elements are in setA.
# opposite method is .issuperset()

setC = {7, 8}
print(setA.isdisjoint(setC))  # both sets do not have the same element

# copy
setD = setC.copy()
setE = set(setA)
