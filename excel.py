#importing the required libraries and modules
from  tkinter import*
from tkinter import ttk, filedialog
import numpy
import pandas as pd


#creating a tkinter window frame
root= Tk()
#application title
root.title("EXCEL DISPLAY")
#create object of style widget
style = ttk.Style()
style.theme_use('clam')

#create a frame
frame=Frame(root, bg="green")
frame.pack(pady=20)

#defining a function for opening the excel file
def open():
    filename = filedialog.askopenfilename(title="open file", filetype=(("xlxs files",".*xlsx"),("All Files", "*.")))
    if filename:
        try:
            filename = r"{}".format(filename)
            df=pd.read_excel(filename)
        except ValueError:
            Label.config(text="file could not be opened")
        except FileNotFoundError:
            Label.config(text="file not found")
        #clear all previous data
        clear_treeview()
        #add new  data in the widget
        tree["column"]=list(df.columns)
        tree["show"]="headings"

        #for headings to iterate over the columns
        for col in tree["column"]:
            tree.heading(col, text=col)

        #put data in rows
        df_rows=df.to_numpy().tolist()
        for row in df_rows:
            tree.insert("", "end", values=row)
        tree.pack()

#function to clear the treeview widget
def clear_treeview():
    tree.delete(*tree.get_children())

#creating  treeview widget
tree=ttk.Treeview(frame)


#add menu
m=Menu(root)
root.config(menu=m)

#add menu dropdown
file_menu=Menu(m, tearoff=False)
m.add_cascade(label="Menu", menu=file_menu)
file_menu.add_command(label="Open Excel", command=open)

#add label to display the file content
label=Label(root, text='')
label.pack(pady=20)

root.mainloop()