# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 12:58:37 2019

@author: Hajra Ahmed
"""
"""PROGRAM 1"""# CREATE PROGRAM TO SHOW A LABEL
import tkinter
window=tkinter.Tk()
window.title('first program')
tkinter.Label(window,text='its just label').pack()
window.mainloop()
"""PROGRAM 2""" #CREATE PROGRAM TO MAKE FRAMES AND LABELS IN IT (USE OF SIDE IN PACK(side=top/bottom/left/right))
import tkinter
window=tkinter.Tk()
window.title('second program')
x_frame=tkinter.Frame(window).pack(side='top')
y_frame=tkinter.Frame(window).pack(side='bottom')

#if i redefine pack in labels then upper value will be overwritten
#default pack side =top can be bottom,left,right as well
tkinter.Label(x_frame,text='horizontal frame1',bg='red').pack(side='left')
tkinter.Label(x_frame,text='horizontal frame2',bg='red').pack(side='right')

tkinter.Label(y_frame,text='vertical frame1',bg='yellow').pack(side='left')
tkinter.Label(y_frame,text='vertical frame2',bg='yellow').pack(side='right')

tkinter.mainloop()

"""PROGRAM 3"""# CREATE PROGRAM FOR MAKING DIFFERENT LABELS AND USE OF FILL IN PACK(fill=x/y)
import tkinter
window=tkinter.Tk()
window.title("Program 3")
tkinter.Label(window,text='fill x',bg='red').pack(side='bottom',fill='x') #fill x from side=top/bottom
tkinter.Label(window,text='fill y',bg='yellow').pack(side='left',fill='y') #fill y from side=left/right
window.mainloop()

"""PROGRAM 4"""# USE GRID ,MAKE LOGIN WINDOW WITH INPUTS AND CHECKBOXES
import tkinter
window=tkinter.Tk()
window.title("prog 4")
tkinter.Label(window,text="Username ").grid(padx=10,pady=10,row=0,column=0)
tkinter.Entry(window).grid(row=0,column=1)

tkinter.Label(window,text="password ").grid(row=1,column=0)
tkinter.Entry(window).grid(row=1,column=1)
#can have separate labrel with checkbox and can give in chkbox as well
tkinter.Checkbutton(window,text="keep me logged in  ").grid(row=2,columnspan=2)
window.mainloop()

"""PROGRAM 5"""#writing program to execute a fn on event click

import tkinter
window=tkinter.Tk()
def greeting():
    tkinter.Label(window,text='Hello Hw are you all???').pack()
    no=5
    print(no)
    return no

tkinter.Button(window,command=greeting,text='Click it!',bg='grey',fg='black').pack()

window.mainloop()

"""PROGRAM 6"""#BINDING METHOD TO EVENT CLICK OR MOUSE CAPTURE VIA <BUTTON-1>
import tkinter
window=tkinter.Tk()
window.title("prog 6")
def left_clk(event):
    tkinter.Label(window,text='its left click',fg='black').pack()
def right_clk(event):
    tkinter.Label(window,text='its right click',fg='black').pack()
def Middle_clk(event):
    tkinter.Label(window,text='its middle click',fg='black').pack()
window.bind('<Button-1>',left_clk)
window.bind('<Button-3>',right_clk)
window.bind('<Button-2>',Middle_clk)
window.mainloop()
"""PROGRAM 7""" #MAKING CLASSES,METHODS AND GUI
#When you use self.quit() the python interpreter closes down without the tkinter application bieng closed . 

class MyGUI:
    def __init__(self,window):
        self.open_btn=tkinter.Button(window,text='OPEN IT!',command = self.say_greeting).pack()
        self.close_btn=tkinter.Button(window,text='CLOSE IT!',command = window.destroy).pack()
        
    def say_greeting(self):
        tkinter.Label(window,text='WELCOME TO USMAN INSTITUTE OF TECHNOLOGY!!!').pack()


import tkinter
window=tkinter.Tk()
mygui=MyGUI(window)
window.mainloop()        
    
"""PROGRAM 8"""
import tkinter
window=tkinter.Tk()
window.title('creating menus')
def Menu():
    pass
#create root menu
root=tkinter.Menu(window)
#configure it
window.config(menu=root)
#create submenu in root 
file=tkinter.Menu(root)

root.add_cascade(label='FILE',menu=file)
    
file.add_command(label='New File',command=Menu)
file.add_command(label='Open File',command=Menu)
file.add_separator()
file.add_command(label='Exit',command=window.destroy)

edit=tkinter.Menu(root)
root.add_cascade(label='EDIT',menu=edit)
edit.add_command(label='Undo',command=Menu)
edit.add_command(label='Redo',command=Menu)
edit.add_separator()
edit.add_command(label='Exit',command=window.destroy)
window.mainloop()
"""PRACTICE"""
import tkinter
window=tkinter.Tk()
window.title('menus')
def Menu():
    tkinter.Label(window,text='in Menu').pack()
root=tkinter.Menu(window)
window.config(menu=root)

file=tkinter.Menu(root)
root.add_cascade(label='FILE',menu=file)
file.add_command(label='New file',command=Menu)
file.add_command(label='Open file',command=Menu)
file.add_command(label='Close file',command=Menu)
file.add_separator()

edit=tkinter.Menu(root)
root.add_cascade(label='EDIT',menu=edit)
edit.add_command(label='Undo',command=Menu)
edit.add_command(label='redo',command=Menu)
edit.add_separator()
edit.add_command(label='exit',command=window.destroy)
window.mainloop()

"""PROGRAM 9"""#CREATE MSG BOX OR QUESTION BOX VIA MSG BOX
import tkinter
import tkinter.messagebox

window=tkinter.Tk()
window.title('message box')
tkinter.messagebox.showinfo('alert box','This is just an alert box')
response=tkinter.messagebox.askquestion('question','do you like python???')

if response == 'yes':
    tkinter.Label(window,text='yes I do!').pack()
else:
    tkinter.Label(window,text='No I don\'t like python !').pack()

window.mainloop()
"""ROGRAM 10""" #CANVAS
import tkinter
window=tkinter.Tk()
window.title('drawing in canvas')
canvas = tkinter.Canvas(window,width=500,height=500)
canvas.pack()
line1=canvas.create_line(30,30,50,50,fill='red') #xi,yi,xf,yf,color 
rect1=canvas.create_rectangle(200,230,100,10,fill='grey')#xi,yi,width,height,fill
canvas.delete(line1)
#or canvas.delete(tkinter.All)
window.mainloop()
"""PROGRAM 11"""#INCLUDING IMAGE
import tkinter
from tkinter import *
window=tkinter.Tk()
window.title('input image')
icon=tkinter.PhotoImage(file="download.png")
l=tkinter.Label(window,image=icon)
l.pack()
window.mainloop()




















