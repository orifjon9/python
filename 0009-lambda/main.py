# lambda arguments: expression
from functools import reduce

add5= lambda x: x + 5
print(add5(10))

multiply=lambda x,y: x*y
print(multiply(20,5))

a = [(1,2), (50, -9), (25, 4), (10,4)]
print(sorted(a))
print(sorted(a, key=lambda x: x[1]))
#[(1, 2), (10, 4), (25, 4), (50, -9)]
#[(50, -9), (1, 2), (25, 4), (10, 4)]


###### map(func, seq)

a =[1,2,3,4,5]
b = map(lambda x: x + 5, a)
print(list(b))
#[6, 7, 8, 9, 10]


##### filter(func, seq)

b = filter(lambda x: x %2==0, a)
print(list(b))
# [2, 4]


##### reduce(func, seq)
r = reduce(lambda x,y: x+y, a)
print(r)
# 15