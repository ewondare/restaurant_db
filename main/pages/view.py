import streamlit as st
import pypyodbc as odbc 
import pandas as pd 

Parinaz_SERVER_NAME = 'DESKTOP-0S9785Q\SQLEXPRESS'
Nazanin_SERVER_NAME = None
Dorsa_SERVER_NAME = 'DESKTOP-CEC2DIQ'
Taha_SERVER_NAME = None


DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = Dorsa_SERVER_NAME
DATABASE_NAME = 'GroupAssignment1'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;

"""

conn = odbc.connect(connectString=connection_string)


def query_select(table_name):
    query = f"SELECT * From {table_name}"
    return query

options = ("Appetizer_item", "Entree_item", "Desert_item","Table",  "Booking" , "Transaction", "Counter" , "Makes_order" , "Employee","Customer" , "Manager" , "Cashier" ,"Chef" , "Waiter" ,  "Receive_order" , "Menu")
selected_option = st.selectbox("Please select the table you want to see the data in.", options)

query = query_select(selected_option)
# df = pd.read_sql(query)
# st.write(df) 

st.write("If you'd like to see the output of custom query, use here:")
custom_query = st.text_input("enter your custom query:")

# Function to fetch data from a table
def get_data(table_name):
    query = f"select * from {table_name}"
    df = conn.query(query)
    return df

query = query_select(custom_query)
# df = pd.read_sql(query)
# st.write(df) 

# Fetch and display data from the selected table
if selected_option:
    data = get_data(selected_option)
    st.write(f"Data from {selected_option}")
    st.dataframe(data)
