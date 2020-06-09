# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 20:37:42 2020

@author: HASSAN ENTERPRISES
"""

from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
from tkinter import messagebox
import datetime
import time

class payroll:
    def __init__(self,root):
        self.root=root
        self.root.title("payroll management system")
        self.root.geometry("1400x800+0+0")
        self.root.configure(bg="gainsboro")
        
        employeeName=StringVar()
        address=StringVar()
        reference=StringVar()
        employerName=StringVar()
        cityweighing=IntVar()
        basicsalary=IntVar()
        overtime=StringVar()
        grosspay=StringVar()
        netpay=StringVar()
        tax=StringVar()
        pension=StringVar()
        studentloan=StringVar()
        NIpayment=StringVar()
        deduction=StringVar()
        postcode=StringVar()
        gender=StringVar()
        payday=StringVar()
        taxperiod=StringVar()
        NInumber=StringVar()
        NIcode=StringVar()
        taxablepay=StringVar()
        pensionablepay=StringVar()
        otherpaymentdue=StringVar()
        taxcode=StringVar()
        
        cityweighing.set("")
        basicsalary.set("")
        #=================================================================================================================
        def exit():
            iexit=tkinter.messagebox.askyesno("payrollsystem","confirm if you want to exit")
            if iexit>0:
                root.destroy()
                return
        #===================================================================================================================    
        def reset():
            employeeName.set("")
            address.set("")
            reference.set("")
            employerName.set("")
            cityweighing.set("")
            basicsalary.set("")
            overtime.set("")
            grosspay.set("")
            netpay.set("")
            tax.set("")
            pension.set("")
            studentloan.set("")
            NIpayment.set("")
            deduction.set("")
            postcode.set("")
            gender.set("")
            payday.set("")
            taxperiod.set("")
            NInumber.set("")
            NIcode.set("")
            taxablepay.set("")
            pensionablepay.set("")
            otherpaymentdue.set("")
            taxcode.set("")
            self.lblRecepit.delete("1.0",END)
        #=======================================================================================================================
        def payment():
            payday.set(time.strftime("%d/%m/%Y"))
            Refpay=random.randint(2000,709494)
            Refpaid=("PR"+str(Refpay))
            reference.set(Refpaid)
            
            NIpay=random.randint(34051,409124)
            NIpaid=("NI"+str(NIpay))
            NInumber.set(NIpaid)
            
            idate=datetime.datetime.now()
            taxperiod.set(idate.month)
            
            Ncode=random.randint(1290,13123)
            codeNI=("NIC"+str(Ncode))
            #NInumber.set(NIpaid)
            NIcode.set(codeNI)
            
            itax =random.randint(7589,15876)
            paymenttaxcode=("Tcode"+str(itax))
            taxcode.set(paymenttaxcode)
        def monthlySalary():
            payment()
            bs=float(basicsalary.get())
            cw=float(cityweighing.get())
            ot=float(overtime.get())
            
            MTax=((bs+cw+ot)*0.3)
            tTax="Rs",str(MTax)
            tax.set(tTax)
            
            Mpension=((bs+cw+ot)*0.02)
            MMpension="Rs",str(Mpension)
            pension.set(MMpension)
            
            Mstudentloan=((bs+cw+ot)*0.012)
            MMstudentloan="Rs"+str("%.2f"%(Mstudentloan))
            studentloan.set(MMstudentloan)
            
            MNIpayment=((bs+cw+ot)*0.011)
            MMNIpayment="Rs"+str("%.2f"%(MNIpayment))
            NIpayment.set(MMNIpayment)
            
            Deduct=(MTax+Mpension+Mstudentloan+MNIpayment)
            Deductpayment="Rs"+str("%.2f"%(Deduct))
            deduction.set(Deductpayment)
            
            Grosspay="Rs",str("%.2f"%(bs+cw+ot))
            grosspay.set(Grosspay)
            
            NetpayAfter=(bs+cw+ot)-Deduct
            NetAfter="Rs",str("%.2f"%(NetpayAfter))
            netpay.set(NetAfter)
            
            taxablepay.set(tTax)
            pensionablepay.set(MMpension)
            otherpaymentdue.set("0.00")
            
            self.lblRecepit.insert(END,"\t\t Monthly Pay Slip"+"\n")
            self.lblRecepit.insert(END,"Reference:\t\t\t"+reference.get()+"\n")
            self.lblRecepit.insert(END,"Reference:\t\t\t"+payday.get()+"\n")
            self.lblRecepit.insert(END,"EmployerName:\t\t\t"+employerName.get()+"\n")
            self.lblRecepit.insert(END,"EmployeeName:\t\t\t"+employeeName.get()+"\n")
            self.lblRecepit.insert(END,"Tax:\t\t\t"+tax.get()+"\n")
            self.lblRecepit.insert(END,"Pension:\t\t\t"+pension.get()+"\n")
            self.lblRecepit.insert(END,"Student Loan:\t\t\t"+studentloan.get()+"\n")
            self.lblRecepit.insert(END,"NI Number:\t\t\t"+NInumber.get()+"\n")
            self.lblRecepit.insert(END,"NI payment:\t\t\t"+NIpayment.get()+"\n")
            self.lblRecepit.insert(END,"Deduction:\t\t\t"+deduction.get()+"\n")
            #==================================================================================================
            self.lblRecepit.insert(END,"City weighing:\t\t\t"+str("Rs %.2f"%(cityweighing.get()))+"\n")
            self.lblRecepit.insert(END,"Overtime:\t\t\t"+"Rs"+overtime.get()+"\n")
            self.lblRecepit.insert(END,"Netpay:\t\t\t"+netpay.get()+"\n")
            self.lblRecepit.insert(END,"Gross pay:\t\t\t"+grosspay.get()+"\n")
            
            
            
            
            
            
#===============================================================================================================
        Mainframe=Frame(self.root,bd=10,width=1350,height=700,bg="gainsboro",relief=RIDGE)
        Mainframe.grid()        
        
        Topframe1=Frame(Mainframe,bd=10,width=1340,height=100,bg="gainsboro",relief=RIDGE)
        Topframe1.grid()
        
        Topframe2=Frame(Mainframe ,bd=10,width=1340,height=100,bg="gainsboro",relief=RIDGE)
        Topframe2.grid()
        
        Topframe3=Frame(Mainframe,bd=10,width=1340,height=500,bg="gainsboro",relief=RIDGE)
        Topframe3.grid()
        
        Leftframe=Frame(Topframe3,bd=5,width=1340,height=400,bg="gainsboro",relief=RIDGE,padx=2)
        Leftframe.pack(side="left")
        
        Leftframe1=Frame(Leftframe ,bd=5,width=1340,height=600,bg="gainsboro",relief=RIDGE,padx=2)
        Leftframe1.pack(side="top")
        
        Leftframe2=Frame(Leftframe,bd=5,width=600,height=180,bg="gainsboro",relief=RIDGE,padx=2)
        Leftframe2.pack(side="top")
        Leftframe2left=Frame(Leftframe2,bd=5,width=300,height=170,bg="gainsboro",relief=RIDGE,padx=2)
        Leftframe2left.pack(side="left")
        Leftframe2right=Frame(Leftframe2,bd=5,width=300,height=170,bg="gainsboro",relief=RIDGE,padx=2)
        Leftframe2right.pack(side="right")
        
       
        Leftframe3left=Frame(Leftframe,bd=5,width=320,height=50,bg="gainsboro",relief=RIDGE,padx=2)
        Leftframe3left.pack(side="left")
        Leftframe3right=Frame(Leftframe,bd=5,width=320,height=50,bg="gainsboro",relief=RIDGE,padx=2)
        Leftframe3right.pack(side="right")
        
        Rightframe1=Frame(Topframe3,bd=5,width=320,height=400,bg="gainsboro",relief=RIDGE,padx=2)
        Rightframe1.pack(side="right")
        Rightframe1a=Frame(Rightframe1,bd=5,width=310,height=300,bg="gainsboro",relief=RIDGE,padx=2)
        Rightframe1a.pack(side="top")
        Rightframe1b=Frame(Rightframe1,bd=5,width=310,height=100,bg="gainsboro",relief=RIDGE,padx=2)
        Rightframe1b.pack(side="top")
        
        
        Rightframe2=Frame(Topframe3,bd=5,width=300,height=400,bg="gainsboro",relief=RIDGE,padx=2)
        Rightframe2.pack(side="right")
        Rightframe2a=Frame(Rightframe2,bd=5,width=280,height=50,bg="gainsboro",relief=RIDGE,padx=2)
        Rightframe2a.pack(side="top")
        Rightframe2b=Frame(Rightframe2,bd=5,width=280,height=180,bg="gainsboro",relief=RIDGE,padx=2)
        Rightframe2b.pack(side="top")
        Rightframe2c=Frame(Rightframe2,bd=5,width=280,height=100,bg="gainsboro",relief=RIDGE,padx=2)
        Rightframe2c.pack(side="top")
        Rightframe2d=Frame(Rightframe2,bd=5,width=280,height=50,bg="gainsboro",relief=RIDGE,padx=2)
        Rightframe2d.pack(side="top")
        
        #========================================================================================
        
        self.lbltitle=Label(Topframe1,font=("arial",40,"bold"),text="    payRoll Management System    ",bd=10
                            ,bg="gainsboro",justify="center")
        self.lbltitle.grid(row=0,column=0)
        

    #===============================================================================================
        self.lblemployeeName=Label(Topframe2,font=("arial",12,"bold"),text="Employee Name",bd=10,anchor="sw"
                                   ,bg="gainsboro")
        self.lblemployeeName.grid(row=0,column=0)
        
        self.lblemployeeName=Entry(Topframe2,font=("arial",12,"bold"),bd=10,justify="left",textvariable=employeeName
                                   ,bg="gainsboro")
        self.lblemployeeName.grid(row=0,column=1)
        #=========================================================================================================
        
        self.lbladdress=Label(Topframe2,font=("arial",12,"bold"),text="Address",bd=10,anchor="sw"
                                   ,bg="gainsboro")
        self.lbladdress.grid(row=1,column=0)
        
        self.lbladdress=Entry(Topframe2,font=("arial",12,"bold"),bd=10,justify="left",textvariable=address
                                   ,bg="gainsboro")
        self.lbladdress.grid(row=1,column=1)
        #============================================================================================================
        self.lblpostcode=Label(Topframe2,font=("arial",12,"bold"),text="PostCode",bd=10,anchor="w"
                                   ,bg="gainsboro")
        self.lblpostcode.grid(row=0,column=2)
        
        self.lblpostcode=Entry(Topframe2,font=("arial",12,"bold"),bd=10,justify="left",textvariable=postcode
                                   ,bg="gainsboro")
        self.lblpostcode.grid(row=0,column=3)
        #=============================================================================================================
        self.lblgender=Label(Topframe2,font=("arial",12,"bold"),text="Gender",bd=10,anchor="w"
                                   ,bg="gainsboro")
        self.lblgender.grid(row=1,column=2)
        
        self.lblgender=Entry(Topframe2,font=("arial",12,"bold"),bd=10,justify="left",textvariable=gender
                                   ,bg="gainsboro")
        self.lblgender.grid(row=1,column=3)
        #============================================================================================================
        self.lblreference=Label(Leftframe1,font=("arial",12,"bold"),text="Reference",bd=10,anchor="e"
                                   ,bg="gainsboro")
        self.lblreference.grid(row=0,column=0)
        
        self.lblreference=Entry(Leftframe1,font=("arial",12,"bold"),bd=10,justify="left",textvariable=reference
                                   ,bg="gainsboro")
        self.lblreference.grid(row=0,column=1)
        #==============================================================================================================
        self.lblemployerName=Label(Leftframe1,font=("arial",12,"bold"),text="EmployerName",bd=10,anchor="w"
                                   ,bg="gainsboro")
        self.lblemployerName.grid(row=1,column=0)
        
        self.lblemployerName=Entry(Leftframe1,font=("arial",12,"bold"),bd=10,justify="left",textvariable=employerName
                                   ,bg="gainsboro")
        self.lblemployerName.grid(row=1,column=1)
        #==================================================================================================================
        self.lblemployeeName=Label(Leftframe1,font=("arial",12,"bold"),text="EmployeeName",bd=10,anchor="w"
                                   ,bg="gainsboro")
        self.lblemployeeName.grid(row=2,column=0)
        
        self.lblemployeeName=Entry(Leftframe1,font=("arial",12,"bold"),bd=10,justify="left",textvariable=employeeName
                                   ,bg="gainsboro")
        self.lblemployeeName.grid(row=2,column=1)
        #====================================================================================================================
        self.lblcityweighing=Label(Leftframe2left,font=("arial",12,"bold"),text="city weighing",bd=10,anchor="e"
                                   ,bg="gainsboro")
        self.lblcityweighing.grid(row=0,column=0)
        
        self.lblcityweighing=Entry(Leftframe2left,font=("arial",12,"bold"),bd=10,justify="left",textvariable=cityweighing,width=20
                                   ,bg="gainsboro")
        self.lblcityweighing.grid(row=0,column=1)
        #===============================================================================================================================
        self.lblbasicsalary=Label(Leftframe2left,font=("arial",12,"bold"),text="Basic Salary",bd=10,anchor="w"
                                   ,bg="gainsboro")
        self.lblbasicsalary.grid(row=1,column=0)
        
        self.lblbasicsalary=Entry(Leftframe2left,font=("arial",12,"bold"),bd=10,justify="left",textvariable=basicsalary,width=20
                                   ,bg="gainsboro")
        self.lblbasicsalary.grid(row=1,column=1)

        #==========================================================================================================================
        self.lblovertime=Label(Leftframe2left,font=("arial",12,"bold"),text="Over Time",bd=10,anchor="w"
                                   ,bg="gainsboro")
        self.lblovertime.grid(row=2,column=0)
        
        self.lblovertime=Entry(Leftframe2left,font=("arial",12,"bold"),bd=10,justify="left",textvariable=overtime,width=20
                                   ,bg="gainsboro")
        self.lblovertime.grid(row=2,column=1)
        #=======================================================================================================================
        self.lblotherpaymentdue=Label(Leftframe2left,font=("arial",12,"bold"),text="Other Payment Due",bd=10,anchor="w"
                                   ,bg="gainsboro")
        self.lblotherpaymentdue.grid(row=3,column=0)
        
        self.lblotherpaymentdue=Entry(Leftframe2left,font=("arial",12,"bold"),bd=10,justify="left",textvariable=otherpaymentdue,width=20
                                   ,bg="gainsboro")
        self.lblotherpaymentdue.grid(row=3,column=1)
        #====================================================================================================================
        self.lbltax=Label(Leftframe2right,font=("arial",12,"bold"),text="Tax",bd=10,anchor="e"
                                   ,bg="gainsboro")
        self.lbltax.grid(row=0,column=0)
        
        self.lbltax=Entry(Leftframe2right,font=("arial",12,"bold"),bd=10,justify="left",textvariable=tax,width=20
                                   ,bg="gainsboro")
        self.lbltax.grid(row=0,column=1)
        #===================================================================================================================
        self.lblpension=Label(Leftframe2right,font=("arial",12,"bold"),text="Pension",bd=10,anchor="w"
                                   ,bg="gainsboro")
        self.lblpension.grid(row=1,column=0)
        
        self.lblpension=Entry(Leftframe2right,font=("arial",12,"bold"),bd=10,justify="left",textvariable=pension,width=20
                                   ,bg="gainsboro")
        self.lblpension.grid(row=1,column=1)
        #======================================================================================================================
        self.lblstudentloan=Label(Leftframe2right,font=("arial",12,"bold"),text="Student Loan",bd=10,anchor="w"
                                   ,bg="gainsboro")
        self.lblstudentloan.grid(row=2,column=0)
        
        self.lblstudentloan=Entry(Leftframe2right,font=("arial",12,"bold"),bd=10,justify="left",textvariable=studentloan,width=20
                                   ,bg="gainsboro")
        self.lblstudentloan.grid(row=2,column=1)
        
        #=======================================================================================================================
        self.lblNIpayment=Label(Leftframe2right,font=("arial",12,"bold"),text="NI payment",bd=10,anchor="w"
                                   ,bg="gainsboro")
        self.lblNIpayment.grid(row=3,column=0)
        
        self.lblNIpayment=Entry(Leftframe2right,font=("arial",12,"bold"),bd=10,justify="left",textvariable=NIpayment,width=20
                                   ,bg="gainsboro")
        self.lblNIpayment.grid(row=3,column=1)
        #=========================================================================================================================
        self.lblgrosspay=Label(Leftframe3left,font=("arial",12,"bold"),text="Gross Pay",bd=10,anchor="w"
                                   ,bg="gainsboro")
        self.lblgrosspay.grid(row=3,column=0)
        
        self.lblgrosspay=Entry(Leftframe3left,font=("arial",12,"bold"),bd=10,justify="left",textvariable=grosspay,width=23
                                   ,bg="gainsboro")
        self.lblgrosspay.grid(row=3,column=1)
        #=============================================================================================================================
        self.lbldeduction=Label(Leftframe3right,font=("arial",12,"bold"),text="Deduction",bd=10,anchor="w"
                                   ,bg="gainsboro")
        self.lbldeduction.grid(row=3,column=0)
        
        self.lbldeduction=Entry(Leftframe3right,font=("arial",12,"bold"),bd=10,justify="left",textvariable=deduction,width=23
                                   ,bg="gainsboro")
        self.lbldeduction.grid(row=3,column=1)
        #=======================================================================================================================
        self.lblpayday=Label(Rightframe2a,font=("arial",12,"bold"),text="Pay day",bd=10,anchor="w"
                                   ,bg="gainsboro")
        self.lblpayday.grid(row=0,column=0)
        
        self.lblpayday=Entry(Rightframe2a,font=("arial",12,"bold"),bd=10,justify="left",textvariable=payday,width=19
                                   ,bg="gainsboro")
        self.lblpayday.grid(row=0,column=1)
        #========================================================================================================
        self.lbltaxperiod=Label(Rightframe2b,font=("arial",12,"bold"),text="Tax period",bd=10,anchor="w"
                                   ,bg="gainsboro")
        self.lbltaxperiod.grid(row=0,column=0)
        
        self.lbltaxperiod=Entry(Rightframe2b,font=("arial",12,"bold"),bd=10,justify="left",textvariable=taxperiod,width=16
                                   ,bg="gainsboro")
        self.lbltaxperiod.grid(row=0,column=1)
        #========================================================================================================================
        self.lbltaxcode=Label(Rightframe2b,font=("arial",12,"bold"),text="Tax Code",bd=10,anchor="w"
                                   ,bg="gainsboro")
        self.lbltaxcode.grid(row=1,column=0)
        
        self.lbltaxcode=Entry(Rightframe2b,font=("arial",12,"bold"),bd=10,justify="left",textvariable=taxcode,width=16
                                   ,bg="gainsboro")
        self.lbltaxcode.grid(row=1,column=1)
        #========================================================================================================================
        self.lblNInumber=Label(Rightframe2b,font=("arial",12,"bold"),text="NI Number",bd=10,anchor="w"
                                   ,bg="gainsboro")
        self.lblNInumber.grid(row=2,column=0)
        
        self.lblNInumber=Entry(Rightframe2b,font=("arial",12,"bold"),bd=10,justify="left",textvariable=NInumber,width=16
                                   ,bg="gainsboro")
        self.lblNInumber.grid(row=2,column=1)
        #=============================================================================================================================
        self.lblNIcode=Label(Rightframe2b,font=("arial",12,"bold"),text="NI Code",bd=10,anchor="w"
                                   ,bg="gainsboro")
        self.lblNIcode.grid(row=3,column=0)
        
        self.lblNIcode=Entry(Rightframe2b,font=("arial",12,"bold"),bd=10,justify="left",textvariable=NIcode,width=16
                                   ,bg="gainsboro")
        self.lblNIcode.grid(row=3,column=1)
        #==============================================================================================================================
        self.lbltaxablepay=Label(Rightframe2c,font=("arial",12,"bold"),text="Taxable Pay",bd=10,anchor="w"
                                   ,bg="gainsboro")
        self.lbltaxablepay.grid(row=0,column=0)
        
        self.lbltaxablepay=Entry(Rightframe2c,font=("arial",12,"bold"),bd=10,justify="left",textvariable=taxablepay,width=11
                                   ,bg="gainsboro")
        self.lbltaxablepay.grid(row=0,column=1)
        
        #=========================================================================================================================
        self.lblpensionablepay=Label(Rightframe2c,font=("arial",12,"bold"),text="Pensionable Pay",bd=10,anchor="w"
                                   ,bg="gainsboro")
        self.lblpensionablepay.grid(row=1,column=0)
        
        self.lblpensionablepay=Entry(Rightframe2c,font=("arial",12,"bold"),bd=10,justify="left",textvariable=pensionablepay,width=11
                                   ,bg="gainsboro")
        self.lblpensionablepay.grid(row=1,column=1)
        #===============================================================================================================================
        self.lblnetpay=Label(Rightframe2d,font=("arial",12,"bold"),text="Net pay",bd=10,anchor="w"
                                   ,bg="gainsboro")
        self.lblnetpay.grid(row=0,column=0)
        
        self.lblnetpay=Entry(Rightframe2d,font=("arial",12,"bold"),bd=10,justify="left",textvariable=netpay,width=18
                                   ,bg="gainsboro")
        self.lblnetpay.grid(row=0,column=1)
        #====================================================================================================================================
        self.lblRecepit=Text(Rightframe1a,height=18,width=40,bd=10,font=("arial",9,"bold"))
        self.lblRecepit.grid(row=0,column=0)
        #=========================================================================================================================
        self.btnpayment=Button(Rightframe1b,padx=18,pady=5,bd=5,font=("arial",16,"bold"),text="payment",width=4,command=monthlySalary).grid(row=0,column=0)
        self.btnpayment=Button(Rightframe1b,padx=18,pady=5,bd=5,font=("arial",16,"bold"),text="Reset",width=4,command=reset).grid(row=0,column=1)
        self.btnpayment=Button(Rightframe1b,padx=18,pady=5,bd=5,font=("arial",16,"bold"),text="Exit",width=4,command=exit).grid(row=0,column=2) 
        
if __name__=="__main__":
    root=Tk()
    application=payroll(root)
    root.mainloop()
    