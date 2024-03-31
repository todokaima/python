class Cow:
    def __init__(self, weight, hunger):
        self.weight = weight
        self.__hunger = hunger
    def express(self):
        if self.__hunger > 8:
            print("moooooooooooo")
        else:
            print("moooo")


molly = Cow(500,10)
molly.express()
print(type(molly))
#print(molly.__hunger)

class Dog:
    def __init__(self, name, weight, breed):
        self.name = name
        self.weight = weight
        self.breed = breed
        self.mood = 5

    def eat(self):
        self.mood +=1

    def bark(self):
        if self.mood > 5:
            print("wooooof")
        else:
            print("woof")

    def walk(self):
        self.mood +=1



piko = Dog("piko",10, "terrier")
lassie = Dog("lassie", 30, "colley")
for i in range(2):
    piko.bark()
    piko.walk()

piko.bark()
piko.eat()
piko.bark()

class Philosopher:
    def __init__(self, full_name, era, books, school):
        self.full_name = full_name
        self.era = era
        self.books = books
        self.school = school
        self.disputed_books = []

plato = Philosopher("Plato","Ancient Greece",["The Republic","Plato{"],"platonium")
spinoza = Philosopher("SSPIINO|","MODErn HO",["ETHIKA","political"],"modern{mlk")
print(spinoza.disputed_books)



class Point:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    def set_x(self,x):
        self.__x = x
    def set_y(self,y):
        self.__y = y
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y

def f(x):
    return x**2
points = [Point(0,0) for i in range(1,11)]

'''points = []
for x in range(1,10+1):
    p = Point(x,f(x))
    points.append(p)'''

i=1
for point in points:
    point.set_x(i)
    point.set_y(i+1)
    print(f"({point.get_x()},{point.get_y()})")

import random
from datetime import datetime


'''class Student(self, full_name):
    def __init__(self):
        self.full_name = full_name
        self.grade = -1

    def grade_student(students):
        s = 0
        for student in students:
            s += student.grade

        print("Average = " + str(s/len(students)))


students = [Student(name[i]) for i in range(len(names))]
for student in students:
    grade_student(student)
    
average(students)'''

