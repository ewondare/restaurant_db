import streamlit as st
import pypyodbc as odbc 
import sqlite3



Parinaz_SERVER_NAME = 'DESKTOP-0S9785Q\SQLEXPRESS'
Nazanin_SERVER_NAME = None
Dorsa_SERVER_NAME = 'DESKTOP-CEC2DIQ'
Taha_SERVER_NAME = None


DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = Parinaz_SERVER_NAME
DATABASE_NAME = 'GroupAssignment1'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;

"""

conn = odbc.connect(connectString=connection_string)
# print(conn)

options = ("Menu item", "Delete Employee", "Delete Details of an order", "Customer" , "Transaction", "Counter", "Table",
           "Booking")
selected_option = st.selectbox("What addition do you want to delete?", options)
st.empty()
if selected_option == "Menu item":
    st.empty()
    with st.container():
        
        item_types = ("Appetizer", "Entree", "Dessert")  
        item_type_selection = st.selectbox("Choose an item type:", item_types)
        if item_type_selection == 'Appetizer':
            with st.form(key='menu_item_form'):
                table_name = 'Appetizer_items'
                item_id = st.text_input("Please Enter Item's ID in Appetizer Table:")
                submit_button = st.form_submit_button(label='Submit')
            if submit_button:
                if(not item_id):
                    st.error("you haven't entered an ID.")
                else: 
                    s = conn.cursor()
                    s.execute("DELETE FROM {} WHERE id = '{}'".format(table_name , item_id))
                    s.commit()
                    st.success("deleted successfully")
        elif item_type_selection == 'Entree':
            with st.form(key='menu_item_form'):
                table_name = 'Entree_items'
                item_id = st.text_input("Please Enter Iten's ID in Entree Table:")
                submit_button = st.form_submit_button(label='Submit')
            if submit_button:
                if(not item_id):
                    st.error("you haven't entered an ID.")
                else: 
                    s = conn.cursor()
                    s.execute("DELETE FROM {} WHERE id = '{}'".format(table_name , item_id))
                    s.commit()
                    st.success("deleted successfully")

        elif item_type_selection == 'Dessert':
                with st.form(key='menu_item_form'):
                    table_name = 'Dessert_items'
                    item_id = st.text_input("Please Enter Iten's ID in Dessert Table:")
                    submit_button = st.form_submit_button(label='Submit')
                if submit_button:
                    if(not item_id):
                        st.error("you haven't entered an ID.")
                    else: 
                        s = conn.cursor()
                        s.execute("DELETE FROM {} WHERE id = '{}'".format(table_name , item_id))
                        s.commit()
                        st.success("deleted successfully")
                        
        




elif selected_option == "Delete Employee":
    st.empty()
    with st.container():
        employee_item_options = ("Manager", "Cashier", "Chef", "Waiter")
        employee_item_selection = st.selectbox("Choose an item option:", employee_item_options)
        
        table_name = employee_item_selection

        if employee_item_selection == 'Manager':
            with st.form(key='employee_form'):
                manager_id = st.text_input("Manager ID:")
                submit_button = st.form_submit_button(label='Submit')

            if submit_button:
                if not manager_id:
                    st.error("you haven't entered an ID.")
                else: 
                    s = conn.cursor()
                    s.execute("DELETE FROM {} WHERE id = '{}'".format(table_name , manager_id))
                    s.commit()
                    st.success("deleted successfully")
            


        elif employee_item_selection == 'Cashier':
            with st.form(key='employee_form'):
                cashier_id = st.text_input("Cashieer ID:")
                submit_button = st.form_submit_button(label='Submit')

            if submit_button:
                if not cashier_id:
                    st.error("you haven't entered an ID.")
                else: 
                    s = conn.cursor()
                    s.execute("DELETE FROM {} WHERE id = '{}'".format(table_name , cashier_id))
                    s.commit()
                    st.success("deleted successfully")


        elif employee_item_selection == 'Chef':
            with st.form(key='employee_form'):
                chef_id = st.text_input("Cashieer ID:")
                submit_button = st.form_submit_button(label='Submit')

            if submit_button:
                if not chef_id:
                    st.error("you haven't entered an ID.")
                else: 
                    s = conn.cursor()
                    s.execute("DELETE FROM {} WHERE id = '{}'".format(table_name , chef_id))
                    s.commit()
                    st.success("deleted successfully")
   

        elif employee_item_selection == 'Waiter':
            with st.form(key='employee_form'):
                waiter_id = st.text_input("Cashieer ID:")
                submit_button = st.form_submit_button(label='Submit')

            if submit_button:
                if not waiter_id:
                    st.error("you haven't entered an ID.")
                else: 
                    s = conn.cursor()
                    s.execute("DELETE FROM {} WHERE id = '{}'".format(table_name , waiter_id))
                    s.commit()
                    st.success("deleted successfully")



  
elif selected_option == "Delete Details of an order":
    st.empty()
    with st.container():
        with st.form(key='order_form'):
            table_name = '[Order]'
            order_id = st.text_input("Please enter Order id:")
            submit_button = st.form_submit_button(label='Submit')

            if submit_button:
                if not order_id:
                    st.error("you haven't entered an ID.")
                else: 
                    s = conn.cursor()
                    s.execute("DELETE FROM {} WHERE id = '{}'".format(table_name , order_id))
                    s.commit()
                    st.success("deleted successfully")
    
elif selected_option == "Customer":
    st.empty()
    with st.container():
        with st.form(key='customer_form'):
            table_name = 'Customer'
            customer_id = st.text_input("Please enter an ID:")
            submit_button = st.form_submit_button(label='Submit')

            if submit_button:
                if not customer_id:
                    st.error("you haven't entered an ID.")
                else: 
                    s = conn.cursor()
                    s.execute("DELETE FROM {} WHERE id = '{}'".format(table_name , customer_id))
                    s.commit()
                    st.success("deleted successfully")
        
elif selected_option == 'Transaction':
    
        with st.form(key='transaction_form'):
            table_name = 'Transaction'
            _id = st.text_input("Please enter an ID:")
            submit_button = st.form_submit_button(label='Submit')

            if submit_button:
                if not _id:
                    st.error("you haven't entered an ID.")
                else: 
                    s = conn.cursor()
                    s.execute("DELETE FROM {} WHERE id = '{}'".format(table_name , _id))
                    s.commit()
                    st.success("deleted successfully")


elif selected_option == 'Counter':
    st.empty()
    with st.container():
        with st.form(key='counter_form'):
            table_name = 'Counter'
            _id = st.text_input("Please enter an ID:")
            submit_button = st.form_submit_button(label='Submit')

            if submit_button:
                if not _id:
                    st.error("you haven't entered an ID.")
                else: 
                    s = conn.cursor()
                    s.execute("DELETE FROM {} WHERE id = '{}'".format(table_name , _id))
                    s.commit()
                    st.success("deleted successfully")
     

elif selected_option == 'Table':
    st.empty()
    with st.container():
        with st.form(key='table_form'):
            table_name = 'Table'
            _id = st.text_input("Please enter an ID:")
            submit_button = st.form_submit_button(label='Submit')

            if submit_button:
                if not _id:
                    st.error("you haven't entered an ID.")
                else: 
                    s = conn.cursor()
                    s.execute("DELETE FROM {} WHERE id = '{}'".format(table_name , _id))
                    s.commit()
                    st.success("deleted successfully")
 

