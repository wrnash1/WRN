from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Verizon Project Manager Menu')
#root.iconbitmap('favicon.ico')
p1 = PhotoImage(file = 'Verizon-logo.png') 
root.iconphoto(False, p1)
root.geometry("600x600")

#create theme
myVerizon_green = "#d2ddff"
myVerison_red = "#dad2ff"

style = ttk.Style()

style.theme_create( "Verizon", parent="alt", settings={
    "TNotebook": {"configure": {"tabmargins": [2,5,2,0]}},
    "TNotebook.Tab": {
        "configure": {"padding": [5,1], "background": myVerison_red},
        "map":        {"background": [("selected", myVerizon_green)],
        "expand": [("selected", [1,1,1,0])]}}})
style.theme_use("Verizon")

my_notebook = ttk.Notebook(root)
my_notebook.pack()

my_frame1 = Frame(my_notebook)
my_frame2 = Frame(my_notebook)
my_frame3 = Frame(my_notebook)
my_frame4 = Frame(my_notebook)
my_frame5 = Frame(my_notebook)
my_frame6 = Frame(my_notebook)
my_frame7 = Frame(my_notebook)
my_frame8 = Frame(my_notebook)

my_frame1.pack(fill="both", expand=1)
my_frame2.pack(fill="both", expand=1)
my_frame3.pack(fill="both", expand=1)
my_frame4.pack(fill="both", expand=1)
my_frame5.pack(fill="both", expand=1)
my_frame6.pack(fill="both", expand=1)
my_frame7.pack(fill="both", expand=1)
my_frame8.pack(fill="both", expand=1)

my_notebook.add(my_frame1, text="Market Info")
my_notebook.add(my_frame2, text="PM Entry")
my_notebook.add(my_frame3, text="Sites")
my_notebook.add(my_frame4, text="Circuits")
my_notebook.add(my_frame5, text="PM 5G BH")
my_notebook.add(my_frame6, text="Maps")
my_notebook.add(my_frame7, text="Active CCR's")
my_notebook.add(my_frame8, text="PM Entry")

label_one=Label(my_frame1,text="First Name")
label_one.grid(row=0, column=0)
root.mainloop()