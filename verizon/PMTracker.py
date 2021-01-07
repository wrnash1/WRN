#Things to do:
#Market tab when select city use that city to fill data on all the other tabs
#Market tab select PM
#Market Tab Add digital clock with date
#Market tab add Manufacre: Cisco or Ciena
#Market tab Display infomration about the project
#market tab drop down menu need to figure out how to add child menu
#PM Entry all white boxes needs to display values from database and be able to update value to database.
#PM Entry need to figure out how to count text and display an alert of more than 70 char in the issue fields
#PM Entry add scroll bar if text is larger then window
#PM Entry Create dropdown boxes with the following values:
#Green = On Track
#Yellow = At risk
#Red = Jeopardy
#Blue = Complete
#PM Entry pull data from either excel or splunk to fill in all Gray boxes.
#Sites search for all sites from city in Database or splunk and print data to screen
#Circuits search for all circuits in city in Database or splunk and print to screen
#Maps Tab need to be able to store a .jpg image and retrieve to display in Powerpoint
#MAPS Note could be multiple visio pictures.
#Map tab display .jpg image
#ActiveCCR connect to database via an DSN connection and select all Open tickets that is assign to PM
#Then display the data.  When PM click on CCR number it will open a web broswer to CCP.


from tkinter import *
from tkinter import ttk
import sqlite3

#Create sqlite3 database to hold values from PM Entry
conn = sqlite3.connect('verizon.db')
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

#define
def mycomboclick(event):
    myLabel=Label(my_frame1, text=myCombo.get()).pack()

def menu_command():
    pass

def hide_all_frames():
    mycomboclick.pack_forget()
    menu_command.pack_forget()

def count_char(txt):
    result = 0
    for char in txt:
        result +=1
    return result

def submit():
    #need to add all values into the database
    c.execute("INSERT INTO market VALUES('psc_complete', )")

def show_all():
    conn = sqlite3.connect('verizon.db')
    c = conn.cursor()
    #Query the Database
    c.execute("SELECT rowid, * FROM market")
    items = c.fetchall()

def add_records():
    conn = sqlite3.connect('verizon.db')
    c = conn.cursor()
    c.executemany("INSERT INTO market VALUES (?,?,?)", (test, test, test))

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

#create theme
#myVerizon_green = "#546391"
#myVerison_red = "#a14a6e"

#style = ttk.Style()

#style.theme_create( "Verizon", parent="alt", settings={
#    "TNotebook": {"configure": {"tabmargins": [2,5,2,0]}},
#    "TNotebook.Tab": {
#        "configure": {"padding": [5,1], "background": myVerison_red},
#        "map":        {"background": [("selected", myVerizon_green)],
#        "expand": [("selected", [1,1,1,0])]}}})
#style.theme_use("Verizon")



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
