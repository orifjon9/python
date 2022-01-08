# Lists: ordered, mutable, allows duplicate elements

mylist = ["banana", 5, True, "Apple", "home"]
print(mylist)

# print a single element
print(mylist[1])
print(mylist[3])
# from last first
print(mylist[-1])
# from last second
print(mylist[-2])

# list in a loop
for item in mylist:
    print(item)

# check
if "Apple" in mylist:
    print("yes")
else:
    print("no")

# length
print(len(mylist))

# insert an element in a list
mylist.append("peach")
mylist.insert(1, False)
print(mylist)

# remove an element
print(mylist.pop())
print(mylist)
mylist.remove(1)
print(mylist)
mylist.remove(False)
print(mylist)
# removes all elements in a list
# mylist.clear()

# sort a list
mylist.remove(5)
mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

# merge two lists
mylist2 = ["chicken", "bird"]
new_list: list[str] = ["1", "2", "3", "4", "5"]
new_list2: list[str] = ["6", "7", "8", "9", "10"]
_mylist = new_list + new_list2
print(_mylist)

# get elements with start and stop
# start:stop - both element positions
print(_mylist[1:5])

# if you dont spesify a start then starts from beginning
print(_mylist[:7])

# if you dont spesify a stop then it until the end
print(_mylist[4:])

# step index
print(_mylist[::1])
print(_mylist[::2])
print(_mylist[::-1])  # reverse

# copy
list_org = ["orifjon", "narkulov"]

list_cp1 = list_org.copy()
list_cp2 = list(list_org)
list_cp3 = list_org[:]

list_org.append("o")
print(list_org)
print(list_cp1)
print(list_cp2)
print(list_cp3)

# expression copy
ex_list = ['|' + i + '|' for i in list_org]
print(ex_list)
