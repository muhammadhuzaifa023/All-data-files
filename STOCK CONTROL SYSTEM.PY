# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:10:43 2020

@author: HASSAN ENTERPRISES
"""

from tkinter import *
import random
import datetime
from tkinter import Tk,StringVar,ttk
root=Tk()
root.geometry("1350x750+0+0")
root.title("STOCK CONTROLL SYSTEM")
Topsframe=Frame(root,width=1350,height=100,bd=14,relief="raise")
Topsframe.pack(side="top")
Bottomframe=Frame(root,width=1350,height=200,bd=14,relief="raise")
Bottomframe.pack(side="bottom")


LeftMidframe=Frame(Bottomframe,width=600,height=1000,bd=14,relief="raise")
LeftMidframe.pack(side="left")

RightMidframe=Frame(Bottomframe,width=750,height=1000,bd=14,relief="raise")
RightMidframe.pack(side="right")

lblTitle=Label(Topsframe,font=("arial",40,"bold"),text="Stock controll System",bd=10,width=40,justify="center")
lblTitle.grid(row=0,column=0)
#=============================================VARIABLE=========================================================
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
Vat=StringVar()
Vat=StringVar()
Tax=StringVar()
var1.set("")
var2.set("")
var3.set("")
var4.set("")
var5.set("0")
var6.set("")
var7.set("")
var8.set("")
var9.set("0")
Vat.set("0")
Tax.set("0")


#============================================LEFT FRAME============================================================
#=============================================PRODUCT DETAILS=====================================================
lblproductId=Label(LeftMidframe,font=("arial",14,"bold"),text="Product_ID",bd=10,width=2,anchor="w")
lblproductId.grid(row=0,column=0)

cmbproductId=ttk.Combobox(LeftMidframe,font=("arial",14,"bold"),textvariable=var1,state='readonly',width=25)
cmbproductId['value']=('','PID001','PID002','PID003','PID004','PID005')
cmbproductId.current(0)
cmbproductId.grid(row=0,column=1)
#---------------------------------------------------------------------------------------------------------------
lblproductName1=Label(LeftMidframe,font=("arial",14,"bold"),text="product_Name",bd=10,width=20,anchor="w")
lblproductName1.grid(row=1,column=0)
lblproductName2=Label(LeftMidframe,font=("arial",14,"bold"),textvariable=var2,bd=10,width=18,relief="sunken")
lblproductName2.grid(row=1,column=1)
#---------------------------------------------------------------------------------------------------------------
lbldescription1=Label(LeftMidframe,font=("arial",14,"bold"),text="Description",bd=10,width=20,anchor="w")
lbldescription1.grid(row=2,column=0)
lbldescription2=Label(LeftMidframe,font=("arial",14,"bold"),textvariable=var3,bd=10,width=18,relief="sunken")
lbldescription2.grid(row=2,column=1)
#--------------------------------------------------------------------------------------------------------------
lblstock_level1=Label(LeftMidframe,font=("arial",14,"bold"),text="Stock Level",bd=10,width=20,anchor="w")
lblstock_level1.grid(row=3,column=0)
lblstock_level2=Label(LeftMidframe,font=("arial",14,"bold"),textvariable=var4,bd=10,width=18,relief="sunken")
lblstock_level2.grid(row=3,column=1)
#--------------------------------------------------------------------------------------------------------------
lblreorderlevel1=Label(LeftMidframe,font=("arial",14,"bold"),text="Reorder_Level",bd=10,width=20,anchor="w")
lblreorderlevel1.grid(row=4,column=0)
lblreorderlevel2=Label(LeftMidframe,font=("arial",14,"bold"),textvariable=var2,bd=10,width=18,relief="sunken")
lblreorderlevel2.grid(row=4,column=1)
#--------------------------------------------------------------------------------------------------------------
lbloutstock1=Label(LeftMidframe,font=("arial",14,"bold"),text="Out of Stock",bd=10,width=20,anchor="w")
lbloutstock1.grid(row=5,column=0)
lbloutstock12=Label(LeftMidframe,font=("arial",14,"bold"),textvariable=var3,bd=10,width=18,relief="sunken")
lbloutstock12.grid(row=5,column=1)
#------------------------------------------------------------------------------------------------------------
lblNO_Of_order1=Label(LeftMidframe,font=("arial",14,"bold"),text="No.of order",bd=10,width=20,anchor="w")
lblNO_Of_order1.grid(row=6,column=0)
lblNO_Of_order2=Label(LeftMidframe,font=("arial",14,"bold"),textvariable=var4,bd=10,width=18,relief="sunken")
lblNO_Of_order2.grid(row=6,column=1)
#---------------------------------------------------------------------------------------------------------
lblAction1=Label(LeftMidframe,font=("arial",14,"bold"),text="Action",bd=10,width=20,anchor="w")
lblAction1.grid(row=7,column=0)
lblAction2=Label(LeftMidframe,font=("arial",14,"bold"),textvariable=var4,bd=10,width=18,relief="sunken")
lblAction2.grid(row=7,column=1)
#-----------------------------------------------------------------------------------------------------------
lblReorder_Date1=Label(LeftMidframe,font=("arial",14,"bold"),text="Reorder_Date",bd=10,width=20,anchor="w")
lblReorder_Date1.grid(row=8,column=0)
lblReorder_Date2=Label(LeftMidframe,font=("arial",14,"bold"),textvariable=var4,bd=10,width=18,relief="sunken")
lblReorder_Date2.grid(row=8,column=1)
#-----------------------------------------------------------------------------------------------------------
lblDiscount=Label(LeftMidframe,font=("arial",14,"bold"),text="Discount",bd=10,width=20,justify="center",anchor="w")
lblDiscount.grid(row=9,column=0)
lblDiscount2=Label(LeftMidframe,font=("arial",14,"bold"),textvariable=var4,bd=10,width=18,relief="sunken")
lblDiscount2.grid(row=9,column=1)

#-----------------------------------------------------------------------------------------------------------
lblcost_per_unit1=Label(LeftMidframe,font=("arial",14,"bold"),text="Cost per unit",bd=10,width=20,anchor="w")
lblcost_per_unit1.grid(row=10,column=0)
lblcost_per_unit2=Label(LeftMidframe,font=("arial",14,"bold"),textvariable=var4,bd=10,width=18,relief="sunken")
lblcost_per_unit2.grid(row=10,column=1)
#==================================================RightFrame========================================================
#==================================================Product_Detail====================================================
lblvalidform1=Label(RightMidframe,font=("arial",14,"bold"),text="Valid_Form",bd=10,width=14,anchor="w")
lblvalidform1.grid(row=0,column=0)
lblvalidform2=Label(RightMidframe,font=("arial",14,"bold"),textvariable=var4,bd=10,width=14,relief="sunken")
lblvalidform2.grid(row=0,column=1)
#=================================================================================================================
lbldateexperies1=Label(RightMidframe,font=("arial",14,"bold"),text="Date_Expires",bd=10,width=14,anchor="w")
lbldateexperies1.grid(row=0,column=2)
lbldateexperies2=Label(RightMidframe,font=("arial",14,"bold"),textvariable=var4,bd=10,width=14,relief="sunken")
lbldateexperies2.grid(row=0,column=3)
#-----------------------------------------------------------------------------------------------------------------
lblRemainder1=Label(RightMidframe,font=("arial",14,"bold"),text="Remainder",bd=10,width=14,anchor="w")
lblRemainder1.grid(row=1,column=0)
lblRemainder2=Label(RightMidframe,font=("arial",14,"bold"),textvariable=var4,bd=10,width=14,relief="sunken")
lblRemainder2.grid(row=1,column=1)
#=================================================================================================================
lblOn_sales1=Label(RightMidframe,font=("arial",14,"bold"),text="On sales",bd=10,width=14,anchor="w")
lblOn_sales1.grid(row=1,column=2)
lblOn_sales2=Label(RightMidframe,font=("arial",14,"bold"),textvariable=var4,bd=10,width=14,relief="sunken")
lblOn_sales2.grid(row=1,column=3)
#---------------------------------------------------------------------------------------------------------------
lblOrder_Id1=Label(RightMidframe,font=("arial",14,"bold"),text="Order Id",bd=10,width=14,anchor="w")
lblOrder_Id1.grid(row=2,column=0)
cmbCustome_ID=ttk.Combobox(RightMidframe,font=("arial",14,"bold"),textvariable=var6,state='readonly',width=14)
cmbCustome_ID['value']=('','ORD0091','ORD0092',"ORD0093","ORD0094","ORD0095","ORD0096","ORD0097")
cmbCustome_ID.current(0)
cmbCustome_ID.grid(row=2,column=1)



#===================================================================================================================
lblDate_Ordered1=Label(RightMidframe,font=("arial",14,"bold"),text="Date Ordered",bd=10,width=14,anchor="w")
lblDate_Ordered1.grid(row=2,column=2)
lblDate_Ordered2=Label(RightMidframe,font=("arial",14,"bold"),textvariable=var4,bd=10,width=14,relief="sunken")
lblDate_Ordered2.grid(row=2,column=3)
#---------------------------------------------------------------------------------------------------------------
lblCustome_ID1=Label(RightMidframe,font=("arial",14,"bold"),text="Customer ID",bd=10,width=14,anchor="w")
lblCustome_ID1.grid(row=3,column=0)
cmbCustome_ID=ttk.Combobox(RightMidframe,font=("arial",14,"bold"),textvariable=var5,state='readonly',width=14)
cmbCustome_ID['value']=('','CID0091','CID0092',"CID0093","CID0094","CID0095","CID0096","CID0097")
cmbCustome_ID.current(0)
cmbCustome_ID.grid(row=3,column=1)
#====================================================================================================================
lblNo_Of_Itemordered1=Label(RightMidframe,font=("arial",14,"bold"),text="No.Of Itemordered",bd=10,width=14,anchor="w")
lblNo_Of_Itemordered1.grid(row=3,column=2)
lblNo_Of_Itemordered2=Label(RightMidframe,font=("arial",14,"bold"),textvariable=var4,bd=10,width=14,relief="sunken")
lblNo_Of_Itemordered2.grid(row=3,column=3)

#-----------------------------------------------------------------------------------------------------------------
lblFirst_Name1=Label(RightMidframe,font=("arial",14,"bold"),text="First Name",bd=10,width=14,anchor="w")
lblFirst_Name1.grid(row=4,column=0)
lblFirst_Name2=Label(RightMidframe,font=("arial",14,"bold"),textvariable=var4,bd=10,width=14,relief="sunken")
lblFirst_Name2.grid(row=4,column=1)
#====================================================================================================================
lblItem_ordered1=Label(RightMidframe,font=("arial",14,"bold"),text="Item_ordered",bd=10,width=14,anchor="w")
lblItem_ordered1.grid(row=4,column=2)
lblItem_ordered2=Label(RightMidframe,font=("arial",14,"bold"),textvariable=var4,bd=10,width=14,relief="sunken")
lblItem_ordered2.grid(row=4,column=3)
#-------------------------------------------------------------------------------------------------------------------
lblSur_Name1=Label(RightMidframe,font=("arial",14,"bold"),text="Sur Name",bd=10,width=14,anchor="w")
lblSur_Name1.grid(row=5,column=0)
lblSur_Name2=Label(RightMidframe,font=("arial",14,"bold"),textvariable=var4,bd=10,width=14,relief="sunken")
lblSur_Name2.grid(row=5,column=1)
#====================================================================================================================
lblPayment_Method1=Label(RightMidframe,font=("arial",14,"bold"),text="Payment_Method",bd=10,width=14,anchor="w")
lblPayment_Method1.grid(row=5,column=2)
cmbPayment_Method=ttk.Combobox(RightMidframe,font=("arial",14,"bold"),textvariable=var8,state='readonly',width=14)
cmbPayment_Method['value']=('','Cash','Master Card','Visa Card','Debit card')
cmbPayment_Method.current(0)
cmbPayment_Method.grid(row=5,column=3)


#------------------------------------------------------------------------------------------------------------------
lblAddress1=Label(RightMidframe,font=("arial",14,"bold"),text="Address",bd=10,width=45,anchor="w")
lblAddress1.grid(row=6,column=0)
lblAddress2=Label(RightMidframe,font=("arial",14,"bold"),textvariable=var4,bd=10,width=14,relief="sunken")
lblAddress2.grid(row=6,column=1)
#-----------------------------------------------------------------------------------------------------------------
lblAccount_Type1=Label(RightMidframe,font=("arial",14,"bold"),text="Account Type",bd=10,width=14,anchor="w")
lblAccount_Type1.grid(row=7,column=0)
cmbAccount=ttk.Combobox(RightMidframe,font=("arial",14,"bold"),textvariable=var7,state='readonly',width=14)
cmbAccount['value']=('','Credit Acc','Debit Acc',"Customer Acc","Comm Acc")
cmbAccount.current(0)
cmbAccount.grid(row=7,column=1)

#====================================================================================================================
lblVAT1=Label(RightMidframe,font=("arial",14,"bold"),text="VAT",bd=10,width=14,anchor="w")
lblVAT1.grid(row=7,column=2)
cmbVAT=ttk.Combobox(RightMidframe,font=("arial",14,"bold"),textvariable=Vat,state='readonly',width=25)
cmbVAT['value']=('','Yes','No')
cmbVAT.current(0)
cmbVAT.grid(row=7,column=3)

#----------------------------------------------------------------------------------------------------------------

lblTax1=Label(RightMidframe,font=("arial",14,"bold"),text="Tax",bd=10,width=14,anchor="w")
lblTax1.grid(row=8,column=0)
lblTax2=Label(RightMidframe,font=("arial",14,"bold"),textvariable=var4,bd=10,width=14,relief="sunken")
lblTax2.grid(row=8,column=1)
#====================================================================================================================
lblSubTotal1=Label(RightMidframe,font=("arial",14,"bold"),text="SubTotal",bd=10,width=14,anchor="w")
lblSubTotal1.grid(row=8,column=2)
lblSubTotal2=Label(RightMidframe,font=("arial",14,"bold"),textvariable=var4,bd=10,width=14,relief="sunken")
lblSubTotal2.grid(row=8,column=3)
#-----------------------------------------------------------------------------------------------------------------
lblTotal1=Label(RightMidframe,font=("arial",14,"bold"),text="Total",bd=10,width=14,anchor="w")
lblTotal1.grid(row=9,column=0)
lblTotal2=Label(RightMidframe,font=("arial",14,"bold"),textvariable=var4,bd=10,width=14,relief="sunken")
lblTotal2.grid(row=9,column=1)

#---------------------------------------------------------------------------------------------------------------
BtnTotal1=Button(RightMidframe,font=("arial",10,"bold"),text="Total",bd=6,width=20)
BtnTotal1.grid(row=9,column=2)

BtnRest1=Button(LeftMidframe,font=("arial",10,"bold"),text="Rest",bd=6,width=20)
BtnRest1.grid(row=11,column=0)

BtnExit1=Button(RightMidframe,font=("arial",10,"bold"),text="Exit",bd=6,width=20)
BtnExit1.grid(row=9,column=3)







root.mainloop()