# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 11:59:31 2020

@author: HASSAN ENTERPRISES
"""
import datetime
from tkinter import*
root=Tk()
x=datetime.date.today()
label_1=Label(root,text=x).grid(row=0,column=0)

label1=Label(root,text="Name:",font="lacida 16 bold").grid(row=1,column=0)
entry=Entry(master=root).grid(row=1,column=1)

label2=Label(root,text="Phone Number:",font="lacida 16 bold").grid(row=2,column=0)
entry=Entry(master=root).grid(row=2,column=1)

label3=Label(root,text="List of Items:",font="lacida 16 bold").grid(row=3,columnspan=5)

label4=Label(root,text="Zinger Burger:180Rs",font="lacida 16 bold").grid(row=4,column=0)
label5=Label(root,text="beef Burger:200Rs",font="lacida 16 bold").grid(row=5,column=0)
label6=Label(root,text="Chatni Roll:90Rs",font="lacida 16 bold").grid(row=6,column=0)
label7=Label(root,text="Chinese rice:220Rs",font="lacida 16 bold").grid(row=7,column=0)
label8=Label(root,text="Enter the burger you want:",font="lacida 16 bold").grid(row=8,column=0)
entry_1=Entry(master=root).grid(row=8,column=1)

label9=Label(root,text="Price of the burger:",font="lacida 16 bold").grid(row=9,column=0)
entry_2=Entry(master=root).grid(row=9,column=1)

label10=Label(root,text="GST=13%",font="lacida 16 bold").grid(row=10,column=0)


root.mainloop()