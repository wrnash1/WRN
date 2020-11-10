from tkinter import *
from tkinter import ttk

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
myVerizon_green = "#546391"
myVerison_red = "#a14a6e"

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
label_total_Market=Label(my_frame2, text="Total Market Deliverables", bg="black", fg="white", anchor=CENTER)

label_psc=Label(my_frame2, text="PSC")
label_psc_instructions=Label(my_frame2, text="Number of sites requiring Power/Structure/Cooling in support of site NEATs; Total equals total NEATs", anchor=W)

label_neat=Label(my_frame2, text="NEATs")
label_neat_instructions=Label(my_frame2, text="Number of sites within the market tracking towards NEAT Complete", anchor=W)

label_fiber=Label(my_frame2, text="Fiber S&T \(Total Spans\)")
label_fiber_instructions=Label(my_frame2, text="Fiber S&T: cable-placed and Spliced & Tested by fiber vendor. Next step would be FIM task. Total is equal to number of OM96 NFIDs for your market.", anchor=W)

label_om96=Label(my_frame2, text = "OM96s In Effect")
label_om96_instructions=Label(my_frame2, text="OM96s In-Effect: spans that are RFT In-Effect \(exclude Path G SAP MSE\)", anchor=W)

label_kpi_Nat=Label(my_frame2, text="KPI NATs")
label_kpi_Nat_instructions=Label(my_frame2, text="NATs: tracking of KPI NAT count for your market.", anchor=W)

label_10G_BH_A=Label(my_frame2, text="10G BH Circuits \(Path A\) Total")
label_10G_BH_A_instructions=Label(my_frame2, text="10G BH Circuits/(Path A/): circuit count from all 5G//CRAN hub sites and fiber-only extensions sites back to MSC", anchor=W)

label_10G_BH_B=Label(my_frame2, text="10G BH Circuits \(Path B\) Total")
label_10G_BH_B_instructions=Label(my_frame2, text="10G BH Circuits/(Path B/): circuit count from all 5G//CRAN hub sites and fiber-only extensions sites back to MSC", anchor=W)

label_consumption=Label(my_frame2, text="Consumption Order Total")
label_consumption_instructions=Label(my_frame2, text="Count of all received consumption orders for the market", anchor=W)

label_fiber_loops=Label(my_frame2, text="Fiber Loops")
label_fiber_loops_instructions=Label(my_frame2, text="Count of delivered Fiber and total number of Loops ", anchor=W)

label_ER_Uplinks=Label(my_frame2, text="ER Uplinks")
label_ER_Uplinks_instructions=Label(my_frame2, text="Count of the appropriately ER to IHR or RHR uplinks, 2 per ER site", anchor=W)

label_IHR=Label(my_frame2, text="IHR - RHR Uplinks")
label_IHR_instructions=Label(my_frame2, text="Count of the appropriately IHR to RHR uplinks, 2 per IHR site", anchor=W)

label_P_5G_CRAN=Label(my_frame2, text="Priority 5G CRAN only", bg="black", fg="white", anchor=CENTER)

label_P_5G_CRANS=Label(my_frame2, text="Priority 5G CRANS")
label_P_5G_CRANS_instructions=Label(my_frame2, text="Number of 5G Priority CRAN sites \(as indicated by the red \"5G\" on diagrams\)", anchor=W)

label_P_5G_consumption=Label(my_frame2, text = "Priority 5G CRANS Consumption Orders Received")
label_P_5G_consumption_instructions=Label(my_frame2, text="Number of priority 5G CRAN consumption orders created.", anchor=W)

label_P_5G_Circuits=Label(my_frame2, text="Priority 5G CRAN Circuits in Effect")
label_P_5G_Circuits_instructions=Label(my_frame2, text="Number of completed priority 5G CRAN 10G BH circuits.  RFT/NAT status of these selected 10G BH circuits.", anchor=W)

Label_target_Date=Label(my_frame2, text="Target Date")
Label_target_Date_instructions=Label(my_frame2, text="Date that all 5G Priority Backhaul circuits are complete", anchor=W)

label_E_Line=Label(my_frame2, text = "E-Line", bg="black", fg="white", anchor=CENTER)

label_MPLS_75=Label(my_frame2, text = "MPLS Current 75% Complete")
label_MPLS_75_instructions=Label(my_frame2, text = "Quarter that 75% of the ER \(ER-IHR\) are complete; requires all IHR & RHR \(IHR-RHR\) to be complete;  xQyy in first block;  Use the dropdown menu to select status", anchor=W)

label_MPLS_90=Label(my_frame2, text = "MPLS Current 90% Complete")
label_MPLS_90_instructions=Label(my_frame2, text = "Quarter that 90% of the ER \(ER-IHR\) are complete; requires all IHR & RHR \(IHR-RHR\) to be complete;  xQyy in first block;   Use the dropdown menu to select status", anchor=W)

label_Current_Complete=Label(my_frame2, text="Current % Complete")
label_Current_Complete_instructions=Label(my_frame2, text="The current percentage of completed ER \(ER-IHR\) installations; requires all IHR & RHR (IHR-RHR) to be complete;  XX% in first block", anchor=W)

label_e_Line_P=Label(my_frame2, text ="E-Line Priority")
label_e_Line_P_instructions=Label(my_frame2, text ="What is the overall PM status of the ELINE installation;  Use the dropdown menu to select status", anchor=W)

lable_5G_P=Label(my_frame2, text ="5G priority")
lable_5G_P_instructions=Label(my_frame2, text ="What is the overall PM Status of the 5G Priority Backhaul;  Use the dropdown menu to select status", anchor=W)


#Place label on frame
label_cheetah.grid(row=0, column=3, columnspan=2) #Cheetah/PMO Data
label_PM_Entry.grid(row=0, column=5, columnspan=3) #PM Entry
label_market.grid(row=1, column=0, columnspan=2) #Per Market
label_complete1.grid(row=1, column=3) #Complete
label_total1.grid(row=1, column=4) #Total
label_complete.grid(row=1, column=5)
label_total.grid(row=1, column=6)
label_Internal_Notes.grid(row=1, column=7)
label_Instructions.grid(row=1, column=8)
label_total_Market.grid(row=2, column=0, columnspan=8)  #Need to expand the whole page
label_psc.grid(row=3, column=1, columnspan=2)
label_psc_instructions.grid(row=3, column=8)
label_neat.grid(row=4, column=1)
label_neat_instructions.grid(row=4, column=8)
label_om96.grid(row=5, column=1)
label_om96_instructions.grid(row=5, column=8)
label_kpi_Nat.grid(row=6, column=1)
label_kpi_Nat_instructions.grid(row=6, column=8)
label_10G_BH_A.grid(row=7, column=1)
label_10G_BH_A_instructions.grid(row=7, column=8)
label_10G_BH_B.grid(row=8, column=1)
label_10G_BH_B_instructions.grid(row=8, column=8)
label_consumption.grid(row=9, column=1)
label_consumption_instructions.grid(row=9, column=8)
label_fiber_loops.grid(row=10, column=1)
label_fiber_loops_instructions.grid(row=10, column=8)
label_ER_Uplinks.grid(row=11, column=1)
label_ER_Uplinks_instructions.grid(row=11, column=8)
label_IHR.grid(row=12, column=1)
label_IHR_instructions.grid(row=12, column=8)
label_P_5G_CRAN.grid(row=13, column=1)
label_P_5G_CRANS.grid(row=14, column=1)
label_P_5G_CRANS_instructions.grid(row=14, column=8)
label_P_5G_consumption.grid(row=15, column=1)
label_P_5G_consumption_instructions.grid(row=15, column=8)
label_P_5G_Circuits.grid(row=16, column=1)
label_P_5G_Circuits_instructions.grid(row=16, column=8)
Label_target_Date.grid(row=17, column=1)
Label_target_Date_instructions.grid(row=17, column=8)
label_E_Line.grid(row=18, column=1)
label_MPLS_75.grid(row=19, column=1)
label_MPLS_75_instructions.grid(row=19, column=8)
label_MPLS_90.grid(row=20, column=1)
label_MPLS_90_instructions.grid(row=20, column=8)
label_Current_Complete.grid(row=21, column=1)
label_Current_Complete_instructions.grid(row=21, column=8)
label_e_Line_P.grid(row=22, column=1)
label_e_Line_P_instructions.grid(row=22, column=8)
lable_5G_P.grid(row=23, column=1)
lable_5G_P_instructions.grid(row=23, column=8)


root.mainloop()
