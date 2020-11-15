from tkinter import *
from tkinter import ttk
import sqlite3

#Create sqlite3 database to hold values from PM Entry
conn = sqlite3.connect('market.db')
c = conn.cursor()

root = Tk()
root.title('Verizon UTPM Tracker Verson 1 Alpha')
#root.iconbitmap('favicon.ico')
p1 = PhotoImage(file = 'Verizon-logo.png')
root.iconphoto(False, p1)
#root.geometry("900x600")
root.state('zoomed')

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

#new theme
s = ttk.Style()
s.theme_names()
('aqua', 'step','clam', 'alt', 'default', 'classic')
s.theme_use()
'step'

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


#Market Info
label_market_instructions=Label(my_frame1, text="Please select your City")
label_market_instructions.pack()


#define dropdown window
options = ['Central', 'NorthCentral', 'Southeast', 'West']
Central = ['Albuquerque', 'Austin', 'Colorado Springs', 'Dallas', 'Denver', 'El Paso', 'Houston', 'Kansas City', 'Little Rock', 'New Orleans', 'Oklahoma City', 'Phoenix', 'Salt Lake City', 'San Antonio', 'Shreveport' , 'St Louis']
NorthCentral = ['Akron', 'Ann Arbor', 'Chicago', 'Cincinnati', 'Cleveland', 'Columbus', 'Des Moines', 'Detroit', 'Grand Rapids', 'Indianapolis', 'Lansing', 'Lexington', 'Louiseville', 'Madison', 'Milwaukee', 'Minneapolis', 'Omaha', 'Youngstown']
West = ['Bakerfield', 'Concord', 'Fresno', 'Las Vegas', 'Los Angeles', 'Mission Viejo', 'Portland', 'Reno', 'Riverside', 'Sacremento', 'San Diego', 'San Francisco', 'San Jose', 'Seattle', 'Spokane']
SouthEast = ['Atlanta', 'Birmingham', 'Charlotte', 'Columbia', 'Durham', 'Greensboro', 'Greenville', 'Jacksonville', 'Knoxville', 'Memphis', 'Nashville', 'Orlando', 'Pensacola', 'Raleigh', 'Tampa', 'Winston Salem']

myCombo = ttk.Combobox(my_frame1, value=options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", mycomboclick)
myCombo.pack()


root.mainloop()