# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 18:41:21 2020

@author: HASSAN ENTERPRISES
"""

class employee:
    pass
#huzaifa is an object of employeee
huzaifa=employee()
#similarly bilal is an object of employee
bilal=employee()
#here we assigning a instance variable
huzaifa.name="huzi"
bilal.name="billliii"
print(huzaifa.name,",",bilal.name)
#==============================================================================
class employee:
    noofleaves=8
    def printdetails(self):
        return f"th name of{self.name},roll number is{self.roll},and the section is{self.section}"
        
    
     
huzaifa=employee()
bilal=employee()
huzaifa.name="huzaifa"
huzaifa.roll="165"
huzaifa.section="b"
employee.noofleaves=9
print(huzaifa.printdetails())
print(huzaifa.noofleaves)
#==============================================================================
class employee:
    def __init__(self,aname,asection,arollnumber):
        self.name=aname
        self.section=asection
        self.roll=arollnumber
    
    
    def printdetails(self):
        return f"th name of{self.name},roll number is{self.section},and the section is{self.roll}"
        
    
     
huzaifa=employee("huzaifa","b","139")
#bilal=employee()
#huzaifa.name="huzaifa"
#huzaifa.roll="165"
#huzaifa.section="b"
print(huzaifa.section)
print(huzaifa.printdetails())
#===============================================================================
class employee:
    #assigning variable in class
         noleaves=8
         pass
    # this vaiable is the class and huzaifa and bilal is sharing this variable 
    
    
#huzaifa=employee()
bilal=employee()
#huzaifa.name="huzi"
#huzaifa.rollnumber=139
#huzaifa.student ="UIT"
bilal.student ="little.folk"
bilal.rollnumber=23
bilal.name="billliii"
print(bilal.name,",",bilal.student,",",bilal.rollnumber,",",huzaifa.name,",",huzaifa.student,",",huzaifa.rollnumber)
#==============================================================================
class dogs():
    print("meri to waath lagh gyii hai programming may")
    def __init__(self,name,age):
         self.name=name
         self.age=age
#dogs use as a instance variable         
dogs=dogs("bultharooo",25)
print(dogs.name,dogs.age)    
#==============================================================================
class employee():
    no_of_leaves=9
    def __init__(self,name,ages):
        self.name=name
        self.age=ages
    def printdata(self):
        return (("my name is {} and i am studing in class{}").format(self.name,self.section))
huzaifa=employee(bilal,13)    
huzaifa.name="huzaifa"
huzaifa.section="14"
employee.no_of_leaves=10
print(huzaifa.no_of_leaves)
print(huzaifa.printdata())
print(huzaifa.name)
print(huzaifa.name)
#================================================================================
class employee():
    no_of_leaves=9
    def __init__(self,name,ages):
        self.name=name
        self.age=ages
    def printdata(self):
        return (("my name is {} and i am studing in class{}").format(self.name,self.section))
    classmethod
    def from_str(cls,strings):
        huzii=strings.split(",")
        return cls(huzii[0],huzii[1],huzii[2])
   
huzaifa=employee(bilal,13)    
huzaifa.name="huzaifa"
huzaifa.section="14"
employee.no_of_leaves=10
print(huzaifa.no_of_leaves)
print(huzaifa.printdata())
print(huzaifa.name)
print(huzaifa.name)
bilal=employee.from_str("karan-480-students")
print(bilal.name)
#==================================================================================
class employee():
    no_of_leaves=9
    def __init__(self,aname,asection,arollnumber):
        self.name=aname
        self.section=asection
        self.roll=arollnumber
    def printdata(self):
        return f"th name of{self.name},roll number is{self.section},and the section is{self.roll}"
    

        
harry=employee("huzaifa","B","139")
print(harry.printdata())
bilal=employee("huzii","a","132")
print(bilal.printdata())

#====================================================================================
class students:
    counter=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        students.counter=students.counter+1
    def msg(self):
        print(self.name,"",self.age)
        
# class method is use to change classssss:::: cls is nothing but class it is         
    @classmethod
    def object_counter(cls):
        return cls.counter
        
#it shoew us 2 object are pass s1 and s2    
s1=students("sara","20")
s2=students("bilal","14")    
s3=students("huzaifa","20")    
print(students.object_counter())
#we can also call it by object 
print(s2.object_counter())
#=====================================================================================
class students:
 
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def msg(self):
        print(self.name,"",self.age)
        
   
s1=students("sara","20")
marks="360"
name="sara"
marks1=str((int(marks)/600)*100)
s2=students(marks1,name)
print(s2.msg())
#==============================================================================================
# class methods decroaters 
class students:
 
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def msg(self):
        print(self.name,"",self.age)
    @classmethod
    def get_percentage(cls,name,marks):
        return cls(name,str((int(marks)/600)*100))
   
s1=students("sara","20")
marks="360"
name="sara"
#marks1=str((int(marks)/600)*100)
s2=students.get_percentage(name,marks)
print(s2.msg())
#===============================================================================================
# statis methods it doesnot required any parameters 
class students:
 
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def msg(self):
        print(self.name,"",self.age)
    @classmethod
    def get_percentage(cls,name,marks):
        return cls(name,str((int(marks)/600)*100))
    @staticmethod
    def getage(age):
        print(age)
        if age<17:
           print("it to short")
        else:
           print("it doesnot belong to school")
s1=students("sara","20")
marks="360"
name="sara"
#marks1=str((int(marks)/600)*100)
s2=students.get_percentage(name,marks)
print(s2.msg())
students.getage(27)
s1.getage(23)
#=======================================================================================
# names spaces and variable scope
# local and global varibvals and enclosing cariables
#========================       LEGB RULE  local,enclosing,global,builtin       =============================================

def f1():
    x=2
    print(x)
f1()
# it is local variable
#====================================================================================== 
#it is global variable which is represent out side the function() y=10
y=10
def f1():
    x=2
    print(x)
f1()
print(y)   
#=========================================================================================
#making enclosing scope into global variable scope
y=10
def f1():
    x=2
    global y
    y=y+1
    print(x)
    print(y)
f1()
print(y)
#============================================================================================
#enclosing scope ==================================================================
def f1():
    x=54   # enclosing scope in nested function 
    def inner():
        y=10
        print(y)
        print(x)
    inner()
    print(x)
f1()    
#==========================================================================================
# builtin function
#like print
print(["my name is huzaifa"])
#================================================================================
# ========================  closures ============================================
#nested function 
def outer():
    x=3
    def inner():
        print(x)
    inner()
outer()    
#===========================================================================
def outer():
    x=3
    def inner():
        y=4
        result=x+y
        return result
    return inner()
# e is the reference of inner( function return ) for this we can excess inner function outside the function    
e=outer()
print(e)    
#=============================================================================
def outer():
    x=3
    def inner():
        y=4
        result=x+y
        return result
    return inner
# e is the reference of inner( function return ) for this we can excess inner function outside the function    
e=outer()
print(e) 
#==============================================================================
#=============================   decorators ===================================















#==============================================================================
class teacher:
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject
    def teaching(self):
        return ("{} is very good teacher of {}".format(self.name,self.subject))
x=teacher("sara","calculus")
print(x.teaching())        
#==============================================================================
class Dog: # Class Attribute species = 'mammal' # Initializer / Instance Attributes 
    def __init__(self, name, age):
        self.name = name 
        self.age = age # instance method 
    def description(self): 
        return "{} is {} years old".format(self.name, self.age) # instance method 
    def speak(self, sound): 
        return "{} says {}".format(self.name, sound) # Instantiate 
    
razer = Dog("Razer", 6) # call our instance methods 
print(razer.description())
print(razer.speak("Woof Woof"))
#================================================================================
#childclass inheritance
class Dog: # Class attribute species = 'mammal' # Initializer / Instance attributes 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age # instance method def description(self): 
        return "{} is {} years old".format(self.name, self.age) # instance method 
    def speak(self, sound): 
        return "{} says {}".format(self.name, sound) # Child class (inherits from Dog() class) 
class RussellTerrier(Dog): 
        def run(self, speed): 
            return "{} runs {}".format(self.name, speed) # Child class (inherits from Dog() class)
class Bulldog(Dog): 
        def run(self, speed):
            return "{} runs {}".format(self.name, speed) # Child classes inherit attributes and # behaviors from the parent class
        
thunder = Bulldog("Thunder", 9) 
print(thunder.description()) # Child classes have specific attributes # and behaviors as well 
print(thunder.run("slowly")) # Is thunder an instance of Dog()?
print(isinstance(thunder, Dog)) # Is thunder_kid an instance of Dog()?
thunder_kid = Dog("ThunderKid", 2) 
print(isinstance(thunder, Dog)) # Is Kate an instance of Bulldog() 
Kate = RussellTerrier("Kate", 4) 
print(isinstance(Kate, Dog)) # Is thunder_kid and instance of kate? 
print(isinstance(thunder_kid, Kate)) 
print("Thanks for understanding the concept of OOPs")
#========================================================================================
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def speak(self):
        return ("{} it age is={} ".format(self.name,self.age))
class bulldog(Dog):
    def ugh(self,run):
        return( "{} it run very fast than me it speed is {}".format(self.name,run))
class bultharooo(Dog):
    def speed(self,lookingvise):
        return("{}it looking wise very {}".format(self.name,lookingvise))
x=Dog("zumbha","18")
print(x.speak())
y=bulldog("zumbha","19")
print(y.ugh("slowly")) 
#==========================================================================================
class house:
    def __init__(self,area,location,number_of_rooms):
        self.area=area
        self.location=location
        self.number_of_rooms=number_of_rooms
    def xyz(self):
        return ("{} nearest from {} and number of rooms is{}".format(self.area,self.location,self.number_of_rooms))
class flat(house):
    def ugh(self,appartment_number):
        return ("{} nearest from {} and number of rooms is{} and appertment number is={}".format(self.area,self.location,self.number_of_rooms,appartment_number))
    
x=house("Nazimabad","5E-9/38","=5")
print(x.xyz())    
y=flat("Nazimabad","opposite side of 5E-9/38","=5")
print(y.ugh(3))
#=============================================================================================
class point:
    def setx(self,xcoord):
        self.x=xcoord
    def sety(self,ycoord):
        self.y=ycoord
    def get(self):
        return(self.x,self.y)
a=point()
print(a.setx(3))
print(a.sety(4))
print(a.get())  
#==================================================================================================      
class rectangle:
    def setsize(self,width,length):
        self.width=width
        self.length=length
    def area(self):
        #return ("area_of_rectangle is={}*{}".format(self.width,self.length))
        return(self.width*self.length)
areas=rectangle()
areas.setsize(3,4)
print(areas.area())
#=====================================================================================================
import fractions
x=fractions.Fraction(3,4)
x
#====================================================
class Card:
    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit
    def rank(self):
        "return rank"
        return (self.rank)
    def suit (self):
        "return suit"
        return (self.suit)
card=Card("3","\u2660")
print(card.rank())
print(card.suit())    

class Quence:
    def __init__(self):
        self.a=[]
    def enqueue(self,items):
        return(self.a)
        return self.a.append(items)
fruit=Quence()
print(fruit.enqueue("apple"))        
fruit.enqueue("banana")

#========================================================
class bankbalance:
    def __init__(self,balances):
        self.balance=balances
    def balance(self):
        return("{}".format(self.balance))
    def withdraw(self,widthdraw):
        global a
        a=widthdraw
        r=self.balance-widthdraw
        return("{}".format(r))
    def deposite(self,deposites):
        global a
    
        a=self.balance-a+deposites
        
        return("{}".format(a))
x=bankbalance(700)
print(x.balance)        
print(x.withdraw(70))
#print(x.balance())
print(x.deposite(7))
#=============================================
class problem:
    def __init__ (self,v):
        self.value=v
try:        
    a=problem(90)
    a.value()
    #print(a.value())        
except:
    print("it not working")
#=====================================================
class point:
    def setx(self,setx):
       self.setx=setx
    def sety(self,sety):
        self.sety=sety
    def xyz(self):
        return(self.setx,self.sety)
    def distance(self):
        return(self.sety-self.setx)
x=point()
print(x.setx(0))
print(x.sety(1))        
print(x.xyz())    
d=point()
print(d.setx(0))
print(d.sety(1))
print(d.distance())    
#=============================================================
#class attributes
class sample:
    x = 23

    def increment (self): 
    self.__class__.x += 1
    a.__class__.x

#===============================================================
class Student:

    "A Class representing a"
    def __init__(self,n,a):
        self.full_name = n
        self.age = a
    def get_age (self):
        return self.age
class Cs_student (Student):

        "A class extending"
        def __init__(self,n,a,s):
            Student.__init__(self,n,a) #Call __init__ for student
            self.section_num = s
        def get_age (): #Redefines get_age method entirely
            print ("Age:", str(self.section))    
    
a=Student("huzaifa",23)
a.get_age()
d=Cs_student("B","huzaifa",23)
d.get_age()   
#=================================================================
import math
math.sqrt
math.acos
math.tan
math.sin
#============================================================
class Teacher:
    name="syed Faisal Ali"
    course="Object oriented programming"
t1=Teacher()
print(t1.name)
print(t1.course) 
#==============================================================
class Teacher:
    #initialinzing the things::
    def __init__(self,name,course):
        self.name=name
        self.course=course
mt=Teacher("syed Faisal Ali","Object oriented programming")
print(mt.name) 
print(mt.course)       
#====================================================================



#Question 1
class personalinfoo:
    def __init__(self,name,university,department,hobbies):
        self.name=name
        self.university=university
        self.department=department
        self.hobbies=hobbies
    def infoo(self):
        print("my name is{} and I studied in {} and my department is {}and I like to {} to make a good programs".format(self.name,  self.university, self.department,self.hobbies) )        
        
I=personalinfoo("Huzaifa","UIT","CS","Coding")
I.infoo()
_#----------------------------------------------------------------------#
#Friend 1:
F1=personalinfoo("zohair","UIT","CS","Coding")
F1.infoo()
#----------------------------------------------------------------------#
#Friend 2:
F2=personalinfoo("Emaid","UIT","CS","Coding")
F2.infoo()
 #-------------------------------------------------------------------#
#Friend 3:
F3=F3=personalinfoo("zain","UIT","CS","Coding")
F3.infoo()



#question 2
class dinner:
    def __init__(self,soup,maincourse,salad,dessert):
        self.soup=soup
        self.maincourse=maincourse
        self.salad=salad
        self.dessert=dessert
    def items(self):
        print("I want this {}\n and this {}\n and this {}\n and this {}".format(self.soup,self.maincourse,self.salad,self.dessert))
#Friend 1:
F1=dinner("cornsoup","goolakabab","italiansalad","ice_cream")
F1.items()        

#Friend 2:
F2=dinner("thisoup","birayanii","italiansalad","mravaldesert")
F2.items()
#Friend 3:
F3=dinner("thisoup","whitehandhii","italiansalad","picholocate_cake")
F3.items()        
#==============================================================
