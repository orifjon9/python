# Strings: ordered, immutable, text representation

my_string = "Orifjon Narkulov"
print(my_string)

# my_string = """Orifjon
# Narkulov
# 35"""
print(my_string)
print(my_string[1])
print(my_string[-2])

# expression
print(my_string[:])
print(my_string[0:7])
print(my_string[::1])
print(my_string[::-1])

# loop
for i in my_string:
    print(i)

if "Orif" in my_string:
    print("yes")

str1 = "   Hello World   "
str1 = str1.strip()  # remove spaces before and after
print(str1)
print(str1.lower())
print(str1.upper())

# find an element index
print(str1.find("ll"))

# count of character
print(str1.count("l"))

# replace
print(str1.replace("World", "Orifjon"))

# list
str2 = "how are you doing dude"
my_list = str2.split(" ")
print(my_list)
print(", ".join(my_list))

my_list = ['a'] * 10
print(my_list)
print(''.join(my_list))

# format
# %, .format(), f-Strings

name = "Orifjon"
mystr = "Hello %s" % name
print(mystr)
print("Hello {}, you are {} old year".format(name, 35))
# new way
print(f"Hello {name}, you are {35} old year")