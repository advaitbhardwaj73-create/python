# list in python
#it is like data type store (int,float,string,etc)
# list me bhi indexing 0 se hogi

"""marks1 = 29.9
marks2 = 13.3
marks3 = 2.99
marks4 = 10.99
marks5 = 10.99
marks6 = 27.99

marks = [29.9,13.3,2.99,10.99,10.99,27.99]
print(marks)
print(type(marks))
print(marks[0]) # list me indexing 0 se start hogi
print(marks[1])
print(len(marks)) # list ki length 6 hai 
"""

# ek student class bnakr samjhte hai
"""Student = ["Advait",72,23,"sonpur"]
print(Student) """

# string is immutable in python
# list is mutable in python

# List method topic 2

list = [2,1,4]
list.append(4)  # append me add kdna end me
print(list)

list =[2,1,3]
list.sort() # short in ascending order
print(list)

list =[2,1,3]
list.sort(reverse=True)  # desending order me
print(list)

list =[2,1,3]
list.reverse()
print(list)  # reverse kd dega ulta kd dega

list =[2,1,3]
#list.insert(idx,el)

list= [2,1,3]
list.remove(1) # remove kd dega
print(list)

list= [2,1,3,1]
list.pop(2) # remove kd dega direct aap jo abhi index hatana chahe
print(list)