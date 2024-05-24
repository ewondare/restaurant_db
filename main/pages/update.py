import streamlit as st
import pypyodbc as odbc
import sqlalchemy
import sqlite3


DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'DESKTOP-0S9785Q\SQLEXPRESS'
DATABASE_NAME = 'GroupAssignment1'


connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;

"""

conn = st.connection('mysql', type='sql')

print(conn)

options = ("Menu item", "Update Employee", "Update Details of an order", "Customer and Transaction", "Counter" , "Table" , "Booking")
selected_option = st.selectbox("What update you going to make?", options)


if selected_option == 'Menu item':
    st.empty()
    with st.container():
        menu_item_options = ("Appetizer", "Entree", "Desert")  
        menu_item_selection = st.selectbox("Choose a menu item option:", menu_item_options)
        
        if menu_item_selection == 'Appetizer':
            update_options = ("name" , "price" , "description" , "recipe")
            menu_item_update = st.selectbox("which item do you want to update" , update_options)
            if(menu_item_update == "name"):
                name_label = "name: "
                id = st.text_input("Appetizer id:")
                name = st.text_input(name_label)
                #if id exists -> update (cascade)
            if(menu_item_update == "price"):
                price_label = "price: "
                id = st.text_input("Appetizer id:")
                price = st.text_input(price_label)
                #if id exists -> update (cascade)
            if(menu_item_update == "description"):
                description_label = "description: "
                id = st.text_input("Appetizer id:")
                description = st.text_input(description_label)
                #if id exists -> update (cascade)
            if(menu_item_update == "recipe"):
                recipe_label = "recipe: "
                id = st.text_input("Appetizer id:")
                recipe = st.text_input(recipe_label)
                #if id exists -> update (cascade)

        if menu_item_selection == 'Entree':
           update_options = ("name" , "price" , "description" , "recipe")
           menu_item_update = st.selectbox("which item do you want to update" , update_options)
           if(menu_item_update == "name"):
                name_label = "name: "
                id = st.text_input("Appetizer id:")
                name = st.text_input(name_label)
                #if id exists -> update (cascade)
           if(menu_item_update == "price"):
                price_label = "price: "
                id = st.text_input("Appetizer id:")
                price = st.text_input(price_label)
                #if id exists -> update (cascade)
           if(menu_item_update == "description"):
                description_label = "description: "
                id = st.text_input("Appetizer id:")
                description = st.text_input(description_label)
                #if id exists -> update (cascade)
           if(menu_item_update == "recipe"):
                recipe_label = "recipe: "
                id = st.text_input("Appetizer id:")
                recipe = st.text_input(recipe_label)
                #if id exists -> update (cascade)
            
        if menu_item_selection == 'Desert':
            update_options = ("name" , "price" , "description" , "recipe")
            menu_item_update = st.selectbox("which item do you want to update" , update_options)
            if(menu_item_update == "name"):
                name_label = "name: "
                id = st.text_input("Appetizer id:")
                name = st.text_input(name_label)
                #if id exists -> update (cascade)
            if(menu_item_update == "price"):
                price_label = "price: "
                id = st.text_input("Appetizer id:")
                price = st.text_input(price_label)
                #if id exists -> update (cascade)
            if(menu_item_update == "description"):
                description_label = "description: "
                id = st.text_input("Appetizer id:")
                description = st.text_input(description_label)
                #if id exists -> update (cascade)
            if(menu_item_update == "recipe"):
                recipe_label = "recipe: "
                id = st.text_input("Appetizer id:")
                recipe = st.text_input(recipe_label)
                #if id exists -> update (cascade)
# Function to update the Customer table
def update_customer_record(customer_id, first_name, last_name):
    update_query = '''
        UPDATE Customer
        SET First_name = :first_name,
            last_name = :last_name
        WHERE Customer_id = :customer_id;
    '''
    with conn.session as s:
        s.execute(sqlalchemy.text(update_query), {
            'customer_id': customer_id,
            'first_name': first_name,
            'last_name': last_name
        })
        s.commit()
        st.write(f"Customer record with Customer_id {customer_id} updated successfully.")

# Function to update the table
def update_employee_record(ssn, first_name, last_name, home_address, date_of_birth, salary):
    update_query = '''
        UPDATE Employee
        SET First_Name = :first_name,
            Last_Name = :last_name,
            Home_Address = :home_address,
            Date_Of_Birth = :date_of_birth,
            Salary = :salary
        WHERE SSN = :ssn;
    '''
    with conn.session as s:
        s.execute(sqlalchemy.text(update_query), {
            'ssn': ssn,
            'first_name': first_name,
            'last_name': last_name,
            'home_address': home_address,
            'date_of_birth': date_of_birth,
            'salary': salary
        })
        s.commit()
        st.write(f"Employee record with SSN {ssn} updated successfully.")
        
def update_table_dine_record(table_id, capacity, is_available, waiter_id_ref):
    update_query = '''
        UPDATE Table_dine
        SET capacity = :capacity,
            Is_available = :is_available,
            Waiter_id_ref = :waiter_id_ref
        WHERE Id = :table_id;
    '''
    with conn.connect() as s:
        s.execute(sqlalchemy.text(update_query), {
            'table_id': table_id,
            'capacity': capacity,
            'is_available': is_available,
            'waiter_id_ref': waiter_id_ref
        })
        st.write(f"Table_dine record with Id {table_id} updated successfully.")    
 
# Function to update the Booking table
def update_booking_record(customer_id_ref, table_dine_id_ref, book_date):
    update_query = '''
        UPDATE Booking
        SET book_date = :book_date
        WHERE Customer_id_ref = :customer_id_ref
        AND Table_dine_id_ref = :table_dine_id_ref;
    '''
    with conn.connect() as s:
        s.execute(sqlalchemy.text(update_query), {
            'customer_id_ref': customer_id_ref,
            'table_dine_id_ref': table_dine_id_ref,
            'book_date': book_date
        })
        st.write(f"Booking record for Customer_id_ref {customer_id_ref} and Table_dine_id_ref {table_dine_id_ref} updated successfully.")
        
if selected_option == 'Update Employee':
    st.empty()
    with st.container():
        empSSN = st.text_input("Employee SSN:")
        newFirstName = st.text_input("New First Name:")
        newLastName = st.text_input("New Last Name:")
        newHomeAddress = st.text_input("New Home Address:")
        newDateOfBirth = st.text_input("New Date of Birth (YYYY-MM-DD):")
        newSalary = st.text_input("New Salary:")
        submit_button = st.button("Submit")

        if submit_button:
            if empSSN and newFirstName and newLastName and newHomeAddress and newDateOfBirth and newSalary:
                update_employee_record(empSSN, newFirstName, newLastName, newHomeAddress, newDateOfBirth, newSalary)
            else:
                st.write("Please fill out all fields to update the record.")            
            
            
if selected_option == 'Update Details of an order':
    st.empty()
    with st.container():
        update_options = ("is paid" , "date" , "counter id" , "table id" , "chef id" , "waiter id")
        order_item_update = st.selectbox("which item do you want to update" , update_options)
        if(order_item_update == "is paid"):
                is_paid_label = "is paid: "
                id = st.text_input("Order id: ")
                is_paid = st.text_input(is_paid_label)
                #if id exists -> update (cascade)
        if(order_item_update == "date"):
                day_label = "date: "
                id = st.text_input("Order id: ")
                date = st.text_input(day_label)
                #if id exists -> update (cascade)
        if(order_item_update == "counter id"):
                counter_id_label = "counter id: "
                id = st.text_input("Order id: ")
                counter_id = st.text_input(counter_id_label)
                #if id exists -> update (cascade)
        if(order_item_update == "table id"):
                table_id_label = "table id: "
                id = st.text_input("Order id: ")
                table_id = st.text_input(table_id_label)
                #if id exists -> update (cascade)
                
        if(order_item_update == "chef id"):
                counter_id_label = "counter id: "
                id = st.text_input("Order id: ")
                counter_id = st.text_input(counter_id_label)
                chef_id = st.text_input("chef id: ") 
                #if id exists -> update (cascade)
        if(order_item_update == "waiter id"):
                counter_id_label = "counter id: "
                id = st.text_input("Order id: ")
                counter_id = st.text_input(counter_id_label)
                chef_id = st.text_input("waiter id: ")  
                #if id exists -> update (cascade)     




elif selected_option == 'Customer and Transaction':
    st.empty()
    with st.container():
        customerId = st.text_input("Customer ID:")
        newFirstName = st.text_input("New First Name:")
        newLastName = st.text_input("New Last Name:")
        submit_button = st.button("Submit")

        if submit_button:
            update_customer_record(customerId, newFirstName, newLastName)
            st.success("Customer information updated successfully")
                


elif selected_option == 'Table':
    st.empty()
    with st.container():
        tableId = st.text_input("Table ID:")
        newCapacity = st.text_input("New Capacity:")
        newIsBooked = st.checkbox("Is Booked?")
        newWaiterId = st.text_input("New Waiter ID:")
        submit_button = st.button("Submit")

        if submit_button:
           update_table_dine_record(tableId,newCapacity,newIsBooked,newWaiterId)

elif selected_option == 'Booking':
    st.empty()
    with st.container():
        customerId = st.text_input("Customer ID:")
        tableId = st.text_input("Table ID:")
        newDate = st.text_input("New Date (YYYY-MM-DD):")
        submit_button = st.button("Submit")

        if submit_button:
            update_booking_record(customerId,tableId,newDate)
