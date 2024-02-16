from tkinter import*
import pymysql

#connecting to the database
conn = pymysql.connect(host='localhost',user='root',password='',database='testing')


#defining a function to insert data to the database tables
def register():
    adm1 = adm.get()
    name1 = name.get()
    date1 = date.get()
    gender1 = gender.get()
    #applying empty validation
def register():
    global reg_screen
    root = Tk()
    #setting tittle for the screen
    root.title("REGISTER FORM")
    #DECLARING VARIABLES
    global message
    global adm
    global name
    global date
    global gender

    adm = IntVar()
    name = StringVar()
    date = StringVar()
    gender = StringVar()
    message = StringVar()
    #creating layout of the registration form
    Label(root,width="300", text="please enter details below")
    #admission label
    Label(root, text="ADMISSION NUMBER").place(x=20,y=40)
    #admission textbox
    Entry(root, textvariable=adm).place(x=90, y=42)
    #name label
    Label(root, text="NAME").place(x=20,y=80)
    #NAME ENTRY TEXTBOX
    Entry(root, textvariable=name).place(x=90, y=82)
    #label for date
    Label(root, text="DATE").place(x=20, y=120)
    #date entry textbox
    Entry(root, textvariable=date).place(x=90, y=122)
    #gender label
    Label(root, text="GENDER").place(x=20, y=160)
    # date entry textbox
    Entry(root, textvariable=gender).place(x=90, y=162)
    #Label(root, text="GENDER").place(x=20, y=160)
    #GENDER RADIO BUTTON

    Label(root, text="", textvariable=message).place(x=95,y=264)
    #BUTTON FOR REGISTRATION
    Button(root, text="Register", width=10, height=1, bg="orange", command=register).place(x=105, y=300)
    root.mainloop()

def registrationForm():
    global reg_screen
    root = Tk()
    #setting tittle for the screen
    root.title("REGISTRATION FORM")
    #DECLARING VARIABLES
    global message
    global adm
    global name
    global date
    global gender

    adm = IntVar()
    name = StringVar()
    date = StringVar()
    gender = StringVar()
    message = StringVar()
    #creating layout of the registration form
    Label(root,width="300", text="please enter details below")
    #admission label
    Label(root, text="ADMISSION NUMBER").place(x=20,y=40)
    #admission textbox
    Entry(root, textvariable=adm).place(x=90, y=42)
    #name label
    Label(root, text="NAME").place(x=20,y=80)
    #NAME ENTRY TEXTBOX
    Entry(root, textvariable=name).place(x=90, y=82)
    #label for date
    Label(root, text="DATE").place(x=20, y=120)
    #date entry textbox
    Entry(root, textvariable=date).place(x=90, y=122)
    #gender label
    Label(root, text="GENDER").place(x=20, y=160)
    # date entry textbox
    Entry(root, textvariable=gender).place(x=90, y=162)
    #Label(root, text="GENDER").place(x=20, y=160)
    #GENDER RADIO BUTTON

    Label(root, text="", textvariable=message).place(x=95,y=264)
    #BUTTON FOR REGISTRATION
    Button(root, text="Register", width=10, height=1, bg="orange", command=register).place(x=105, y=300)
    root.mainloop()
#calling the function registrationForm


