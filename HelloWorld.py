#Variables, Functions, Typecasting ===========================================================================
x = 1
if x == 1:
    print("Hello World. This is a python cheat-sheet")
else:
    print(x)

print("An example of a List: ")
x = [1,2,3] #changed data type to "Lists", jesus
print(x)

print("Example of a for loop: ")
for x in range(5):
    print(x)

#functions
def myFunction(a, b = 5, c = 10): # we have default arguments in python  
    return a+b+c                  # function body is demarkated using blocks
res = myFunction(300,255)
res = myFunction(300, c=100)
res = myFunction(300)

name = "sTrInG"
age = 50
eh = True
print(name.capitalize() + " is ", age, "years old.")
#print(name + " is " + age + "years old.") throws error
lie = "Giraffes are weird at age "
# casting is explicit, called like a function
print(lie.replace("Giraffe", "Elephant") + str(age))

# equivalent to namespaces, we can determine what means what by
from math import sqrt   #or from math import *
print(sqrt(36))

print("Prompting works like: \n")
name = input("Hi! What's your name? ")
print("Hi, "+ str(name).capitalize())
age = input("What's your age? ")
#typecasts are functions
print("In 5 years you'll be " + str(float(age) + 5))

#Array types ==================================================================================================
#Lists
anything = [2, "Wow", True, 5.56]
print(anything) #prints everything
for i in range(len(anything)):
    print(anything[i])
anything.append(["Wut", "Butt", "Tut"]) #we made a list a member of a list
print(anything[2:])      #MATLAB flashback
anything.append(5)
print(anything[1:3])
anything.clear()
anything.extend(["Apple", "apple", "beer", "cat", "lulz", "bear", "Bear", "Bear"])
anything.sort()
print(anything)

#Tuple: Immutable
example = (5, 7, 2)
#example[1] = 10 will throw an error
# tuples are used to swap two variables
a = 5
b = 7
b, a = a, b
print("a = ", a, ", b = ", b)
# or return multiple objects from a function
def tupleFunc():
    return 3 , 4
x, y = tupleFunc()
print("x = ", x, ", y = ", y)   

#dictionary: key and value. keys must be immutable
dict = {'Name': 'Jonaq', 'Age': 70, 'Class': 'Lazy'}
dict['Age'] = 90 # update existing entry
dict['School'] = "Memes" # Add new entry

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

#grid
matrix = [[1,2,3],[4,5,6],[7,0,9]]
print(matrix[0][1])
for m in matrix:
    for n in m:
        if n == 0:
            print(n)
        #print matrix[m][n] doesn't work, because matrix[list][element]

#try catch blocks ============================================================================================
try:
    var = int(input("Enter an int: (also try char)"))
    var = var/1
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Ayy don't divide by zero bruh!")

try:
    16/1
except ZeroDivisionError as m:
    print(m)

#File I/O =====================================================================================================
def primeCheck(n):
    count = 0
    for i in range(n-1):
        if n % (i+1) == 0:
            count = count + 1
            if count >= 2:
                break
    if count == 1:
        return True
    else:
        return False

limit = 100
fileVar = open("./log.txt", "w")  #use "a" if you don't want to overwrite
if fileVar.writable():
    for i in range(limit):
        if primeCheck(i):
            fileVar.writelines(str(i) + "\n")
fileVar.close()

# Classes and Objects ==========================================================================================
# everything is public by default
class person:
    def __init__(self, n, w, h):    #constructor yay
        self.name = n
        self.weight = w
        self.height = h
    def isOverweight(self):
        if self.weight >= 90:
            return True
        else:
            return False
# if the class was in a different file, import the class
# from FileName import person
genericPerson = person("Jonaq", 92, 170)
print(genericPerson.name + " is fat. " + str(genericPerson.isOverweight()))

class student(person):  #inheritance yo
    def __init__(self, n, w, h, scr):
        self.score = scr
    def isOverweight(self):     #override
        if self.weight > 100:
            return True
        else:
            return False
jj = student("Jonaq", 95, 169, 90)
# print(jj.name) throws error saying that .name is not even a member

#date and time ===============================================================================================
import time
localtime = time.asctime(time.localtime(time.time()))   #localtime gives a struct
print("Local current time :", localtime)

#multithreading is advanced. Will touch later in a separate file.

# system calls using eval()
holder = input("Enter a mathematical expression to evaluate (e.g. sqrt(49) or 3+56 etc.) : ")
print(eval(holder))

#