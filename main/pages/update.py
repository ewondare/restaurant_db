import streamlit as st
import pypyodbc as odbc

DRIVER_NAME = "SQL SERVER"
SERVER_NAME = "DESKTOP-0S9785Q\SQLEXPRESS"
DATABASE_NAME = "GroupAssignment1"

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""

conn = odbc.connect(connectString=connection_string)

options = (
    "Menu item",
    "Update Employee",
    "Update Details of an order",
    "Customer and Transaction",
    "Counter",
    "Table",
    "Booking",
)
selected_option = st.selectbox("What update you going to make?", options)

if selected_option == "Menu item":
    st.empty()
    with st.container():
        menu_item_options = ("Appetizer", "Entree", "Dessert")
        menu_item_selection = st.selectbox("Choose a menu item option:", menu_item_options)

        if menu_item_selection in ["Appetizer", "Entree", "Dessert"]:
            update_options = ("name", "price", "description", "recipe")
            menu_item_update = st.selectbox("Which item do you want to update", update_options)
            
            id_label = f"{menu_item_selection} id: "
            id = st.text_input(id_label)
            
            if st.button("Submit"):
                if menu_item_update in update_options:
                    new_value = st.text_input(f"New {menu_item_update.capitalize()}:")
                    
                    try:
                        with conn.cursor() as cursor:
                            cursor.execute(
                                f"""
                                UPDATE {menu_item_selection}
                                SET {menu_item_update} = ?
                                WHERE Id = ?;
                                """,
                                (new_value, id),
                            )
                            conn.commit()
                            st.success(f"{menu_item_selection.capitalize()} information updated successfully")

                            cursor.execute(
                                f"SELECT 'Updated {menu_item_selection}' AS Status, * FROM {menu_item_selection} WHERE Id = ?;",
                                (id,),
                            )
                            result = cursor.fetchall()
                            st.table(result)

                    except Exception as e:
                        st.error(f"Error: {e}")
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
            try:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        UPDATE Employee
                        SET 
                            First_Name = ?,
                            Last_Name = ?,
                            Home_Address = ?,
                            Date_Of_Birth = ?,
                            Salary = ?
                        WHERE SSN = ?;
                        """,
                        (newFirstName, newLastName, newHomeAddress, newDateOfBirth, newSalary, empSSN),
                    )
                    conn.commit()

                    cursor.execute(
                        """
                        SELECT 'Updated Employee' AS Status, * FROM Employee WHERE SSN = ?;
                        """,
                        (empSSN,),
                    )
                    result = cursor.fetchall()
                    st.success("Employee information updated successfully")
                    st.table(result)

            except Exception as e:
                st.error(f"Error: {e}")

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
            try:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        UPDATE Order_food
                        SET 
                            Table_condition = ?,
                            is_paid = ?,
                            price = ?,
                            order_date = ?,
                            table_id_ref = ?
                        WHERE Order_id = ?;
                        """,
                        (newTableCondition, newIsPaid, newPrice, newOrderDate, newTableIdRef, orderId),
                    )
                    conn.commit()

                    cursor.execute(
                        """
                        SELECT 'Updated Order_food' AS Status, * FROM Order_food WHERE Order_id = ?;
                        """,
                        (orderId,),
                    )
                    result = cursor.fetchall()
                    st.success("Order details updated successfully")
                    st.table(result)

            except Exception as e:
                st.error(f"Error: {e}")

elif selected_option == 'Customer and Transaction':
    st.empty()
    with st.container():
        customerId = st.text_input("Customer ID:")
        newFirstName = st.text_input("New First Name:")
        newLastName = st.text_input("New Last Name:")
        submit_button = st.button("Submit")

        if submit_button:
            try:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        UPDATE Customer
                        SET 
                            First_name = ?,
                            last_name = ?
                        WHERE Customer_id = ?;
                        """,
                        (newFirstName, newLastName, customerId),
                    )
                    conn.commit()

                    cursor.execute(
                        """
                        SELECT 'Updated Customer' AS Status, * FROM Customer WHERE Customer_id = ?;
                        """,
                        (customerId,),
                    )
                    result = cursor.fetchall()
                    st.success("Customer information updated successfully")
                    st.table(result)

            except Exception as e:
                st.error(f"Error: {e}")

elif selected_option == 'Counter':
    st.empty()
    with st.container():
        counterId = st.text_input("Counter ID:")
        newId = st.text_input("New ID:")
        submit_button = st.button("Submit")

        if submit_button:
            try:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        UPDATE Counter
                        SET 
                            Id = ?
                        WHERE Id = ?;
                        """,
                        (newId, counterId),
                    )
                    conn.commit()

                    cursor.execute(
                        """
                        SELECT 'Updated Counter' AS Status, * FROM Counter WHERE Id = ?;
                        """,
                        (newId,),
                    )
                    result = cursor.fetchall()
                    st.success("Counter information updated successfully")
                    st.table(result)

            except Exception as e:
                st.error(f"Error: {e}")

elif selected_option == 'Table':
    st.empty()
    with st.container():
        tableId = st.text_input("Table ID:")
        newCapacity = st.text_input("New Capacity:")
        newIsBooked = st.checkbox("Is Booked?")
        newWaiterId = st.text_input("New Waiter ID:")
        submit_button = st.button("Submit")

        if submit_button:
            try:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        UPDATE Table_dine
                        SET 
                            capacity = ?,
                            Is_available = ?,
                            Waiter_id_ref = ?
                        WHERE Id = ?;
                        """,
                        (newCapacity, newIsBooked, newWaiterId, tableId),
                    )
                    conn.commit()

                    cursor.execute(
                        """
                        SELECT 'Updated Table_dine' AS Status, * FROM Table_dine WHERE Id = ?;
                        """,
                        (tableId,),
                    )
                    result = cursor.fetchall()
                    st.success("Table information updated successfully")
                    st.table(result)

            except Exception as e:
                st.error(f"Error: {e}")

elif selected_option == 'Booking':
    st.empty()
    with st.container():
        customerId = st.text_input("Customer ID:")
        tableId = st.text_input("Table ID:")
        newDate = st.text_input("New Date (YYYY-MM-DD):")
        submit_button = st.button("Submit")

        if submit_button:
            try:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        UPDATE Booking
                        SET 
                            book_date = ?
                        WHERE Customer_id_ref = ? AND Table_dine_id_ref = ?;
                        """,
                        (newDate, customerId, tableId),
                    )
                    conn.commit()

                    cursor.execute(
                        """
                        SELECT 'Updated Booking' AS Status, * FROM Booking WHERE Customer_id_ref = ? AND Table_dine_id_ref = ?;
                        """,
                        (customerId, tableId),
                    )
                    result = cursor.fetchall()
                    st.success("Booking information updated successfully")
                    st.table(result)

            except Exception as e:
                st.error(f"Error: {e}")

