#--------calling required modules-------------------------
from tkinter import*
from tkinter import messagebox
import pymysql


def close():
    root.destroy()


def clear():
    UserName.delete(0, END)
    passEntry.delete(0, END)

#----------------------ADMIN LOGIN -----------------------------------------------------
def admin():
    admin = Tk()
    admin.title("PYTHON DATABASE LOGIN APP")
    admin.configure(background="green")
    admin.geometry('500x450')

    def close():
        admin.destroy()

    def clear():
        UserName.delete(0, END)
        passEntry.delete(0, END)

    # ----------------------ADMIN LOGIN -----------------------------------
    def admlogin():
        if user.get() == "" or password.get() == "":
            messagebox.showerror("Error", "Enter User Name And Password", parent=admin)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="python")
                cur = con.cursor()

                cur.execute("select * from user_information where username=%s and password = %s",
                            (user.get(), password.get()))
                row = cur.fetchone()

                if row == None:
                    messagebox.showerror("Error", "Invalid User Name And Password", parent=admin)

                else:
                    messagebox.showinfo("Success", "Successfully Login", parent=admin)

                    close()
                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=admin)

    user = StringVar()
    password = StringVar()

    titleLabel = Label(admin, text="PYTHON DATABASE LOGIN APP", bg="red", relief="flat", font=("oswald", 20, "bold"))
    titleLabel.pack()

    loginEntry = LabelFrame(admin, text="Login", bg="Blue", bd=5, padx=20, pady=50, font=("times", 18, "bold"),
                            relief=RIDGE)
    loginEntry.place(x=1, y=60)

    User1 = Label(loginEntry, text="Username:", font=("Verdana", 18, "bold"), bg="blue", fg="white")
    User1.grid(column=0, row=0)
    UserName = Entry(loginEntry, textvariable=user, font=("Verdana", 14, "bold"), bg="yellow", relief=SUNKEN)
    UserName.grid(column=1, row=0)

    PASS1 = Label(loginEntry, text="Password:", font=("Verdana", 18, "bold"), bg="blue", fg="white")
    PASS1.grid(column=0, row=1)
    passEntry = Entry(loginEntry, textvariable=password, show="*", font=("Verdana", 14, "bold"), bg="yellow",
                      relief=SUNKEN)
    passEntry.grid(column=1, row=1)

    loginButton = Button(loginEntry, command=login, text="Login", bg="orange", fg="blue", activebackground="red",
                         activeforeground="green", relief=RAISED, font=("Verdana", 12, "bold"))
    loginButton.place(x=150, y=80)

    clearButton = Button(loginEntry, command=clear, text="Clear", bg="green", fg="red", activebackground="red",
                         activeforeground="green", relief=RAISED, font=("Verdana", 12, "bold"))
    clearButton.place(x=250, y=80)

    regButton = Button(admin, command=admin, text="ADMIN", bg="yellow", fg="red", activebackground="red",
                       activeforeground="green", relief=RAISED, font=("Verdana", 16, "bold"))
    regButton.place(x=190, y=300)

    admin.mainloop()
def login():
    if user.get() == "" or password.get() == "":
        messagebox.showerror("Error", "Enter User Name And Password", parent=root)
    else:
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="python")
            cur = con.cursor()

            cur.execute("select * from user_information where username=%s and password = %s",
                        (user.get(), password.get()))
            row = cur.fetchone()

            if row == None:
                messagebox.showerror("Error", "Invalid User Name And Password", parent=root)

            else:
                messagebox.showinfo("Success", "Successfully Login", parent=root)
                close()
                admin()
            con.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=root)

#-----------------Login windoww----------------------------------------------------------------------

root=Tk()
root.title("PYTHON DATABASE LOGIN APP")
root.configure(background="green")
root.geometry('500x450')

user=StringVar()
password=StringVar()

titleLabel = Label(root, text="PYTHON DATABASE LOGIN APP", bg="red", relief="flat", font=("oswald", 20, "bold"))
titleLabel.pack()

loginEntry = LabelFrame(root, text="Login", bg="Blue", bd=5,  padx=20, pady=50, font=("times", 18,"bold"), relief=RIDGE)
loginEntry.place(x=1, y=60)

User1 = Label(loginEntry, text="Username:", font=("Verdana", 18, "bold"), bg="blue", fg="white")
User1.grid(column=0, row=0)
UserName = Entry(loginEntry, textvariable=user, font=("Verdana", 14, "bold"), bg="yellow", relief=SUNKEN)
UserName.grid(column=1, row=0)

PASS1 = Label(loginEntry, text="Password:", font=("Verdana", 18, "bold"), bg="blue", fg="white")
PASS1.grid(column=0, row=1)
passEntry = Entry(loginEntry, textvariable=password, show="*", font=("Verdana", 14, "bold"), bg="yellow", relief=SUNKEN)
passEntry.grid(column=1, row=1)

loginButton=Button(loginEntry, command = login, text="Login", bg="orange", fg="blue", activebackground="red", activeforeground="green", relief=RAISED, font=("Verdana", 12, "bold"))
loginButton.place(x=150, y=80)

clearButton=Button(loginEntry, command = clear, text="Clear", bg="green", fg="red", activebackground="red", activeforeground="green", relief=RAISED, font=("Verdana", 12, "bold"))
clearButton.place(x=250, y=80)

regButton=Button(root, command=admin,text="ADMIN", bg="yellow", fg="red", activebackground="red", activeforeground="green", relief=RAISED, font=("Verdana", 16, "bold"))
regButton.place(x=190, y=300)

root.mainloop()