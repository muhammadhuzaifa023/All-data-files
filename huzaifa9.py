# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 20:35:55 2020

@author: HASSAN ENTERPRISES
"""
n=input("enter the number:")
for i in range(1,10):
    pro=n*i
    print(pro,"n","A")
    
#=======================================================================
S_P=int(input("enter the number:"))
C_P=int(input("enter the number:"))
let_profit=(S_P-C_P)
print(let_profit)    
 #======================================================================   
 
# gui with status bar ::::::

 
from tkinter import*
def upload():
     statusvar.set("busy...")
     sbar.update()
     import time
     time.sleep(1)
     statusvar.set("Ready Now")
root=Tk()
root.geometry=("455x233")
root.title("my status bar bottom at the screen")
statusvar=StringVar()
statusvar.set("Ready")
sbar=Label(root,textvariable=statusvar,relief=SUNKEN,anchor="w")
sbar.pack(side=BOTTOM,fill=X)
Button(root,text="upload",command=upload).pack()
root.mainloop() 
 
#================================================================
#More tkinter tips functiuon 
from tkinter import*
root=Tk()
root.geometry=("655x444")
root.title("more tkinter tips function")
root.wm_iconbitmap("icon.ico.png")
root.configure(background="white")
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
#using f string and destroy function::::::
print(f"{width}x{height}")
Button(text="close",command=root.destroy).pack()
root.mainloop() 


#=====================================================================
#creating a text editor::::: notepad 
from tkinter import*
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename 
import os
def newFile():
    global file
    root.title("untitled-Notepad")
    file=None
    # 1.0 ka matlabhai phali line ka phalay character say lay ker end ki line takh sb hathadoooooo
    Textarea.delete(1.0,END)
def openFile():
    global file
    file=askopenfilename(defaulttextextension="txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) +" -Notepad")
        Textarea.delete(1.0,END)
        f=open(file,"r")
        Textarea.insert(1.0,f.read())
        f.close()
def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",
                               defaulttextextension="txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            #save as a new file
            f=open(file,"w")
            file.write(Textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) +" -Notepad")
            print("File saved")
    else:
            #save the  file
            f=open(file,"w")
            file.write(Textarea.get(1.0,END))
            f.close()      
def QuitApp():
    root.destroy()
def cut():
    Textarea.event_generate(("<<Cut>>"))
def copy():
     Textarea.event_generate(("<<Copy>>"))
def paste():
     Textarea.event_generate(("<<Paste>>"))
def saveall():
     Textarea.event_generate(("<<Saveall>>"))
def about():
    showinfo("Notepad","Notepad by huzaifa")
    
    
root=Tk()
root.title("creating a text editor")
#root.wm_iconbitmap("icon.ico.png")
root.geometry=("655x444")
#adding a text area ::::
Textarea=Text(root,font="lucida 13")
File=None
#using expand true kernay sat apka text poori width lay layga 
Textarea.pack(expand=True,fill=BOTH)
#lets create a menu bar
Menubar=Menu(root)
#file menu start 
Filemenu=Menu(Menubar,tearoff=0)
# to open a new file 
Filemenu.add_command(label="New",command=newFile)

#to open a already exicting file
Filemenu.add_command(label="open",command=openFile)
#Tom save the current file 
Filemenu.add_command(label="save",command=saveFile)
Filemenu.add_separator()
Filemenu.add_command(label="Exit",command=QuitApp)
Menubar.add_cascade(label="file",menu=Filemenu)
#file menu ends
#Edit menu starts
Editmenu=Menu(Menubar,tearoff=0)
# to give a feature of cut,copy,paste
Editmenu.add_command(label="cut",command=cut)
Editmenu.add_command(label="copy",command=copy)
Editmenu.add_command(label="paste",command=paste)
Editmenu.add_command(label="save all",command=saveall)
Menubar.add_cascade(label="Edit",menu=Editmenu)
#Edit menu ends 
#Help menu starts
Helpmenu=Menu(Menubar,tearoff=0)
Helpmenu.add_command(label="About notepad",command=about)
Menubar.add_cascade(label="Help",menu=Helpmenu)
#Help menu Ends
root.config(menu=Menubar)
#adding scroll bar 
Scroll=Scrollbar(Textarea)
Scroll.pack(side=RIGHT,fill=Y)
Scroll.config(command=Textarea.yview)
Textarea.config(yscrollcommand=Scroll.set)
root.mainloop() 

  