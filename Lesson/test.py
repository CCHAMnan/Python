class Person:
 def __init__(self, id, name, age):
    self.id = id
    self.name = name
    self.age = age
# open a file
file1 = open("People.txt", "r")
# read contents to the file
data = file1.read().rstrip("\n")
# close the file
file1.close()
# slite the data and store it into a list
list1 = data.split("\n")
# loop through the list, then split each item of the list and
# store them in a dictionary of Person
dict1 = {}
for item in list1:
 p = Person("", "", "")
 p.id, p.name, p.age = item.split(" ")
 dict1[p.id] = p
# display the dictionary
for p in dict1.values():
 print(p.id, p.name, p.age)
