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


def fetch_data(table_name):
    query = "SELECT * FROM [{}]".format(table_name)
    with conn.cursor() as cursor:
        cursor.execute(query)
        columns = [column[0] for column in cursor.description]
        return pd.DataFrame(cursor.fetchall(), columns=columns)
    

Log_Tables_query = """SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME LIKE '%Log%';"""
cursor = conn.cursor()
cursor.execute(Log_Tables_query)
options = tuple(row[0] for row in cursor.fetchall() )

selected_option = st.selectbox("What Log table you want to observe?", options)
st.empty()
with st.container():
    data = fetch_data(selected_option)
    st.dataframe(data)



cursor.close()
conn.close()