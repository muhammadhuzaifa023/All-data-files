# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 02:42:17 2020

@author: HASSAN ENTERPRISES
"""

import time
import datetime
from tkinter import *

root=Tk()
root.title("payroll management system")
root.geometry("1350x650+0+0")

Tops=Frame(root,width=1350,height=50,bd=8,relief="raised")
Tops.pack(side="top")
f1=Frame(root,width=600,height=600,bd=8,relief="raised")
f1.pack(side="left")
f2=Frame(root,width=600,height=600,bd=8,relief="raised")
f2.pack(side="right")

fla=Frame(f1,width=600,height=200,bd=20,relief="raised")
fla.pack(side="top")
flb=Frame(f1,width=600,height=200,bd=20,relief="raised")
flb.pack(side="top")

lblinfo=Label(Tops,font=("arial",60,"bold"),text="payroll Management systems",bd=10)
lblinfo.grid(row=0,column=0)
#=========================================================================================================
def exit():
    qexit=messagebox.askyesno("Payroll system","do you want to exit the system")
    if qexit>0:
        root.destroy()
        return

def reset():
    Name.set("")
    Address.set("")
    Employer.set("")
    NIC.set("")
    HoursWorked.set("")
    HourlyRate.set("")
    Tax.set("")
    OverTime.set("")
    Grosspay.set("")
    NetPay.set("")
    txtpayslip.delete("1.0",END)
def Enterinfoo():
    txtpayslip.insert(END, "\t\tpayslip\n\n")
    txtpayslip.insert(END, "Name: \t\t"+Name.get()+"\n\n")
    txtpayslip.insert(END, "Address: \t\t"+Address.get()+"\n\n")
    txtpayslip.insert(END, "Employer: \t\t"+Employer.get()+"\n\n")
    txtpayslip.insert(END, "NIC\t\t"+NIC.get()+"\n\n")
    txtpayslip.insert(END, "HoursWorked\t\t"+HoursWorked.get()+"\n\n")
    txtpayslip.insert(END, "HourlyRate\t\t"+HourlyRate.get()+"\n\n")
    txtpayslip.insert(END, "Tax\t\t"+Tax.get()+"\n\n")
    txtpayslip.insert(END, "OverTime\t\t"+OverTime.get()+"\n\n")
    txtpayslip.insert(END, "Grosspay\t\t"+Grosspay.get()+"\n\n")
    txtpayslip.insert(END, "Netpay\t\t"+Netpay.get()+"\n\n")
def huzii():
    hoursworkedperweek=float(HoursWorked.get())
    wagesperhours=float(HourlyRate.get())
    
    paydue=wagesperhours * hoursworkedperweek
    
    paymentdue="rs",str("%.2f" %(paydue))
    Grosspay.set(paymentdue)
    
    tax=paydue*0.2
    Taxables="rs",str("%2f" %(tax))
    Tax.set(Taxables)
    
    netpay=paydue-tax
    Netpays="rs",str("%.2f" %(netpay))
    NetPay.set(Netpays)
    
    if hoursworkedperweek > 40:
        overtimehours=(hoursworkedperweek-40)+wagesperhours*1.5
        overtimehrs="rs",str("%.2f" %(overtimehours))
        OverTime.set(overtimehrs)
    elif hoursworkedperweek <= 40:
        overtimehours=(hoursworkedperweek-40)+wagesperhours*1.5
        overtimehrs="rs",str("%.2f" %(overtimehours))
        OverTime.set(overtimehrs)
    return
        
    
    
    
    
    
Name=StringVar()
Address=StringVar()
Employer=StringVar()
NIC=StringVar()
HoursWorked=StringVar()
HourlyRate=StringVar()
Tax=StringVar()
OverTime=StringVar()
Grosspay=StringVar()
NetPay=StringVar()
Dateoforder=StringVar()

Dateoforder.set(time.strftime("%d/%m/5Y"))

#=========================  Label widget =================================================================
lblName=Label(fla,font=("arial",16,"bold"),text="Name",bd=20)
lblName.grid(row=0,column=0)

lblAddress=Label(fla,font=("arial",16,"bold"),text="Address",bd=20)
lblAddress.grid(row=0,column=2)

lblEmployer=Label(fla,font=("arial",16,"bold"),text="Employer",bd=20)
lblEmployer.grid(row=1,column=0)

lblNICNumber=Label(fla,font=("arial",16,"bold"),text="NIC",bd=20)
lblNICNumber.grid(row=1,column=2)

lblHoursWorked=Label(fla,font=("arial",16,"bold"),text="HoursWorked",bd=20)
lblHoursWorked.grid(row=2,column=0)

lblHourlyRate=Label(fla,font=("arial",16,"bold"),text="Hourly Rate",bd=20)
lblHourlyRate.grid(row=2,column=2)

lblTax=Label(fla,font=("arial",16,"bold"),text="Tax",anchor="w",bd=20)
lblTax.grid(row=3,column=0)

lblOverTime=Label(fla,font=("arial",16,"bold"),text="OverTime",bd=20)
lblOverTime.grid(row=3,column=2)

lblGrosspay=Label(fla,font=("arial",16,"bold"),text="Grosspay",bd=20)
lblGrosspay.grid(row=4,column=0)

lblNetPay=Label(fla,font=("arial",16,"bold"),text="NetPay",bd=20)
lblNetPay.grid(row=4,column=2)

#=========================================================================================================
#========================== Entry widget==================================================================

etxtName=Entry(fla,textvariable=Name,font=("arial",16,"bold"),bd=16,width=22,justify="left")
etxtName.grid(row=0,column=1)

etxtAddress=Entry(fla,textvariable=Address,font=("arial",16,"bold"),bd=16,width=22,justify="left")
etxtAddress.grid(row=0,column=3)

etxtEmployer=Entry(fla,textvariable=Employer,font=("arial",16,"bold"),bd=16,width=22,justify="left")
etxtEmployer.grid(row=1,column=1)

etxtNIC=Entry(fla,textvariable=NIC,font=("arial",16,"bold"),bd=16,width=22,justify="left")
etxtNIC.grid(row=1,column=3)

etxtHoursWorked=Entry(fla,textvariable=HoursWorked,font=("arial",16,"bold"),bd=16,width=22,justify="left")
etxtHoursWorked.grid(row=2,column=1)

etxtHourlyRate=Entry(fla,textvariable=HourlyRate,font=("arial",16,"bold"),bd=16,width=22,justify="left")
etxtHourlyRate.grid(row=2,column=3)

etxtTax=Entry(fla,textvariable=Tax,font=("arial",16,"bold"),bd=16,width=22,justify="left")
etxtTax.grid(row=3,column=1)

etxtOverTime=Entry(fla,textvariable=OverTime,font=("arial",16,"bold"),bd=16,width=22,justify="left")
etxtOverTime.grid(row=3,column=3)

etxtGrosspay=Entry(fla,textvariable=Grosspay,font=("arial",16,"bold"),bd=16,width=22,justify="left")
etxtGrosspay.grid(row=4,column=1)

etxtNetPay=Entry(fla,textvariable=NetPay,font=("arial",16,"bold"),bd=16,width=22,justify="left")
etxtNetPay.grid(row=4,column=3)
#================================ text widget ==============================================================
lblpayslip=Label(f2,textvariable=Dateoforder,font=("arial",20,"bold"),bd=20)
lblpayslip.grid(row=0,column=0)

txtpayslip=Text(f2,width=34,height=22,bd=16,font=("arial",12,"bold"))
txtpayslip.grid(row=1,column=0)
#=============================================================================================================
buttonsalary=Button(flb,text="Weekly salary",padx=16,pady=16,bd=8,fg="black",font=("arial",16,"bold"),width=14,height=1,command=huzii).grid(row=0,column=0)

buttonreset=Button(flb,text="Reset",padx=16,pady=16,bd=8,fg="black",font=("arial",16,"bold"),width=14,height=1,command=reset).grid(row=0,column=1)

buttonpayslip=Button(flb,text="pay slip",padx=16,pady=16,bd=8,fg="black",font=("arial",16,"bold"),width=14,height=1,command=Enterinfoo).grid(row=0,column=2)

buttonExit=Button(flb,text="Exit",padx=16,pady=16,bd=8,fg="black",font=("arial",16,"bold"),width=14,height=1,command=exit).grid(row=0,column=3)

root.mainloop()