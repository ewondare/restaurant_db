import streamlit as st
import pandas as pd
#import pypyodbc as odbc
from datetime import datetime, timedelta

Parinaz_SERVER_NAME = 'DESKTOP-0S9785Q\SQLEXPRESS'
Nazanin_SERVER_NAME = 'DESKTOP-LMGNA9O\DEFAULT2023'
Dorsa_SERVER_NAME = 'DESKTOP-CEC2DIQ'
Taha_SERVER_NAME = 'DESKTOP-2V8SO2H\SQLEXPRESS'

Parinaz_DB = 'db_project'
Nazanin_DB = 'proj'
Dorsa_DB = 'GroupAssignment1'
Taha_DB = 'database_withdata'

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = Parinaz_SERVER_NAME
DATABASE_NAME = Parinaz_DB

connection_string = f"DRIVER={{SQL Server}};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};Trust_Connection=yes;"

# establish connection
#conn = odbc.connect(connectString=connection_string)

options = ('Insert' , 'Update' , 'Delete')
with st.container():
    st.empty()
    selected_option = st.selectbox("What Kind of Log Data do you want to observe?", options)

    #start_year = st.slider("From year:", 2000 , 2024)
    #end_year = st.slider("To year:", 2000, 2024)
    start_date = datetime(2020, 1, 1)
    end_date = start_date + timedelta(weeks=1)
    
    selected_date = st.slider(
        "Select a date range",
        min_value=start_date,
        max_value=end_date,
        value=(start_date, end_date),
        step=timedelta(days=1),
    )

