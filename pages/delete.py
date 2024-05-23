import streamlit as st
import pypyodbc as odbc 

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'DESKTOP-CEC2DIQ'
DATABASE_NAME = 'GroupAssignment1'


connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;

"""

conn = odbc.connect(connectString=connection_string)
print(conn)

options = ("Menu item", "Delete Employee", "Delete Details of an order", "Customer and Transaction", "Counter" , "Table" , "Booking")
selected_option = st.selectbox("What deletion you going to make?", options)


if selected_option == 'Menu item':
    st.empty()
    with st.container():
        menu_item_options = ("Appetizer", "Entree", "Desert")  
        menu_item_selection = st.selectbox("Choose a menu item option:", menu_item_options)

        if menu_item_selection == 'Appetizer':
            id = st.text_input("Appetizer id:")
            # if id exists -> delete 
        if menu_item_selection == 'Entree':
            id = st.text_input("Entree id:")
            # if id exists -> delete 
        if menu_item_selection == 'Desert':
            id = st.text_input("Desert id:")
            # if id exists -> delete 

if selected_option == 'Delete Employee':
    st.empty()
    with st.container():
        ssn = st.text_input("Enter Employee's ssn: ")
        #if id exists -> delete (cascade)
        
if selected_option == 'Delete Details of an order':
    st.empty()
    with st.container():
        order_id = st.text_input("Order id: ")
        #if id exists -> delete (cascade)
        
if selected_option == 'Customer and Transaction':
    st.empty()
    with st.container():
        customer_id = st.text_input("Customer id: ")
        #if id exists -> delete (cascade)    
        transaction_id = st.text_input("Transaction id:")
        #if id exists -> delete (cascade)

if selected_option == 'Counter':
    st.empty()
    with st.container():
        counter_id = st.text_input("Counter id: ")
        #if id exists -> delete (cascade)    

if selected_option == 'Table':
    st.empty()
    with st.container():
        table_id = st.text_input("Table id: ")
        #if id exists -> delete (cascade)  

if selected_option == 'Booking':
    st.empty()
    with st.container():
        customer_id = st.text_input("Customer id: ")
        table_id = st.text_input("Table id: ")
        #if id exists -> delete (cascade) 
        
