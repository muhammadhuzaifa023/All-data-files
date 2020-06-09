# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 18:35:30 2020

@author: HASSAN ENTERPRISES
"""

#using main concept in pyhton 
#if__name__=="__main__"
#__name__ is builtin variable in python which return name of module jesay abbhii may es module may km ker raha hoo ya eska main program haii

def mul(x,y):
    return (x**y)
print(mul(2,3))
print(__name__)
#__main__ answerv is main\
#---------------------------------- using args and kwargs --------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
#Using *args and **Kwargs or we say that *vars and **kvars
def function_1(name,age,roll_number):
    print("my name is ",name,"and my age is ",age,"my roll_numbre is ",roll_number)
function_1("GHuxzaifa","20",139)    
#------------------------------------------------------------------------------------------------------------------------------------------------
#args is basically a method to store number of argument in *args and then we pass a multiple parameters on it:
def function_1(*args):
    print("my name is ",args[0],"and my age is ",args[1],"my roll_numbre is ",args[2])# [0],[1],[2] is basically a index number of args containing a number of 
    #variable on it
    print(type(args))# makinf a tuple on it type = typle
function_1("GHuxzaifa","20",139)    
#--------------------------------------------------------------------------------------------------------------------------------------------
def function_1(*args):
    #print("my name is ",args[0],"and my age is ",args[1],"my roll_numbre is ",args[2])# [0],[1],[2] is basically a index number of args containing a number of 
    #variable on it
    if (len(args)==3):
        print("my name is ",args[0],"and my age is ",args[1],"my roll_numbre is ",args[2])
    else:
        print("my name is ",args[0],"and my age is ",args[1]) 
        
function_1("GHuxzaifa","20",139)  
function_1("GHuxzaifa","20")    
#-------------------------------------------------------------------------------------------------------------------
def function_1(*li):
#we can pass also parameter as we can give any name of ardef function_1(*li):
    #print("my name is ",args[0],"and my age is ",args[1],"my roll_numbre is ",args[2])# [0],[1],[2] is basically a index number of args containing a number of 
    #variable on it
    if (len(li)==3):
        print("my name is ",li[0],"and my age is ",li[1],"my roll_numbre is ",li[2])
    else:
        print("my name is ",li[0],"and my age is ",li[1]) 
li=["huzaifa","20",139]        
function_1(*li)  
function_1("GHuxzaifa","20")    
#-------------------------------------------------------------------------------------------------------------------
#The difference between args and kwargs is in args their is using in list one argument is pass 
#but in kwargs their is use of dictionary 
#using kwargs
def printmarks(**kwargs):
    for x,y in kwargs.items():
        print(x,y)
    print(type(kwargs)) # the type is kwargs       
marks={"huzaifa":42,"Bilal":34,"shaiz":13}
printmarks(**marks)    
#--------------------------------------------------------------------------------------------------------------------
#aghr humay ek function may normal and args and kwargs sb koo pass kray too kiya hooogaa
def master(normal,*args,**kwargs):
    print(normal)
    for i in args:
        print(i)
    for x,y in kwargs.items():
        print(x,y)
li=["huzaifa","20",139]
marks={"huzaifa":42,"Bilal":34,"shaiz":13}
print(master("huzii",*li,**marks))    
#----------------------------------------------------------------------------------------------------------------
#Using for loop in else condition:
khana=["roti","chawal","pharatha"]
for i in khana:
    if i =="pharatha":
        print("This thing is found in your item_of_khana")
        break
else:
    print("This thing is not found in ypour khana")
#-------------------------------------------------------------------------------------------------------------
 #-------------------------------------  Caching A function ---------------------------------------------------   
import time
#from functools import lru_cache

def some_work(n):
    time.sleep(n)
    return n
if __name__=="__main__":
    print("Done....A calling function")
    some_work(4)
    print("calling again.......function")
    some_work(4)
    print("Again Calling.......function")
    some_work(4)
# aghr may ya chata hoookaa ya joo load time lay raha haii yaa naalay too may ek decroater use krayooga @lur_cache ka jessay ya load time nh laygaa
import time
from functools import lru_cache

@lru_cache(maxsize=3) #maxsize woo attribute hoota haii ka app kitnii value koo cache kerna chatay haii ka ka woo memeory may woohii 3 value store kerka rakhaygaaa or delay time nh hooga
def some_work(n):
    time.sleep(n)
    return n
if __name__=="__main__":
    print("Done....A calling function")
    some_work(4)
    print("calling again.......function")
    some_work(4)
    print("Again Calling.......function")
    some_work(4)
#---------------------------------------------------------------------------------------------------------------
@lru_cache(maxsize=int(input('how many cache data you want ? \n')))
def run_cache(n):
    print('cache run')
    time.sleep(n)
    time.sleep(5)
    print('file run again')
run_cache(3)
#--------------------------------------------------------------------------------------------------------------
#using a finallyto cleanup your code
#aghr hum ya chathay haii kaa humgaraha code try ka run hooya ya phir except kaa undonoo mat say kjoi bhi run hooo
#tooo uskoo finally may dhall dooo may
f=open("huzaifa.txt")
try:#try or except may say ek cheez run hooti haiiii
    f2=open("bilal.txt")
except:
    print("Bilal file doesnot exit so it will give me some error")
else:
    print("This will only run when except is not run and if except will run soo else will not run")    
finally:# finally humasha run hoo ga chahay app try may hoo ya except may hoo ya phir else may hoo finally hamesha run hooga 
    print("Run this way")
    f.close() 
    f2.close()
#-------------------------------------------------------------------------------------------------------------    
f=open("huzaifa.txt")
try:#try or except may say ek cheez run hooti haiiii
    f2=open("bilal.txt")
except EOFError as EOL:
    print("ya error ayaga",EOL)
    print("Bilal file doesnot exit so it will give me some error")
except IOError as IO:
    print("ya error ayaga",IO)    
else:
    print("This will only run when except is not run and if except will run soo else will not run")    
finally:# finally humasha run hoo ga chahay app try may hoo ya except may hoo ya phir else may hoo finally hamesha run hooga 
    print("Run this way")
    f.close() 
    f2.close()
#----------------------------------------------------------------------------------------------------------------    
# defining a coroutine in python  coroutine is just like a a pause and execute .....................................
#to make any function a coroutine we will use async to make it coroutine    
#example make simple function like
def main():
    print("It juct like a simlpe function")    
main()    
# making a coroutine we wil use async
async def main():
    print("It juct like a simlpe function")    
main()    
#---------------------------------------------------------------------------------------------------------------
#------------------------------ how to pause a corroutine-------------------------------------------------------
#-------------------------------------  In python --------------------------------------------------------------
#we will use a word for it and it is await 
async def main():
    await awaitable_object
    print("It juct like a simlpe function")    
main()    


#------------------------------------- Using os module ---------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
import os
print(dir(os))
# now we will find current directory soo we will use 
print(os.getcwd())#getcwd stand for (current_directory)
#if we want to change current directory
os.chdir("C://") #chdir change it current directory to new directory
print(os.getcwd())
print(os.listdir())  # listdir() kiya kerayga es folder kiii sarii file kooo dydygaaaaa      
print(os.listdir("E://")) 
os.mkdir("this is my folder")   #mkdir kita kerta haiii ek folder buna dyta haiii
os.makedirs("This/That") #make sub directory in folders
os.rename("huzaifa.txt","code_with_harry.txt")
print(os.path.join("C://","//huzaifa.txt")) #joining the path of directory
print(os.path.exists("C://"))#ya mujhy return kerta haii ka ya path meray cpu may haii ka nhhh
#-----------------------------------------------------------------------------------------------------------------
# OH soldier preety my folder:
import os
def soldier(path,filename,mode):
    f1 = open(filename)
    list1 = f1.read().split('\n')
    f1.close()
    os.chdir(path)
    files = os.listdir(path)
    i = 1
    for file in files:
        if file not in list1 and file.endswith(f'.{mode}'):
            os.rename(f"{file}", f"{i}.{mode}")
            i += 1
        else:
            if file not in list1:
                os.rename(file, file.capitalize())

if __name__ == '__main__':
    try:
        print("##The filename which you will write should be in your current directory..\n\n")
        print("##The filename(with extension) which you will write should be in your current directory..\n\n")
        path=input("Enter full path where you want to do changes ")
        filename=input("Enter file name ")
        mode=input("Plz define mode..for special changes ")
        soldier(path, filename, mode)
        print("!!!!!Work Done!!!!")
    except:
        print("Somethong Went Wrong!!!")
#------------------------------------------------------------------------------------------------------------------
#---------------------------------   Request Module in python -----------------------------------------------------
import requests #ya module kiya kerta haiii humhararii sariii request ko joo bhi hum program
#koo dyga like url us ka material humay textmay layayagaa or humharay console pr show kerdygaaa
r=requests.get("https://financialmodelingprep.com/developer/docs/")
print(r.text)        
#------------------------------ Using a json java script object notation -----------------------------------------
#------------ server objected language to communicate with client and server--------------------------------------        
import json        
data='{"var1":"harry","var2":56}'
#print(data["varl"])
parsed=json.loads(data)#json.loads kiya kerta haii data koo parts may kerdyta haiiii
print(parsed["var2"])        
#-----------------------------------------------------------------------------------------------------------------
data2={"channel_name":"code with huzaifa","cars":["bmw","ferrarii","audhiii"],"family_name":"siddique","isbad":False}
jsum=json.dumps(data2)
print(jsum)#json basically compatable programming hotii haiii joo python ko java may uskernay ka qabil bunna dytii haiii

#----------------------------------------------------------------------------------------------------------------
#Example
#Convert from JSON to Python:
import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])
#-----------------------------------------------------------------------------------------------------------------
#Convert from Python to JSON:
#import json
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)
#-----------------------------------------------------------------------------------------------------------------
#Convert Python objects into JSON strings, and print the values:

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
#-----------------------------------------------------------------------------------------------------------------
#When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:
#Python	JSON
#dict	Object
#list	Array
#tuple	Array
#str	String
#int	Number
#float	Number
#True	true
#False	false
#None	null
#=================================================================================================================
#Convert a Python object containing all the legal data types:
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
#Use the indent parameter to define the numbers of indents:

print(json.dumps(x, indent=4))
print(json.dumps(x))
print(json.dumps(x,indent=5,sort_keys=True))
#------------------------------------------------------------------------------------------------------------------
def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.spVoice")
    speak.Speak(str)

if __name__ == '__main__':
    import requests
    import json
    url = ('https://newsapi.org/v2/top-headlines?'
           'sources=bbc-sport&'
           'apiKey=49e391e7066c4158937096fb5e55fb5d')

    response = requests.get(url)
    text = response.text
    my_json = json.loads(text)
    for i in range(0, 11):
        speak(my_json['articles'][i]['title'])

#---------------------------------------------------------------------------------------------------------------
#------------------------------------    pickle module ---------------------------------------------------------
#pickle module is used as work as a achaaar yani may python may koi bhi oject koo bhulay wooo list hooo dict hoo ya set hooo koi bhi hoooo uskooo may pickle 
#ki help say preserve kerlooo gaaaa 
import pickle
cars=["audii","bmw","corolla","mercediess"]
file="cars.pkl"
obj_file=open(file,"wb")
#now  we use a function dump jesmay file kooo rukhna haiii dump function tooo arguments layta haiiii 
pickle.dump(cars,obj_file)
obj_file.close()          
# essay ek object bungaya ku ka kay may nay binary mode may rakha hoya haii too "wb" tooo may written in binary 
# soo may eskoo aesay read nh kersakta soo mujhy eskooo binary read may kerna pharaygaaa
file="cars.pkl"
obj_file=open(file,"rb")
cars_obj=pickle.load(obj_file)
print(cars_obj)
#---------------------------------------------------------------------------------------------------------------
#-------------------------- Local scope variable ---------------------------------------------------------------
#3A variable created inside a function is available inside that function:
def myfunc():
  x = 300
  print(x)
myfunc()
#----------------------------------------------------------------------------------------------------------------
#Function Inside Function
#As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:

#Example
#The local variable can be accessed from a function within the function:
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
    def huzii():
        print(x)
    huzii()    
  myinnerfunc()
myfunc()
#-----------------------------------------------------------------------------------------------------------------
#Global Scope
#A variable created in the main body of the Python code is a global variable and belongs to the global scope.
#Global variables are available from within any scope, global and local.
#Example
#A variable created outside of a function is global and can be used by anyone:
x = 4999
def myfunc():
  print(x)
myfunc()
print(x)
#-----------------------------------------------------------------------------------------------------------------
#Naming Variables
#If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):
#Example
#The function will print the local x, and then the code will print the global x:
x = 300
def myfunc():
  x = 200
  print(x)
myfunc()
print(x)
#----------------------------------------------------------------------------------------------------------------------------
#Global Keyword
#If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
#The global keyword makes the variable global.
#Example
#If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = 300
  x=500
myfunc()

print(x)
#------------------------------------------------------------------------------------------------------------------
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = 300
def myfunc():
  global x
  x = 200
myfunc()
print(x)
#----------------------------- Exercise of pickle module --------------------------------------------------------------------------
import pickle
import requests
url='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
respons=requests.get(url)
respons_text=respons.text
data=respons_text.splitlines()
red=[[i] for i in data]
#pickling the python object
fileobj=open('irisData.pkl','wb')
pickle.dump(red,fileobj)
fileobj.close()

#Reading Of Pickel file
fileobj=open('irisData.pkl','rb')
data=pickle.load(fileobj)
print(data)
#---------------------------------------------------------------------------------------------------------------
#---------------------------------- Iterators ------------------------------------------------------------------
#Python Iterators
#An iterator is an object that contains a countable number of values.
#An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
#Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
#Iterator vs Iterable
#Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
#All these objects have a iter() method which is used to get an iterator:
#Example
#Return an iterator from a tuple, and print each value:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
#----------------------------------------------------------------------------------------------------------------
#Example
#Strings are also iterable objects, containing a sequence of characters:

mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
#-----------------------------------------------------------------------------------------------------------------
HUZAIFA={"NAME":"HUZAIFA","FATHER_NAME":"SOHAIL","MOTHER_NAME":"NAZIA"}
b=iter(HUZAIFA.values())
b=iter(HUZAIFA.items())
print(next(b))
print(next(b))
print(next(b))
#-----------------------------------------------------------------------------------------------------------------
# here we using three word iterable,iterator,iteration
# What is iterable ( __iter__() or  __getitem__() )   #iter function is run on string
# What is iterator (   __next__ ())
# What is iteration
#weasy range function is a generator haii meraa
#example :1
#for i in range(230000000000):
    #print(i)
def gen(n):
    for i in range(n):
        yield i
g=gen(345545235467899000) 
print(g)  
g=gen(4)
print(g.__next__())     
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
  
h="huzaifa"
print(h[1])
print(iter(h))
itr=iter(h)
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
#------------------------------------------------------------------------------------------------------------------
#Looping Through an Iterator
#We can also use a for loop to iterate through an iterable object:
#Example
#Iterate the values of a tuple:
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x,end=",")
#-----------------------------------------------------------------------------------------------------------------
 #Example
#Iterate the characters of a string:
mystr = "banana"
for x in mystr:
  print(x) 
#-----------------------------------------------------------------------------------------------------------------
#Create an Iterator
#To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
#As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.
#The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
#The __next__() method also allows you to do operations, and must return the next item in the sequence.
#Example
#Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
#-----------------------------------------------------------------------------------------------------------------
#StopIteration
#The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
T#o prevent the iteration to go on forever, we can use the StopIteration statement.
#In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:

#Example
#Stop after 20 iterations:

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
for x in myiter:
  print(x)
#------------------------------------------------------------------------------------------------------------------
#---------------------------------------- string formatting -------------------------------------------------------
#String format()
#The format() method allows you to format selected parts of a string.
#Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?
#To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:
#Example
#Add a placeholder where you want to display the price:

price = 49
txt = "The price is {} dollars"
print(txt.format(price))
#--------------------------------------------------------------------------------------------------------------------
#Example
#Format the price to be displayed as a number with two decimals:
price=43.567889
txt = "The price is {:.2f} dollars"  
print(txt.format(price))  
#----------------------------------------------------------------------------------------------------------------------
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
#-----------------------------------------------------------------------------------------------------------------------
#Index Numbers
#You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:
#Example
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
#------------------------------------------------------------------------------------------------------------------------
#Also, if you want to refer to the same value more than once, use the index number:

#Example
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
#-----------------------------------------------------------------------------------------------------------------
#Named Indexes
#You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford"):
#Example
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

#================================================================================================================
# difference between "is vs =="
# == is a value equality two object have the same value
# is a reference equality two references refers have the same objects
# Example 
a=[0,1,2,3,4,5,6,7,8,9,10]
b=a
print(b)
b==a
b[2]=6
print(b)
print(a)
b is a
c=a[:]
b==c
print(b)
a==c
print(a)
a is c
a=[6,4,"34"]
b=[6,4,"34"]
print(a is b)
#---------------------------------------------------------------------------------------------------------------
#difference between 2.x vs 3.x
#---------------------------------------------------------------------------------------------------------------
# MCQ
2**(3**2)
(2**3)**2
2**3**2
  