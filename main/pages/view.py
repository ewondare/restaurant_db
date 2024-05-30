import streamlit as st
import pandas as pd
import pypyodbc as odbc

Parinaz_SERVER_NAME = 'DESKTOP-0S9785Q\\SQLEXPRESS'
Nazanin_SERVER_NAME = 'DESKTOP-LMGNA9O\\DEFAULT2023'
Dorsa_SERVER_NAME = 'DESKTOP-CEC2DIQ'
Taha_SERVER_NAME = None

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = Nazanin_SERVER_NAME
DATABASE_NAME = 'proj'

connection_string = f"DRIVER={{SQL Server}};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};Trust_Connection=yes;"

# establish connection
conn = odbc.connect(connectString=connection_string)

# query to select all data from a table
def query_select(table_name):
    query = f"SELECT * FROM [{table_name}]"
    return query

# fetch data from the database and return a dataframe
def get_data(query):
    with conn.cursor() as cursor:
        cursor.execute(query)
        columns = [column[0] for column in cursor.description]
        return pd.DataFrame(cursor.fetchall(), columns=columns)

# table selection
options = ("Appetizer_item", "Entree_item", "Desert_item", "Table", "Booking", 
           "Transaction", "Counter", "Makes_order", "Employee", "Customer", 
           "Manager", "Cashier", "Chef", "Waiter", "Receive_order", "Menu")

# table selection UI
selected_option = st.selectbox("Please select the table you want to see the data in.", options)

# fetch and display data from the selected table
if selected_option:
    query = query_select(selected_option)
    data = get_data(query)
    with st.container():
        st.write(f"Data from {selected_option}")
        st.dataframe(data)
