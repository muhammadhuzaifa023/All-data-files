# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 17:18:16 2020

@author: HASSAN ENTERPRISES
"""

numlist1=[1,2,3,4,5,6]
numlist2=[2,3,4,5,6,7]
add=[]
sub=[]
multi=[]
div=[]
mod=[]
expo=[]
for i in range(6):
    add.append(numlist1[i]+numlist2[i])
    sub.append(numlist1[i]-numlist2[i])
    multi.append(numlist1[i]*numlist2[i])
    div.append(numlist1[i]/numlist2[i])
    mod.append(numlist1[i]%numlist2[i])
    expo.append(numlist1[i]**numlist2[i])
print("the list of item after addition is equal to=",add)
print("the list of item after subtraction is equal to=",sub)
print("the list of item after multiply is equal to=",multi)
print("the list of item after division is equal to=",div)
print("the list of item after module is equal to=",mod)
print("the list of item after exponent is equal to=",expo)
    
    
#=========================================================================
list_of_fruit=["apple","banana","mangoes","pineapple","watermillion"]
list_of_fruit.count()        



#============================================================================
print("a","b","c",sep="sep")
 #===========================================================================
 #list manupulation
list=[1,2,3,44,5,56,7,]
list.append(34)
list     

list=[1,2,3,44,5,56,7,]# value error because their is no 34 it the list 
list.remove(34)
list     
#====================================================
#remove method
list=[1,2,3,44,5,56,7,]# value error because their is no 34 it the list 
list.remove(44)
list

#=========================================================
# insert Method:
list=[1,2,3,44,5,56,7,]# value error because their is no 34 it the list 
list.insert(2,34)
list
#===========================================================
# Index method
list=[1,2,3,44,5,56,7,]
#list[3]
print(list[3])

#==========================================================
#count method:
list=[1,2,3,44,5,56,7,44]
list.count(44)
#==========================================================

#list operation : sort(),reverse(),delete(),append(),replace(old,new),remove(old,new)



#==============================================================
#dialog boxess
from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
def myfunction():
    print("my name is huzaifa")
def help():
    print("I will help you")
    tmsg.showinfo(title="bs",message="huzaifa will help you in making this gui")
    # print give me it return value;;;;;;;
    #print(a)
def rate():
    print("rate us")
    value=tmsg.askquestion(title="was your experience good",message="are you happy to use this gui of python" )
    #print(value)
    if value=="yes":
        msg="rate us on app store plz"
    else:
        msg="tell me what will wrong we will correct it soon"
        tmsg.showinfo("Experience",msg)
def anus():
    ans=tmsg.askretrycancel(title="anus say dosti kerlooo",msg="sorry anus nahi bunnay ga apka dost")
    if ans:
        print("retry kernay pr bhi kuch nh hooga")
    else:
        print("bht acha kiya werna dostii kerlaytay too bhi kuch fadiya na tha")
#use these to create non drop down menu    
root.geometry("733x566")
root.title("creating a submenu")
#mymenu=Menu(root)
#mymenu.add_command(label="File",command=myfunction)
#in built commad quit
#mymenu.add_command(label="exit",command=quit)
#for packing a menu we here config
#root.config(menu=mymenu)
yourmenu=Menu(root)
m2=Menu(yourmenu,tearoff=0)
m2.add_command(label="undo",command=myfunction)
m2.add_separator()
m2.add_command(label="redo",command=myfunction)
m2.add_command(label="cut",command=myfunction)
m2.add_command(label="copy",command=myfunction)
root.config(menu=yourmenu)
yourmenu.add_cascade(label="Edit",menu=m2)

#=====================================================
m1=Menu(yourmenu,tearoff=0)
m1.add_command(label="save",command=myfunction)
m1.add_separator()
m1.add_command(label="save all",command=myfunction)
m1.add_command(label="save as",command=myfunction)
m1.add_command(label="print",command=myfunction)
root.config(menu=yourmenu)
yourmenu.add_cascade(label="file",menu=m1)
#======================================================
m3=Menu(yourmenu,tearoff=0)
m3.add_command(label="Find text ",command=myfunction)
m3.add_separator()
m3.add_command(label="Find next",command=myfunction)
m3.add_command(label="Find previous",command=myfunction)
m3.add_command(label="Replace text",command=myfunction)
root.config(menu=yourmenu)
yourmenu.add_cascade(label="Search",menu=m3)


m4=Menu(yourmenu,tearoff=0)
m4.add_command(label="show me that you will help me ",command=help)
m4.add_command(label="rate us ",command=rate)
m4.add_command(label="anasbest ",command=anus)
#m4.add_separator()
#m4.add_command(label="Find next",command=myfunction)
#m4.add_command(label="Find previous",command=myfunction)
#m4.add_command(label="Replace text",command=myfunction)
root.config(menu=yourmenu)
yourmenu.add_cascade(label="help",menu=m4)




root.mainloop()