import random

print(random.uniform(1, 100))
print(random.randint(1, 100))
print(random.normalvariate(0, 1))

# random element from a list
mylist = list("ABSDFTRUJFKRO")
print(random.choice(mylist))
print(random.sample(mylist, 4))
print(random.shuffle(mylist))

