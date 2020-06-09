# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 15:12:56 2020

@author: 19B-125-CS
"""

#Q1
t=int(input("enter the range of the table:"))
table=[i*12 for i in range(1,t)]
table

#Q2
lst=[1,2,-4,-7]
x=[i for i in lst if i<0]
x
y=[j for j in lst if j>0]
y

#q3
j=1
final={i:j for i in range(1,101) if i>5 and i%5==0 and i%7==0}
final

#Q4
nest={1:{'burger':2},#k1 v1
      2:{'pizza':3},
      3:{'cake':4}
      }
res={k1:{v2 for (k2,v2) in v1.items()} for (k1,v1) in nest.items()}
res

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

#Q6
lst=[1,2,3,4,5,6,7,8,9,10]
no=int(input('enter the value'))
f=list(map(lambda x:x*no ,lst ))
print(f)

#    

#======================================================
list=[1,[2,3],4,[2,3,4]]
list[3][2]

add=[]
for i in range(4):
    add.append(list[i]+list[i])
print(add)
#=====================================================
#callable() things which are callable or not
class car:
    def __methods__(self):
        return x**2
car_me=car()
callable(car_me)    

#==============================
