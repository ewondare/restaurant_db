import streamlit as st
import pandas as pd
import pypyodbc as odbc


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
conn = odbc.connect(connectString=connection_string)

# query to select all data from a table
def query_select(table_name):
    query = "SELECT * FROM [{}]".format(table_name)
    return query

# fetch data from the database and return a dataframe
def get_data(query):
    with conn.cursor() as cursor:
        cursor.execute(query)
        columns = [column[0] for column in cursor.description]
        return pd.DataFrame(cursor.fetchall(), columns=columns)

# table selection
options = ("Menu", "Appetizer_items", "Entree_items" , "Dessert_items", 
           "Employee", "Manager" , "Cashier" , "Waiter" , "Chef" ,
            "Customer" , "Booking" , "Table" , "Counter" , "Transaction" ,
            "Order" , "Makes_order" , "Receive_order", "order_appetizer" , "Order_entree" , "Order_dessert" )

# table selection UI
selected_option = st.selectbox("Please select the table you want to see the data in.", options)

# fetch and display data from the selected table
if selected_option:
    query = query_select(selected_option)
    data = get_data(query)
    with st.container():
        st.write(f"Data from {selected_option}")
        st.dataframe(data)


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