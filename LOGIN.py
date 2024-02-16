from tkinter import*
import tkinter.messagebox
from PIL import ImageTk,Image
import  connection_mysql

global root
global pas
global user
root=Tk()
root.config(background="maroon")
myimage=Image.open("hac.png")
resized=myimage.resize((30, 30),Image.ANTIALIAS)
newimage=ImageTk.PhotoImage(resized)
pas=StringVar()
user=StringVar()
global username
global password
lab3=Label(root, text="enter username").grid(column=0,row=0)
E1=Entry(root,textvariable=user).grid(column=1,row=0)
lab4=Label(root, text="enter password").grid(column=0,row=1)
E2=Entry(root,textvariable=pas).grid(column=1,row=1)


def window2():
    password = pas.get()
    username = user.get()
    if ((password==str("12345")) and (username==str("daniel"))):
        root.destroy()
        connection_mysql.register()
    else:
        tkinter.messagebox.showinfo("System", "You have entered incorrect login details")

btn=Button(root,image=newimage,command=window2,relief=RAISED).grid(column=1,row=2)

mainloop()
