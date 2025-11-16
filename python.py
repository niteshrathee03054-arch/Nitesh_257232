print("hello")
#this is multiline comment 

x = 12
a=6
aa="naman"
bb="nitin"
q=2
u=4

print(float(a))

print(type(x))

print("hello",end=" ")

print("ye")
print("to")

print("my age is",x)


print(aa[:-4:-1])
print(aa.upper())
print(aa.replace("m","b"))

print(aa+" "+bb)

print(f"my age is {x} years")

print(f" this sis floating value {x:.2f}")

print(aa.capitalize())

c = aa.center(60)
print(c)

b = aa.count("e")
print(b)

r=aa.islower()
print(r)

print(u**q)
print(u%q)
print(u+q)
print(u/q)
print(u//q)
print(u*q)
print(u-q)

a+=5
print(a)

print(12==13)
print(12>13)
print(12<13)
print(12!=13)
print(13>=13)

#logical operator : and , or , not
#and : it give true when both condition are true
print(12>3 and 12>11)

#or : it give true even one codition is true 
print(1>3 or 5>3)

#not : it give opposite result 
print(not(12>3 and 12>11))

#task 1
a = int(input("enter a no : "))
if a >= 18:
 print("you are eligible to vote")
else:
 print("you are not eligible")

 
#task 2        
s = int(input(" enter your grade :"))
if s <= 35:
 print("your grade is c ")        
elif s >35 and s<=65:
 print("your grade is b")
elif s>65 and s<95:
 print("your grade is a")
elif s>=95:
 print(" your grade is a++")
    
#List
w=["ayush","virat","nitesh"]
print(w[0])

#Tuples
e=(12,"hello")
print(type(e))

r=list(e)
print(r)

#Sets : are used to store multiple value in single variable but sets are unordered and unindexed

t={1,2,5,"rachit", "virat"}
print(t)

#Dict
y={"name":"ayush","college":"saitm"}
print(y["college"])

#Loops

i=0
while i<19:
    i=i+2
    print(i)

    
for i in range(0,9):
    print(i)

count=5

while count>0:
    if count %2==0:
        print("even")
    else:
        print("odd")
    count-=1

    
a="hello"
v=6
while v>0:
    print(a)
    v=v-1

print("your grade is c ")        
elif s >35 and s<=65:
 print("your grade is b")
elif s>65 and s<95:
 print("your grade is a")
elif s>=95:
 print(" your grade is a++")


#task 3
a=[]
for i in range(5):
 s = int(input(" enter your marks :"))
 a.append(s)
print(a)
grade = 0

for i in a: 
 if i <= 35:
     grade="c"

 elif i >35 and i<=65:
     grade="b"
  
 elif i>65 and i<95:
     grade="a"
  
 elif i>=95:
     grade="a"
 print(f"your marks is {i}and your grade is {grade}")  


def abc():
    print("hello")

abc()

def square(num):
    return num*num
result=square(5)
print("square is ",result)
my_dict = {}
num_entries = int(input("Enter the number of key-value pairs you want to add: "))


for i in range(num_entries):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value for {key}: ")
    my_dict[key] = value
print(my_dict)

s=int(input("enter your book number:"))

if s in my_dict:
    print("your book is:")


import aa
print(aa.greet("ayush"))

#random module

import random

print("Random number between 1-10 : ", random.randint(1,10))
colors = ["red", "blue", "green"]
print("Random color: ",random.choice(colors))

import datetime

today = datetime.date.today()
print("Today's date:", today)

#date and time module

import datetime

today = datetime.date.today()
print("Today's date:", today)

now = datetime.datetime.now()
print("Current time:", now)

#sys module

import sys

print("Python version:", sys.version)
print("Platform:", sys.platform)"""

#math module

"""import math

print("Square root of 49:", math.sqrt(49))
print("value of pi:", math.pi)
print("Ceil of 6.9:", math.ceil(6.9))
print("Floor of 4.8", math.floor(4.8))"""""
"""import random
def abc():
 x= random.randint(-10,10)
 print(" your random no is:",x)
 if x >0:
     print("no is +ve")
 else:
     print("no is negative")    
 if x % 5==0:
     print("no is divisible by 5")   
 else:
     print("no is not divisible by 5")    
 if x%2==0:
     print("no is even")
 else:
     print("no is odd")    
abc()     

class abc:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = abc("Yash", 18)
print(p1.name,p1.age)
#print(p1.age)

# class Person:
#     x=5
# a = Person()
# print(a.x)  
class Person:
    def init(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"My name is {self.name} and I am {self.age} years old")
result=Person("Yash",18) 
result.greet()



class Calculator:"""
"""def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid choice")

# Run the calculator
calculator()"""

"""#class
class car:
    def __init__(self,brand,color):
        self.brand=brand #attribute
        self.color=color #attribute

    def drive(self): #mentioned
        print(f"{self.color}{self.brand}is driving 🚗")
#object
car1=car("bmw","black")
car2=car("tesla","white")

car1.drive()
car2.drive()"""

"""class bankaccount:
    def __init__(self,balance):
        self.__balance+=amount
    def deposite(self,amount):
        self.__balance+=amount
    def get_balance(self):
        return self.__balance
account = bankaccount(1000)
account.deposite(500)
print(account.get_balance())#1500
        
class car:
    def __init__(self,brand,color):
        self.brand=brand #attribute
        self.__color=color #attribute

    def drive(self): #mentioned
        print(f"{self.__color}{self.brand}is driving 🚗")
#object
car1=car("bmw","black")

print(car1.brand)
print(car1.__color)
car1.drive()

class animal:
    def speak(self):
        print("animal speaks")
class Dog(animal):
    def speak(self):
        print("Dog breaks")
dog=Dog()  
dog.speak()


class Person:
    def __init__(self, name, age):
        self.name=name
        self.__age=age
    p1=Person("Email",25)
    print(p1.name)
    print(p1.Person__age)   

class Cat:
    def sound(self):
        return"Meow"
class Dog:
    def sound(self):
        return"Woof
class Animal:
    def speak(self):
        print("Animals make differentsound")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
class Cat(Animal):
    def speak(self):
        print("Cat meows")
for pet in (Dog(),Cat()):
    pet.speak()                    
     
       
import pandas as pd

data=[10,20,30]
s=pd.Series(data)
print(s)
       
data= {
    'name':['ritik','aman','priya'],
    'age':[21,23,34],
    'marks':[23,45,78]
}    

df = pd.DataFrame(data)
print(df)

Data=[34,67,89]
y=pd.Series(Data)
print(y)

a=[1,2,3,]
myvar=pd.Series(a,index=['x','y','z'])
print(myvar["y"])
print(myvar)


calories={"day1":420,"day2":380,"day3":390}
myvar=pd.Series(calories)
print(myvar)

marks={"math":89,"science":45,"sst":67}
e=pd.Series(marks)
print(e)
print(e[1])

#Made by Ayush

======================== x x x x x x x ========================

DBMS - DATABASE MANAGEMENT SYSTEM



RDBMS - REGLUAR DBMS (GIVES DATA IN TABULAR FORM)



DEFINATION OF DBMS - 

- Stores data in a structured way

- Allows users to insert, update, delete, and retrieve data

- Ensures data security, integrity, and consistency 



#QUEARY TO ADD DATABASE AND U SAVED DATABASE --

CREATE DATABASE SCHOOL;
USE SCHOOL;



CREATE IS USED TO CREATE A  DATABASE.
SHOW IS USED TO SEE ALL AVAILABLE DATABASE IN SQL.
"INSERT INTO" IS USED TO GIVE VALUE IN SQL.
";" MUST BE USED AFTER EVERY QUERY UNLESS QUERY WILL NOT RUN.
AS WE ADD "PRIMARY KEY" AFTER THE COLUMN BAR THEN THE VALUE IN THAT COLUMN WILL NOT REPEAT.
WE ALSO HAVE TO ADD QUERY "SELECT * FROM PERSONAL_INFO;" AFTER EVERY CHANGES TO SEE THE CHANGES.



#FOR MAKING TABLE

CREATE TABLE STUDENTS (
  Id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  CLASS TEXT NOT NULL
);


# TO INSERT VALUES IN TABLE

NSERT INTO STUDENTS VALUES (0001, 'RISHI', '3');
INSERT INTO STUDENTS VALUES (0002, 'DEV', '4');
INSERT INTO STUDENTS VALUES (0003, 'MOHIT', '5');
INSERT INTO STUDENTS VALUES (0004, 'AMAN', '6');
INSERT INTO STUDENTS VALUES (0005, 'SUMIT', '7');

+----+-------+-------+
| Id | name  | CLASS |
+----+-------+-------+
|  1 | RISHI | 3     |
|  2 | DEV   | 4     |
|  3 | MOHIT | 5     |
|  4 | AMAN  | 6     |
|  5 | SUMIT | 7     |
+----+-------+-------+




#TO CHECK OUR TABLE COULUMNS

SELECT * FROM STUDENTS


# TO CHECK THE PARTICULAR COLUMN

SELECT NAME , ID FROM STUDENTS ;

+-------+----+
| NAME  | ID |
+-------+----+
| RISHI |  1 |
| DEV   |  2 |
| MOHIT |  3 |
| AMAN  |  4 |
| SUMIT |  5 |
+-------+----+

# WHERE "NAME" IS COLUMN NAME OF TABLE



# "ADDRESS" IS A COLUMN FROM WHERE I HAVE TO CHECK DATA
# "NAME" IS A COLUMN OF WHICH COLUMN'S DATA IS SHOWN.



# TO CHANGE  SOMETHING IN BETWEEN 2 COLUMNS
  
UPDATE STUDENTS SET NAME = "AYUSH" WHERE ID  = "1";
SELECT * FROM STUDENTS;

+----+-------+-------+
| Id | NAME1 | CLASS |
+----+-------+-------+
|  1 | AYUSH | 3     |
|  2 | DEV   | 4     |
|  4 | AMAN  | 6     |
|  5 | SUMIT | 7     |
+----+-------+-------+

# WHERE "ADDRESS" IS A COLUMN IN WHICH I HAVE TO DO SOME CHANGES.
# AND "NAME" IS A COLUMN OF WHICH THE ADDRESS IS CHANGED.

======================== x x x x x x x ========================

#TO DELETE A SPECIFIC COLUMN

DELETE FROM STUDENTS WHERE ID = '3';
SELECT * FROM STUDENTS;

+----+--------+-------+
| Id | NAME1  | CLASS |
+----+--------+-------+
|  1 | RISHIT | 3     |
|  2 | DEV    | 4     |
|  4 | AMAN   | 6     |
|  5 | SUMIT  | 7     |




DDL = (DATA DEFINATION LANGUAGE) - TO CHANGE THE STRUCTURE OF DATA.

1) - CREATE - TO CREATE A DATABASE.
2) - ALTER - TO CHANGE IN THE EXISTING TABLE.
3) - DROP - REMOVE THE DATABASE.
4) - TRUNCATE - REMOVE THE TABLE.



DML = (DATA MANUPULATION LANGUAGE) - TO CHANGE THE DATA IN TABLE.

1) SELECT - FOR SHOWING OUTPUT
2) UPDATE - FOR UPDATION IN TABLE.
3) INSERT - FOR ADDING VALUES IN COLUMN.
4) DELETE - FOR REMOVING SOMETHING IN TABLE.