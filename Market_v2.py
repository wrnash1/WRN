from tkinter import *
from tkinter import ttk
import sqlite3
#from tkcalendar import *
import datetime 
import time

#create window
root = Tk()
root.title('UTPM Tracker Verson 1 Alpha')
#root.iconbitmap('favicon.ico')
p1 = PhotoImage(file = 'Verizon-logo.png')
root.iconphoto(False, p1)

try:
    root.attributes('-zoomed', True)  #Linux
except Error:
    root.state('zoomed')  #windows

def menu_command():
    pass

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

def get_time():
    hour_min = time.strftime("%H:%M")
    clock.config(text=hour_min)
    clock.after(200, get_time)

def get_second():
    sec = time.strftime("%S")
    second.config(text=sec)
    second.after(200, get_second)

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

my_frame1=Frame(root, width=100, height=300)
my_frame1.grid(row=0, column=0)
#Market Info
label_market_instructions=Label(my_frame1, text="Please select your City")
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
myCombo.grid(row=3, column=0)


#Create Clock in it's own frame
x = datetime.datetime.now()
clock_canvas = Frame(root, height=400, width=750)
clock_canvas.grid(row=30, column=0)
frame = Canvas(clock_canvas, bg='#696969')
frame.place(relx=0, rely=0, relheight=1, relwidth=1)

#Displays the 24-hour clock 00:00
clock = Label(clock_canvas, fg="#8FBC8F", bg='#696969', font="Verdana 110", anchor="nw")
clock.place(relx=0.05, rely=0.15, relheight=0.6, relwidth=0.7)

#Displays the seconds in clock
second = Label(clock_canvas, fg="#8FBC8F", bg='#696969', font="Verdana 30", anchor="nw")
second.place(relx=0.7, rely=0.55, relheight=0.3, relwidth=0.1)

#Label for month
month = Label(clock_canvas, fg='#BDB76B', bg='#696969', text="MONTH", font="Verdana 15")
month.place(relx=0.790, rely=0.1, relheight=0.15, relwidth=0.2)

#Displays month name, short version (e.g. FEB)
b = Label(clock_canvas, fg='#8FBC8F', bg='#696969', text=x.strftime("%b"), font="Verdana 25 bold")
b.place(relx=0.790, rely=0.230, relheight=0.15, relwidth=0.2)

#Label for date
date = Label(clock_canvas, fg='#BDB76B', bg='#696969', text="DATE", font="Verdana 15")
date.place(relx=0.790, rely=0.380, relheight=0.15, relwidth=0.2)

#Displays day of month
d = Label(clock_canvas, fg='#8FBC8F', bg='#696969', text=x.strftime("%d"), font="Verdana 25 bold")
d.place(relx=0.790, rely=0.51, relheight=0.15, relwidth=0.2)

#Label for weekday
day = Label(clock_canvas, fg='#BDB76B', bg='#696969', text="DAY", font="Verdana 15")
day.place(relx=0.790, rely=0.650, relheight=0.15, relwidth=0.2)

#Displays weekday, short version (e.g. Wed)
a = Label(clock_canvas, fg='#8FBC8F', bg='#696969', text=x.strftime("%a"), font="Verdana 25 bold")
a.place(relx=0.790, rely=0.77, relheight=0.15, relwidth=0.2)

get_time()
get_second()



root.mainloop()