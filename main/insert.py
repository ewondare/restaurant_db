import streamlit as st
import pypyodbc as odbc 
import sqlite3
import sqlalchemy

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'DESKTOP-0S9785Q\SQLEXPRESS'
DATABASE_NAME = 'databaseprojphase2_db'


connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;

"""

conn = st.connection('databaseprojphase2_db', type='sql')
print(conn)


options = ("Menu item", "New Employee", "New Details of an order", "Customer and Transaction", "Counter" , "Table" , "Booking")
selected_option = st.selectbox("What new addition are you going to make?", options)


if selected_option == "Menu item":
    with st.container():
        menu_item_options = ("Appetizer", "Entree", "Desert")  
        menu_item_selection = st.selectbox("Choose a menu item option:", menu_item_options)

        if menu_item_selection == 'Appetizer':
            #name, price, description, recipe = None
            
            id_label = "id: "
            name_label = "name: "
            price_label = "price:"
            description_label = "description: "
            recipe_label = "recipe: "

            col1,col2,col3 = st.columns(3)
            id = col1.text_input(id_label)
            name = col2.text_input(name_label)
            price = col3.text_input(price_label)
            col4, col5 = st.columns(2)
            description = col4.text_input(description_label)
            recipe = col5.text_input(recipe_label)
            menu_id = 1

            # if id does not exist -> insert
        elif menu_item_selection == 'Entree':
            #name, price, description, recipe = None
            
            id_label = "id: "
            name_label = "name: "
            price_label = "price:"
            description_label = "description: "
            recipe_label = "recipe: "

            col1,col2,col3 = st.columns(3)
            id = col1.text_input(id_label)
            name = col2.text_input(name_label)
            price = col3.text_input(price_label)
            col4, col5 = st.columns(2)
            description = col4.text_input(description_label)
            recipe = col5.text_input(recipe_label)
            menu_id = 2

            # if id does not exist -> insert
        elif menu_item_selection == 'Desert':
            #name, price, description, recipe = None
            
            id_label = "id: "
            name_label = "name: "
            price_label = "price:"
            description_label = "description: "
            recipe_label = "recipe: "

            col1,col2,col3 = st.columns(3)
            id = col1.text_input(id_label)
            name = col2.text_input(name_label)
            price = col3.text_input(price_label)
            col4, col5 = st.columns(2)
            description = col4.text_input(description_label)
            recipe = col5.text_input(recipe_label)
            menu_id = 3

            # if id does not exist -> insert


        

elif selected_option ==  "New Employee":
    st.empty()
    with st.container():
        employee_item_options = ("Manager", "Cashier", "Chef" , "Waiter")  
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
                
                # Use the submit button inside the form context
                submit_button = st.form_submit_button(label='Submit')

            if submit_button:
                # Validate the inputs (basic validation)
                if not ssn or not home_address or not birthday or not salary or not first_name or not last_name or not manager_id:
                    st.error("Please fill out all the fields.")
                else:
                    # Define the insert statement with ON CONFLICT clause
                    # Create a dictionary with the collected values
                    employee_values = {
                        "SSN": int(ssn),
                        "Home_Address": home_address,
                        "Date_Of_Birth": birthday,
                        "Salary": float(salary),
                        "First_Name": first_name,
                        "Last_Name": last_name,
                    }
                    print(employee_values)
                    
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
                        ON CONFLICT (SSN) DO NOTHING
                    """)          
                    
                    insert_manager_query = """
                        INSERT INTO Manager (Id, Employee_id)
                        VALUES (:Id, :Employee_id)
                        ON CONFLICT(Id)  DO NOTHING
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
            with st.form(key='Cashier_form'):
                col0, col1 = st.columns(2)
                col2,col3 = st.columns(2)
                ssn = col1.text_input("ssn:")
                home_address = col2.text_input("home address:")
                birthday = col3.text_input("date of birthday:")
    
                col4, col5, col6, col7 = st.columns(4)
                salary = col4.text_input("salary: ")
                first_name = col5.text_input("first name:")
                last_name = col6.text_input("last name:")
                # 1.insert into employee if ssn doesn not already exist
    
                Cashier_id = col7.text_input("Cashier id:")
                ########
                ### query = "Select id from counter"
                ### df = 
                ###Names = df['id]
                counter_id_options = tuple([1 , 2 , 3]) # = id
                counter_id = col0.selectbox("counter id: " , counter_id_options)
                # Use the submit button inside the form context
                submit_button = st.form_submit_button(label='Submit')

            if submit_button:
                # Validate the inputs (basic validation)
                if not ssn or not home_address or not birthday or not salary or not first_name or not last_name or not Cashier_id:
                    st.error("Please fill out all the fields.")
                else:
                    # Define the insert statement with ON CONFLICT clause
                    # Create a dictionary with the collected values
                    employee_values = {
                        "SSN": int(ssn),
                        "Home_Address": home_address,
                        "Date_Of_Birth": birthday,
                        "Salary": float(salary),
                        "First_Name": first_name,
                        "Last_Name": last_name,
                    }
                    
                    Cashier_values = {
                         "Id": int(Cashier_id),
                         "Employee_id": int(ssn),
                         "Counter_id": int(counter_id)
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
                        ON CONFLICT (SSN) DO NOTHING
                    """)          
                    
                    insert_Cashier_query = """
                        INSERT INTO Cashier (Id, Employee_id,Counter_id)
                        VALUES (:Id, :Employee_id , :Counter_id)
                        ON CONFLICT(Id)  DO NOTHING
                    """

                    try:
                        with conn.session as s:
                            s.execute(insert_employee_query, employee_values)
                            s.execute(insert_Cashier_query, Cashier_values)
                            s.commit()
                        st.success("Cashier information inserted successfully")
                    except sqlite3.Error as err:
                        st.error(f"Error: {err}")
                

        elif employee_item_selection == 'Chef':
            #home_address, birthday , salary, first_name, last_name = None
            with st.form(key='Chef_form'):
    
                col1,col2,col3 = st.columns(3)
                ssn = col1.text_input("ssn:")
                home_address = col2.text_input("home address:")
                birthday = col3.text_input("date of birthday:")
    
                col4, col5, col6, col7 = st.columns(4)
                salary = col4.text_input("salary: ")
                first_name = col5.text_input("first name:")
                last_name = col6.text_input("last name:")
                # 1.insert into employee if ssn doesn not already exist
    
                Chef_id = col7.text_input("Chef id:")
                # 2.insert id, ssn into chef if id does not already exist 
                # Use the submit button inside the form context
                submit_button = st.form_submit_button(label='Submit')

            if submit_button:
                # Validate the inputs (basic validation)
                if not ssn or not home_address or not birthday or not salary or not first_name or not last_name or not Chef_id:
                    st.error("Please fill out all the fields.")
                else:
                    # Define the insert statement with ON CONFLICT clause
                    # Create a dictionary with the collected values
                    employee_values = {
                        "SSN": int(ssn),
                        "Home_Address": home_address,
                        "Date_Of_Birth": birthday,
                        "Salary": float(salary),
                        "First_Name": first_name,
                        "Last_Name": last_name,
                    }
                    print(employee_values)
                    
                    Chef_values = {
                         "Id": int(Chef_id),
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
                        ON CONFLICT (SSN) DO NOTHING
                    """)          
                    
                    insert_Chef_query = """
                        INSERT INTO Chef (Id, Employee_id)
                        VALUES (:Id, :Employee_id)
                        ON CONFLICT(Id)  DO NOTHING
                    """

                    try:
                        with conn.session as s:
                            s.execute(insert_employee_query, employee_values)
                            s.execute(insert_Chef_query, Chef_values)
                            s.commit()
                        st.success("Chef information inserted successfully")
                    except sqlite3.Error as err:
                        st.error(f"Error: {err}")

                
        elif employee_item_selection == 'Waiter':
            #home_address, birthday , salary, first_name, last_name = None
            with st.form(key='Waiter_form'):

                col1,col2,col3 = st.columns(3)
                ssn = col1.text_input("ssn:")
                home_address = col2.text_input("home address:")
                birthday = col3.text_input("date of birthday:")
    
                col4, col5, col6, col7 = st.columns(4)
                salary = col4.text_input("salary: ")
                first_name = col5.text_input("first name:")
                last_name = col6.text_input("last name:")
                # 1.insert into employee if ssn doesn not already exist
    
                Waiter_id = col7.text_input("Waiter id:")
                # 2.insert id, ssn into waiter if id does not already exist      
                submit_button = st.form_submit_button(label='Submit')

            if submit_button:
                # Validate the inputs (basic validation)
                if not ssn or not home_address or not birthday or not salary or not first_name or not last_name or not Waiter_id:
                    st.error("Please fill out all the fields.")
                else:
                    # Define the insert statement with ON CONFLICT clause
                    # Create a dictionary with the collected values
                    employee_values = {
                        "SSN": int(ssn),
                        "Home_Address": home_address,
                        "Date_Of_Birth": birthday,
                        "Salary": float(salary),
                        "First_Name": first_name,
                        "Last_Name": last_name,
                    }
                    print(employee_values)
                    
                    Waiter_values = {
                         "Id": int(Waiter_id),
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
                        ON CONFLICT (SSN) DO NOTHING
                    """)          
                    
                    insert_Waiter_query = """
                        INSERT INTO Waiter (Id, Employee_id)
                        VALUES (:Id, :Employee_id)
                        ON CONFLICT(Id)  DO NOTHING
                    """

                    try:
                        with conn.session as s:
                            s.execute(insert_employee_query, employee_values)
                            s.execute(insert_Waiter_query, Waiter_values)
                            s.commit()
                        st.success("Chef information inserted successfully")
                    except sqlite3.Error as err:
                        st.error(f"Error: {err}")




elif selected_option == "New Details of an order":
    st.empty()
    with st.container():
        with st.form(key='Waiter_form'):
   
            order_id_label = "order id:"
            table_id_label = "table id:"
            is_paid_label = "is paid:"
            date_label = "date:"
            counter_id_label = "select counter id:"
            col1, col2, col3 = st.columns(3)
            order_id = col1.text_input(order_id_label)
            
            paid_id_label = "select paid status:"
            is_paid_options =  tuple(["no" , "yes"])
            is_paid = col3.selectbox(paid_id_label , is_paid_options)
    
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
    
    
            col4, col5 , col15 = st.columns(3)
            date  = col4.text_input(date_label)
            price  = col4.text_input("price:")

            select_available_Waiters_query = sqlalchemy.text("""
                    SELECT Id
                    FROM Waiter
                    
                """)
                
            with conn.session as s:
                result = s.execute(select_available_Waiters_query)
                # Fetch all results and convert to a tuple of IDs
                waiter_ids = tuple(row[0] for row in result)        
    
            select_available_chef_query = sqlalchemy.text("""
                    SELECT Id
                    FROM Chef
                """)
                
            with conn.session as s:
                result = s.execute(select_available_chef_query)
                # Fetch all results and convert to a tuple of IDs
                chef_ids = tuple(row[0] for row in result)        
        
            ########
            ### query = "Select id from counter"
            ### df = 
            ###Names = df['id]
            counter_id_options = tuple([1 , 2 , 3]) # = id
            counter_id = col5.selectbox(counter_id_label , counter_id_options)
    
            st.write("for also entering details for [Recieve Order] table, please fill the following setions.")
            col6,col7,col8 = st.columns(3)
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
            customer_id = col8.selectbox(customer_ids_id_label , customer_id_options)
           
            chef_ids_id_label = "select chef id:"
        
            counter_chef_id_options = chef_ids
            chef_id = col6.selectbox(chef_ids_id_label , counter_chef_id_options)
    
                    
            waiter_ids_id_label = "select waiter id:"
        
            counter_waiter_id_options = waiter_ids
            waiter_id = col7.selectbox(waiter_ids_id_label , counter_waiter_id_options)
            
            
            
            col1, col2, col3, col4 = st.columns(4)
            transaction_id = col1.text_input("Transaction id:")
            
            transaction_id_options = tuple([1 , 2]) # = id
            Type = col2.selectbox("1 for cash, 2 credit card",transaction_id_options)
            
            discount_id_label = "select discount status:"
            is_discount_options =  tuple(["no" , "yes"])
            discount = col3.selectbox(discount_id_label , is_discount_options)

            submit_button = st.form_submit_button(label='Submit')
  
        if submit_button:
                    # Validate the inputs (basic validation)
                    if not waiter_id or not chef_id or not customer_id or not counter_id or not price or not order_id or not price or not date or not transaction_id:
                        st.error("Please fill out all the fields.")
                    else:
                        statues_bool = False
                        # Define the insert statement with ON CONFLICT clause
                        # Create a dictionary with the collected values
                        if(is_paid == "no"):
                            statues_bool = False
                        else:
                            statues_bool = True
                            
                        statues_bool_discount = False
                        # Define the insert statement with ON CONFLICT clause
                        # Create a dictionary with the collected values
                        if(discount == "no"):
                            statues_bool_discount = False
                        else:
                            statues_bool_discount = True

                        # Define the insert statement with ON CONFLICT clause
                        # Create a dictionary with the collected values
                        Order_food_values = {
                            "Order_id": int(order_id),
                            "Table_condition": "state of art",
                            "is_paid": statues_bool,
                            "price": float(price),
                            "order_date": date,
                            "table_id_ref": int(table_id),
                        }
                        

                                                
                        insert_Order_food_query = sqlalchemy.text("""
                            INSERT INTO Order_food (
                                Order_id,
                                Table_condition,
                                is_paid,
                                price,
                                order_date,
                                table_id_ref
                            ) 
                            VALUES (:Order_id, :Table_condition, :is_paid, :price, :order_date, :table_id_ref)
                            ON CONFLICT (Order_id) DO NOTHING
                        """)         
                        
                        Makes_order_values = {
                            "Customer_id_ref": int(customer_id),
                            "Order_id_ref": int(order_id),
                            "Transaction_id_ref": int(transaction_id),
                        }

                        insert_Makes_order_query = sqlalchemy.text("""
                            INSERT INTO Makes_order (
                                Customer_id_ref,
                                Order_id_ref,
                                Transaction_id_ref
                                ) 
                            VALUES (:Customer_id_ref, :Order_id_ref, :Transaction_id_ref)
                        """)   
                        
                        Receives_order_values = {
                            "Chef_id_ref": int(chef_id),
                            "Order_id_ref": int(order_id),
                            "Waiter_id_ref": int(waiter_id),
                        }     
                        
                        insert_Receives_order_query = sqlalchemy.text("""
                            INSERT INTO Receive_order (
                                Chef_id_ref,
                                Order_id_ref,
                                Waiter_id_ref
                                ) 
                            VALUES (:Chef_id_ref, :Order_id_ref, :Waiter_id_ref)
                        """)                            
                        transaction_values = {
                            "Id": int(transaction_id),
                            "Is_discounter": statues_bool_discount,
                            "transaction_tyep": int(Type),
                            "Counter_id_ref": int(counter_id)
                        } 
                        insert_transaction_query = sqlalchemy.text("""
                            INSERT INTO Transaction_ (
                                Id,
                                Is_discounter,
                                transaction_tyep,
                                Counter_id_ref
                                ) 
                            VALUES (:Id, :Is_discounter, :transaction_tyep, :Counter_id_ref)
                        """)           
                        
                        update_availability_query = sqlalchemy.text("""
                            UPDATE Table_dine
                            SET Is_available = False
                            WHERE Id = :table_id
                        """)    
                        
                        update_table_values = {
                            "table_id": int(table_id)
                         } 
                        try:
                            with conn.session as s:
                                s.execute(insert_Order_food_query, Order_food_values)
                                s.execute(insert_Makes_order_query, Makes_order_values)
                                s.execute(insert_Receives_order_query, Receives_order_values)
                                s.execute(insert_transaction_query, transaction_values)
                                s.execute(update_availability_query, update_table_values)

                                s.commit()
                            st.success("order information inserted successfully")
                        except sqlite3.Error as err:
                            st.error(f"Error: {err}")
            ######
            ## if chef_id and waiter_id exist => chef_id , waiter_id , order_id insert into [Recieve Order]






elif selected_option == "Customer and Transaction":
    st.empty()
    with st.container():
        with st.form(key='Waiter_form'):
    
            st.write("please update all the details relating to the order and its transaction.")
            
            customer_id_label = "Customer ID:"
            first_name_label = "First Name:"
            last_name_label = "Last Name:"
            col1, col2, col3 = st.columns(3)
            customer_id = col1.text_input(customer_id_label)
            first_name = col2.text_input(first_name_label)
            last_name = col3.text_input(last_name_label)
    

            submit_button = st.form_submit_button(label='Submit')
    
        if submit_button:
                    # Validate the inputs (basic validation)
                    if not customer_id or not first_name_label or not first_name or not last_name :
                        st.error("Please fill out all the fields.")
                    else:

                        # Define the insert statement with ON CONFLICT clause
                        # Create a dictionary with the collected values
                        Customer_values = {
                            "Customer_id": int(customer_id),
                            "First_name": first_name,
                            "last_name": last_name
                        }
                        


                                                
                        insert_Customer_query = sqlalchemy.text("""
                            INSERT INTO Customer (
                                Customer_id,
                                First_name,
                                last_name
                            ) 
                            VALUES (:Customer_id, :First_name, :last_name)
                            ON CONFLICT (Customer_id) DO NOTHING
                        """)          

  
                        try:
                            with conn.session as s:
                                s.execute(insert_Customer_query, Customer_values)

                                s.commit()
                            st.success("Customer information inserted successfully")
                        except sqlite3.Error as err:
                            st.error(f"Error: {err}")

        



elif selected_option == 'Counter':
    st.empty()
    with st.container():
         with st.form(key='Counter_form'):

             counter_id = st.text_input("Counter id: ")
    ### query -> if counter id does not exist -> insert
                # Use the submit button inside the form context
             submit_button = st.form_submit_button(label='Submit')
             if submit_button:
                 # Validate the inputs (basic validation)
                 if not counter_id:
                     st.error("Please fill out all the fields.")
                 else:
                     # Define the insert statement with ON CONFLICT clause
                     # Create a dictionary with the collected values
                     counter_values = {
                         "Id": int(counter_id),
                     }               
                     
                     insert_counter_query = sqlalchemy.text("""
                         INSERT INTO Counter (
                             Id
                         ) 
                         VALUES (:Id)
                         ON CONFLICT (Id) DO NOTHING
                     """)          
                     
                     try:
                         with conn.session as s:
                             s.execute(insert_counter_query, counter_values)
                             s.commit()
                         st.success("Counter information inserted successfully")
                     except sqlite3.Error as err:
                         st.error(f"Error: {err}")



elif selected_option == 'Table':
    st.empty()
    with st.container():
        with st.form(key='Table_form'):

            col1, col2, col3 , col4 = st.columns(4)
            table_id = col1.text_input("Table id: ")
            capacity = col2.text_input("Capacty:")
            counter_id_label = "select table status:"

            is_booked_options =  tuple(["no" , "yes"])
            is_booked = col3.selectbox(counter_id_label , is_booked_options)
            waiter_id = col4.text_input("Waiter id:")
            
            submit_button = st.form_submit_button(label='Submit')

            if submit_button:
                # Validate the inputs (basic validation)
                if  not table_id or not capacity or not is_booked or not waiter_id:
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
                    
                    insert_employee_query = sqlalchemy.text("""
                        INSERT INTO Table_dine (
                            Id,
                            capacity,
                            Is_available,
                            Waiter_id_ref
                        ) 
                        VALUES (:Id, :capacity, :Is_available, :Waiter_id_ref)
                        ON CONFLICT (Id) DO NOTHING
                    """)          
                    
                    try:
                        with conn.session as s:
                            s.execute(insert_employee_query, employee_values)
                            s.commit()
                        st.success("Table information inserted successfully")
                    except sqlite3.Error as err:
                        st.error(f"Error: {err}")


elif selected_option == 'Booking':
    st.empty()
    with st.container():
        with st.form(key='Waiter_form'):

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
            
            # if customer id and table id already exist -> insert
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
                    
                    insert_Booking_query = sqlalchemy.text("""
                        INSERT INTO Booking (
                            Customer_id_ref,
                            Table_dine_id_ref,
                            book_date
                        ) 
                        VALUES (:Customer_id_ref, :Table_dine_id_ref, :book_date)
                    """)          
                    
                    try:
                        with conn.session as s:
                            s.execute(insert_Booking_query, Booking_values)
                            s.commit()
                        st.success("booking information inserted successfully")
                    except sqlite3.Error as err:
                        st.error(f"Error: {err}")
         


# elif     un 3 ta
# retrieve order tuye Order anjam mishe.
