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
root.title('Verizon UTPM Tracker Verson 1 Alpha')
#root.iconbitmap('favicon.ico')
p1 = PhotoImage(file = 'Verizon-logo.png')
root.iconphoto(False, p1)
#root.geometry("900x600")
root.state('zoomed')


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

#PM Entry

#create label
label_market=Label(my_frame2,text="Per Market", anchor=CENTER)
label_cheetah=Label(my_frame2, text="Cheetah/PMO Data", anchor=CENTER)
label_complete=Label(my_frame2, text="Complete")
label_total=Label(my_frame2,text="Total")
label_complete1=Label(my_frame2, text="Complete")
label_total1=Label(my_frame2,text="Total")
label_PM_Entry=Label(my_frame2, text="PM Entry")
label_Internal_Notes=Label(my_frame2, text="Internal Notes / Data Collection")
label_Instructions=Label(my_frame2, text="Instructions")
label_cheetah.grid(row=0, column=3, columnspan=2) #Cheetah/PMO Data
label_PM_Entry.grid(row=0, column=5, columnspan=3) #PM Entry
label_market.grid(row=1, column=0, columnspan=2) #Per Market
label_complete1.grid(row=1, column=3) #Complete
label_total1.grid(row=1, column=4) #Total
label_complete.grid(row=1, column=5)
label_total.grid(row=1, column=6)
label_Internal_Notes.grid(row=1, column=7)
label_Instructions.grid(row=1, column=8)

label_total_Market=Label(my_frame2, text="Total Market Deliverables", bg="black", fg="white", anchor=CENTER)
label_total_Market.grid(row=2, column=0, columnspan=9, sticky="ew")

label_psc=Label(my_frame2, text="PSC", bg="sky blue")
psc_instructions=Label(my_frame2, text="Number of sites requiring Power/Structure/Cooling in support of site NEATs; Total equals total NEATs", anchor=W, bg="sky blue")
psc_complete=Entry(my_frame2, width=10)
psc_total=Entry(my_frame2, width=10)
psc_notes=Entry(my_frame2, width=70)
psc_cheetah_complete=Entry(my_frame2, width=10, bg="gray")
psc_cheetah_total=Entry(my_frame2, width=10, bg="gray")
label_psc.grid(row=3, column=1, columnspan=2, sticky="ew")
psc_instructions.grid(row=3, column=8, sticky="ew")
psc_complete.grid(row=3, column=5)
psc_total.grid(row=3, column=6)
psc_notes.grid(row=3, column=7)
psc_cheetah_complete.grid(row=3, column=3)
psc_cheetah_total.grid(row=3, column=4)

label_neat=Label(my_frame2, text="NEATs", bg="sky blue")
neat_instructions=Label(my_frame2, text="Number of sites within the market tracking towards NEAT Complete", anchor=W, bg="sky blue")
neat_complete=Entry(my_frame2, width=10)
neat_total=Entry(my_frame2, width=10)
neat_notes=Entry(my_frame2, width=70)
neat_cheetah_complete=Entry(my_frame2, width=10, bg="gray")
neat_cheetah_total=Entry(my_frame2, width=10, bg="gray")
label_neat.grid(row=4, column=1, sticky="ew")
neat_instructions.grid(row=4, column=8, sticky="ew")
neat_complete.grid(row=4, column=5)
neat_total.grid(row=4, column=6)
neat_notes.grid(row=4, column=7)
neat_cheetah_complete.grid(row=4, column=3)
neat_cheetah_total.grid(row=4, column=4)

label_fiber=Label(my_frame2, text="Fiber S&T (Total Spans)", bg="sky blue")
fiber_instructions=Label(my_frame2, text="Fiber S&T: cable-placed and Spliced & Tested by fiber vendor. Next step would be FIM task. Total is equal to number of OM96 NFIDs for your market.", anchor=W, bg="sky blue")
fiber_Complete=Entry(my_frame2, width=10)
fiber_total=Entry(my_frame2, width=10)
fiber_notes=Entry(my_frame2, width=70)
fiber_cheetah_complete=Entry(my_frame2, width=10, bg="gray")
fiber_cheetah_total=Entry(my_frame2, width=10, bg="gray")
label_fiber.grid(row=5, column=1, sticky="ew")
fiber_instructions.grid(row=5, column=8, sticky="ew")
fiber_Complete.grid(row=5, column=5)
fiber_total.grid(row=5, column=6)
fiber_notes.grid(row=5, column=7)
fiber_cheetah_complete.grid(row=5, column=3)
fiber_cheetah_total.grid(row=5, column=4)

label_om96=Label(my_frame2, text = "OM96s In Effect", bg="sky blue")
om96_instructions=Label(my_frame2, text="OM96s In-Effect: spans that are RFT In-Effect \(exclude Path G SAP MSE\)", anchor=W, bg="sky blue")
om96_complete=Entry(my_frame2, width=10)
om96_total=Entry(my_frame2, width=10)
om96_notes=Entry(my_frame2, width=70)
om96_cheetah_complete=Entry(my_frame2, width=10, bg="gray")
om96_cheetah_total=Entry(my_frame2, width=10, bg="gray")
label_om96.grid(row=6, column=1, sticky="ew")
om96_instructions.grid(row=6, column=8, sticky="ew")
om96_complete.grid(row=6, column=5)
om96_total.grid(row=6, column=6)
om96_notes.grid(row=6, column=7)
om96_cheetah_complete.grid(row=6, column=3)
om96_cheetah_total.grid(row=6, column=4)

label_kpi_Nat=Label(my_frame2, text="KPI NATs", bg="sky blue")
kpi_Nat_instructions=Label(my_frame2, text="NATs: tracking of KPI NAT count for your market.", anchor=W, bg="sky blue")
kpi_Nat_Complete=Entry(my_frame2, width=10)
kpi_Nat_total=Entry(my_frame2, width=10)
kpi_Nat_notes=Entry(my_frame2, width=70)
kpi_cheetah_complete=Entry(my_frame2, width=10, bg="gray")
kpi_cheetah_total=Entry(my_frame2, width=10, bg="gray")
label_kpi_Nat.grid(row=7, column=1, sticky="ew")
kpi_Nat_instructions.grid(row=7, column=8, sticky="ew")
kpi_Nat_Complete.grid(row=7, column=5)
kpi_Nat_total.grid(row=7, column=6)
kpi_Nat_notes.grid(row=7, column=7)
kpi_cheetah_complete.grid(row=7, column=3)
kpi_cheetah_total.grid(row=7, column=4)

label_10G_BH_A=Label(my_frame2, text="10G BH Circuits (Path A) Total", bg="sky blue")
E_10G_BH_A_instructions=Label(my_frame2, text="10G BH Circuits(Path A): circuit count from all 5G/CRAN hub sites and fiber-only extensions sites back to MSC", anchor=W, bg="sky blue")
E_10G_BH_A_Complete=Entry(my_frame2, width=10)
E_10G_BH_A_total=Entry(my_frame2, width=10)
E_10G_BH_A_notes=Entry(my_frame2, width=70)
E_10G_BH_A_cheetah_complete=Entry(my_frame2, width=10, bg="gray")
E_10G_BH_A_cheetah_total=Entry(my_frame2, width=10, bg="gray")
label_10G_BH_A.grid(row=8, column=1, sticky="ew")
E_10G_BH_A_instructions.grid(row=8, column=8, sticky="ew")
E_10G_BH_A_Complete.grid(row=8, column=5)
E_10G_BH_A_total.grid(row=8, column=6)
E_10G_BH_A_notes.grid(row=8, column=7)
E_10G_BH_A_cheetah_complete.grid(row=8, column=3)
E_10G_BH_A_cheetah_total.grid(row=8, column=4)

label_10G_BH_B=Label(my_frame2, text="10G BH Circuits (Path B) Total", bg="sky blue")
E_10G_BH_B_instructions=Label(my_frame2, text="10G BH Circuits(Path B): circuit count from all 5G/CRAN hub sites and fiber-only extensions sites back to MSC", anchor=W, bg="sky blue")
E_10G_BH_B_Complete=Entry(my_frame2, width=10)
E_10G_BH_B_total=Entry(my_frame2, width=10)
E_10G_BH_B_notes=Entry(my_frame2, width=70)
E_10G_BH_B_cheetah_complete=Entry(my_frame2, width=10, bg="gray")
E_10G_BH_B_cheetah_total=Entry(my_frame2, width=10, bg="gray")
label_10G_BH_B.grid(row=9, column=1, sticky="ew")
E_10G_BH_B_instructions.grid(row=9, column=8, sticky="ew")
E_10G_BH_B_Complete.grid(row=9, column=5)
E_10G_BH_B_total.grid(row=9, column=6)
E_10G_BH_B_notes.grid(row=9, column=7)
E_10G_BH_B_cheetah_complete.grid(row=9, column=3)
E_10G_BH_B_cheetah_total.grid(row=9, column=4)

label_consumption=Label(my_frame2, text="Consumption Order Total", bg="sky blue")
consumption_instructions=Label(my_frame2, text="Count of all received consumption orders for the market", anchor=W, bg="sky blue")
consumption_Complete=Entry(my_frame2, width=10)
consumption_total=Entry(my_frame2, width=10)
consumption_notes=Entry(my_frame2, width=70)
consumption_cheetah_complete=Entry(my_frame2, width=10, bg="gray")
consumption_cheetah_total=Entry(my_frame2, width=10, bg="gray")
label_consumption.grid(row=10, column=1, sticky="ew")
consumption_instructions.grid(row=10, column=8, sticky="ew")
consumption_Complete.grid(row=10, column=5)
consumption_total.grid(row=10, column=6)
consumption_notes.grid(row=10, column=7)
consumption_cheetah_complete.grid(row=10, column=3)
consumption_cheetah_total.grid(row=10, column=4)

label_fiber_loops=Label(my_frame2, text="Fiber Loops", bg="sky blue")
fiber_loops_instructions=Label(my_frame2, text="Count of delivered Fiber and total number of Loops ", anchor=W, bg="sky blue")
fiber_loops_Complete=Entry(my_frame2, width=10)
fiber_loops_total=Entry(my_frame2, width=10)
fiber_loops_notes=Entry(my_frame2, width=70)
fiber_loops_cheetah_complete=Entry(my_frame2, width=10, bg="gray")
fiber_loops_cheetah_total=Entry(my_frame2, width=10, bg="gray")
label_fiber_loops.grid(row=11, column=1, sticky="ew")
fiber_loops_instructions.grid(row=11, column=8, sticky="ew")
fiber_loops_Complete.grid(row=11, column=5)
fiber_loops_total.grid(row=11, column=6)
fiber_loops_notes.grid(row=11, column=7)
fiber_loops_cheetah_complete.grid(row=11, column=3)
fiber_loops_cheetah_total.grid(row=11, column=4)

label_ER_Uplinks=Label(my_frame2, text="ER Uplinks", bg="sky blue")
ER_Uplinks_instructions=Label(my_frame2, text="Count of the appropriately ER to IHR or RHR uplinks, 2 per ER site", anchor=W, bg="sky blue")
ER_Uplinks_Complete=Entry(my_frame2, width=10)
ER_Uplinks_total=Entry(my_frame2, width=10)
ER_Uplinks_notes=Entry(my_frame2, width=70)
ER_Uplinks_cheetah_complete=Entry(my_frame2, width=10, bg="gray")
ER_Uplinks_cheetah_total=Entry(my_frame2, width=10, bg="gray")
label_ER_Uplinks.grid(row=12, column=1, sticky="ew")
ER_Uplinks_instructions.grid(row=12, column=8, sticky="ew")
ER_Uplinks_Complete.grid(row=12, column=5)
ER_Uplinks_total.grid(row=12, column=6)
ER_Uplinks_notes.grid(row=12, column=7)
ER_Uplinks_cheetah_complete.grid(row=12, column=3)
ER_Uplinks_cheetah_total.grid(row=12, column=4)

label_IHR=Label(my_frame2, text="IHR - RHR Uplinks", bg="sky blue")
IHR_instructions=Label(my_frame2, text="Count of the appropriately IHR to RHR uplinks, 2 per IHR site", anchor=W, bg="sky blue")
IHR_Complete=Entry(my_frame2, width=10)
IHR_total=Entry(my_frame2, width=10)
IHR_notes=Entry(my_frame2, width=70)
IHR_cheetah_complete=Entry(my_frame2, width=10, bg="gray")
IHR_cheetah_total=Entry(my_frame2, width=10, bg="gray")
label_IHR.grid(row=13, column=1, sticky="ew")
IHR_instructions.grid(row=13, column=8, sticky="ew")
IHR_Complete.grid(row=13, column=5)
IHR_total.grid(row=13, column=6)
IHR_notes.grid(row=13, column=7)
IHR_cheetah_complete.grid(row=13, column=3)
IHR_cheetah_total.grid(row=13, column=4)

Pri_5G_CRAN=Label(my_frame2, text="Priority 5G CRAN only", bg="black", fg="white", anchor=CENTER)
Pri_5G_CRAN.grid(row=14, column=0, columnspan=9, sticky="ew")

label_P_5G_CRANS=Label(my_frame2, text="Priority 5G CRANS", bg="sky blue")
P_5G_CRANS_instructions=Label(my_frame2, text="Number of 5G Priority CRAN sites (as indicated by the red \"5G\" on diagrams)", anchor=W, bg="sky blue")
P_5G_CRANS_complete=Entry(my_frame2, width=10, bg="gray")
P_5G_CRANS_total=Entry(my_frame2, width=10)
P_5G_CRANS_notes=Entry(my_frame2, width=70)
P_5G_CRANS_cheetah_complete=Entry(my_frame2, width=10, bg="gray")
P_5G_CRANS_cheetah_total=Entry(my_frame2, width=10, bg="gray")
label_P_5G_CRANS.grid(row=15, column=1, sticky="ew")
P_5G_CRANS_instructions.grid(row=15, column=8, sticky="ew")
P_5G_CRANS_complete.grid(row=15, column=5)
P_5G_CRANS_total.grid(row=15, column=6)
P_5G_CRANS_notes.grid(row=15, column=7)
P_5G_CRANS_cheetah_complete.grid(row=15, column=3)
P_5G_CRANS_cheetah_total.grid(row=15, column=4)

label_P_5G_consumption=Label(my_frame2, text = "Priority 5G CRANS Consumption Orders Received", bg="sky blue")
P_5G_consumption_instructions=Label(my_frame2, text="Number of priority 5G CRAN consumption orders created.", anchor=W, bg="sky blue")
P_5G_consumption_Complete=Entry(my_frame2, width=10)
P_5G_consumption_total=Entry(my_frame2, width=10)
P_5G_consumption_notes=Entry(my_frame2, width=70)
P_5G_consumption_cheetah_complete=Entry(my_frame2, width=10, bg="gray")
P_5G_consumption_cheetah_total=Entry(my_frame2, width=10, bg="gray")
label_P_5G_consumption.grid(row=16, column=1, sticky="ew")
P_5G_consumption_instructions.grid(row=16, column=8, sticky="ew")
P_5G_consumption_Complete.grid(row=16, column=5)
P_5G_consumption_total.grid(row=16, column=6)
P_5G_consumption_notes.grid(row=16, column=7)
P_5G_consumption_cheetah_complete.grid(row=16, column=3)
P_5G_consumption_cheetah_total.grid(row=16, column=4)

label_P_5G_Circuits=Label(my_frame2, text="Priority 5G CRAN Circuits in Effect", bg="sky blue")
P_5G_Circuits_instructions=Label(my_frame2, text="Number of completed priority 5G CRAN 10G BH circuits.  RFT/NAT status of these selected 10G BH circuits.", anchor=W, bg="sky blue")
P_5G_Circuits_Complete=Entry(my_frame2, width=10)
P_5G_Circuits_total=Entry(my_frame2, width=10)
P_5G_Circuits_notes=Entry(my_frame2, width=70)
P_5G_Circuits_cheetah_complete=Entry(my_frame2, width=10, bg="gray")
P_5G_Circuits_cheetah_total=Entry(my_frame2, width=10, bg="gray")
label_P_5G_Circuits.grid(row=17, column=1, sticky="ew")
P_5G_Circuits_instructions.grid(row=17, column=8, sticky="ew")
P_5G_Circuits_Complete.grid(row=17, column=5)
P_5G_Circuits_total.grid(row=17, column=6)
P_5G_Circuits_notes.grid(row=17, column=7)
P_5G_Circuits_cheetah_complete.grid(row=17, column=3)
P_5G_Circuits_cheetah_total.grid(row=17, column=4)

label_target_Date=Label(my_frame2, text="Target Date", bg="sky blue")
target_Date_instructions=Label(my_frame2, text="Date that all 5G Priority Backhaul circuits are complete", anchor=W, bg="sky blue")
target_Date_complete=Entry(my_frame2, width=10, bg="gray")
target_Date_total=Entry(my_frame2, width=10)
target_Date_notes=Entry(my_frame2, width=70)
target_Date_cheetah_complete=Entry(my_frame2, width=10, bg="gray")
target_Date_cheetah_total=Entry(my_frame2, width=10, bg="gray")
label_target_Date.grid(row=18, column=1, sticky="ew")
target_Date_instructions.grid(row=18, column=8, sticky="ew")
target_Date_complete.grid(row=18, column=5)
target_Date_total.grid(row=18, column=6)
target_Date_notes.grid(row=18, column=7)
target_Date_cheetah_complete.grid(row=18, column=3)
target_Date_cheetah_total.grid(row=18, column=4)

label_E_Line=Label(my_frame2, text = "E-Line", bg="black", fg="white", anchor=CENTER)
label_E_Line.grid(row=19, column=0, columnspan=9, sticky="ew")

label_MPLS_75=Label(my_frame2, text = "MPLS Current 75% Complete", bg="sky blue")
MPLS_75_instructions=Label(my_frame2, text = "Quarter that 75% of the ER (ER-IHR) are complete; requires all IHR & RHR (IHR-RHR) to be complete;  xQyy in first block;  Use the dropdown menu to select status", anchor=W, bg="sky blue")
MPLS_75_Complete=Entry(my_frame2, width=10)
MPLS_75_total=Entry(my_frame2, width=10, bg="green")
MPLS_75_notes=Entry(my_frame2, width=70)
MPLS_75_cheetah_complete=Entry(my_frame2, width=10, bg="gray")
MPLS_75_cheetah_total=Entry(my_frame2, width=10, bg="gray")
label_MPLS_75.grid(row=20, column=1, sticky="ew")
MPLS_75_instructions.grid(row=20, column=8)
MPLS_75_Complete.grid(row=20, column=5)
MPLS_75_total.grid(row=20, column=6)
MPLS_75_notes.grid(row=20, column=7)
MPLS_75_cheetah_complete.grid(row=20, column=3)
MPLS_75_cheetah_total.grid(row=20, column=4)

label_MPLS_90=Label(my_frame2, text = "MPLS Current 90% Complete", bg="sky blue")
MPLS_90_instructions=Label(my_frame2, text = "Quarter that 90% of the ER (ER-IHR) are complete; requires all IHR & RHR (IHR-RHR) to be complete;  xQyy in first block;   Use the dropdown menu to select status", anchor=W, bg="sky blue")
MPLS_90_Complete=Entry(my_frame2, width=10)
MPLS_90_total=Entry(my_frame2, width=10, bg="green")
MPLS_90_Notes=Entry(my_frame2, width=70)
MPLS_90_cheetah_complete=Entry(my_frame2, width=10, bg="gray")
MPLS_90_cheetah_total=Entry(my_frame2, width=10, bg="gray")
label_MPLS_90.grid(row=21, column=1, sticky="ew")
MPLS_90_instructions.grid(row=21, column=8, sticky="ew")
MPLS_90_Complete.grid(row=21, column=5)
MPLS_90_total.grid(row=21, column=6)
MPLS_90_Notes.grid(row=21, column=7)
MPLS_90_cheetah_complete.grid(row=21, column=3)
MPLS_90_cheetah_total.grid(row=21, column=4)

label_Current_Complete=Label(my_frame2, text="Current % Complete", bg="sky blue")
Current_Complete_instructions=Label(my_frame2, text="The current percentage of completed ER (ER-IHR) installations; requires all IHR & RHR (IHR-RHR) to be complete;  XX% in first block", anchor=W, bg="sky blue")
Current_Complete_complete=Entry(my_frame2, width=10)
Current_Complete_total=Entry(my_frame2, width=10, bg="gray")
Current_Complete_notes=Entry(my_frame2, width=70)
Current_Complete_cheetah_complete=Entry(my_frame2, width=10, bg="gray")
Current_Complete_cheetah_total=Entry(my_frame2, width=10, bg="gray")
label_Current_Complete.grid(row=22, column=1, sticky="ew")
Current_Complete_instructions.grid(row=22, column=8, sticky="ew")
Current_Complete_complete.grid(row=22, column=5)
Current_Complete_total.grid(row=22, column=6)
Current_Complete_notes.grid(row=22, column=7)
Current_Complete_cheetah_complete.grid(row=22, column=3)
Current_Complete_cheetah_total.grid(row=22, column=4)

label_e_Line_P=Label(my_frame2, text ="E-Line Priority", bg="sky blue")
e_Line_P_instructions=Label(my_frame2, text ="What is the overall PM status of the ELINE installation;  Use the dropdown menu to select status", anchor=W, bg="sky blue")
e_Line_P_complete=Entry(my_frame2, width=10, bg="gray")
e_Line_P_total=Entry(my_frame2, width=10, bg="green")
e_Line_P_notes=Entry(my_frame2, width=70)
e_Line_P_cheetah_complete=Entry(my_frame2, width=10, bg="gray")
e_Line_P_cheetah_total=Entry(my_frame2, width=10, bg="gray")
label_e_Line_P.grid(row=23, column=1, sticky="ew")
e_Line_P_instructions.grid(row=23, column=8, sticky="ew")
e_Line_P_complete.grid(row=23, column=5)
e_Line_P_total.grid(row=23, column=6)
e_Line_P_notes.grid(row=23, column=7)
e_Line_P_cheetah_complete.grid(row=23, column=3)
e_Line_P_cheetah_total.grid(row=23, column=4)

lable_5G_P=Label(my_frame2, text ="5G priority", bg="sky blue")
e_5G_P_instructions=Label(my_frame2, text ="What is the overall PM Status of the 5G Priority Backhaul;  Use the dropdown menu to select status", anchor=W, bg="sky blue")
e_5g_P_complete=Entry(my_frame2, width=10, bg="gray")
e_5g_P_total=Entry(my_frame2, width=10, bg="green")
e_5g_P_notes=Entry(my_frame2, width=70)
e_5g_P_cheetah_complete=Entry(my_frame2, width=10, bg="gray")
e_5g_P_cheetah_total=Entry(my_frame2, width=10, bg="gray")
lable_5G_P.grid(row=24, column=1, sticky="ew")
e_5G_P_instructions.grid(row=24, column=8, sticky="ew")
e_5g_P_complete.grid(row=24, column=5)
e_5g_P_total.grid(row=24, column=6)
e_5g_P_notes.grid(row=24, column=7)
e_5g_P_cheetah_complete.grid(row=24, column=3)
e_5g_P_cheetah_total.grid(row=24, column=4)


#Issues section
ttk.Separator(my_frame2,orient=HORIZONTAL).grid(row=25, column=0, columnspan=8, ipadx=300)

label_UT_Build=Label(my_frame2, text = "UT Build Issues", bg="black", fg="white")
label_E_Line.grid(row=26, column=0, columnspan=2, sticky="ew")
label_External=Label(my_frame2, text = "External Issues Comments (70 char max)", bg="black", fg="white")
label_External.grid(row=26, column=3, columnspan=4, sticky="ew")
label_Example=Label(my_frame2, text = "Example Issues Comments", bg="black", fg="white")
label_Example.grid(row=26, column=7, columnspan=3, sticky="ew")

issue1=Label(my_frame2, text ="Issue 1", bg="sky blue")
issue2=Label(my_frame2, text ="Issue 2", bg="sky blue")
issue3=Label(my_frame2, text ="Issue 3", bg="sky blue")
issue4=Label(my_frame2, text ="Issue 4", bg="sky blue")
issue5=Label(my_frame2, text ="Issue 5", bg="sky blue")
issue6=Label(my_frame2, text ="Issue 6", bg="sky blue")
issue1.grid(row=27, column=1, sticky="ew")
issue2.grid(row=28, column=1, sticky="ew")
issue3.grid(row=29, column=1, sticky="ew")
issue4.grid(row=30, column=1, sticky="ew")
issue5.grid(row=31, column=1, sticky="ew")
issue6.grid(row=32, column=1, sticky="ew")

#count the characters in the comment field.  Show alert when 70 characters have been type.
#char_count1
#char_count1.grid(row26, column=2)
#char_count2.grid(row27, column=3)
#char_count3.grid(row28, column=3)
#char_count4.grid(row29, column=3)
#char_count5.grid(row30, column=3)
#char_count6.grid(row31, column=3)

comment1=Entry(my_frame2, width=70)
comment2=Entry(my_frame2, width=70)
comment3=Entry(my_frame2, width=70)
comment4=Entry(my_frame2, width=70)
comment5=Entry(my_frame2, width=70)
comment6=Entry(my_frame2, width=70)
comment1.grid(row=27, column=7)
comment2.grid(row=28, column=7)
comment3.grid(row=29, column=7)
comment4.grid(row=30, column=7)
comment5.grid(row=31, column=7)
comment6.grid(row=32, column=7)

example1=Label(my_frame2, text ="Expected comments should answer any Jeopardy statuses.", anchor=W, bg="sky blue")
example2=Label(my_frame2, text ="Major fiber delay will impact Eline schedule/5G/etc.  ", anchor=W, bg="sky blue")
example3=Label(my_frame2, text ="PSC issues impacting x number of sites, ETC.", anchor=W, bg="sky blue")
example4=Label(my_frame2, text ="Final span of fiber delivery scheduled for mm/yyyy.", anchor=W, bg="sky blue")
example5=Label(my_frame2, text ="Temporary by-pass impacting x sites.", anchor=W, bg="sky blue")
example6=Label(my_frame2, text ="Center Stage issues and impact, ETC .", anchor=W, bg="sky blue")
example1.grid(row=27, column=8, sticky="ew")
example2.grid(row=28, column=8, sticky="ew")
example3.grid(row=29, column=8, sticky="ew")
example4.grid(row=30, column=8, sticky="ew")
example5.grid(row=31, column=8, sticky="ew")
example6.grid(row=32, column=8, sticky="ew")


#create Submit Button
submit_btn = Button(my_frame2, text="Add Record to Database", command=submit)
submit_btn.grid(row=33, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#Comment Changes
conn.commit()
#Close database connection
conn.close()

root.mainloop()
