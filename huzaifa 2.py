# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 23:26:20 2020

@author: HASSAN ENTERPRISES
"""

# creating car travel agency
#====================================
#==========
from tkinter import *
def x():
    print("It works")
root=Tk()
root.geometry("644x344")
#text for our form and pack it in our form
Label(root,text="welcome to huzaifa travels",font="comicsansms 13 bold").grid(row=0,column=3)
name=Label(root,text="name").grid(row=1,column=2)
Phone_number=Label(root,text="Phone_number").grid(row=2,column=2)
Gender=Label(root,text="Gender").grid(row=3,column=2)
Emergency_contact=Label(root,text="Emergency contact").grid(row=4,column=2)
Payment_mode=Label(root,text="payment mode").grid(row=5,column=2)
#=================================================================================================
#namevalue=stringvar()
#Phone_numbervalue=stringvar()
#Gendervalue=stringvar()
#==================================================================================================
nameentry=Entry(root)
phone_numberentry=Entry(root)
Genderentry=Entry(root)
Emergency_contactentry=Entry(root)
payment_modeentry=Entry(root)
#======================================================================================================
nameentry.grid(row=1,column=3)
phone_numberentry.grid(row=2,column=3)
Genderentry.grid(row=3,column=3)
Emergency_contactentry.grid(row=4,column=3)
payment_modeentry.grid(row=5,column=3)
#check boxxxx......................
food_service=Checkbutton(text="want you get your meal").grid(row=6,column=3)
#button and packing it and asinging and command
Button(root,text="submit to huzaifa travels",command=x).grid(row=7,column=3)
root.mainloop()



#======================================================================================================
#Accepting user input:


from tkinter import *
def x():
    print("It works")
    print(f"{nameentry.get(),phone_numberentry.get(),Genderentry.get(),Emergency_contactentry.get(),payment_modeentry.get()}")
root=Tk()
root.geometry("644x344")
#text for our form and pack it in our form
Label(root,text="welcome to huzaifa travels",font="comicsansms 13 bold").grid(row=0,column=3)
name=Label(root,text="name").grid(row=1,column=2)
Phone_number=Label(root,text="Phone_number").grid(row=2,column=2)
Gender=Label(root,text="Gender").grid(row=3,column=2)
Emergency_contact=Label(root,text="Emergency contact").grid(row=4,column=2)
Payment_mode=Label(root,text="payment mode").grid(row=5,column=2)
#=================================================================================================
#namevalue=stringvar()
#Phone_numbervalue=stringvar()
#Gendervalue=stringvar()
#==================================================================================================
nameentry=Entry(root)
phone_numberentry=Entry(root)
Genderentry=Entry(root)
Emergency_contactentry=Entry(root)
payment_modeentry=Entry(root)
#======================================================================================================
nameentry.grid(row=1,column=3)
phone_numberentry.grid(row=2,column=3)
Genderentry.grid(row=3,column=3)
Emergency_contactentry.grid(row=4,column=3)
payment_modeentry.grid(row=5,column=3)
#check boxxxx......................
food_service=Checkbutton(text="want you get your meal").grid(row=6,column=3)
#button and packing it and asinging and command
Button(root,text="submit to huzaifa travels",command=x).grid(row=7,column=3)
root.mainloop()



# CREATING A CANVAS WIDGET IN PYTHON>>>>>>>>>>>>>>>>>>>>>>>.
from tkinter import *
root=Tk()
canvas_width=800
canvas_height=400
root.geometry(f"{canvas_width}x{canvas_height}")
can_widget=Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack()
#create a line in canvas 
#can_widget.create_line(0,200,800,0,fill="blue")
#C
#create a rectangle in canvas point of cordinate is top left and bottom right ::::
#can_widget.create_rectangle(0,200,800,0,fill="blue")
# create a text in cancas::::::::::::
#can_widget.create_text(200,200,text="python",fill="red")
# creating a oval which take two coordinate and 4 value ku ka rectangle ka undher oval hai;;;;
can_widget.create_oval(200,200,400,400,fill="red")

root.mainloop()
