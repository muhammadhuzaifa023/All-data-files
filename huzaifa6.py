# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 02:20:52 2020

@author: HASSAN ENTERPRISES
"""

# creating a slider in python by Scalewidget
from tkinter import *
import tkinter.messagebox as tmsg
#import tkinter as tk
def dollars():
    print(f"we have credited\t{myslider1.get()}\tdollars to your bank account")
    tmsg.showinfo(f"we have credited\t{myslider1.get()}\tdollars to your bank account")
root=Tk()
root.title("creating a slider")
#myslider1=Scale(root,from_=0,to=100,resolution=1,orient=HORIZONTAL)
##myslider2=Scale(root,from_=0,to=100,resolution=1)
#myslider2.pack()
Label(root,text="how many dollars do you want").pack()
#myslider1=Scale(root,from_=0,to=100,resolution=1,orient=HORIZONTAL)
#myslider1.set(34)
myslider1=Scale(root,from_=0,to=100,resolution=1,orient=HORIZONTAL,tickinterval=5)
myslider1.pack()
Button(root,text="get your dollar payment",command=dollars).pack()
root.mainloop() 


#=========================================================================
#question 1
#creating a gui of stationary shop:
from tkinter import *
def click_me():
    print(c.get())

    
root=Tk()
root.title("creating a gui of stationary shop")
c=StringVar()
checkentry1=Checkbutton(root,text="pensil",variable=c,offvalue="unchecked",onvalue="checked")
checkentry1.pack()
Button(root,text="Enter",command=click_me).pack()
root.mainloop() 
#================================================================================================
#question2
from tkinter import *
def click_me():
    print(c.get())

    
root=Tk()
root.title("creating a gui of stationary shop")
c=IntVar()
checkentry1=Checkbutton(root,text="pensil c",variable=c)
checkentry1.pack()

Button(root,text="Enter",command=click_me).pack()
root.mainloop() 
#====================================================================================================
#question 3
from tkinter import *
def click_me():
    
   print("pensil has been ",c.get())
   print("rubber has been ",i.get())
   print("pen has been",z.get())
    



root=Tk()
root.title("creating a gui of stationary shop")
c=StringVar()
checkentry1=Checkbutton(root,text="pensil",variable=c,offvalue="unchecked",onvalue="checked")
checkentry1.grid(row=0,column=0)

i=StringVar()
checkentry2=Checkbutton(root,text="rubber ",variable=i,offvalue="unchecked",onvalue="checked")
checkentry2.grid(row=1,column=0)

z=StringVar()
checkentry3=Checkbutton(root,text="pen ",variable=z,offvalue="unchecked",onvalue="checked")
checkentry3.grid(row=2,column=0)


label1=Label(root,text="Quantity").grid(row=1,column=2)
label1=Entry(root).grid(row=1,column=3)
        

Button(root,text="Enter",command=click_me).grid(row=4,column=2)
root.mainloop()
#===================================================================================================
#Question 4
from tkinter import *
def click_me():
    global labelentry1,q,v,w,Amount
    q=int(labelentry1.get())*c.get()*10
    v=int(labelentry1.get())*i.get()*5
    w=int(labelentry1.get())*z.get()*15
    Amount=q+v+w
    print(Amount)
    



root=Tk()
root.title("creating a gui of stationary shop")
c=IntVar()
checkentry1=Checkbutton(root,text="pensil",variable=c)
checkentry1.grid(row=0,column=0)

i=IntVar()
checkentry2=Checkbutton(root,text="rubber ",variable=i)
checkentry2.grid(row=1,column=0)

z=IntVar()
checkentry3=Checkbutton(root,text="pen ",variable=z)
checkentry3.grid(row=2,column=0)


label1=Label(root,text="Quantity").grid(row=1,column=2)
labelentry1=Entry(root)
labelentry1.grid(row=1,column=3)
        

Button(root,text="Enter",command=click_me).grid(row=4,column=2)
root.mainloop()

#=======================================================================================
#question 5

from tkinter import *
def click_me():
    global labelentry1,q,v,w,Amount#labelentry2,labelentry3
    q=int(labelentry1.get())*c.get()*10
    v=int(labelentry1.get())*i.get()*5
    w=int(labelentry1.get())*z.get()*15
    Amount=q+v+w
    Label(root,text=Amount).grid(row=5,column=2)
    B=("THANKYOU FOR SHOPPING")
    Label(root,text=B).grid(row=6,column=2) 



root=Tk()
root.title("creating a gui of stationary shop")
c=IntVar()
checkentry1=Checkbutton(root,text="pensil",variable=c)
checkentry1.grid(row=0,column=0)

i=IntVar()
checkentry2=Checkbutton(root,text="rubber ",variable=i)
checkentry2.grid(row=1,column=0)

z=IntVar()
checkentry3=Checkbutton(root,text="pen ",variable=z)
checkentry3.grid(row=2,column=0)


label1=Label(root,text="Quantity").grid(row=1,column=2)
labelentry1=Entry(root)
labelentry1.grid(row=1,column=3)

#label2=Label(root,text="Quantity").grid(row=0,column=2)
#labelentry2=Entry(root)
#labelentry2.grid(row=0,column=3)     

#label3=Label(root,text="Quantity").grid(row=2,column=2)   
#labelentry3=Entry(root)
#labelentry3.grid(row=2,column=3)

Button(root,text="Enter",command=click_me).grid(row=4,column=2)
root.mainloop()

#======================================================================
print('\\\')
print('\\\\')
#==============================================================
print("\\\")
print("\\\\")
#===============================================================


class car:
    def __init__(self,wheel,model,engine):
        self.wheel=wheel
        self.model=model
        self.engine=engine
    def huz(self):
         return ("wheel of the car is {},model{},engine number is {}".format(self.wheel,self.model,self.engine))
                 
x=car("Black","2019","VXR")
print(x.huz())


#======================================================================
class employee:
    no_of_leaves=8
    pass
#huzaifa is an object of employeee
huzaifa=employee()
#similarly bilal is an object of employee
bilal=employee()
#here we assigning a instance variable
huzaifa.name="huzi"
bilal.name="billliii"
print(huzaifa.name,",",bilal.name)
employee.no_of_leaves=9
print(employee.__dict__)

#=====================================================================
#reversed a number by for loop:
def reverse(string):
    reversed_string=""
    for i in string:
        reversed_string=i+reversed_string
    print("reversed_string",reversed_string)
string=input("enter the string:")
print("reversed string is:" ,string)    
reverse(string)

#===================== +creating a bubble sort algorithms +==================
#starting with the first (index=O) compare the next element with the current element in the list 
# if the current element is greater than the next element of the list swap them
# if the current element is less than thew next element move to the next elewment.Repeat next one
# accending algorithum
list=[2,4,8,56,45,65,20] 
#for i in range(len(list)-1):
    #if list[i]>list[i+1]:
        # swapping done here
        #list[i],list[i+1]=list[i+1],list[i]
for j in range(len(list)-1):
    for i in range(len(list)-1-j):
       if list[i]>list[i+1]:
        # swapping done here
        list[i],list[i+1]=list[i+1],list[i]
        print(list)
       else:
           print(list)
    print()
        
print("sorted list:",list)        
#desending algorithum:
list=[2,4,8,56,45,65,20] 
#for i in range(len(list)-1):
    #if list[i]>list[i+1]:
        # swapping done here
        #list[i],list[i+1]=list[i+1],list[i]
for j in range(len(list)-1):
    for i in range(len(list)-1):
       if list[i]<list[i+1]:
        # swapping done here
        list[i],list[i+1]=list[i+1],list[i]
    
        
print("sorted list:",list)        