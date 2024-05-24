import streamlit as st
import sqlite3

DATABASE_NAME = 'databaseprojphase2_db'

conn = sqlite3.connect(DATABASE_NAME)

options = ("Menu item", "Delete Employee", "Delete Details of an order", "Customer and Transaction", "Counter", "Table",
           "Booking")
selected_option = st.selectbox("What addition do you want to delete?", options)

if selected_option == "Menu item":
    st.empty()
    with st.container():
        item_types = ("Appetizer", "Entree", "Dessert")  
        item_type_selection = st.selectbox("Choose an item type:", item_types)

        with st.form(key='menu_item_form'):
            col1, col2, col3 = st.columns(3)
            item_name = col1.text_input("Item Name:")
            price = col2.number_input("Price:", value=0.0, step=0.01)
            menu_id = col3.number_input("Menu ID:", value=1)

            additional_fields = {}

            if item_type_selection == 'Appetizer':
                additional_fields["Description"] = st.text_input("Description:")
                additional_fields["Recipe"] = st.text_input("Recipe:")

            if item_type_selection == 'Entree':
                additional_fields["Description"] = st.text_input("Description:")
                additional_fields["Recipe"] = st.text_input("Recipe:")

            if item_type_selection == 'Dessert':
                additional_fields["Description"] = st.text_input("Description:")
                additional_fields["Recipe"] = st.text_input("Recipe:")

            submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            if not item_name or not price or not menu_id:
                st.error("Please fill out all the fields.")
            else:
                item_values = {
                    "ItemName": item_name,
                    "Price": float(price),
                    "MenuId": int(menu_id)
                }

                if item_type_selection == 'Appetizer':
                    delete_query = """
                        DELETE FROM Appetizer_item
                        WHERE item_name = :ItemName AND price = :Price AND menu_id = :MenuId
                    """

                if item_type_selection == 'Entree':
                    delete_query = """
                        DELETE FROM Entree_item
                        WHERE item_name = :ItemName AND price = :Price AND menu_id = :MenuId
                    """

                if item_type_selection == 'Dessert':
                    delete_query = """
                        DELETE FROM Dessert_item
                        WHERE item_name = :ItemName AND price = :Price AND menu_id = :MenuId
                    """

                try:
                    with conn.session as s:
                        s.execute(delete_query, item_values)
                        s.commit()
                    st.success(f"{item_type_selection} item deleted successfully")
                except sqlite3.Error as err:
                    st.error(f"Error: {err}")

elif selected_option == "Delete Employee":
    st.empty()
    with st.container():
        employee_item_options = ("Manager", "Cashier", "Chef", "Waiter")
        employee_item_selection = st.selectbox("Choose an item option:", employee_item_options)
        
        if employee_item_selection == 'Manager':
            with st.form(key='employee_form'):
                col1, col2, col3 = st.columns(3)
                ssn = col1.text_input("SSN:", max_chars=11)
                home_address = col2.text_input("Home Address:")
                birthday = col3.text_input("Date of Birth (YYYY-MM-DD):")

                col4, col5, col6, col7 = st.columns(4)
                salary = col4.text_input("Salary:")
                first_name = col5.text_input("First Name:")
                last_name = col6.text_input("Last Name:")
                manager_id = col7.text_input("Manager ID:")
                
                submit_button = st.form_submit_button(label='Submit')

            if submit_button:
                if not ssn or not home_address or not birthday or not salary or not first_name or not last_name or not manager_id:
                    st.error("Please fill out all the fields.")
                else:
                    employee_values = {
                        "SSN": int(ssn),
                        "Home_Address": home_address,
                        "Date_Of_Birth": birthday,
                        "Salary": float(salary),
                        "First_Name": first_name,
                        "Last_Name": last_name,
                    }
                    
                    manager_values = {
                         "Id": int(manager_id),
                         "Employee_id": int(ssn)
                    }
                    
                    insert_employee_query = sqlalchemy.text("""
                        INSERT INTO Employee (
                            SSN,
                            First_Name,
                            Last_Name,
                            Home_Address,
                            Date_Of_Birth,
                            Salary
                        ) 
                        VALUES (:SSN, :First_Name, :Last_Name, :Home_Address, :Date_Of_Birth, :Salary)
                    """)          
                    
                    insert_manager_query = """
                        INSERT INTO Manager (Id, Employee_id)
                        VALUES (:Id, :Employee_id)
                    """

                    try:
                        with conn.session as s:
                            s.execute(insert_employee_query, employee_values)
                            s.execute(insert_manager_query, manager_values)
                            s.commit()
                        st.success("Manager information inserted successfully")
                    except sqlite3.Error as err:
                        st.error(f"Error: {err}")

        elif employee_item_selection == 'Cashier':
            with st.form(key='employee_form'):
                col1, col2, col3 = st.columns(3)
                ssn = col1.text_input("SSN:", max_chars=11)
                home_address = col2.text_input("Home Address:")
                birthday = col3.text_input("Date of Birth (YYYY-MM-DD):")

                col4, col5, col6, col7 = st.columns(4)
                salary = col4.text_input("Salary:")
                first_name = col5.text_input("First Name:")
                last_name = col6.text_input("Last Name:")
                cashier_id = col7.text_input("Cashier ID:")
                
                submit_button = st.form_submit_button(label='Submit')

            if submit_button:
                if not ssn or not home_address or not birthday or not salary or not first_name or not last_name or not cashier_id:
                    st.error("Please fill out all the fields.")
                else:
                    employee_values = {
                        "SSN": int(ssn),
                        "Home_Address": home_address,
                        "Date_Of_Birth": birthday,
                        "Salary": float(salary),
                        "First_Name": first_name,
                        "Last_Name": last_name,
                    }
                    
                    cashier_values = {
                         "Id": int(cashier_id),
                         "Employee_id": int(ssn)
                    }
                    
                    insert_employee_query = sqlalchemy.text("""
                        INSERT INTO Employee (
                            SSN,
                            First_Name,
                            Last_Name,
                            Home_Address,
                            Date_Of_Birth,
                            Salary
                        ) 
                        VALUES (:SSN, :First_Name, :Last_Name, :Home_Address, :Date_Of_Birth, :Salary)
                    """)          
                    
                    insert_cashier_query = """
                        INSERT INTO Cashier (Id, Employee_id)
                        VALUES (:Id, :Employee_id)
                    """

                    try:
                        with conn.session as s:
                            s.execute(insert_employee_query, employee_values)
                            s.execute(insert_cashier_query, cashier_values)
                            s.commit()
                        st.success("Cashier information inserted successfully")
                    except sqlite3.Error as err:
                        st.error(f"Error: {err}")

        elif employee_item_selection == 'Chef':
            with st.form(key='employee_form'):
                col1, col2, col3 = st.columns(3)
                ssn = col1.text_input("SSN:", max_chars=11)
                home_address = col2.text_input("Home Address:")
                birthday = col3.text_input("Date of Birth (YYYY-MM-DD):")

                col4, col5, col6, col7 = st.columns(4)
                salary = col4.text_input("Salary:")
                first_name = col5.text_input("First Name:")
                last_name = col6.text_input("Last Name:")
                chef_id = col7.text_input("Chef ID:")
                
                submit_button = st.form_submit_button(label='Submit')

            if submit_button:
                if not ssn or not home_address or not birthday or not salary or not first_name or not last_name or not chef_id:
                    st.error("Please fill out all the fields.")
                else:
                    employee_values = {
                        "SSN": int(ssn),
                        "Home_Address": home_address,
                        "Date_Of_Birth": birthday,
                        "Salary": float(salary),
                        "First_Name": first_name,
                        "Last_Name": last_name,
                    }
                    
                    chef_values = {
                         "Id": int(chef_id),
                         "Employee_id": int(ssn)
                    }
                    
                    insert_employee_query = sqlalchemy.text("""
                        INSERT INTO Employee (
                            SSN,
                            First_Name,
                            Last_Name,
                            Home_Address,
                                                        Date_Of_Birth,
                            Salary
                        ) 
                        VALUES (:SSN, :First_Name, :Last_Name, :Home_Address, :Date_Of_Birth, :Salary)
                    """)          
                    
                    insert_chef_query = """
                        INSERT INTO Chef (Id, Employee_id)
                        VALUES (:Id, :Employee_id)
                    """

                    try:
                        with conn.session as s:
                            s.execute(insert_employee_query, employee_values)
                            s.execute(insert_chef_query, chef_values)
                            s.commit()
                        st.success("Chef information inserted successfully")
                    except sqlite3.Error as err:
                        st.error(f"Error: {err}")

        elif employee_item_selection == 'Waiter':
            with st.form(key='employee_form'):
                col1, col2, col3 = st.columns(3)
                ssn = col1.text_input("SSN:", max_chars=11)
                home_address = col2.text_input("Home Address:")
                birthday = col3.text_input("Date of Birth (YYYY-MM-DD):")

                col4, col5, col6, col7 = st.columns(4)
                salary = col4.text_input("Salary:")
                first_name = col5.text_input("First Name:")
                last_name = col6.text_input("Last Name:")
                waiter_id = col7.text_input("Waiter ID:")
                
                submit_button = st.form_submit_button(label='Submit')

            if submit_button:
                if not ssn or not home_address or not birthday or not salary or not first_name or not last_name or not waiter_id:
                    st.error("Please fill out all the fields.")
                else:
                    employee_values = {
                        "SSN": int(ssn),
                        "Home_Address": home_address,
                        "Date_Of_Birth": birthday,
                        "Salary": float(salary),
                        "First_Name": first_name,
                        "Last_Name": last_name,
                    }
                    
                    waiter_values = {
                         "Id": int(waiter_id),
                         "Employee_id": int(ssn)
                    }
                    
                    insert_employee_query = sqlalchemy.text("""
                        INSERT INTO Employee (
                            SSN,
                            First_Name,
                            Last_Name,
                            Home_Address,
                            Date_Of_Birth,
                            Salary
                        ) 
                        VALUES (:SSN, :First_Name, :Last_Name, :Home_Address, :Date_Of_Birth, :Salary)
                    """)          
                    
                    insert_waiter_query = """
                        INSERT INTO Waiter (Id, Employee_id)
                        VALUES (:Id, :Employee_id)
                    """

                    try:
                        with conn.session as s:
                            s.execute(insert_employee_query, employee_values)
                            s.execute(insert_waiter_query, waiter_values)
                            s.commit()
                        st.success("Waiter information inserted successfully")
                    except sqlite3.Error as err:
                        st.error(f"Error: {err}")
elif selected_option == "Delete Details of an order":
    st.empty()
    with st.container():
        with st.form(key='Delete_order_form'):
            order_id_label = "Order ID:"
            order_id = st.text_input(order_id_label)
            
            submit_button = st.form_submit_button(label='Delete')

        if submit_button:
            if not order_id:
                st.error("Please provide the Order ID.")
            else:
                delete_order_query = sqlalchemy.text("""
                    DELETE FROM Order_food
                    WHERE Order_id = :order_id
                """)
                
                delete_makes_order_query = sqlalchemy.text("""
                    DELETE FROM Makes_order
                    WHERE Order_id_ref = :order_id
                """)
                
                delete_receives_order_query = sqlalchemy.text("""
                    DELETE FROM Receive_order
                    WHERE Order_id_ref = :order_id
                """)
                
                delete_transaction_query = sqlalchemy.text("""
                    DELETE FROM Transaction_
                    WHERE Id IN (
                        SELECT Transaction_id_ref
                        FROM Makes_order
                        WHERE Order_id_ref = :order_id
                    )
                """)
                
                update_availability_query = sqlalchemy.text("""
                    UPDATE Table_dine
                    SET Is_available = TRUE
                    WHERE Id = (
                        SELECT table_id_ref
                        FROM Order_food
                        WHERE Order_id = :order_id
                    )
                """)
                
                try:
                    with conn.session as s:
                        s.execute(delete_order_query, {"order_id": order_id})
                        s.execute(delete_makes_order_query, {"order_id": order_id})
                        s.execute(delete_receives_order_query, {"order_id": order_id})
                        s.execute(delete_transaction_query, {"order_id": order_id})
                        s.execute(update_availability_query, {"order_id": order_id})
                        s.commit()
                    st.success("Order details deleted successfully")
                except sqlite3.Error as err:
                    st.error(f"Error: {err}")
elif selected_option == "Customer and Transaction":
    st.empty()
    with st.container():
        with st.form(key='Delete_customer_transaction_form'):
            customer_id_label = "Customer ID:"
            customer_id = st.text_input(customer_id_label)
            
            submit_button = st.form_submit_button(label='Delete')

        if submit_button:
            if not customer_id:
                st.error("Please provide the Customer ID.")
            else:
                delete_customer_query = sqlalchemy.text("""
                    DELETE FROM Customer
                    WHERE Customer_id = :customer_id
                """)
                
                delete_makes_order_query = sqlalchemy.text("""
                    DELETE FROM Makes_order
                    WHERE Customer_id_ref = :customer_id
                """)
                
                delete_transaction_query = sqlalchemy.text("""
                    DELETE FROM Transaction_
                    WHERE Id IN (
                        SELECT Transaction_id_ref
                        FROM Makes_order
                        WHERE Customer_id_ref = :customer_id
                    )
                """)
                
                try:
                    with conn.session as s:
                        s.execute(delete_customer_query, {"customer_id": customer_id})
                        s.execute(delete_makes_order_query, {"customer_id": customer_id})
                        s.execute(delete_transaction_query, {"customer_id": customer_id})
                        s.commit()
                    st.success("Customer and transaction details deleted successfully")
                except sqlite3.Error as err:
                    st.error(f"Error: {err}")
elif selected_option == 'Counter':
    st.empty()
    with st.container():
        with st.form(key='Delete_Counter_form'):
            counter_id = st.text_input("Counter id: ")
            
            submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            if not counter_id:
                st.error("Please fill out all the fields.")
            else:
                delete_counter_query = sqlalchemy.text("""
                    DELETE FROM Counter
                    WHERE Id = :Id
                """)
                
                counter_values = {
                    "Id": int(counter_id)
                }
                
                try:
                    with conn.session as s:
                        s.execute(delete_counter_query, counter_values)
                        s.commit()
                    st.success("Counter information deleted successfully")
                except sqlite3.Error as err:
                    st.error(f"Error: {err}")
                           
elif selected_option == 'Table':
    st.empty()
    with st.container():
        with st.form(key='Delete_Table_form'):
            col1, col2, col3 , col4 = st.columns(4)
            table_id = col1.text_input("Table id: ")
            capacity = col2.text_input("Capacty:")
            counter_id_label = "select table status:"
            is_booked_options =  tuple(["no" , "yes"])
            is_booked = col3.selectbox(counter_id_label , is_booked_options)
            waiter_id = col4.text_input("Waiter id:")
            
            submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            if not table_id or not capacity or not is_booked or not waiter_id:
                st.error("Please fill out all the fields.")
            else:
                statues_bool = False
                # Define the insert statement with ON CONFLICT clause
                # Create a dictionary with the collected values
                if(is_booked == "no"):
                    statues_bool = False
                else:
                    statues_bool = True

                employee_values = {
                    "Id": int(table_id),
                    "capacity": int(capacity),
                    "Is_available": statues_bool,
                    "Waiter_id_ref": int(waiter_id)
                }
                
                delete_table_query = sqlalchemy.text("""
                    DELETE FROM Table_dine
                    WHERE Id = :Id
                """)
                
                try:
                    with conn.session as s:
                        s.execute(delete_table_query, employee_values)
                        s.commit()
                    st.success("Table information deleted successfully")
                except sqlite3.Error as err:
                    st.error(f"Error: {err}")

elif selected_option == 'Booking':
    st.empty()
    with st.container():
        with st.form(key='Delete_Booking_form'):
            col1 , col2 , col3 = st.columns(3)
            date = col3.text_input("Date: ")
            
            select_available_customer_query = sqlalchemy.text("""
                    SELECT Customer_id
                    FROM Customer
                """)
                
            with conn.session as s:
                result = s.execute(select_available_customer_query)
                # Fetch all results and convert to a tuple of IDs
                customer_ids = tuple(row[0] for row in result)        
            
            customer_ids_id_label = "select customer id:"
        
            customer_id_options = customer_ids
            customer_id = col1.selectbox(customer_ids_id_label , customer_id_options)
            
            select_available_tables_query = sqlalchemy.text("""
                SELECT Id
                FROM Table_dine
                WHERE Is_available = TRUE
            """)
    
            with conn.session as s:
                result = s.execute(select_available_tables_query)
                # Fetch all results and convert to a tuple of IDs
                table_ids = tuple(row[0] for row in result)        
                
            table_ids_id_label = "select table id:"
        
            counter_table_id_options = table_ids
            table_id = col2.selectbox(table_ids_id_label , counter_table_id_options)
            
            submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            # Validate the inputs (basic validation)
            if  not date :
                st.error("Please fill out all the fields.")
            else:

                Booking_values = {
                    "Customer_id_ref": int(customer_id),
                    "Table_dine_id_ref": int(table_id),
                    "book_date": date
                }
                
                delete_booking_query = sqlalchemy.text("""
                    DELETE FROM Booking
                    WHERE Customer_id_ref = :Customer_id_ref
                    AND Table_dine_id_ref = :Table_dine_id_ref
                    AND book_date = :book_date
                """)
                
                try:
                    with conn.session as s:
                        s.execute(delete_booking_query, Booking_values)
                        s.commit()
                    st.success("Booking information deleted successfully")
                except sqlite3.Error as err:
                    st.error(f"Error: {err}")

