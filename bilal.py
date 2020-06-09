# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 02:23:30 2020

@author: HASSAN ENTERPRISES
"""
#Making a python regristration form

from tkinter import *
import tkinter as tkr
root =Tk()
root.geometry("500x500")
label=Label(root,text="regristeationform",width=20,font="bold 20")
label.place(x=90,y=53)
label1=Label(root,text="full name",width=20,font="bold 10")
label.place(x=80,y=130)
entry1=Entry(root)
entry1.place(x=240,y=130)
label2=Label(root,text="Email",width=20,font="bold 10")
label2.place(x=68,y=180)
entry2=Entry(root)
entry2.place(x=240,y=180)
label3=Label(root,text="Gender",width=20,font="bold 10")
label3.place(x=70,y=230)
entry3=Entry(root)
entry3.place(x=70,y=230)
var=tkr.IntVar()
Radiobutton(root,text="Male",padx=5,variable=var,value=1).place(x=235,y=230)
Radiobutton(root,text="Female",padx=20,variable=var,value=2).place(x=290,y=230)

label4=Label(root,text="country",width=20,font="bold 10")
label4.place(x=70,y=280)

list=["canada" ,"India","USA","Pakistan","South Africa"]
c=tkr.StringVar()
droplist=OptionMenu(root,c,*list)
droplist.config(width=15)
c.set("select your country")
droplist.place(x=240,y=280)

label5=Label(root,text="programming",width=20,font="bold 10")
label5.place(x=85,y=330)
var1=tkr.IntVar()
Checkbutton(root,text="java",variable=var1).place(x=235,y=330)
var2=tkr.IntVar()
Checkbutton(root,text="python",variable=var2).place(x=290,y=330)
Button(root,text="submit",width=20,bg="red",fg="white").place(x=180,y=380)
root.mainloop()
