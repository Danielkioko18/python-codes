#====IMPORTING THE REQUIRED LIBRARIES================================================
from tkinter import*
import tkinter.messagebox
import pymysql
import datetime as dt


root = Tk()
root.configure(background="blue")
root.geometry('500x600')
root.title("daniel database")
#============CREATING THE DATABASE CONNNECTOR===================================================
global conn  #==GLOBAL VARIABLE MEANS IT CAN BE CALLED IN ANY FUNCTION
conn = pymysql.connect(host='localhost', user='root', password='', database='testing')

#===============================TEXT VARIABLES TO BE USED IN THE ENTRIES=============================
ID = StringVar()
Name = StringVar()
Adm = StringVar()
Gender = StringVar()
date = dt.datetime.now()
format_date = f"{date:%d/%m/%Y}"

#===========FUNCTION FOR INSERTING DATA INTO THE DATAASE USING BUTTON========================

def register():
    if Name.get() == "" or Adm.get() == "":
        tkinter.messagebox.showerror("Error","The fields must be filled")
    else:
        try:
            cur = conn.cursor()
            query = "INSERT INTO students(ID, NAME, ADM, GENDER) VALUES(%s,%s,%s,%s)"
            VAL = ("", Name.get(), Adm.get(), Gender.get())
            cur.execute(query, VAL)
            conn.commit()
            conn.close()
            Name.set("")
            Adm.set("")
            Gender.set("")
            tkinter.messagebox.showinfo("Success", "Record saved successfully")
        except:
            tkinter.messagebox.showerror("Error", "Error Occured")



#============================== The Widgets==========================================================

l1 = Label(root, text="mysql database entry", bg="blue", font=("oswald", 24, "bold")).grid(column=1,row=0)

l2 = Label(root, text="Full Name", bg="blue", font=("oswald", 20, "bold")).grid(column=0, row=2,sticky=W)
entry2 = Entry(root, textvariable=Name, bd=5, bg="sky blue", relief=SUNKEN, font=("oswald", 12, "bold")).grid(column=1,row=2)

l3 = Label(root, text="Admission", bg="blue",font=("oswald",20,"bold")).grid(column=0, row=3,sticky=W)
entry3 = Entry(root, textvariable=Adm, bd=5, bg="sky blue", relief=SUNKEN,font=("oswald", 12, "bold")).grid(column=1,row=3)

l4 = Label(root, text="Gender", bg="blue", font=("oswald", 20, "bold")).grid(column=0, row=4, sticky=W)
entry4 = Entry(root, textvariable=Gender, bd=5, bg="sky blue", relief=SUNKEN, font=("oswald", 12, "bold"))
entry4.insert(END,format_date)
entry4.grid(column=1,row=4)


btn1 = Button(root, text="Register", bd=5, relief=RAISED, command=register, bg="green",font=("oswald",20,"bold")).grid(column=1,row=5)


root.mainloop()
