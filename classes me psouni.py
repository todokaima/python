class Dog:
    def __init__(self, name, weight, breed):
        self.name = name
        self.weight = weight
        self.breed = breed
        self.mood = 5

    def eat(self):
        self.mood += 1

    def bark(self):
        if self.mood > 5: print("WOOF WOOF WOOF")
        else: print("WOOF")

    def walk(self):
        self.mood += 1

Piko = Dog("Piko", 10, "Terrier")
Lassie = Dog("Lassie", 30, "Colley")

print(Piko.name)

Piko.bark()
Piko.bark()
Piko.eat()
Piko.bark()

class Philosopher:
    def __init__(self, name, age, books, dis_books, school):
        self.name = name
        self.age = age
        self.books = books
        self.dis_books = []
        self.school = school
plato = Philosopher("Plato", "ANCIENT GREECE", ["republic","phaidon"],"platonismos",2)
spinoza = Philosopher("barouf spinoza", "MODERN HOLLAND", ["!","2"],"SPINOZA","3")

print(spinoza.school)
print(plato.school)

class Cow:
    def __init__(self, hunger, weight):
        self.__hunger = hunger
        self.weight = weight

    def express(self):
        if self.__hunger >20: print("mooooooooo")
        else: print("mooo")

    def boredom(self):
        self.__hunger += 4

molly = Cow(20, 2000)
molly.express()
molly.boredom()
molly.express()
print(molly.weight)



from random import randrange, seed
from datetime import datetime

class Student:
    def __init__(self, full_name):
        self.full_name = full_name
        self.grade = -1

def GradeStudent(student):
    student.grade = randrange(1,11)

def average(students):
    s=0
    for student in students:
        s += student.grade
    print("Average: "+ str(s/len(students)))

names = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h']

students = [Student(names[i]) for i in range(0,len(names))]

for student in students:
    GradeStudent(student)

average(students)
########################################################################################################################
class Flat:
    def __init__(self):
        self.people = 0

class Storey:
    def __init__(self, number_flats):
        self.people = 0
        self.flats = [Flat() for i in range(number_flats)]

class Building:
    def __init__(self, num_of_storeys, num_of_flats):
        self.storeys = [Storey(num_of_flats) for i in range(num_of_storeys)]


    def add_people(self,flat, storey,  people):
        self.storeys[storey].flats[flat].people += people

    def print_people(self):
        for i  in range(len(self.storeys)):
            for j in range(len(self.storeys[i].flats)):
                print(f"Storey {i}, Flat {j}: {self.storeys[i].flats[j].people} people")


b = Building(3,4)
b.add_people(0,1,2)
b.print_people()

#####################################################################################
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, D):
        self.x = D

    def set_y(self, D):
        self.y = D

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def Print(self):
        print(f"({self.get_x()},{self.get_y()})")

from math import sqrt

class Line:
    def __init__(self, point_A = None, point_B = None):
        if point_A is None:
            self.point_A = Point(0,0)
        else: self.point_A = Point_A

        if point_B is None:
            self.point_B = Point(0,0)
        else: self.point_B = Point_B

    def setter_A(self, point_A):
        self.point_A = point_A

    def setter_B(self, point_B):
        self.point_B = point_B

    def length(self):
        return sqrt((self.point_A.x - self.point_B.x)**2+(self.point_A.y - self.point_B.y)**2)

    def print(self):
        self.point_A.Print()
        self.point_B.Print()


l = Line()
l.print()
print(l)

l.setter_A(Point(1,1))
l.setter_B(Point(4,5))
l.print()
print(l)
print(l.length())

#############
class Time:
    def __init__(self, hour, minute, second):
        self.hour = self.__validate(hour, 0, 23)
        self.minute = self.__validate(minute, 0, 59)
        self.second = self.__validate(second,0,59)

    def set_hour(self, hour):
        self.hour = hour.__validate(hour,0,23)

    def set_minute(self,minute):
        self.minute = __validate(minute, 0, 59)

    def set_second(self, second):
        self.second = __validate(second, 0 ,59)

    def __validate(self, val, low, upp):
        if val >= low and val <= upp:
            return val
        else:
            return 0
    def total_seconds(self):
        return self.hour*3600 + self.minute *60+self.second

    def print(self):
        print(f"{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}:{str(self.second).zfill(2)}")


    def next_second(self):
        second = self.second + 1
        carry = second // 60
        second = second % 60

        minute = self.minute + carry
        carry = minute // 60
        minute = minute % 60

        hour = (self.hour + carry) % 24

        return Time(hour, minute, second)




t = Time(1,45,9)
t.print()

t1 = Time(11, 12, 13)
t1.print()
t1.next_second().print()

######################################################
class Empty:
    def __init__(self):
        print(self)

e = Empty()
print(e)

class C:
    counter = 0

    def __int__(self):
        C.counter += 1
    def __del__(self):
        C.counter -= 1
A = C()
B = C()
print(C.counter, A.counter, B.counter)

l = [1,2,3]
del l[0]
print(l)

d = {1:1,2:"2"}
print(d)
del d[1]
print(d)

del A

class Myclass:
    def __init__(self, x):
        self.x = x

o1 = Myclass(2)
o2 = Myclass(3)
o3 = o2

print(o3 is o2)

print([1,2] is [1,2])

o1 = Myclass(1)
o2 = Myclass(1)
print(o1 is o2)
print(o1 == o2)

