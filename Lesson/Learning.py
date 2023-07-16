name1 = "Bro code"
age1 = 19
print("Hello "+ name1 )
print("Your age is :"+ str(age1))




#multiple assignment

place1, date1 ,human1 = "home", 19, True 
print(place1)




#if all varible has the same value 

Math1 = English1 = History1 = 30
print(Math1)
print(English1)
print(History1)




#string method

#name = "Hello"

#print(len(name))  length of a string
#print(name.find("H"))  Find character in a string
#print(name.capitalize())  Captitalize the first letter of a string
#print(name.upper())  Captitalize all the letter of a string
#print(name.lower())  Lower case all the the letter of a string
#print(name.isdigit())  Check if the name is a number or not
#print(name.isalpha())  Check if the name is a letter or not 
#print(name.count("l"))  count the letter or thing you want to count
#print(name.replace("l","y"))  replace the letter to another like l to y
#print(name*4) display the string as many time as you want



#Type casting / covert any daya type to another data type 
g1 = 2.2
print(int(g1))



#Accept user input
dire1 = input("What is that you want?: ")
print(dire1)




#function related to number
import math

pi = 3.14
#print(round(pi)) round a number to a whole number
#print(math.ceil(pi)) round a number up to a whole number
#print(math.floor(pi)) round a number down too a whole number
#print(abs(pi)) make an absolute number which is always positive number
#print(pow(pi,2)) power function , pi to the power of 2
#print(math.sqrt(pi)) squart root a number
#print(max(x,y,z)) find the largest number among them
#print(min(x,y,z)) find the smallest number among them





#String slicing = by using indexing[] or slice()
#                  [start:stop:step]

test = "Bro Code"
first_name = test[0:3] #or first_name = test[:3]
last_name = test[4:8] #or last_name = test[4:]
funcky_name = test[0:8:2] #or funky_name = test[::2] How many step to skip for the next letter
reversed_name = test[::-1] #for reversing a string

#we can also use slice
slice = slice(7,-4)
print(test[slice])





#If statement
age = int(input("How old are you?: "))

if age >= 18:
    print("You are an adult!")
elif age < 0:
    print("You are apoted!")
else:
    print("You are a child")




#logical Operators(and,or,not)

temp = int(input("What is the temperature outside?: "))
if temp >=0 and temp <= 30: #both condition must be true(and)
    print('The temperature is good today!')

elif temp < 0 or temp > 30: #any condition works(or)
    print("The temperature is bad today!")

if not(temp >=0 and temp <= 30): #make false to true/ true to false
    print("the temperature is bad!")




#While loop = unlimited
name = ""
while len(name) == 0:
    name = input("Please Enter your name: ")
print("Hello "+name)



#For Loop = limited

for i in range(10):
    print(i+1)
for i in range(50,100):            #from what range to what range
    print(i)
for i in range(50,100,2):           #This will count up by 2 cus of the last argument
    print(i)
for i in "Bro Code":                #print out a string
    print(i)





#Nested loops
rows = int(input("How many row?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="") #the end="" is for not making it print to the new lines but next to it
    print()
    







#loop control statement

#break =   used to terminate the loop entirely
#cntinue = skips to the next iteration of the loop
#pass =    does nothing, acts as a placeholder

while True: #break / end a loop
    name2 =  input("Enter your name: ")
    if name2 != "":
        break

phone_number = "123-456-7890" #continue /ignore a string or letter
for i2 in phone_number:
    if i2 == "-":
        continue
    print(i2, end="")

for i in range(1,21): #pass / to skip
    if i == 13:
        pass
    else:
        print(i)








#list/ like array = used to store miltiple items in a single variable

food = ["pizza","hamburger","hotdog","spaghetti"]
food[0] = "sushi" #replace an item in the list
print(food[2])

food.append("ice cream") #add an item to the list
food.remove("hotdog") #remove an item from the list
food.pop() #will remove the last element
food.insert(0,"cake") #add an item to a certain index
food.sort() #sort the list in alphabetically abc...
food.clear() #remove everything from the list

for x in food:
    print(x)






#2D list = 2D array

drinks = ["coffee","soda","tea"]
dinner = ["pizza","hambirger","hotdog"]
dessert = ["cake","ice cream"]

food = [drinks, dinner,dessert]
print(food[2][1])








#Tuple =  collection which is ordered an unchangable/ used to group related data

student = ("Bro",21,"male")

print(student.count("Bro"))
print(student.index("male"))

for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here to play!")







#set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup"}

utensils.add("napkin")
utensils.remove("fork")
utensils.clear()
utensils.update(dishes) #add all the dishes element to the utensils
dinner_table = utensils.union(dishes) #add 2 sets to create another set

print(utensils.difference(dishes)) #compare what the set have but the other don't
print(utensils.intersection(dishes)) #show sth they have in common

for x in utensils:
    print(x)










#dictionary = A changable, unordered collection of unique key: value pairs
#             Fast because they use hashing, allow us to access a value quickly

captials = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}

captials.update({'Germany':'Berlin'}) #add new key
captials.update({'USA':'Las Vegas'}) #update the value in existing key
captials.pop('China') #remove a key

print(captials['Russia']) 
print(captials.get('Germany'))  #find key
print(captials.keys())  #only the key
print(captials.values())  #only the value
print(captials.items())  #print both

for key,value in captials.items(): #print the hole dictionary
    print(key, value)












#index operator [] = gives access to a sequence's element(str,list,tuples)

name4= "bro code!"

if(name4[0].islower()):
    name4 = name4.capitalize()

first_name = name4[0:3].upper()
last_name = name4[4:].lower()
last_character = name4[-1]

print(first_name)
print(last_name)
print(last_character)









#function

def hello(first_name,last_name,age):
    print("Hello "+first_name+" "+last_name)
    print("You are "+str(age)+" years old")
    print("Have a nice day!")

hello("Bro","Code",21)






#return statement in function
def multiply(number1,number2):
    result = number1 * number2
    return result # = return number1 + number2

x = multiply(6,8)

print(x)








#keywork arguments in the function = allow argument in any position but with a identifier

def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

hello(last="dude", middle="cool", first="Mister")








#nested function

print(round(abs(float(input("Enter a whole postive number: ")))))







#scope = The region that a varible is recongnized

name01= "Bro"

def display_name():
    name01 = "Code"
    print(name01)

display_name()
print(name01)











#*args = parameter that will pack all arguments into a tuple 
#        useful so that a function can accept a varying amount of arguments

def add(*args): #can name anything just don't forget the *
    sum = 0
    args = list(args)
    args[0] = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6))












#**Kwargs = parameter that will pack all arguments into a dictionary
#           useful so that a function can accept a varying amount of keyword argument

def hello(**kwargs):
    #print("Hello "+ kwargs['first'] + " " + kwargs['last'])
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")

hello(title="Mr.",first="Bro",middle="Dude",last="Code")











# str.format() =    optional method that gives users
#                   more control when displaying output

animal = "cow"
item = "moon"

print("The "+animal+" jumped over the "+item)

# {} = format field
print("The {} jumped over the {}".format("cow","moon"))
print("The {0} jumped over the {1}".format(animal,item)) # positional arguments
print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))   # keyword arguments

text = "The {} jumped over the {}"
print(text.format("cow","moon"))

name = "Bro"

print("My name is {}".format(name))
print("My name is {:10}".format(name,name))   # amount of padding
print("My name is {:<10}".format(name,name))  # < = left align
print("My name is {:>10}".format(name,name))  # > = right align
print("My name is {:^10}".format(name,name))  # ^ = center align


# str.format() =    optional method that gives users
#                   more control when displaying output

number = 1000

print("The number pi is {:.3f}".format(number))  #how many digit behind decimal
print("The number is {:,}".format(number))       #add , to every thousandth place
print("The number is {:b}".format(number))       #show binary digit 
print("The number is {:o}".format(number))       #show ota-decimal
print("The number is {:X}".format(number))       #show Hexa-decimal
print("The number is {:E}".format(number))       #Show scientific number










import random
x = random.randint(1,6) #generate a number from 1-6
y = random.random() #generate a float 

mylist = ['rock','paper','scissors']
z = random.choice(mylist) #generate a choice in the list

cards = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
random.shuffle(cards) #shuffle the list

print(cards)










#File dectection 
import os  #For files

path = "C:\\Users\\M\\Desktop\\Class\\python.txt"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exist!")








#Reading Files
with open('C:\\Users\\M\\Desktop\\Class\\Python.txt') as file:
    print(file.read())






#Writing files

text = "\nYoooooooo"

with open('C:\\Users\\M\\Desktop\\Class\\Python.txt','a') as file:  #'w' to over write a file
    file.write(text)                                                #'a' to append a file













#Copying a file

#copyfile() = copies contents of a file
#copy() =     copyfile() + permission mode + destination can be a directory
#copy2() =    copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile('C:\\Users\\M\\Desktop\\Class\\Python.txt','C:\\Users\\M\\Desktop\\Class\\copy.txt') #from where - to where








#Moving a file
import os

source = "C:\\Users\\M\\Desktop\\Class\\Python.txt"
destination = "C:\\Users\\M\\Desktop\\Class\\Python.txt"

os.replace(source,destination)






#Deleting a file
import os
import shutil
os.remove('random.txt') #for deleting file
os.rmdir('random.txt') #for deleting folder
shutil.rmtree('random.txt') #for folder containing file






#module = a file containing python code
help("modules")
#or go to this ink   https://docs.python.org/3.9/py-modindex.html








#OOP-------------------------------------------------------------
class Car:
    #contructor
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

car_1.drive()
car_2.stop()
#-----------------------------------------------------------------










#Inheritance

class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")
        
    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal): #Inheritance
    def run(self):
        print("This rabbit is running")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming")

class Hawak(Animal):
    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawak()

print(rabbit.alive)
fish.eat()
hawk.sleep()

hawk.fly()
fish.swim()
rabbit.run()








#Multiple Inheritance

class Prey:
    def flee(self):
        print("This animal flees")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey,Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

fish.flee()
fish.hunt()









#Method chaining

class Car:
    def turn_on(self):
        print("You start the engine")
        return self             #Use return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brake")
        return self

    def turn_off(self):
        print("you turn off the engine")
        return self

car = Car()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off() #Or write in 1 line without the \







#Super function = super() : function used to give access to the method of a parent class

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length,width)
    
    def area(self):
        return self.length*self.width

class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length,width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height

square = Square(3,3)
cube = Cube(3,3,3)

print(square.area())
print(cube.volume())











#Abstract class = a class which contains one or more abstact mthods
#                 ,Its prevents a user from creating an object of that class
#Abstract method = a method that has a declaration but does not have an implementation

from abc import ABC, abstractclassmethod

class Vehicle(ABC):

    @abstractclassmethod
    def go(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You dive the car")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")


car = Car()
motorcycle = Motorcycle()









#pass Object as Argument
class Car:

    color = None

class Motorcycle:

    color = None

def change_color(vehicle,color):

    vehicle.color = color


car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()

change_color(car_1,"red")
change_color(car_2,"white")
change_color(car_3,"blue")
change_color(bike_1,"black")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)






#Duck typing = concept where the class of an object is less important than the methods/attributes

class Duck:
    def walk(self):
        print("This duck is walking")
    def talk(self):
        print("This duck is qwuacking")

class Chicken:
    def walk(self):
        print("This chicken is walking")
    def talk(self):
        print("This chicken is clucking")

class Person():
    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)









#walrus operator :=

# assignment expression aka walris operator
#assigns values to variable as part of  larger expression


#foods = list()
#while True:
#    food = input("What food do you like?: ")
#    if food == "quit":
#        break
#    foods.append(food)

foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)






#assign Function to a varible

def hello():
    print("Hello")

hi = hello
hello()
hi()







#Higher Order Function = a function that either:
#                        1. accepts a function as an argument
#                           or
#                        2. returns a function

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)
#or

def divisor(x):
    def dividend(y):
        return y/x 
    return dividend

divide = divisor(2)
print(divide(10))








#lambda function = function written in 1 line using lambda keyword(Useful when u only use it once)
#lambda parameters:expression

double = lambda x:x * 2
print(double(5))

multiply = lambda x,y: x*y
print(multiply(5,6))

add = lambda x,y,z: x + y + z
print(add(5,6,7))

full_name = lambda first_name, last_name: first_name+" "+last_name
print(full_name("Bro","Code"))

age_check = lambda age:True if age >= 18 else False
print(age_check(18))







#sorted() method = used with lists
#sort() function = used with iterables

#students = ["Squidward","Sandy","Patrick","Spongebob","Mr.Krabs"]
students = ("Squidward","Sandy","Patrick","Spongebob","Mr.Krabs")

#students.sort(reverse = True)
sorted_students = sorted(students,reverse=True)

for i in sorted_students:
    print(i)


students = [("Squidward","F", 60),
            ("Sandy","A", 33)
            ("Patrick", "D", 36)
            ("Spongebob", "B", 20)
            ("Mr.krabs", "C", 78)]

grade = lambda grades:grades[1]
students.sort(key=grade)

for i in students:
    print(i)







#Map() = applies a function to each item in an iterable(list, tuple, etc.)
#map(function, iterable)

store = [("short",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]

to_euros = lambda data: (data[0],data[1]*0.82)
to_dollars = lambda data: (data[0],data[1]/0.82)

store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)








#filter() = create a collection of elements from an iterable for which a function returns true
#filter(function,iterable)

friends = [("Rachel",19),
           ("Monica",18),
           ("Phoebe",17),
           ("Joey",16),
           ("Chandler",21),
           ("Ross",20)]

age = lambda data:data[1] >= 18

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)






#Reduce() = apply a function to an terable and reduce it to a signle cumulative value.
#reduce(function, iterable)

import functools
letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x,y,:x+y,letters)

print(word)
#or
factorial = [5,4,3,2,1]
result = functools.reduce(lambda x,y,:x*y,factorial)
print(result)












#list comprehension = a way to create a new list with less syntax

#list = [expression for item in iterble]

squares = []
for i in range(1,11):
    squares.append(i*i)
print(squares)
#or
squares = [i*i for i in range(1,11)]
print(squares)

students = [100,90,80,70,60,50,40,30,0]
passed_students = list(filter(lambda x:x>= 60, students))
print(passed_students)
#or
#passed_students = [i for i in students if i >= 60]
passed_students = [i if i >= 60 else "FAILED" for i in students]
print(passed_students)









#dictionary comprehension = create dictionaries using an expression

#dictionary = {key: expression for (key,value) in iterable }

cities_in_F = {'New York': 32, 'Boston':75,'Los Angeles': 100,'Chicago':50}

cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()} 
print(cities_in_C)








#zip(*iterables) = aggreagate elements from two or more iterables (list,tuples,sets, etc)

usernames = ["Dude","Bro","Mister"]
passwords = ("p@ssword", "anc123","guest")
login_data = ["1/1/2021","1/2/2021","1/3/2021"]

users = dict(list(zip(usernames, passwords)))

for key,value in users.items():
    print(key+":"+value)











#Time Module
import time

print(time.ctime(0)) #covert time expressed in seconds to a readable string
                    #epoch = when your computer thinks time began(reference point)


print(time.time()) #return current seconds since epoch

print(time.ctime(time.time())) #get the current time
#or
time_object = time.localtime()
print(time_object)
local_time = time.strftime("%B %d %Y %H:%M:%S",time_object) # another way of getting the current time
print(local_time)

#(year,month,day,hours,minutes,second, day of the week, day of the year)
time_tuple = (2020,4,20,4,20,0,0,0,0)
time_string = time.asctime(time_tuple)
print(time_string)









#Thread = a flow of execution(allow one thread to run at a time) or all

#Multi thread = can have program run at different time

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee")

def study():
    time.sleep(5)
    print("You finish studying")

x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x = threading.Thread(target=eat_breakfast, args=())
x.start()
z.join() #join the main thread
##eat_breakfast()
#drink_coffee()
#study()

print(threading.active_count()) #List how many threads are running
print(threading.enumerate()) #List all the threads that are running
print(time.perf_counter()) #tell how long the thread perform











#daemon thread = a thread that run in the background, not important for program to run and will killed when main program is done

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ",count, "seconds")

x = threading.Thread(target=timer,daemon=True)
x.start()


answer = input("Do you wish to exit?: ")










#Multiprocessing = running tasks in parallel on different cpu cores(Heavy cpu usage)
#for faster process

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():

    print(cpu_count()) #multiprocessing must not be more than cpu count
    a = Process(target=counter, args=(62500000,))
    b = Process(target=counter, args=(62500000,))
    c = Process(target=counter, args=(62500000,))
    d = Process(target=counter, args=(62500000,))
    e = Process(target=counter, args=(62500000,))
    f = Process(target=counter, args=(62500000,))
    g = Process(target=counter, args=(62500000,))
    h = Process(target=counter, args=(62500000,))
    i = Process(target=counter, args=(62500000,))
    j = Process(target=counter, args=(62500000,))
    k = Process(target=counter, args=(62500000,))
    l = Process(target=counter, args=(62500000,))
    m = Process(target=counter, args=(62500000,))
    n = Process(target=counter, args=(62500000,))
    o = Process(target=counter, args=(62500000,))
    
    

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()
    i.start()
    j.start()
    k.start()
    l.start()
    m.start()
    n.start()
    o.start()
   


    b.join()
    a.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()
    i.join()
    j.join()
    k.join()
    l.join()
    m.join()
    n.join()
    o.join()
    


    start = time.perf_counter() #if counter seconds error
    print("finished in:",time.perf_counter() - start,"seconds")
 
if __name__ == '__main__':  #for window
    main() 













#GUI window :DDD

from tkinter import * 

#widgets = GUI elements: buttons, textboxes, labels, images
#windows = serves as a container to hold or contain these widgets

window = Tk() #instantiate an instance of a window
window.geometry("420x420") #size
window.title("Fun with the Bro")

icon = PhotoImage(file='C:\\Users\M\\Pictures\\Wallpaper\\676U5HW.gif') #insert icon
window.iconphoto(True,icon)
window.config(background="#6efff5")

window.mainloop() #place window on computer screen, listen for events











#Label = an area widget that holds text and/or an image within a window

from tkinter import *

window = Tk()

photo = PhotoImage(file='C:\\Users\M\\Pictures\\Wallpaper\\676U5HW.gif')

label = Label(window,
              text="Sussy Baka!? (°ー°〃)",
              font=('Arial',40,'bold'),
              fg='#00FF00', #words color
              bg='black', #background color
              relief=RAISED, #add Border
              bd=10, #bd size
              padx=20, #add space between the word and the border in x axis
              pady=20, #add space between the word and the border in y axis
              image=photo, #add photo from line 7
              compound='bottom') #add text with the image
label.pack() #set the label in the very top-middle
#And
label.place(x=100,y=100) #place anywhere u want to set

window.mainloop()










#Make Button

from tkinter import *

count = 0

def click():
    global count
    count +=1
    print("You are sus!",count)


window = Tk()

photo = PhotoImage(file='C:\\Users\M\\Pictures\\Wallpaper\\676U5HW.gif')

button = Button(window,
                text="click me!", #add text to the button
                command=click, #add it to a function
                font=("Comic Sans",30),
                fg='#00FF00',#words color
                bg='black', #background color
                activeforeground='#00FF00', #words color when clicked
                activebackground='blue', #background color when clicked
                state=ACTIVE, #Let the button can be click or not
                image=photo,
                compound='bottom')


button.pack()

window.mainloop()

















#Entry wdget = textbox that accepts a single line of user input

from tkinter import *

def submit():
    username = entry.get()
    print("Hello",username)
    entry.config(state=DISABLED)
def delete():
    entry.delete(0,END)

def backspace(): 
    entry.delete(len(entry.get())-1, END) 

window = Tk()

entry = Entry(window,font=('Arial',50),fg="#00FF00",bg='black',show="*")
entry.insert(0,"SpongeBob")

entry.pack(side=LEFT)

submit_button = Button(window,text="Submit",command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,text="Delete",command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,text="Backspace",command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()












#Checkbox

from tkinter import *

def display():
    if(x.get()==1):
        print("You agree!")
    else:
        print("You don't agree :(")

window = Tk()

x = IntVar()

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial',20),
                           fg='#00FF00',
                           bg='black',
                           activebackground='black',
                           activeforeground='#00FF00',
                           padx=25,
                           pady=10)

check_button.pack()
window.mainloop()















#Radio button = can select only one from a group

from tkinter import *

food= ["pizza","hamburger","hotdog"]

def order():
    if (x.get()==0):
        print("You ordered pizza!")
    elif (x.get()==1):
        print("You ordered hamburger!")
    elif (x.get()==2):
        print("You ordered Hotdog!")
    else:
        print("Huh?!")

window = Tk()

pizzaImage = PhotoImage(file='C:\\Users\\M\Pictures\\Wallpaper\\676U5HW.gif')
hamImage = PhotoImage(file='C:\\Users\\M\Pictures\\Wallpaper\\676U5HW.gif')
hotdogImage = PhotoImage(file='C:\\Users\\M\Pictures\\Wallpaper\\676U5HW.gif')

foodImages = [pizzaImage,hamImage,hotdogImage]
x = IntVar()

for index in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[index], #add text
                               variable=x,  #group the radioButton together
                               value=index, #assigns each radioButton a different Value
                               padx= 25,
                               font=("Impact",50),
                               image= foodImages[index],
                               compound='left',
                               indicatoron=0, #remove the circle indicators
                               command=order #add function
                               )
    radio_button.pack(anchor=W)


window.mainloop()










#Scale = something like the thermormeter

from tkinter import *

def Submit():
    print("The temperature is: "+str(scale.get())+"degrees C")

window = Tk()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,
              font=('Consolas',20),
              tickinterval=10, #Indicate the number on the scale
              #showvalue=0 #Hide the current value
              resolution= 5, #increment on the slider
              troughcolor='#69EAFF',
              fg = '#FF1C00',
              bg="#111111") 
scale.set((scale['from']-scale['to'])/2)

button = Button(window,
                text='Submit',
                command=Submit)

scale.pack()
button.pack()

window.mainloop()












#ListBox = A listing of selectable tet items within it's own container

from tkinter import *

def Submit():

    food= []

    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    print("You have ordered: ")
    for index in food:
        print(index)
    

def Add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def Delete():
    listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())
window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia",35),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,"Pizza")
listbox.insert(2,"Pasta")
listbox.insert(3,"Garlic Bread")
listbox.insert(4,"Soup")
listbox.insert(5,"Salad")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window,
                      text="Submit",
                      command=Submit
                      )

AddButton = Button(window,
                      text="Add",
                      command=Add
                      )

DeleteButton = Button(window,
                      text="Delete",
                      command=Delete
                      )

submitButton.pack()
AddButton.pack()
DeleteButton.pack()
window.mainloop()














#Message box(Look like virus)

from tkinter import *
from tkinter import messagebox

def click():
    messagebox.showinfo(title='WARNING!',message='YOU GOT VIRUS!')
    messagebox.showwarning(title='WARNING!',message='You have a VIRUS!') #same as showinfo but change the logo
    messagebox.showerror(title='ERROR!',message='Something went wrong.')

    if messagebox.askokcancel(title='Ask Ok cancel',message='Do you want to do the thing?'): #Show the ok/cancel UAC
        print('You did a thing')
    else:
        print('You canceled a thing!')

    if messagebox.askretrycancel(title='Ask retry cancel',message='Do you want to retry the thing?'): #Show the retry/cancel UAC
        print('You retried a thing')
    else:
        print('You canceled a thing!')

    if messagebox.askyesno(title='Ask Yes or no',message='Do you like cake?'): #Show the yes/no UAC
        print('I like cake too')
    else:
        print('Why do you not like cake?')

    answer = messagebox.askquestion(title='Ask Question',message='Do u like pie?') #Question with yes/no
    if(answer == 'yes'):
        print('I like pie too')
    else:
        print('Why do you not like pie?')

    answers = messagebox.askyesnocancel(title='Yes no Cancel',message='Do you like to code?')
    if(answers == True):
        print('You like to code!')
    elif(answers == False):
        print('Why do you watch the coding video?')
    else:
        print('YOu have dodged the question')
    


window = Tk()

button = Button(window,command=click,text='Click Me!')
button.pack()

window.mainloop()










#ColorChooser
from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor()
    colorHex = color[1]
    window.config(bg=colorHex)

window = Tk()

window.geometry("420x420")

button = Button(text='Click me!',command=click)
button.pack()

window.mainloop()











#Text widget
from tkinter import *
def submit():
    input = text.get("1.0",END)
    print(input)

window = Tk()

text = Text(window,bg="light yellow",font=("Ink Free",25),height=8,width=20,padx=20,pady=20,fg="Purple")
text.pack()

button = Button(window,text='Submit',command=submit)
button.pack()

window.mainloop()











#open a file
from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(title='Open File Okay?',filetypes=(("text file","*.txt"),("all files","*.*")))
    file = open(filepath, 'r')
    print(file.read())
    file.close()

window = Tk()

button = Button(text='Open',command=openFile)
button.pack()
window.mainloop()











#Save a file

from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.txt',filetypes=[
                                                              ("Text file",".txt"),
                                                              ("HTML file",".html"),
                                                              ("All file","*.*")          
                                                            ])
    filetext = str(text.get(1.0,END))
    file.write(filetext)
    file.close()

window = Tk()

button = Button(text='Save', command=saveFile)
button.pack()

text = Text(window)
text.pack()
window.mainloop()















#Menu Bar
from tkinter import *

def openFile():
    print("File has been opened!")

def saveFile():
    print("File has been saved!")

def cut():
    print("You cut some text!")

def copy():
    print("You copy some text!")

def paste():
    print("You paste some text!")

window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit)
fileMenu.add_separator()

editMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)

window.mainloop()












#Frame

from tkinter import *

window = Tk()

frame =Frame(window,bg='pink',bd=5,relief=SUNKEN)
frame.pack(side=BOTTOM)

Button(frame,text="W",font=("Consolas",25),width=3).pack(side=TOP)
Button(frame,text="A",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame,text="S",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame,text="D",font=("Consolas",25),width=3).pack(side=LEFT)


window.mainloop()








#New Window

def create_window():
    new_window = Toplevel()


from tkinter import *

window = Tk()

Button(window,text="Create new window",command=create_window).pack()

window.mainloop()











#Window tabs

from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window) #Widget that manages a collection of windows/displays

tab1 = Frame(notebook) #new frame for tab 1
tab2 = Frame(notebook)

notebook.add(tab1,text="Tab 1")
notebook.add(tab2,text="Tab 2")
notebook.pack(expand=True,fill="both") #expand = will expand to fill the space

Label(tab1,text="Hello, this is taba#1",width=50,height=25).pack()
Label(tab2,text="Goodbye, this is taba#2",width=50,height=25).pack()

window.mainloop()













#Grid = Like 2D array

from tkinter import *

window = Tk()

titlelabel = Label(window,text="Enter your info",font=("Arial",25)).grid(row=0,column=0,columnspan=2)

firstNameLabel = Label(window,text="Fist name: ",width=20,bg="red").grid(row=1,column=0)
firstNameEntry = Entry(window).grid(row=1,column=1)

lastNameLabel = Label(window,text="Last name: ",bg="green").grid(row=2,column=0)
lastNameEntry = Entry(window).grid(row=2,column=1)

emailLabel = Label(window,text="Email: ",bg="blue").grid(row=3,column=0)
emailEntry = Entry(window).grid(row=3,column=1)

submitButton = Button(window,text="Submit").grid(row=4,column=0,columnspan=2)

window.mainloop()


















#Progress Bar

from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 50
    download = 0
    speed = 2
    while(download<GB):
        time.sleep(0.05)
        bar['value']+=(speed/GB)*100
        download+=speed
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB)+" GB completed")
        window.update_idletasks()

window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

percentLabel = Label(window,textvariable=percent).pack()
taskLabel = Label(window,textvariable=text).pack()

button = Button(window,text="Download",command=start).pack()

window.mainloop()













#canvas = widget that is used to draw graphs, plots , images in a window

from tkinter import *

window = Tk()

canvas = Canvas(window,height=500,width=500)
canvas.create_line(0,0,500,500,  #Starting point of (x,y) to ending point (x,y)
                   fill="Blue",width=5)  
canvas.create_line(0,500,500,0,fill="red",width=5)
canvas.create_rectangle(50,50,250,250,fill="Purple")

points = [250,0,500,500,0,500]
canvas.create_polygon(points,fill="Yellow",outline="Black",width=5)

canvas.pack()

window.mainloop()









#Key Event
from tkinter import *

def doSomething(event):
    print("You pressed: "+ event.keysym)
    label.config(text=event.keysym)
window = Tk()

window.bind("<Key>",doSomething) #Return = The Enter Key

label = Label(window,font=("Helvetica",100))
label.pack()

window.mainloop()







#Mouse Event
from tkinter import *

def doSomething(event):
    print("You did a thing!" + str(event.x)+","+str(event.y)) #Show coordinate

window = Tk()

window.bind("<Button-1>",doSomething)  #Leftclick
window.bind("<Button-2>",doSomething)  #MiddleClick
window.bind("<Button-3>",doSomething)  #RightClick
window.bind("<ButtonRelease>",doSomething) #Let go after click
window.bind("<Enter>",doSomething) #Where you enter the window
window.bind("<Leave>",doSomething)  #Where you leave the window 
window.bind("<Motion>",doSomething) #Where the mouse move

window.mainloop()












#Drag and Drop
from tkinter import *

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)


window = Tk()

label = Label(window,bg="red",width=10,height=5)
label.place(x=0,y=0)

label2 = Label(window,bg="blue",width=10,height=5)
label2.place(x=100,y=100)

label.bind("<Button-1>",drag_start)
label.bind("<B1-Motion>",drag_motion)

label2.bind("<Button-1>",drag_start)
label2.bind("<B1-Motion>",drag_motion)

window.mainloop()











#Move images with keys/ window
from tkinter import *

def move_up(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()-10)

def move_down(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()+10)

def move_left(event):
    label.place(x=label.winfo_x()-10,y=label.winfo_y())

def move_right(event):
    label.place(x=label.winfo_x()+10,y=label.winfo_y())

window = Tk()
window.geometry("500x500")

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)

window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)

myimage = PhotoImage(file="C:\\Users\\M\\Desktop\\2-middle.png")
label = Label(window,image=myimage)
label.place(x=0,y=0)

window.mainloop()










#Move images with keys in Canvas
from tkinter import *

def move_up(event):
   canvas.move(myimage,0,-10)
def move_down(event):
   canvas.move(myimage,0,10)
def move_left(event):
   canvas.move(myimage,-10,0)
def move_right(event):
   canvas.move(myimage,10,0)

window = Tk()

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)

canvas = Canvas(window,width=500,height=500)
canvas.pack()

photoimage = PhotoImage(file='racecar.png')
myimage = canvas.create_image(0,0,image=photoimage,anchor=NW)

window.mainloop()












#Animating

from tkinter import *
import time

WIDTH = 500
HEIGHT = 500

xVelocity = 3 #speed
yVelocity = 3

window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

photo = PhotoImage(file="C:\\Users\\M\\Desktop\\index.png")
my_image = canvas.create_image(0,0,image=photo,anchor=NW)

image_width = photo.width()
image_height = photo.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0] < 0):
        xVelocity = -xVelocity
    if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1] < 0):
        yVelocity = -yVelocity
    canvas.move(my_image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()










#Multiple Animation
from tkinter import *

import time

class Ball:

    def __init__(self,canvas,x,y,diameter,xVelocity,yVelocity,color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diameter,diameter,fill=color)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self):
        coordinates = self.canvas.coords(self.image)
        if(coordinates[2]>=(self.canvas.winfo_width())or coordinates[0] < 0):
            self.xVelocity = -self.xVelocity
        if(coordinates[3]>=(self.canvas.winfo_height())or coordinates[1] < 0):
            self.yVelocity = -self.yVelocity
        self.canvas.move(self.image,self.xVelocity,self.yVelocity)


window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

#objects
volley_ball = Ball(canvas,0,0,100,1,1,"white")
tennis_ball = Ball(canvas,0,0,50,4,3,"yellow")
basket_ball = Ball(canvas,0,0,125,8,7,"orange")

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()









#run .py file with cmd
#*************************
#save file as .py (Python file)
#go to command prompt
#navigate to directory w/ your file: cd C:\Users\...
#invoke Python interpreter + script: python (name .py)

print("Hello World!")

name = input("What's your name?: ")

print("Hello "+name)









#Python pip
#************************
#pip = package manager for packages ad modules from Python Package Index

#help:                         pip
#check:                        pip --version
#update:                       pip install --upgrade pip
#installed packges:            pip list
#check outdated packages:      pip list --outdated
#install a package:            pip install "package name"








#convert .py to .exe
#cd to directory that contains your .py file
#pyinstaller ...
#  -F                    (all in 1 file)
#  -w                    (removes terminal window)
#  -i icon.ico           (adds custom icon to .exe)
#  (name.py)             (name ofyour main python file)

# .exe is located in the dist folder