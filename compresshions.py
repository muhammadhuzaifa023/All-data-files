# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""#=========================list comprission==============================
#=========================== Lambda function ===============================
list=[]
for i in range(1,11):
    if i%2==0:
       list.append(i)
print(list)    



#via list comression
#list=[]
#input=[1,2,3,4,5,6,7,8,9,10]
final=[i for i in range(1,11)]
print(final)


#================================
final=[i**2 for i in range(1,11)if i%2==0]
print(final)


#====================================== 2d array [[]]denoted by row and ineer value is [[2,3]]
# is column   [[1,2],[3,4]] i=0 i=1  j=0 j=1
matric=[[1,2],[3,4]]
for i in range(0,2):
    for j in range(0,2):
        print(matric[i][j],end="\t")
    print("\n")
final=[[matric[i][j]for j in range(0,2)]for j in range(0,2)]
print(final)    
    
#========================================================================
# transpose matric row change into column and column change into row 
matric=[[1,2],[3,4]]
for j in range(0,2):
    for i in range(0,2):
        print(matric[i][j],end="\t")
    print("\n")
final=[[matric[i][j]for i in range(0,2)]for j in range(0,2)]
print(final)     


#================================================================
list=[]
for i in range(1,145):
    list.append(i)
    print(list)
    for i in list:
        n=input("enter the value:")
        z=i*n
        if z%2==0:
            print("it ok")
        else:
            print("not ok")
            
#===============================================================
list=[]
for i in range(1,145):
    list.append(i)
    print(i)
            
n=int(input("enter the value:"))
for j in range(1,i):
    z=j*n
    if z<=144:
        print(z)
#=======================================================================

#list=[]
final=[[i for i in range(1,145)] for j in range(1,i) ]
list.append(i)
print(i)
n=int(input("enter the value:"))
#for j in range(1,i):
z=j*n
if z<=144:
    print(z)




        

#==========================================================-
list=[-1,2,-3,-4]
pos,neg=[i for i in list if i>0],[j for j in list if j<0]
print(pos,neg)    


#====================== dictionary compression==============================

dic={1:"a",2:"b",3:"c",4:"d"}
dict={i:j for i,j in dic.items()}
print(dict)

#=============================================================================

dic={1:"a",2:"b",3:"c",4:"d"}
dict={j for j in dic.values()}
print(dict)

#=================================================================================

dic={1:"a",2:"b",3:"c",4:"d"}
dict={i for i in dic.keys()}
print(dict)

#=============================================================================
dic={1:"a",2:"b",3:"c",4:"d"}
dict={j for j in dic.values()}
print(dict)

#========================================================================
dic={1:"a",2:"b",3:"c",4:"d"}
dict={j*2 for j in dic.values()}
print(dict)
#==========================================================================
dic={1:"a",2:"b",3:"c",4:"d"}
dict={i*2:j+"a" for j in dic.values()}
print(dict)
#=====================================================================
# nested dictionary n nested dictionary nested dictionary compression======

nested={1:{1:"A"},2:{2:"B"},3:{3:"C"},4:{4:"D"}}
final={k1:{k2 for (k2,v2) in v1.items()}for(k1,v1) in nested.items()}
print(final)


#==============================================================================


nested={1:{1:"A"},2:{2:"B"},3:{3:"C"},4:{4:"D"}}
final={k1:{v2 for (k2,v2) in v1.items()}for(k1,v1) in nested.items()}
print(final)

#=========================================================================
nested={1:{1:"A"},2:{2:"B"},3:{3:"C"},4:{4:"D"}}
final={k1:{v2:k2 for (k2,v2) in v1.items()}for(k1,v1) in nested.items()}
print(final)

#=============================================================================

nested={1:{1:"A"},2:{2:"B"},3:{3:"C"},4:{4:"D"}}
final={k1:{v2 for (k2,v2) in v1.items()}for (k1,v1) in nested.items()}
print(final)


#=============================================================================

def square(n):
    res=n*n
    return res
square(2)
#===================== lambda function =======================================
final=lambda x,a,e:x*a*e
print(final(2,3,4))
#=====================================================================
#Code:
# Constructing output list WITHOUT Using List comprehensions
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
output_list = []
# Using loop for constructing output list
for var in input_list:
    
    if var % 2 == 0:
        output_list.append(var)

print("Output List using for loop:", output_list)

#=====================================================================
#Code:
# Using List comprehensions for constructing output list

input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
list_using_comp = [var for var in input_list if var % 2 == 0]
print("Output List using list comprehensions:",list_using_comp)
#=========================================================================

#Constructing output list using for loop
output_list = []
for var in range(1, 10):
 output_list.append(var ** 2)

print("Output List using for loop:", output_list)

#=======================================================================
#Code:
# Constructing output list using list comprehension
list_using_comp = [var**2 for var in range(1, 10)]

print("Output List using list comprehension:",list_using_comp)

#========================================================================
#Code:
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)

#========================================================================

matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print (transpose)
#===========================================================================
#Code:
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Double each value in the dictionary
double_dict1 = {k:v*2 for (k,v) in dict1.items()}
print(double_dict1)

#======================================================================
#Code:
#Code:
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g':7}
dict1_doubleCond = {k:v for (k,v) in dict1.items() if v>2 if v%2 == 0}
print(dict1_doubleCond)
#========================================================================
#Code:
nested_dict = {'first':{'a':1}, 'second':{'b':2}, 'third':{'c':3} ,
'forth':{'d':4} }
float_dict = {outer_k: {float(inner_v) for (inner_k, inner_v) in
outer_v.items()} for (outer_k, outer_v) in nested_dict.items()}
print(float_dict)
#====================
#=====================================================

n=input("enter the value:")
for i in range(1,11):
    print("{}*{}={}".format(n,i,n*i))
       
#=============================================================================
#==================== lambda anomonoyomus function python=====================
#======= use as convience and one line function and linear fuction============
minus=lambda x,y:x-y
print(minus(2,3))    

#================= use a lambda function by sort ===========================
#key ek argument hota hai joo function koo input layta hai     
 def huz(a):
     return a[1]
     return a[0]
a=[[1,43],[98,32],[35,64]]   
a.sort(key=huz)
print(a)
#=======================================
a=[[1,43],[98,32],[35,64]]  
a.sort(key=lambda a:a[1])
print(a)
#==============================================
def sum(a,b):
    x=a+b
    return x
sum(2,3)
#============ by lambda function ======================
final=lambda a,b:a+b 
print(final(2,3))       

#=============================================================
#Q5
# filter()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = tuple((filter(lambda x: (x%2 != 0) , li)))
print(final_list)

#map()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = tuple((map(lambda x: x*2 , li)))
print(final_list)

#reduce
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print (sum)

#Q6
lst=[1,2,3,4,5,6,7,8,9,10]
no=int(input('hgjhg'))
f=list(map(lambda x:x*no ,lst ))
print(f)

print(s(lst))
  #=====================================================================
#using list compression to remember it 
#[x for x in iterable_list ]
#[x for x in iterable_list if conditional statement]
# if we want to use both conditional statement in list compresion then syntax is 
#[x if conditional_statement else statement for i in iterable]  
  list=[]
  a=[i for i in range(1,15)]
  a.append(list)
  print(a)
#==============
 final=[i for i in range(1,15)]
print(final) 
#===============
final=[i for i in range(1,15) if i%3==0]
print(final)
#================
final=[i if i%2==0 else i%3==0 for i in range(1,15,2)]
print(final)
#====================
final=final=[i if i>2 else i+1 for i in range(1,15)]
print(final)
#============= mapfuction , filterfuction and reducefunction===============
number=["1","2","3"]
for i in range(len(number)):
    number[i]=int(number[i])
number[2]=number[2]+1
print(number[i])    
#==================================
number=["1","2","3","45","6","6","6","7"]
for i in range(len(number)):
    number[i]=int(number[i])
number[4]=number[4]+1
print(number[i])    
#==========================================
list=[1,2,3,34,5,6,78]
list1=[]
for i in list:
    list1.append(i)
    x=list1
    y=str(x)
    print(list1)
print(y)  

#=============================================
 list=[1,2,3,34,5,6,78]
list1=[]
for i in list:
    list1.append(i)
    x=list1
    y=str(x)
    print(list1,end="")
print(y)  
#================================================
number=["1","2","3"]
number=list(map(int,number))
number[2]=number[2]+1
print(number[2])

#==================
#================================
#def sq(a):
    #return a*a
#num=[1,2,3,4]
#square=list(map(sq,num))
#print(square)
#=====================
#num=[1,2,3,4]
#square=(map(lambda a:a*a,num))
#print(square) 

# ===================
 def square(a):
     return a*a
 def cube(a):
     return a*a*a
 #function ka name store kerwaliya ;;;;;;;
 function=[square,cube]
 for i in range(7):
     val=list(map(lambda x:x[i],function))
     print(val)
#===============================================================
final=[i for i in range(1,10) if i%2==0]
print(final)     
#==============================================================
final=[i**2 if i>10==0 else i+1 for i in range(1,10)]
print(final)
#===============================================================
li=[1,2,3,4,5,6,7,8,9]
final_list=tuple((filter(lambda x:(x%2==0),li)))
print(final_list)
#===============================================================
x=2
final=lambda x:x**2 return x
print(final)
#============================       python compreehession      ====================================
ls=[]
for i in range(300):
    if i%3==0:
        ls.append(i)
print(ls)        
#by list compreession
ls=[i for i in range(300) if i%3==0]
print(ls)
#-----------------------------------------------------------------------------------------------
#aghr mujhy dictionary bunnaii ahii 
dict={1:"item1",2:"item2",3:"item3",4:"items4",5:"items5"}
#ek method too ya
#Aghr mayeskooo dictionary compreesion say krayoo too
dict={i:f"item{i}" for i in range(300)}
print(dict)  
#-----------------------------------------------------------
dict={i:f"item{i}" for i in range(300) if i%100==0}
print(dict)  
#------------------------------------------------------------
#Reversing a  key value pair in dictionary in dictcompression 
dict={i:f"item{i}" for i in range(300) if i%100==0}
dict={y:x for x,y in dict.items() }
print(dict) 
print(type(dict)) 
#-------------------------------------------------------------
dict1={i:f"item{i}" for i in range(300) if i%100==0}
dict2={y:x for x,y in dict1.items() }
print(dict1,"\n",dict2)  
#==============================================================================================================
# making a set compreeshion 
#---------------------------------------------------------------------------------------------------------------
dress={dress for dress in ["dress1","dress2","dress1","dress2","dress1","dress2","dress1","dress2"]}
print(dress)
print(type(dress))
#-------------------------------   Making a generator compression  ------------------------------------------------
#list is defined by ([] square brecket)
#dictionary is defined by ({} curely bracket)
#set is defined by ({} but in set object are not recouring)
#generators is defined by (() by paratheses )
evens=(i for i in range(100) if i%2==0)
print(evens)
print(type(evens))
#---------------------------------------------------------------------------------------------------------
no_of_list = int(input("How many items add in a list: "))
input_string = input("Enter a list element separated by space ")
list = input_string.split()
t = int(input("Which type of comprehension you use 1. List Comprehension 2.Dictionary Comprehension 3. Set Comprehension "))
if t==1:
    ls = [i for i in list]
    print(ls)
    print(type(ls))
elif t==2:
    dict1 = {f'item{i}': i for i in list}
    print(dict1)
    print(type(dict1))
elif t==3:
    s ={i for i in list}
    print(s)
    print(type(s))
#----------------------------------------------------------------------------------------------------------
