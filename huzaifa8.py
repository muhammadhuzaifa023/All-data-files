# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 22:50:24 2020

@author: HASSAN ENTERPRISES
"""
#question 2:
list=[-1,2,-3,-4,5,6,7,10,23]
pos,neg=[i for i in list if i>0],[j for j in list if j<0]
print(pos,neg)    


#==================================================================
#question 1
#list=[]
x,y=[i for i in range(1,145)],[j for j in range(1,i) if y<=144 ]
y=j*n

print(x,y)
x.append(i)
print(x)
n=int(input("enter the value:"))
#for j in range(1,i):
#y=j*n
#if y<=144:
   # print(y)
#=========================================================================
#question 3:
x,y=[i for  i in range(1,101) if i>5 and i%5==0],[j for  j in range(1,101) if j>5 and j%7==0]
print(x,y)
#==========================================================================
#question 3:
final=[i for i in range(1,101) if i>5 and i%5==0 or i%7==0]
final

#question 4:
nested={1:{1:"A"},2:{2:"B"},3:{3:"C"},4:{4:"D"}}
final={k1:{k2:v2 for (k2,v2) in v1.items()}for(k1,v1) in nested.items()}
print(final)
#==========================================================================
nested={1:{1:"A"},2:{2:"B"},3:{3:"C"},4:{4:"D"}}
final={k1:{k2 for (k2,v2) in v1.items()}for(k1,v1) in nested.items()}
print(final)
#=============================================================================
nested={1:{1:"A"},2:{2:"B"},3:{3:"C"},4:{4:"D"}}
final={k1:{v2 for (k2,v2) in v1.items()}for(k1,v1) in nested.items()}
print(final)
#=============================================================================
#========= filter,reduce,map================================================
#question 5
#Q5
# filter()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_li=list(filter(lambda x: (x%2!=0), li))
print(final_li)
#map()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = (map(lambda x: x*2 , li))
print(final_list)

#reduce
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print (sum)

#question 6
lst=[1,2,3,4,5,6,7,8,9,10]
no=int(input('enter the value'))
f=list(map(lambda x:x*no ,lst ))
print(f)

print((lst))


    

