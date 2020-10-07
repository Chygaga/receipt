#import tkinter as tk
from tkinter import*
import random
import time
import datetime

root =Tk()
root.geometry("700x400+0+0")
root.title("Receipt")

Tops= Frame(root, width= 700, height= 75, bd=8, relief="raise")
Tops.pack(side= TOP)
f1= Frame(root, width= 700, height= 400,bd= 8,relief= "raise")
f1.pack()
f1a= Frame(f1, width= 680, height= 300,bd= 8,relief= "raise",)
f1a.pack(side= TOP)
f1b= Frame(f1, width= 680, height= 75,bd= 8,relief= "raise")
f1b.pack(ipadx=50,ipady=50,side= BOTTOM)

ItemName=StringVar()
ItemCost=StringVar()
VatAmt=StringVar()
Totalcost=StringVar()
Text_input=StringVar()

ItemCost.set(0)

operator=""
def btnClearDisplay():
    global operator
    operator=""
    ItemCost.set("")

def vatCalc():
    Price = (ItemCost.get())
    if int(Price)<5000:
        VatAmt=int(ItemCost)*0
    else:
        VatAmt= int(Price)*0.05
    return VatAmt 
    #ItemCost.set(vatCalc)
    
    

    print("VAT amount: N", vatCalc(ItemCost))
        #totalprice = vat_amount+price


lblInfo= Label(Tops, font=('Arial', 30, 'bold'), text="RECEIPT", bd=8, fg='black')
lblInfo.pack(fill=X, padx=250)


lblItem= Label(f1a, font=('Arial', 15, 'bold'), text="ITEM =                                           ", bd= 15, justify='left')
lblItem.grid(row=0, column=0)    
txtItem=Entry(f1a, font=('Arial', 15, 'bold'), textvariable=ItemName, bd= 10,insertwidth=2, justify='left')
txtItem.grid(row=0, column=1)

lblCost= Label(f1a, font=('Arial', 15, 'bold'), text="PRICE =                                          ", bd= 15, justify='left')
lblCost.grid(row=1, column=0)    
txtCost=Entry(f1a, font=('Arial', 15, 'bold'), textvariable=10, bd= 10,insertwidth=2, justify='left')
txtCost.grid(row=1, column=1)

btnVat= Button(f1a, font=('Arial', 15, 'bold'), text="VAT =                                             ", command=vatCalc, bd= 15, justify='left')
btnVat.grid(row=2, column=0)    
txtVat=Entry(f1a, font=('Arial', 15, 'bold'), textvariable=ItemCost, bd= 10,insertwidth=4, justify='left')
txtVat.grid(row=2, column=1)

btnTotal= Button(f1a, font=('Arial', 15, 'bold'), text="TOTAL COST =                                ", bd= 15, justify='left')
btnTotal.grid(row=3, column=0)    
txtTotal=Entry(f1a, font=('Arial', 15, 'bold'), textvariable=Totalcost, bd= 10,insertwidth=4, justify='left')
txtTotal.grid(row=3, column=1)

btnClear=Button(f1b,text= "Clear", font=('Arial', 15), command=btnClearDisplay)
btnClear.place(relheight=1, relwidth=0.3)

btnPrint=Button(f1b,text= "Print", font=('Arial', 15))
btnPrint.place(relx=0.70, relheight=1, relwidth=0.3)


root.mainloop()