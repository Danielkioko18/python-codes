from tkinter import *
from tkinter import messagebox
import openpyxl
from openpyxl import Workbook


def Verification(*args):
    value = ZT1.get()
    if len(value) != 6 or value[:1] != "T" or not value[1:6].isdigit():
        messagebox.showwarning("Error", "ID not valide")
        ZT1.delete(0, END)


# Put the value of Col "I" in ZT2 (if the ID is found in Col "B" of course)

fen = Tk()
fen.state('zoomed')
fen.title('Rapports CCU')
Label1 = Label(fen, text="N° ID :", font='times')
Label1.place(x=35, y=16)

Label2 = Label(fen, text="Region :", font='times')
Label2.place(x=268, y=16)

ZT1 = Entry(fen, width=17, justify='center', bg="#aee6ff")
ZT1.place(x=155, y=20)
ZT1.bind("<Return>", Verification)

ZT2 = Text(fen, width=13, height=1, bg="#c9d4ff")
ZT2.place(x=405, y=20)
ZT2.config(state=DISABLED)

wb = openpyxl.load_workbook('My_Excel.xlsx')
ws = wb.active

fen.mainloop()
