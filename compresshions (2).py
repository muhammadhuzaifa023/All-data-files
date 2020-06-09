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
            
n=int(input("enter the value;"))
for j in range(list):
    z=j*n
    if z<144:
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

#=======================================================================

