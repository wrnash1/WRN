from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

import sqlite3

#Create sqlite3 database to hold values from PM Entry
conn = sqlite3.connect('map.db')
c = conn.cursor()

root = Tk()
root.title('UTPM Tracker Verson 1 Alpha')
#root.iconbitmap('favicon.ico')
p1 = PhotoImage(file = 'Verizon-logo.png')
root.iconphoto(False, p1)
try:
    root.attributes('-zoomed', True)  #Linux
except error:
    root.state('zoomed')  #windows

def menu_command():
    pass

def update_map():
    pass

def show_map():
    pass


#new theme
s = ttk.Style()
s.theme_names()
('aqua', 'step','clam', 'alt', 'default', 'classic')
s.theme_use()
'step'

#Menu
file_menu = Menu(root)
root.config(menu=file_menu)
f_menu = Menu(file_menu)
file_menu.add_cascade(label="File", menu=f_menu)
f_menu.add_command(label="Test...", command=menu_command)
f_menu.add_command(label="Exit", command=root.quit)

#Menu tabs
tabs_menu = Menu(file_menu)
file_menu.add_cascade(label="Tabs", menu=tabs_menu)
tabs_menu.add_command(label="Market Info", command=menu_command)
tabs_menu.add_command(label="PM Entry", command=menu_command)
tabs_menu.add_command(label="Sites", command=menu_command)
tabs_menu.add_command(label="Circuits", command=menu_command)
tabs_menu.add_command(label="PM 5G BH", command=menu_command)
tabs_menu.add_command(label="Maps", command=menu_command)
tabs_menu.add_command(label="Active CCRs", command=menu_command)
tabs_menu.add_command(label="PM Entry", command=menu_command)

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



root.mainloop()