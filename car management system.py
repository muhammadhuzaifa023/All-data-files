# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 02:27:33 2020

@author: HASSAN ENTERPRISES
"""
from tkinter import *
import tkinter.messagebox
from tkinter import messagebox
import random
#import datetime
##from tkinter import ttk
root=Tk()
root.geometry("1350x700+0+0")
root.title("car management system") 
vr1=IntVar()
vr2=IntVar()
vr3=IntVar()
vr4=IntVar()
vr5=IntVar()
vr6=IntVar()
vr7=IntVar()
vr8=IntVar()
#================================================================================================================================
customerId=StringVar()
numberofdays=StringVar()
dayrented=StringVar()
invoice=StringVar()
discount=StringVar()
total=StringVar()
enginesize=StringVar()
style=StringVar()
regristatedyear=StringVar()
classId=StringVar()
cardescription=StringVar()
milesbefore=StringVar()
milesafter=StringVar()
makes=StringVar()
model=StringVar()
enginemake=StringVar()
car_color=StringVar()
car_insurance=StringVar()
customer=StringVar()
title=StringVar()
firstName=StringVar()
surname=StringVar()
street=StringVar()
area=StringVar()
postcode=StringVar()
licence=StringVar()
issueDate=StringVar()
dailyrentealdate=StringVar()  
regristerno=StringVar()
issueby=StringVar()
  
def exit():
    iexit=tkinter.messagebox.askyesno("car management system","confirm if you want to exit")
    if iexit>0:
        root.destroy()
        return

def total():
    Noofday=float(numberofdays.get())
    Cardiscount=float(discount.get())
    DailyRate=float(dailyrentealdate.get())
    
    RentalCost=(((Noofday * DailyRate)* Cardiscount)/100)
    
    CostofRental="Rs",(RentalCost+(Noofday+DailyRate))
    total.set(CostofRental)
    #==================================================================
    ID=random.randint(51,95)
    randomID=(ID)
    customerId.set("CAR"+randomID)
    #=================================================================
    Inv=random.randint(15,112)
    InvID=str(Inv)
    invoice.set("INV"+InvID)
#===========================================================================================================================  
def reset():
    vr1.set(0)
    vr2.set(0)
    vr3.set(0)
    vr4.set(0)
    vr5.set(0)
    vr6.set(0)
    vr7.set(0)    
    vr8.set(0)
    #==============================================================================================================
    customerId.set("")
    numberofdays.set("")
    dayrented.set("")
    invoice.set("")
    discount.set("")
    total.set("")
    enginesize.set("")
    style.set("")
    regristatedyear.set("")
    classId.set("")
    cardescription.set("")
    milesbefore.set("")
    milesafter.set("")
    makes.set("")
    model.set("")
    enginemake.set("")
    car_color.set("")
    car_insurance.set("")
    customer.set("")
    title.set("")
    firstName.set("")
    surname.set("")
    street.set("")
    area.set("")
    postcode.set("")
    licence.set("")
    issueDate.set("")
    dailyrentealdate.set("")
    issueby.set("")
    regristerno.set("")
    txtRecepit.delete("1.0",END)
#=======================================================================================================================    
    








Leftframe=Frame(root,width=1000,height=700,bd=8,relief="raise")
Leftframe.pack(side="left")
Rightframe=Frame(root,width=350,height=700,bd=8,relief="raise")
Rightframe.pack(side="right")

Leftframe1=Frame(Leftframe,width=1000,height=225,bd=8,relief="raise")
Leftframe1.pack(side="top")
#========================================================================================================
Leftframe2=Frame(Leftframe,width=1000,height=225,bd=8,relief="raise")
Leftframe2.pack(side="top")
#=======================================================================================================
Leftframe3=Frame(Leftframe,width=1000,height=100,bd=8,relief="raise")
Leftframe3.pack(side="top")
#=======================================================================================================
Leftframe4=Frame(Leftframe,width=1000,height=100,bd=8,relief="raise")
Leftframe4.pack(side="top")
#=======================================================================================================
Rightframe1=Frame(Rightframe,width=350,height=325,bd=8,relief="raise")
Rightframe1.pack(side="top")
#======================================================================================================
RightFrame2=Frame(Rightframe,width=350,height=325,bd=8,relief="raise")
RightFrame2.pack(side="bottom")
#=========================================================================================================
txtRecepit=Text(RightFrame2,height=16,width=34,bd=8,font=("arial",12,"bold"))
txtRecepit.grid(row=0,column=0)
#==========================================================================================================
CustomerId=Label(Leftframe3,font=("arial",10,"bold"),text="Customer Id",bd=8)
CustomerId.grid(row=0,column=0,sticky="w")
CustomerId=Entry(Leftframe3,font=("arial",10,"bold"),bd=8,width=31,textvariable=customerId)
CustomerId.grid(row=0,column=1)
#============================================================================================================
Numberofdays=Label(Leftframe3,font=("arial",10,"bold"),text="Number of days",bd=8)
Numberofdays.grid(row=1,column=0,sticky="w")
Numberofdays=Entry(Leftframe3,font=("arial",10,"bold"),bd=8,width=31,textvariable=numberofdays)
Numberofdays.grid(row=1,column=1)
#=============================================================================================================
DayRented=Label(Leftframe3,font=("arial",10,"bold"),text="Day Rented",bd=8)
DayRented.grid(row=0,column=2,sticky="w")
DayRented=Entry(Leftframe3,font=("arial",10,"bold"),bd=8,width=31,textvariable=dayrented)
DayRented.grid(row=0,column=3)
#==============================================================================================================
Invoice=Label(Leftframe3,font=("arial",10,"bold"),text="Invoice",bd=8)
Invoice.grid(row=1,column=2,sticky="w")
Invoice=Entry(Leftframe3,font=("arial",10,"bold"),bd=8,width=31,textvariable=invoice)
Invoice.grid(row=1,column=3)
#=================================================================================================================
Discount=Label(Leftframe3,font=("arial",10,"bold"),text="Discount",bd=8)
Discount.grid(row=0,column=4,sticky="w")
Discount=Entry(Leftframe3,font=("arial",10,"bold"),bd=8,width=31,textvariable=discount)
Discount.grid(row=0,column=5)
#=====================================================================================================================
Total=Label(Leftframe3,font=("arial",10,"bold"),text="Total",bd=8)
Total.grid(row=1,column=4,sticky="w")
Total=Entry(Leftframe3,font=("arial",10,"bold"),bd=8,width=31,textvariable=total)
Total.grid(row=1,column=5)
#======================================================================================================================
Enginesize=Label(Leftframe2,font=("arial",10,"bold"),text="Engine Size",bd=8)
Enginesize.grid(row=0,column=0,sticky="w")
Enginesize=Entry(Leftframe2,font=("arial",10,"bold"),bd=8,width=31,textvariable=enginesize)
Enginesize.grid(row=0,column=1)
#=======================================================================================================================
Style=Label(Leftframe2,font=("arial",10,"bold"),text="Style",bd=8)
Style.grid(row=0,column=2,sticky="w")
Style=Entry(Leftframe2,font=("arial",10,"bold"),bd=8,width=31,textvariable=style)
Style.grid(row=0,column=3)
#==========================================================================================================================
Regristedyear=Label(Leftframe2,font=("arial",10,"bold"),text="Regristerd Year",bd=8)
Regristedyear.grid(row=0,column=4,sticky="w")
Regristedyear=Entry(Leftframe2,font=("arial",10,"bold"),bd=8,width=31,textvariable=regristatedyear)
Regristedyear.grid(row=0,column=5)
#===============================================================================================================================
ClassId=Label(Leftframe2,font=("arial",10,"bold"),text="ClassId",bd=8)
ClassId.grid(row=1,column=0,sticky="w")
ClassId=Entry(Leftframe2,font=("arial",10,"bold"),bd=8,width=31,textvariable=classId)
ClassId.grid(row=1,column=1)
#=============================================================================================================================
Cardescription=Label(Leftframe2,font=("arial",10,"bold"),text="Cars Description",bd=8)
Cardescription.grid(row=1,column=2,sticky="w")
Cardescription=Entry(Leftframe2,font=("arial",10,"bold"),bd=8,width=31,textvariable=cardescription)
Cardescription.grid(row=1,column=3)
#=============================================================================================================================
Milesbefore=Label(Leftframe2,font=("arial",10,"bold"),text="Miles_Before",bd=8)
Milesbefore.grid(row=1,column=4,sticky="w")
Milesbefore=Entry(Leftframe2,font=("arial",10,"bold"),bd=8,width=31,textvariable=milesbefore)
Milesbefore.grid(row=1,column=5)





#=============================================================================================================================
Milesafter=Label(Leftframe2,font=("arial",10,"bold"),text="Mile_sAfter",bd=8)
Milesafter.grid(row=2,column=0,sticky="w")
Milesafter=Entry(Leftframe2,font=("arial",10,"bold"),bd=8,width=31,textvariable=milesafter)
Milesafter.grid(row=2,column=1)
#============================================================================================================================
Makes=Label(Leftframe2,font=("arial",10,"bold"),text="Makes",bd=8)
Makes.grid(row=2,column=2,sticky="w")
Makes=Entry(Leftframe2,font=("arial",10,"bold"),bd=8,width=31,textvariable=makes)
Makes.grid(row=2,column=3)
#============================================================================================================================
Model=Label(Leftframe2,font=("arial",10,"bold"),text="Model",bd=8)
Model.grid(row=2,column=4,sticky="w")
Model=Entry(Leftframe2,font=("arial",10,"bold"),bd=8,width=31,textvariable=model)
Model.grid(row=2,column=5)
#============================================================================================================================
Enginemake=Label(Leftframe2,font=("arial",10,"bold"),text="Engine_Make",bd=8)
Enginemake.grid(row=3,column=0,sticky="w")
Enginemake=Entry(Leftframe2,font=("arial",10,"bold"),bd=8,width=31,textvariable=enginemake)
Enginemake.grid(row=3,column=1)
#===================================================================================================================================
Car_color=Label(Leftframe2,font=("arial",10,"bold"),text="car_color",bd=8)
Car_color.grid(row=3,column=2,sticky="w")
Car_color=Entry(Leftframe2,font=("arial",10,"bold"),bd=8,width=31,textvariable=car_color)
Car_color.grid(row=3,column=3)
#==================================================================================================================================
Car_insurance=Label(Leftframe2,font=("arial",10,"bold"),text="car_Insurance",bd=8)
Car_insurance.grid(row=3,column=4,sticky="w")
Car_insurance=Entry(Leftframe2,font=("arial",10,"bold"),bd=8,width=31,textvariable=car_insurance)
Car_insurance.grid(row=3,column=5)
#=================================================================================================================================
Customer=Label(Leftframe1,font=("arial",10,"bold"),text="Customer",bd=8)
Customer.grid(row=0,column=0,sticky="w")
Customer=Entry(Leftframe1,font=("arial",10,"bold"),bd=8,width=31,textvariable=customer)
Customer.grid(row=0,column=1)
#===================================================================================================================================
Title=Label(Leftframe1,font=("arial",10,"bold"),text="Title",bd=8)
Title.grid(row=0,column=2,sticky="w")
Title=Entry(Leftframe1,font=("arial",10,"bold"),bd=8,width=31,textvariable=title)
Title.grid(row=0,column=3)
#==============================================================================================================================
FirstName=Label(Leftframe1,font=("arial",10,"bold"),text="First_Name",bd=8)
FirstName.grid(row=0,column=4,sticky="w")
FirstName=Entry(Leftframe1,font=("arial",10,"bold"),bd=8,width=31,textvariable=firstName)
FirstName.grid(row=0,column=5)
#===============================================================================================================================
Surname=Label(Leftframe1,font=("arial",10,"bold"),text="Sur_Name",bd=8)
Surname.grid(row=1,column=0,sticky="w")
Surname=Entry(Leftframe1,font=("arial",10,"bold"),bd=8,width=31,textvariable=surname)
Surname.grid(row=1,column=1)
#================================================================================================================================
Street=Label(Leftframe1,font=("arial",10,"bold"),text="Street",bd=8)
Street.grid(row=1,column=2,sticky="w")
Street=Entry(Leftframe1,font=("arial",10,"bold"),bd=8,width=31,textvariable=street)
Street.grid(row=1,column=3)
#==============================================================================================================================
Area=Label(Leftframe1,font=("arial",10,"bold"),text="Area",bd=8)
Area.grid(row=1,column=4,sticky="w")
Area=Entry(Leftframe1,font=("arial",10,"bold"),bd=8,width=31,textvariable=area)
Area.grid(row=1,column=5)
#==================================================================================================================================
Postcode=Label(Leftframe1,font=("arial",10,"bold"),bd=8,text="Postcode")
Postcode.grid(row=2,column=0,sticky="w")
Postcode=Entry(Leftframe1,font=("arial",10,"bold"),bd=8,width=31,textvariable=postcode)
Postcode.grid(row=2,column=1)
#===============================================================================================================================
Licence=Label(Leftframe1,font=("arial",10,"bold"),bd=8,text="Licence")
Licence.grid(row=2,column=2,sticky="w")
Licence=Entry(Leftframe1,font=("arial",10,"bold"),bd=8,width=31,textvariable=licence)
Licence.grid(row=2,column=3)
#===============================================================================================================================
IssueDate=Label(Leftframe1,font=("arial",10,"bold"),bd=8,text="IssueDate")
IssueDate.grid(row=2,column=4,sticky="w")
IssueDate=Entry(Leftframe1,font=("arial",10,"bold"),bd=8,width=31,textvariable=issueDate)
IssueDate.grid(row=2,column=5)
#===============================================================================================================================
Issueby=Label(Leftframe1,font=("arial",10,"bold"),bd=8,text="Issue Buy")
Issueby.grid(row=3,column=0,sticky="w")
Issueby=Entry(Leftframe1,font=("arial",10,"bold"),bd=8,width=31,textvariable=issueby)
Issueby.grid(row=3,column=1)
#==================================================================================================================================
RegristerNO=Label(Leftframe1,font=("arial",10,"bold"),bd=8,text="Regrister No")
RegristerNO.grid(row=3,column=2,sticky="w")
RegristerNO=Entry(Leftframe1,font=("arial",10,"bold"),bd=8,width=31,textvariable=regristerno)
RegristerNO.grid(row=3,column=3)
#=====================================================================================================================================
dailyrentealdate=Label(Leftframe1,font=("arial",10,"bold"),bd=8,text="Daily Rental Date")
dailyrentealdate.grid(row=3,column=4,sticky="w")
dailyrentealdate=Entry(Leftframe1,font=("arial",10,"bold"),bd=8,width=31,textvariable=dailyrentealdate)
dailyrentealdate.grid(row=3,column=5)
#=================================================================================================================================
#======================================  Right frame =============================================================================
Style=Checkbutton(Rightframe1,text="Style \t",onvalue=1,offvalue=0,font=("arial",14,"bold"),variable=vr1).grid(row=0,sticky="w")
ClassID=Checkbutton(Rightframe1,text="ClassID \t",onvalue=1,offvalue=0,font=("arial",14,"bold"),variable=vr2).grid(row=1,sticky="w")
Invoice=Checkbutton(Rightframe1,text="Invoice \t",onvalue=1,offvalue=0,font=("arial",14,"bold"),variable=vr3).grid(row=2,sticky="w")
DailyRate=Checkbutton(Rightframe1,text="DailyRate \t",onvalue=1,offvalue=0,font=("arial",14,"bold"),variable=vr4).grid(row=3,sticky="w")
Automatic=Checkbutton(Rightframe1,text="Automatic \t",onvalue=1,offvalue=0,font=("arial",14,"bold"),variable=vr5).grid(row=4,sticky="w")
AirCondition=Checkbutton(Rightframe1,text="AirCondition \t",onvalue=1,offvalue=0,font=("arial",14,"bold"),variable=vr6).grid(row=5,sticky="w")
InsuranceSold=Checkbutton(Rightframe1,text="Insurance \t",onvalue=1,offvalue=0,font=("arial",14,"bold"),variable=vr7).grid(row=6,sticky="w")
CustomerDetail=Checkbutton(Rightframe1,text="CustomerDetail \t",onvalue=1,offvalue=0,font=("arial",14,"bold"),variable=vr8).grid(row=7,sticky="w")
#==================================================================================================================================
#txtRecepit=Text(RightFrame2,height=17,width=21,bd=8,font=("arial",12,"bold")).grid(row=0,column=0)




btnTotal=Button(Leftframe4,text="Total",padx=4,pady=4,bd=4,fg="black",font=("arial",12,"bold"),width=20,height=1,command=total).grid(row=0,column=0)
btnReset=Button(Leftframe4,text="Reset",padx=4,pady=4,bd=4,fg="black",font=("arial",12,"bold"),width=20,height=1,command=reset).grid(row=0,column=1)
btnRecepit=Button(Leftframe4,text="Recepit",padx=4,pady=4,bd=4,fg="black",font=("arial",12,"bold"),width=20,height=1).grid(row=0,column=2)
btnExit=Button(Leftframe4,text="Exit",padx=4,pady=4,bd=4,fg="black",font=("arial",12,"bold"),width=20,height=1,command=exit).grid(row=0,column=3)

root.mainloop()