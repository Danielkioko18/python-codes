from tkinter import*
from tkinter import ttk, filedialog
import pandas as pd
import numpy as np
import matplotlib as plt
import math

root=Tk()
root.title("gui application")
entry=StringVar()
m=StringVar()
labe1=Label(root,text="please enter what you want to read").grid(column=3,row=3)
entry1=Entry(root,bd=5,textvariable=entry).grid(column=3,row=4)
Label(root,text="",textvariable=m,bg="yellow").grid(column=3,row=5)
def read():
    global rd
    global l
    rd=entry.get()
    l=m.get()
    df=pd.read_excel(r'C:\Users\admin\Desktop\New folder\LITE.xlsx')
    df1=df["CRN"]
    df2= df["SUBJ"]
    df3= df["Crse"]
    df4= df["Instructor"]

    #df5= df["Sec"]
    if(rd == 'CRN'):
        m.set(df1)
    elif(rd=='SUBJ'):
        m.set(df2)
    elif (rd == 'Crse'):
        m.set(df3)
    elif (rd == 'Instructor'):
        m.set(df4)
    elif (rd == 'Instructor'):
        m.set(df4)
    else:
        m.set("INPUT A VALID COLUMN")






btn = Button(root, text="read", command=read).grid(column=4,row=4)


root.mainloop()

