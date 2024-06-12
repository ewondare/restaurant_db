import streamlit as st
import pandas as pd
import pypyodbc as odbc


Parinaz_SERVER_NAME = 'DESKTOP-0S9785Q\SQLEXPRESS'
Nazanin_SERVER_NAME = 'DESKTOP-LMGNA9O\DEFAULT2023'
Dorsa_SERVER_NAME = 'DESKTOP-CEC2DIQ'
Taha_SERVER_NAME = 'DESKTOP-2V8SO2H\SQLEXPRESS'

Parinaz_DB = 'GroupAssignment'
Nazanin_DB = 'proj'
Dorsa_DB = 'GroupAssignment1'
Taha_DB = 'database_withdata'

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = Parinaz_SERVER_NAME
DATABASE_NAME = Parinaz_DB

connection_string = f"DRIVER={{SQL Server}};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};Trust_Connection=yes;"

# establish connection
conn = odbc.connect(connectString=connection_string)

