# collections: Counter, namedtuple, OrderedDict, deque
from collections import Counter, deque, namedtuple, OrderedDict, defaultdict

# Counter
a = "aaaaabbbbcc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(1))
print(my_counter.most_common(2))

print(my_counter.elements())

# nametuple
Point = namedtuple('Point', "x,y")
pt = Point(1,4)
print(pt)
print(pt.x, pt.y)

# OrderedDict
orderedDict = OrderedDict()
orderedDict['b'] = 10
orderedDict['a'] = 200
orderedDict['c'] = 2
print(orderedDict)

# default dict
d = defaultdict(int)
d['a'] = 10
d['b'] = 30
print(d)
print(d['a'])
print(d['c'])

# dique
dq = deque()
dq.append(10)
dq.append(56)
dq.append(46)

print(dq.pop())
print(dq)
dq.appendleft(1)
dq.extend([5,6,7,8])

print(dq)
dq.rotate(1)