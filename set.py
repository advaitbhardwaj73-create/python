# sets 
"""collection = {1,2,3,4}

print(collection)
print(type(collection))
print(len(collection))

# empty set
collection = set()
print(type(collection))""" # sets are mutable

# Set methods
# 1 - set.add(el) #adds an element

"""collection = {2,10}
collection.add(13)
collection.add(11)
collection.add(29)
collection.add(27)

# remove bhi kd sakte hai
collection.remove(27)
print(collection)
print(len(collection))"""

# set.clear() empties the set

# set.pop() kisi element ko udane ko

"""Set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2)) """

"""subjects = {
    "python", "java", "c++", " java script",
}
print(subjects) """

# 1 wap to enter marks of 3 subjects from the user and store them in a dictioanry . start with an empty 
#dictioary & add one by one . use subjects name as a key and marks as value.

marks = {}

x = int(input("enter OOPS : "))
marks.update({"oops " :x}) 

x = int(input(" enter dbms :"))
marks.update({"dbms :x "})

x = int(input("enter web :"))
marks.update({"web" : x })








