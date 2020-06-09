# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 15:46:19 2020

@author: HASSAN ENTERPRISES
"""

# creating a menu and  submenu in tkinter 
#============================================================
from tkinter import *
root=Tk()
def myfunction():
    print("my name is huzaifa")
    
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


root.mainloop()