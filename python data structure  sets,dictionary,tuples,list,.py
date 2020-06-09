# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 15:20:08 2020

@author: HASSAN ENTERPRISES
"""
# python data type tuples
stock = "FB", 75.00, 75.03, 74.90
stock2 = ("FB", 75.00, 75.03, 74.90)

#==============================================
import datetime
def middle(stock, date):
    symbol, current, high, low = stock
    return (((high + low) / 2), date)
mid_value, date = middle(("FB", 75.00, 75.03, 74.90),datetime.date(2020, 2,5 ))
print(mid_value,date)
#==============================================   
#                
stock = "FB", 75.00, 75.03, 74.90
high = stock[2]
high
#=========slicing===============================
stock[1:3]
stock[-4:-4]
stock[1:-1]

#def huzii(quality,speed):
   # quality=qui,exy
    #speed=ety,ugh,xyz
    #return(quality,speed)
#bilal=huzii(("good","excellent"),("low","medium","high"))#print(bilal)    
    
# dictionary=======================================
stocks = {"GOOG": (613.30, 625.86, 610.50),"MSFT": (30.25, 30.70, 30.19)}  
stocks["GOOG"][0],stocks["MSFT"][1]   
#remove duplicate word from set ::::
    

names=[]
x=int(input("enter the name:"))
for i in range(x):
    #print("please enter your name")
    names.append(input())
s=set(names)
print(s)
#======================================================================
#remove duplicate word from list
names=[]
n=int(input("enter the names;"))
for i in range(n):
    print(i+1,"Enter the name:")
    names.append(input())
s=set(names)
#names=list(s)
for x in  s:
    print(x)
#============================================================================
#remove duplicate character from string
s=input("enter the value:") 
x=0
s1=""
for i in s:
    if s.index(i)==x:
        s1+=i
    x+=1
print(s1)  
#========================================================================
list=["huzaifa","bilal","nazia","huzaifa"]
s=set(list)
print(s)
#========================================================================
name=[]
for i in range(0,5):
    n=input("enter the names:")
    name.append(n)
    print(name)
y=set(name)
print(y)    
#========================================================================
# dsictionaries
# unorders hotii hai, key-value pairs hoti hai divtionary may ,or keys unique hoti hai likin ek key multiple value store kersaktoi hai
#dictgionary method to ectract data 
#dictionary are  created with two curely braces and separated by colon For every key there are only one single value however multiple key can store 
# the same value key can be string,number,tuple but values can be data type  
stocks = {"GOOG": (613.30, 625.86, 610.50),
"MSFT": (30.25, 30.70, 30.19)}
stocks["GOOG"]
#=========================================================================
dict={"Name":"huzaifa","brother":"bilal","mother":"nazia"}
print(dict["Name"])
#==========================================================================
#returning a value of dict
dict={"Name":"huzaifa","brother":"bilal","mother":"nazia"}
for i in dict:
    print(dict[i])
print(dict.items())
print(dict.values())    
#============================================================================
stocks = {"GOOG": (613.30, 625.86, 610.50),"MSFT": (30.25, 30.70, 30.19)}
#stocks["GOOG"][0] 
stocks["GOOG"][0],stocks["MSFT"][1]   
#===================================================================
stocks = {"GOOG": (613.30, 625.86, 610.50),"MSFT": (30.25, 30.70, 30.19)}
print(stocks.get("RIM"))
#basicalliy popitems() dictionary ,ay say first element ko remove kerdyt hai
print(stocks.popitem())
#======================================================================
stocks = {"GOOG": (613.30, 625.86, 610.50),"MSFT": (30.25, 30.70, 30.19)}
stocks.clear()
print(stocks)
#==========================================================================
dict={"name":"jibran","Age":13,"Class":"seveth","DOB":"16"}
for i in dict.keys():
    print(i,"thats awesome")
    #print("{}".format(i),"that awesome")
#===========================================================================
# set default values basically new value lay raha haii joo ap phalay 
stocks = {"GOOG": (613.30, 625.86, 610.50),"MSFT": (30.25, 30.70, 30.19)}    
stocks.setdefault("GOOG", "INVALID")
#==========================================================================    
stocks = {"GOOG": (613.30, 625.86, 610.50),"MSFT": (30.25, 30.70, 30.19)}    
stocks.setdefault("MSFT", "HUZAIFA")
#==========================================================================
stocks = {"GOOG": (613.30, 625.86, 610.50),"MSFT": (30.25, 30.70, 30.19)} 
stocks.setdefault( (30.25, 30.70, 30.19), (30, 35, 36))
stocks
#==========================================================================
dict={"A":1,("1"):[3,4],"B":[3,4,5,6,7],"C":4}
dict[("1")]
#========================================================================
dict={"A":1,("1,2"):[3,4],"B":[3,4,5,6,7],"C":4}
dict[("1,2")]
#=======================================================================
#adding new key-value pair in dictionary
dict["Name"]="huzaifa"
print(dict)    
#=========================================================================
#want to delete some record in th dictionary
del dict["Name"]
print(dict) 
#============================================================================
#verify the key in the dictionary
"Name" in dict
"A" in dict
#===========================================================================
len(dict)
#for i in (len(dict)):
    #print(i)
#=============================================================================
#adding two dictionary by update method
dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}

dict1.update(dict2)
print(dict1)
dict1.update(dict3)
print(dict1) 
#==============================================================================
for x,y in dict1.items():
    print(x,y)
#==================================================================================
#===================== NESTED DICTIONARY ==========================================
BIALAL={1:{"name":"huzaifa","brother":"bilal"},2:{"mother":"nazia","father":"sohail"},3:{"grandfather":"naeemuddin","grandmother":"daadiiii"}}
for i in BIALAL:
    print(i,"",BIALAL[i])
   # for j in BIALAL[i]:
        #print(j)
    
    
        
#=========================================================================================
stocks = {"GOOG": (613.30, 625.86, 610.50),
"MSFT": (30.25, 30.70, 30.19)}
for stock, values in stocks.items():
    print("{} last value is {}".format(stock, values[0])) 
#==========================================================================================    
stocks = {"GOOG": (613.30, 625.86, 610.50),
"MSFT": (30.25, 30.70, 30.19)}
for x,y in stocks.items():
    print("{} last value is={}".format(x,y[1]))
#=========================================================================================
random_keys = {}
random_keys["astring"] = "somestring"
random_keys[5] = "aninteger"
random_keys[25.2] = "floats work too"
random_keys[("abc", 123)] = "so do tuples"    
print(random_keys)
print(len(random_keys)) 
#===============================================================================================
#using classes with dictionaries
class AnObject:
    def __init__(self, avalue):
        self.avalue = avalue
my_object = AnObject(14)
random_keys[my_object] = "We can even store objects"
#my_object.avalue = 12
print(random_keys)
for key, value in random_keys.items():
    print("{} has value {}".format(key, value))
    #====================================================================
class AnObject:
    def __init__(self, avalue):
        self.avalue = avalue
my_object = AnObject(14)
random_keys[my_object] = "We can even store objects"
my_object.avalue = 12
try:
    random_keys[[1,2,3]] = "we can't store lists though"
except:
    print("unable to store list\n")
for key, value in random_keys.items():
    print("{} has value {}".format(key, value))    
#====================================================================
#write a code of count number of occurence of letter ,words and
string ="hello how are you".count("")
print(string)    
#=====================
string1="aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeeeeeeeeedddddddddddddd".count("e")
print(string1)    

#=============================
string2="it is a beautifulsunny sunny day".count("sunny")
print(string2)
#=============================
dict={"name":"huzaifa","brother":"bial","mother":"nazia"}.pop("name")
print(dict)
#=============================
dict={"name":"huzaifa","age":"12","Class":"13","2006":"school","friend1":"mohib","friend2":"akhber","friend3":"billii"}
for x,y in dict.items():
    print(x,y)
dict.pop("friend1")
print(dict.popitem())
print(dict)    
#================ NESTED DICTIONARY=========================================================================
BIALAL={1:{"name":"huzaifa","brother":"bilal"},2:{"mother":"nazia","father":"sohail"},3:{"grandfather":"naeemuddin","grandmother":"daadiiii"}}
for i in BIALAL:
    print(i,"",BIALAL[i])
    for j in BIALAL[i]:
        print(j)
#=================================================================================================================
BIALAL={1:{"name":"huzaifa","brother":"bilal"},2:{"mother":"nazia","father":"sohail"},3:{"grandfather":"naeemuddin","grandmother":"daadiiii"}}
for i in BIALAL:
    print(i,"",BIALAL[i])
    for j in BIALAL[i]:
        print(j,BIALAL[i])        
#=============================================================================================================
BIALAL={1:{"name":"huzaifa","brother":"bilal"},2:{"mother":"nazia","father":"sohail"},3:{"grandfather":"naeemuddin","grandmother":"daadiiii"}}
for i in BIALAL:
    print(i,"",BIALAL[i])
    for j in BIALAL[i]:
        print(j,BIALAL[i][j][0])
#=============================================================================================================
BIALAL={1:{"name":"huzaifa","brother":"bilal"},2:{"mother":"nazia","father":"sohail"},3:{"grandfather":"naeemuddin","grandmother":"daadiiii"}}
for i in BIALAL:
    print(i,"",BIALAL[i])
    for j in BIALAL[i]:
        print(BIALAL[i][j])   
#==============================================================================================
#in this every for is storing a key         
dict={"name":"huzaifa","brother":"bial","mother":"nazia"}
for i in dict:
    print([i])        
#========================================================================
dict={"name":"huzaifa","brother":"bial","mother":"nazia"}
for i in dict:
    print(dict[i])        
#=====================================================================
dict={1:{"name":"huzaifa","brother":"bilal"},2:{"grandfather":"naeem","grandmother":"daddii" }}
dict1={3:{"father":"sohail"},4:{"fatherbrother":"yaseen"}}

for i in dict:
   # print(i,dict[i])
    for j in dict[i]:
        print("[{},{}]".format(j,dict[i][j]),end='')
        
for k in dict1:
    for l in dict1[k]:
        print("[{},{}]".format(l,dict1[k][l]),end='')
                
#======================= LIST data structure ==============================================
#• The append(element) method adds an element to the end of the list
#• The insert(index, element) method inserts an item at a specific position
#• The count(element) method tells us how many times an element appears
#in the list
#exception if it can't find it
#• The find()method does the same thing, but returns -1 instead of raising
#an exception for missing items
#• The reverse() method does exactly what it says—turns the list around
#• The sort() method has some rather intricate object-oriented behaviors,
dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}
#merge the dictionary::::
dict4=dict1
dict4.update(dict2)
dict4.update(dict3)
print("dict4",dict4)
#======================= DIFFERENCE BETWEEN ====================================================
#APPEND AND EXTEND
#APEEND USED TO ADD ANY THING IN THE END OFF THE LIST
#ITERABLE ANY THING WHICH CAN BE LOOP OVER            
list1=[1,2,3,4,5]
list1.append(6)
list1
#=================================extend+========================================================
#extend take each character as single unit and also increase the of list
list1=[1,2,3,4,5] 
list1.extend("huzaifa")
print(list1)
print(len(list1))
#finding a index
print("the index of 5 is",len(list1)-1)
#==================================================================================================
list1=[1,2,3,4,5]
list1[4]
print(len(list1)-1)
print(list1[len(list1)-1])
#==================================================================================================
dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}
dict4={**dict1,**dict2,**dict3}
print(dict4)
#==================================================================================================
countries=["Germany","Japan","Austrila"]
Capitals=["Berlin","tokyo","canberra"]
### we want to doo it {"Germany":"Berlin","Japan":"tokyo","Austrila":"canberra"}
#by usiny for loop
country_capital_dict={}
for i in range(len(countries)):
    country_capital_dict[countries[i]]=Capitals[i]
print(country_capital_dict)    
#=================================================================================================    
#============ by using zip it aniterator================================================================
countries=["Germany","Japan","Austrila"]
Capitals=["Berlin","tokyo","canberra"]
it=zip(countries,Capitals)
print(it)  
country_capital_pair=list(it)
print(country_capital_pair)
country_capital_dict=dict(country_capital_pair)
print(country_capital_dict)
#=================================================================================================
countries=["Germany","Japan","Austrila"]
Capitals=["Berlin","tokyo","canberra"]
it=zip(countries,Capitals)
list1=list(it)
list2=list(it)
#thats iterators work it will remember the things and use things so it cannot use use regain the use things
print(list1,list2)
#====================================================================================================
list1=[1,2,3,4,5]
list2=[2,3,4,5,6]
x={}
for i in range(len(list1)):
    x[list1[i]]=list2[i]
print(x)    
#=====================================================================================================
#starting with an empty dictionary:::
name={}
name["huzaifa"]="working"
print(name)
#======================================================================================================
alien={"x_position":0,"y_position":25,"speed":"medium"}
if alien["x_position"]==0:
    print("alien is very slow")
elif alien["y_position"]<=19:
    print("alien is very fast")
else:
    print("aleien is nothing to do we just waste our money on it")
print()    
#removin g key values pairs
alien={"x_position":0,"y_position":25,"speed":"medium"}
del alien["x_position"]
print(alien)    
#===================================================================================================
favourite_language={"jen":"python","huzaifa":"python","rameez":"c++"}
print(favourite_language["huzaifa"].upper())    
#===========================================================================================
list=["huzaifa","rameez","jen"]
favourite_language={"jen":"python","huzaifa":"python","rameez":"c++"}
for i in favourite_language.keys():
    print(i.title())
    if i in list:
        print("i am very happy that i made this code")
    else:
        print("nothing")
#==============================================================================================
pizza={"crust":"thick","topping":["mushroom","extra","cheese"]}
print(pizza["topping"])
for i in pizza.values():
    print(i,"\t",end="")
#=============================================================================================
#getting a average of dictionnary
mylist={"emp1":1000,"emp2":2000,"emp3":3000,"emp4":4000}
length=len(mylist)  
print(length)  
sum=0    
for i in mylist.values():
    sum=i+1
print(sum)    
avg=length/sum    
print(avg)
#==========================================================================================
dict={1:10,2:20,3:30,4:40,5:50,6:60}
length=len(dict)
sum=0    
for i in dict.values():
    sum=i+1
print(sum)  
avg=length/sum
print(avg)
#=========================================================================================
dict={1:10,2:20,3:30,4:40,5:50,6:60}
length=len(dict)
sum=0
count=0
for i in dict.values():
    sum=sum+i
    count=count+1
print(sum)
print(length)
avg=sum//length
print(avg)
print(count)
#==========================================================================================
def huzaifa(x):
    print(x,"this is my list")
huzaifa([1,2,3,4,5])    
#============================================================================================
x="my name is huzaifa"
y=x.split(".")

z.append(y)
print(z)
for i in z:
    x=i[0]
print(x)
   
   
    


#=========================================================================================
#============================ string methods================================================
message="this message is top secret and should not be divuled to anyone without top secret clearence"
message.find("message")
# find basically give a index were the element should start 
message.count("top secret")
message.upper(),message.lower(),message.title()
message.split(".")
message.replace("message","chat")
message.index("is")
message.capitalize()
# translate is used to replace certain letter in a string with other based on a mapping of character to character
string="abcd"
dict1={"a":"1","b":"2","c":"3"}
t=string.maketrans(dict1)
t
ord("a")


#===========================================================================================
string="hello this is my first video"
dict1={"a":"1","b":"2","c":"3"}
t=string.maketrans(dict1)
t
chr(97)
#=============================================================================================
#unicode ordinal(integers) or character to unicode ordinal
string="hello this is my first video"
str1="abcd"
str2="1234"
t=string.maketrans(str1,str2)
t
string.translate(t)
#================================================================================================
print("@@@@@@@@")
print("*************")
print(r"\n""\t")
#================================================================================================
string="hello this is my first video"
str1="abcd"
str2="1234"
str3="#%$"
#str4="qasd"
t=string.maketrans(str1,str2,str3)
t
string.translate(t)
#==========================================================================================
table=string.maketrans("abcd","uxyz")
print(table)
"fasd".translate(table)
#==========================================================================================
string="hello this is my first video"
dict={97: 49, 98: 50, 99: 51, 100: 52, 35: None, 37: None, 36: None}
table=string.maketrans(dict)
table
chr(52)
string.translate(table)
#===============================================================================================
#string formatting
def function(n):
    for i in range(0,n):
        print("the binary number is bi\t{}\nthe octal number is o{}".format(i**2,i**3))
function(17)        
#======================================================================================================
def function(n):
    for i in range(0,n):
        print("the binary number is bi\t{:8}\nthe octal number is o\t{:8}\n the unicode character is c\t{}".format(i**2,i**3,i))
function(17) 
#====================================================================================================     
student=[]
student.append(["huzaifa","bilal","nazia"])
student.append(["huzaifa","bilal","nazia"])
student.append(["huzaifa","bilal","nazia"])
student.append(["huzaifa","bilal","nazia"])
roster(students)

#=============================================================================================

#finding a execution time of your program bu using time module
import time
initial=time.time()
k=0
for i in range(45):
    print("this is huzaifa")
print("for loop ka time:",time.time()-initial,"seconds")
initial2=time.time()    
while(k<45):
    k+=1
    print("this is huzaifa")
    time.sleep(2)
print("while loop ka time:",time.time()-initial2,"seconds")
#==============================================================================================================
import time
localtime=time.asctime(time.localtime(time.time()))    
print(localtime)    
#=====================================================================================================
import calendar
cl=calendar.month(2018,2)
print(cl)
#=========================================================================================================
import datetime
x=datetime.date.today()
print(x)
#=============================
import time
huzii=time.localtime(time.time())
print(huzii)
#==============================
from datetime import datetime
ct=datetime.now()
print(ct)
#=============================
import time
x=(time.strftime("%a %A %b %B %H %I %Y %y %m %M %z %p %S" ),time.localtime())
print(x)
#===============================
n = int(input("enter the value;"))
for i in range(0,10):
    for j in range(1,11):
        x=n*j
    print(x)  

#===================================================================================
def function(n):
    x=n
    x.sort()
    print(x)
function([1,4,7,23,3,5,7]) 
#=======================================================================================
def function(n):
    for i in range(1,n):
        if i%2==0:
            print(i,"I will do it",end="")
        elif i%3==0:
            print(i," I will do it")
        else:
            print("i will not done it")
function(18)            
#======================================================================================
import time
x=time.gmtime()
y=time.localtime()
print(x,y)
#==================================================================================
def hexii(str):
    x=ord(str)
    print(x)
str=(input("enter the value"))
hexii(str)
#=====================================================================================
def hexii(str):
    x=ord(str)
    print("{:x}".format(x))
str=(input("enter the value"))
hexii(str)
#============================================================================================
dict={"name":"huzaifa","age":"12","Class":"13","2006":"school","friend1":"mohib","friend2":"akhber","friend3":"billii"}
dict["huzaifa"]="goodboy"
print(dict)    
#===========================================================================================

#=========================== set ===========================================================



    
    
    


#===============================================================================================
#=================== sorting a list=============================================================

  
