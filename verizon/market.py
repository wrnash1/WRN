from tkinter import *
from tkinter import ttk
import sqlite3
from tkcalendar import *
from datetime import *

#Create sqlite3 database to hold values
conn = sqlite3.connect('market.db')
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

def clock():
    format ="%A %d %b %Y %H:%M:%S"
    today = datetime.now()
    s=today.strftime(format)
    clock_label.config(text=s)
    clock_label.after(1000, clock)

def mycomboclick(event):
    global myCombo
    if myCombo.get() == 'Central':
            myCombo = ttk.Combobox(my_frame1, value=Central)
            myCombo.current(0)
            myCombo.bind("<<ComboboxSelected>>", mycomboclick)
            myCombo.grid(row=3, column=3)
    elif myCombo.get() == 'NorthCentral':
            myCombo = ttk.Combobox(my_frame1, value=NorthCentral)
            myCombo.current(0)
            myCombo.bind("<<ComboboxSelected>>", mycomboclick)
            myCombo.grid(row=3, column=3)
    elif myCombo.get() == 'SouthEast':
            myCombo = ttk.Combobox(my_frame1, value=SouthEast)
            myCombo.current(0)
            myCombo.bind("<<ComboboxSelected>>", mycomboclick)
            myCombo.grid(row=3, column=3)
    elif myCombo.get() == 'West':
            myCombo = ttk.Combobox(my_frame1, value=West)
            myCombo.current(0)
            myCombo.bind("<<ComboboxSelected>>", mycomboclick)
            myCombo.grid(row=3, column=3)
    

#theme
s = ttk.Style()
s.theme_names()
('aqua', 'step','clam', 'alt', 'default', 'classic')
s.theme_use()
'aqua'


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

my_notebook = ttk.Notebook(root)
my_notebook.pack()

my_frame1 = Frame(my_notebook)

my_frame1.pack(fill="both", expand=1)

my_notebook.add(my_frame1, text="Market Info")

#Market Info
label_market_instructions=Label(my_frame1, text="Please select your City")
#label_market_instructions.pack()
label_market_instructions.grid(row=2, column=1)

#define dropdown window
Regions = ['Central', 'NorthCentral', 'Southeast', 'West']
Central = ['Albuquerque', 'Austin', 'Colorado Springs', 'Dallas', 'Denver', 'El Paso', 'Houston', 'Kansas City', 'Little Rock', 'New Orleans', 'Oklahoma City', 'Phoenix', 'Salt Lake City', 'San Antonio', 'Shreveport' , 'St Louis']
NorthCentral = ['Akron', 'Ann Arbor', 'Chicago', 'Cincinnati', 'Cleveland', 'Columbus', 'Des Moines', 'Detroit', 'Grand Rapids', 'Indianapolis', 'Lansing', 'Lexington', 'Louiseville', 'Madison', 'Milwaukee', 'Minneapolis', 'Omaha', 'Youngstown']
West = ['Bakerfield', 'Concord', 'Fresno', 'Las Vegas', 'Los Angeles', 'Mission Viejo', 'Portland', 'Reno', 'Riverside', 'Sacremento', 'San Diego', 'San Francisco', 'San Jose', 'Seattle', 'Spokane']
SouthEast = ['Atlanta', 'Birmingham', 'Charlotte', 'Columbia', 'Durham', 'Greensboro', 'Greenville', 'Jacksonville', 'Knoxville', 'Memphis', 'Nashville', 'Orlando', 'Pensacola', 'Raleigh', 'Tampa', 'Winston Salem']

#Create combobox
myCombo = ttk.Combobox(my_frame1, value=Regions)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", mycomboclick)
myCombo.grid(row=3, column=1)

#Create clock

clock_label = Label(my_frame1, text="", font=("Helvetica", 48))
#clock_label.pack(pady=20)
clock_label.grid(row=1, column=0, columnspan=9)
clock()


#Create Calendar
cal = Calendar(my_frame1, selectmode="day")
#cal.pack(fill="both", expand=True)
cal.grid(row=10, column=0, columnspan=9, sticky="ew", padx=5, pady=10)

root.mainloop()