import streamlit as st
import pypyodbc as odbc

# Establishing database connection
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

# execute SQL stored procedures
def execute_stored_procedure(procedure_name, *args):
    try:
        with conn.session as s:
            s.execute(f"EXEC {procedure_name} " + ", ".join("?" * len(args)), args)
            result = s.fetchall()
            s.commit()
        st.success("Stored procedure executed successfully")
        return result
    except Exception as e:
        st.error(f"Error: {e}")
        return None
    
options = ("Menu item", "Update Employee", "Update Details of an order", "Customer and Transaction", "Counter", "Table", "Booking")
selected_option = st.selectbox("What update are you going to make?", options)

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
            result = execute_stored_procedure("UpdateEmployee", empSSN, newFirstName, newLastName, newHomeAddress, newDateOfBirth, newSalary)
            if result:
                st.success("Employee information updated successfully")
                st.table(result)

elif selected_option == 'Menu item':
    st.empty()
    with st.container():
        menuId = st.text_input("Menu ID:")
        newTitle = st.text_input("New Title:")
        newSummary = st.text_input("New Summary:")
        newIsAvailable = st.checkbox("Is Available?")
        submit_button = st.button("Submit")

        if submit_button:
            result = execute_stored_procedure("UpdateMenu", menuId, newTitle, newSummary, newIsAvailable)
            if result:
                st.success("Menu item updated successfully")
                st.table(result)

elif selected_option == 'Update Details of an order':
    st.empty()
    with st.container():
        orderId = st.text_input("Order ID:")
        newTableCondition = st.text_input("New Table Condition:")
        newIsPaid = st.checkbox("Is Paid?")
        newPrice = st.text_input("New Price:")
        newOrderDate = st.text_input("New Order Date (YYYY-MM-DD):")
        newTableIdRef = st.text_input("New Table ID Reference:")
        submit_button = st.button("Submit")

        if submit_button:
            result = execute_stored_procedure("UpdateOrder", orderId, newTableCondition, newIsPaid, newPrice, newOrderDate, newTableIdRef)
            if result:
                st.success("Order details updated successfully")
                st.table(result)

elif selected_option == 'Customer and Transaction':
    st.empty()
    with st.container():
        customerId = st.text_input("Customer ID:")
        newFirstName = st.text_input("New First Name:")
        newLastName = st.text_input("New Last Name:")
        submit_button = st.button("Submit")

        if submit_button:
            result = execute_stored_procedure("UpdateCustomer", customerId, newFirstName, newLastName)
            if result:
                st.success("Customer information updated successfully")
                st.table(result)

elif selected_option == 'Counter':
    st.empty()
    with st.container():
        counterId = st.text_input("Counter ID:")
        newId = st.text_input("New ID:")
        submit_button = st.button("Submit")

        if submit_button:
            result = execute_stored_procedure("UpdateCounter", counterId, newId)
            if result:
                st.success("Counter information updated successfully")
                st.table(result)
elif selected_option == 'Table':
    st.empty()
    with st.container():
        tableId = st.text_input("Table ID:")
        newCapacity = st.text_input("New Capacity:")
        newIsBooked = st.checkbox("Is Booked?")
        newWaiterId = st.text_input("New Waiter ID:")
        submit_button = st.button("Submit")

        if submit_button:
            result = execute_stored_procedure("UpdateTableDine", tableId, newCapacity, newIsBooked, newWaiterId)
            if result:
                st.success("Table information updated successfully")
                st.table(result)
elif selected_option == 'Booking':
    st.empty()
    with st.container():
        customerId = st.text_input("Customer ID:")
        tableId = st.text_input("Table ID:")
        newDate = st.text_input("New Date (YYYY-MM-DD):")
        submit_button = st.button("Submit")

        if submit_button:
            result = execute_stored_procedure("UpdateBooking", customerId, tableId, newDate)
            if result:
                st.success("Booking information updated successfully")
                st.table(result)
