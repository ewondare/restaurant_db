import streamlit as st
import pypyodbc as odbc 

def query_select(table_name):
    query = f"SELECT * From {table_name}"
    return query

options = ("Appetizer_items", "Entree_items", "Dessert_items", "Order", "Booking" , "Transaction", "Counter" , "Makes_order" , "Employee","Customer" , "Manager" , "Cashier" ,"Chef" , "Waiter" ,"Deliver_food" , "Makes_order" , "Menu")
selected_option = st.selectbox("Please select the table you want to see the data in.", options)

query = query_select(selected_option)
# df = pd.read_sql(query)
# st.write(df) 

st.write("If you'd like to see the output of custom query, use here:")
custom_query = st.text_input("enter your custom query:")

query = query_select(custom_query)
# df = pd.read_sql(query)
# st.write(df) 