# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 00:48:37 2020

@author: HASSAN ENTERPRISES
"""

import datetime
from tkinter import Tk,Label,Button,Entry
def a():
    x=datetime.date.today()
    Gst="13%"
    a=("{}\n GST : {}\n Name : {}\n Phone_entry : {}".format(x,Gst,nameentry1.get(),phoneentry2.get()))
    Label(root,text=a).grid(row=10,column=1)
def A():
    global quantityentry4,b
    b=int(quantityentry4.get())*180  
    print(b)
   
def C():
    global quantityentry5,c
    c=int(quantityentry5.get())*90
    print(c)

def E():
    global quantityentry6,d
    d=int(quantityentry6.get())*120
    print(d)
def G():
    global quantityentry7,e
    e=int(quantityentry7.get())*220
    print(e)
    
    
def z():    
    Amount=b+c+d+e
    Amount1=Amount*0.13
    A=("total amount is Rs:",Amount1)
    B=("THANKYOU FOR SHOPPING")
    Label(root,text=A).grid(row=11,column=1)
    Label(root,text=B).grid(row=12,column=1)

   


root=Tk()
x=datetime.date.today()
label_1=Label(root,text=x,font="16").grid(row=0,column=0)

label1=Label(root,text="Name:",font="16").grid(row=1,column=0)
nameentry1=Entry(master=root)
nameentry1.grid(row=1,column=1)   

label2=Label(root,text="Phone Number:",font="16").grid(row=2,column=0)
phoneentry2=Entry(root)
phoneentry2.grid(row=2,column=1)

label3=Label(root,text="List of Items:",font="l6").grid(row=4,column=0)

label4=Label(root,text="Zinger Burger:180Rs",font="l6").grid(row=5,column=0)
label_4=Label(root,text="Quantity",font="16").grid(row=5,column=1)
quantityentry4=Entry(root)
quantityentry4.grid(row=5,column=2)
button4=Button(root,text="ok",command=A).grid(row=5,column=3)

label5=Label(root,text="Chatni Roll:90Rs",font="l6").grid(row=6,column=0)
label_5=Label(root,text="Quantity",font="16").grid(row=6,column=1)
quantityentry5=Entry(root)
quantityentry5.grid(row=6,column=2)
button5=Button(root,text="ok",command=C).grid(row=6,column=3)

label6=Label(root,text="Manchorean:120Rs",font="l6").grid(row=7,column=0)
label_6=Label(root,text="Quantity",font="16").grid(row=7,column=1)
quantityentry6=Entry(root)
quantityentry6.grid(row=7,column=2)
button6=Button(root,text="ok",command=E).grid(row=7,column=3)

label7=Label(root,text="Club Sandwitch:220Rs",font="l6").grid(row=8,column=0)
label_7=Label(root,text="Quantity",font="16").grid(row=8,column=1)
quantityentry7=Entry(root)
quantityentry7.grid(row=8,column=2)
button7=Button(root,text="ok",command=G).grid(row=8,column=3)

button=Button(root,text="ok",command=a).grid(row=3,column=1)
button=Button(root,text="enter",command=z).grid(row=9,column=1)
root.mainloop()
