import sqlite3

conn = sqlite3.connect('verizon.db')

c = conn.cursor()

#create a table

c.execute("""CREATE TABLE market (
        psc_complete NUMERIC,
        psc_total NUMERIC,
        psc_notes TEXT,
        neat_complete NUMERIC,
        neat_total NUMERIC,
        neat_notes TEXT,
        fiber_Complete NUMERIC,
        fiber_total NUMERIC,
        fiber_notes TEXT,
        om96_complete NUMERIC,
        om96_total NUMERIC,
        om96_notes TEXT,
        kpi_Nat_Complete NUMERIC,
        kpi_Nat_total NUMERIC,
        kpi_Nat_notes TEXT,
        E_10G_BH_A_Complete NUMERIC,
        E_10G_BH_A_total NUMERIC,
        E_10G_BH_A_notes TEXT,
        E_10G_BH_B_Complete NUMERIC,
        E_10G_BH_B_total NUMERIC,
        E_10G_BH_B_notes TEXT,
        consumption_Complete NUMERIC,
        consumption_total NUMERIC,
        consumption_notes TEXT,
        fiber_loops_Complete,
        fiber_loops_total NUMERIC,
        fiber_loops_notes TEXT,
        ER_Uplinks_Complete NUMERIC,
        ER_Uplinks_total NUMERIC,
        ER_Uplinks_notes TEXT,
        IHR_Complete NUMERIC,
        IHR_total NUMERIC,
        IHR_notes TEXT,
        P_5G_CRANS_total NUMERIC,
        P_5G_CRANS_notes TEXT,
        P_5G_consumption_Complete NUMERIC,
        P_5G_consumption_total NUMERIC,
        P_5G_consumption_notes TEXT,
        P_5G_Circuits_Complete NUMERIC,
        P_5G_Circuits_total NUMERIC,
        P_5G_Circuits_notes TEXT,
        target_Date_complete TEXT,
        target_Date_notes TEXT,
        MPLS_75_Complete NUMERIC,
        MPLS_75_total NUMERIC,
        MPLS_75_notes TEXT,
        MPLS_90_Complete NUMERIC,
        MPLS_90_total NUMERIC,
        MPLS_90_Notes TEXT,
        Current_Complete_complete NUMERIC,
        Current_Complete_notes TEXT,
        e_Line_P_total NUMERIC,
        e_Line_P_notes TEXT,
        e_5g_P_total NUMERIC,
        e_5g_P_notes TEXT,
        issue1 TEXT,
        issue2 TEXT,
        issue3 TEXT,
        issue4 TEXT,
        issue5 TEXT,
        issue6 TEXT
)""")

#write data to database
conn.commit()

#Close the database connection
conn.close()
