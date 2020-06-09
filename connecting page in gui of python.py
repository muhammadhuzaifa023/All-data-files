# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 00:02:50 2020

@author: HASSAN ENTERPRISES
"""

from tkinter import *
root=Tk()
root.geometry("425x280")
def Login():
    F2=Frame() 
    F2.place(x=0,y=0,width="425",height="280")
    e1=Entry(F2)
    e1.pack()
    e2=Entry(F2)
    e2.pack()
    b2=Button(F2,text="yes It me")
    b2.pack()
F1=Frame() 
F1.place(x=0,y=0,width="425",height="280")#ya pr humnay width or height woohi diya haiii jooo geometry may diya haiii   
b1=Button(F1,text="click It " ,command=Login)
b1.pack()
root.mainloop()


#---------------------------------------------------------------------------------------------------------------

from tkinter import *
root=Tk()
root.geometry("425x280")
def Login():
    F2=Frame() 
    F2.place(x=0,y=0,width="425",height="280")
    e1=Entry(F2)
    e1.pack()
    e2=Entry(F2)
    e2.pack()
    b2=Button(F2,text="I want to go on previous page",command=home)
    b2.pack()
    b3=Button(F2,text="login")
    b3.pack()
def Regrister():
    F3=Frame() 
    F3.place(x=0,y=0,width="425",height="280")
    e1=Entry(F3)
    e1.pack()
    e2=Entry(F3)
    e2.pack()
    e3=Entry(F3)
    e3.pack()
    b2=Button(F3,text="Back",command=home)
    b2.pack()
    b3=Button(F3,text="I want to go on previous page")
    b3.pack()
    
def home():    
    F1=Frame() 
    F1.place(x=0,y=0,width="425",height="280")#ya pr humnay width or height woohi diya haiii jooo geometry may diya haiii   
    b1=Button(F1,text="click It " ,command=Login)
    b1.pack()
    b2=Button(F1,text="Regrister",command=Regrister)
    b2.pack()
home()    
root.mainloop()
#------------------------------------------------------------------------------------------------------------
from tkinter import *
root=Tk()
root.geometry("425x350")
def Login():
    F2=Frame() 
    F2.place(x=0,y=0,width="425",height="350")
    u3=Label(F2,text="Welcomr to our page")
    u3.grid(row=0,column=2)
    u1=Label(F2,text="Enter your first name:")
    u1.grid(row=4,column=2)
    e1=Entry(F2)
    e1.grid(row=4,column=3)
    u2=Label(F2,text="Enter Your Passord:")
    u2.grid(row=5,column=2)
    e2=Entry(F2)
    e2.grid(row=5,column=3)
    b2=Button(F2,text="<--",command=home)
    b2.grid(row=0,column=0)
    b3=Button(F2,text="login")
    b3.grid(row=8,column=3)
def Regrister():
    F3=Frame() 
    F3.place(x=0,y=0,width="425",height="350")
    e1=Entry(F3)
    e1.pack()
    e2=Entry(F3)
    e2.pack()
    e3=Entry(F3)
    e3.pack()
    b2=Button(F3,text="Back",command=home)
    b2.pack()
    b3=Button(F3,text="I want to go on previous page")
    b3.pack()
    
def home():    
    F1=Frame() 
    F1.place(x=0,y=0,width="425",height="350")#ya pr humnay width or height woohi diya haiii jooo geometry may diya haiii   
    b1=Button(F1,text="click It " ,command=Login)
    b1.place(x=100,y=50,width=80,height=40)
    b2=Button(F1,text="Regrister",command=Regrister)
    b2.place(x=200,y=50,width=80,height=40)
home()    
root.mainloop()
