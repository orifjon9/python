# Itertools: product, permutations, combinations, accumulate, groupby and infinity iterators
from itertools import product, permutations, combinations, accumulate, groupby, count, cycle, repeat
import operator

# product - combines elements each other
a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod))  # (1, 3), (1, 4), (2, 3), (2, 4)]
#print(list(product(a, b, repeat=2)))

# permutations - different ordering
a = [1, 2, 3]
perm = permutations(a)
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
print(list(perm))

# Combinations -
a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))  # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]S

a = [1, 2, 3, 4, 5]
acc = accumulate(a)
print(a)         # [1, 2, 3, 4, 5]
print(list(acc))  # [1, 3, 6, 10, 15]

a = [1, 2, 7, 4, 5]
print(list(accumulate(a, func=max)))  # [1, 2, 7, 7, 7]

print(list(accumulate(a, func=operator.mul)))  # [1, 2, 14, 56, 280]

# groupby


def smaller_than_four(x):
    return x < 4


a = [1, 2, 3, 4, 5, 6, 7, 8]
groupby_obj = groupby(a, key=smaller_than_four)
for key, value in groupby_obj:
    print(key, list(value))

# True [1, 2, 3]
# False [4, 5, 6, 7, 8]

persons = [
    {'name': 'Tim', 'age': 25},
    {'name': 'Dan', 'age': 25},
    {'name': 'Lisa', 'age': 27},
    {'name': 'Claire', 'age': 28},
]

for key, value in groupby(persons, key=lambda x: x['age']):
    print(key, list(value))

# 25 [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}]
# 27 [{'name': 'Lisa', 'age': 27}]
# 28 [{'name': 'Claire', 'age': 28}]


# infinite iterators - count, cycle and repeat
for x in count(10):
    print(x)

#a = [1, 2, 3, 4, 5, 6, 7, 8]
#for x in cycle(a):
#    print(x)
#
for x in repeat(10, 5):
    print(x)
