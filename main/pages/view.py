import streamlit as st
import pypyodbc as odbc 
import pandas as pd 

Parinaz_SERVER_NAME = 'DESKTOP-0S9785Q\SQLEXPRESS'
Nazanin_SERVER_NAME = 'DESKTOP-LMGNA9O\DEFAULT2023'
Dorsa_SERVER_NAME = 'DESKTOP-CEC2DIQ'
Taha_SERVER_NAME = None

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = Nazanin_SERVER_NAME
DATABASE_NAME = 'proj'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""

# connect to the database
conn = odbc.connect(connection_string)

# create a query to select all data from a table
def query_select(table_name):
    query = f"SELECT * FROM {table_name}"
    return query

# fetch data from the database and return a dataframe
def get_data(query):
    return pd.read_sql(query, conn)

options = ("Appetizer_item", "Entree_item", "Desert_item", "Table", "Booking", 
           "Transaction", "Counter", "Makes_order", "Employee", "Customer", 
           "Manager", "Cashier", "Chef", "Waiter", "Receive_order", "Menu")

# table selection UI
selected_option = st.selectbox("Please select the table you want to see the data in.", options)

# Fetch and display data from the selected table
if selected_option:
    query = query_select(selected_option)
    data = get_data(query)
    with st.container():
        st.write(f"Data from {selected_option}")
        st.dataframe(data)

# Custom query input and execution
st.write("If you'd like to see the output of custom query, use here:")
custom_query = st.text_input("Enter your custom query:")

if custom_query:
    try:
        custom_data = get_data(custom_query)
        with st.container():
            st.write("Output of your custom query:")
            st.dataframe(custom_data)
    except Exception as e:
        st.error(f"Error executing query: {e}")


import delete
import update
import insert

st.write("Perform other operations:")

operation = st.selectbox("Select an operation:", ("Insert", "Update", "Delete"))

if operation == "Insert":
    st.write("Insert operation selected")
    insert.selected_option = st.selectbox("Choose an insert option:", insert.options)
    exec(open("insert.py").read())

elif operation == "Update":
    st.write("Update operation selected")
    update.selected_option = st.selectbox("Choose an update option:", update.options)
    exec(open("update.py").read())

elif operation == "Delete":
    st.write("Delete operation selected")
    delete.selected_option = st.selectbox("Choose a delete option:", delete.options)
    exec(open("delete.py").read())
