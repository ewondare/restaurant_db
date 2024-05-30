import streamlit as st
import pypyodbc as odbc 
import sqlite3
import sqlalchemy

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'DESKTOP-2V8SO2H\SQLEXPRESS'
DATABASE_NAME = 'mydb'


connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""

conn = odbc.connect(connectString=connection_string)
print(conn)


options = ("Menu item", "New Employee", "New Details of an order", "Customer and Transaction", "Counter" , "Table" , "Booking","create menu")
selected_option = st.selectbox("What new addition are you going to make?", options)


if selected_option == "Menu item":
    with st.container():
        with st.form(key='employee_form'):

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

                # Use the submit button inside the form context
            submit_button = st.form_submit_button(label='Submit')

            if submit_button:
                # Validate the inputs (basic validation)
                if not price or not recipe or not name or not description:
                    st.error("Please fill out all the fields.")
                else:
                    # Define the insert statement with ON CONFLICT clause
                    # Create a dictionary with the collected values

                    if(menu_id ==1):
                            insert_employee_query = """
                                INSERT INTO Appetizer_item (
                                    Id,
                                    name,
                                    price,
                                    description,
                                    recipie,
                                    menu_id
                                ) 
                                VALUES (?, ?, ?, ?, ?, ?)
                            """          
                    if(menu_id ==2):
                          insert_employee_query ="""
                              INSERT INTO Entree_item (
                                  Id,
                                  name,
                                  price,
                                  description,
                                  recipie,
                                  menu_id
                              ) 
                              VALUES (?, ?, ?, ?, ?, ?)
                          """   
                    if(menu_id ==3):
                          insert_employee_query = """
                              INSERT INTO Desert_item (
                                  Id,
                                  name,
                                  price,
                                  description,
                                  recipie,
                                  menu_id
                              ) 
                              VALUES (?, ?, ?, ?, ?, ?)
                          """
                          
                    employee_values = (
                         int(id),
                         name,
                        float(price),
                         description,
                         recipe,
                         menu_id,
                   )
                    

                    try:
                        s = conn.cursor()
                        s.execute(insert_employee_query, employee_values)
                        s.commit()
                        st.success("food information inserted successfully")
                    except sqlite3.Error as err:
                        st.error(f"Error: {err}")



        

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

                    # Extracting values from dictionary
                    employee_data = (
                        employee_values["SSN"],
                        employee_values["First_Name"],
                        employee_values["Last_Name"],
                        employee_values["Home_Address"],
                        employee_values["Date_Of_Birth"],
                        employee_values["Salary"]
                    )                    
                    manager_values = {
                         "Id": int(manager_id),
                         "Employee_id": int(ssn)
                        }
                    # Extracting values from dictionary
                    manager_data = (
                        manager_values["Id"],
                        manager_values["Employee_id"]
                    )          
                    sql_insert = """
                        INSERT INTO Employee (SSN, First_Name, Last_Name, Home_Address, Date_Of_Birth, Salary)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """
                    insert_manager_query = """
                        INSERT INTO Manager (Id, Employee_id)
                        VALUES (?, ?)
                    """

                    try:
                        cursor = conn.cursor()

                        cursor.execute(sql_insert, employee_data)
                        cursor.execute(insert_manager_query, manager_data)
                        cursor.commit()
                        cursor.close()
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
                    
                    Cashier_values = (
                          int(Cashier_id),
                         int(ssn),
                          int(counter_id)
                        )
                    
                    sql_insert = """
                        INSERT INTO Employee (SSN, First_Name, Last_Name, Home_Address, Date_Of_Birth, Salary)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """
                    
                    insert_Cashier_query = """
                        INSERT INTO Cashier (Id, Employee_id,Counter_id)
                        VALUES (?, ? , ?)
                    """
                    # Extracting values from dictionary
                    employee_data = (
                        employee_values["SSN"],
                        employee_values["First_Name"],
                        employee_values["Last_Name"],
                        employee_values["Home_Address"],
                        employee_values["Date_Of_Birth"],
                        employee_values["Salary"]
                    )                    

                    try:
                        cursor = conn.cursor()

                        cursor.execute(sql_insert, employee_data)
                        cursor.execute(insert_Cashier_query, Cashier_values)
                        cursor.commit()
                        cursor.close()
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
                    
                    Chef_values = (
                         int(Chef_id),
                         int(ssn)
                        )
                    
                    sql_insert = """
                        INSERT INTO Employee (SSN, First_Name, Last_Name, Home_Address, Date_Of_Birth, Salary)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """
                                        # Extracting values from dictionary
                    employee_data = (
                        employee_values["SSN"],
                        employee_values["First_Name"],
                        employee_values["Last_Name"],
                        employee_values["Home_Address"],
                        employee_values["Date_Of_Birth"],
                        employee_values["Salary"]
                    )                    
                    
                    insert_Chef_query = """
                        INSERT INTO Chef (Id, Employee_id)
                        VALUES (?, ?)
                    """

                    try:
                        cursor = conn.cursor()

                        cursor.execute(sql_insert, employee_data)
                        cursor.execute(insert_Chef_query, Chef_values)
                        cursor.commit()
                        cursor.close()
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
                    
                    Waiter_values = (
                         int(Waiter_id),
                          int(ssn)
                        )
                    
                    sql_insert = """
                        INSERT INTO Employee (SSN, First_Name, Last_Name, Home_Address, Date_Of_Birth, Salary)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """
                                        # Extracting values from dictionary
                    employee_data = (
                        employee_values["SSN"],
                        employee_values["First_Name"],
                        employee_values["Last_Name"],
                        employee_values["Home_Address"],
                        employee_values["Date_Of_Birth"],
                        employee_values["Salary"]
                    )                    
                    
                    insert_Waiter_query = """
                        INSERT INTO Waiter (Id, Employee_id)
                        VALUES (?,?)
                    """

                    try:
                        cursor = conn.cursor()

                        cursor.execute(sql_insert, employee_data)
                        cursor.execute(insert_Waiter_query, Waiter_values)
                        cursor.commit()
                        cursor.close()
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
    
            select_available_tables_query = """
                SELECT Id
                FROM Table_dine
                WHERE Is_available = 1
                    """
    
            with conn.cursor() as s:
                result = s.execute(select_available_tables_query)
                # Fetch all results and convert to a tuple of IDs
                table_ids = tuple(row[0] for row in result)        
                
            table_ids_id_label = "select table id:"
        
            counter_table_id_options = table_ids
            table_id = col2.selectbox(table_ids_id_label , counter_table_id_options)
    
    
            col4, col5 , col15 = st.columns(3)
            date  = col4.text_input(date_label)
            price  = col4.text_input("price:")

            select_available_Waiters_query ="""
                    SELECT Id
                    FROM Waiter
                    
                """
                
            with conn.cursor() as s:
                result = s.execute(select_available_Waiters_query)
                # Fetch all results and convert to a tuple of IDs
                waiter_ids = tuple(row[0] for row in result)       
    
            select_available_chef_query = """
                    SELECT Id
                    FROM Chef
                """
                
            with conn.cursor() as s:
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
            select_available_customer_query ="""
                    SELECT Customer_id
                    FROM Customer
                """
                
            with conn.cursor() as s:
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
                        statues_bool = 0
                        # Define the insert statement with ON CONFLICT clause
                        # Create a dictionary with the collected values
                        if(is_paid == "no"):
                            statues_bool = 0
                        else:
                            statues_bool = 1
                            
                        statues_bool_discount = 0
                        # Define the insert statement with ON CONFLICT clause
                        # Create a dictionary with the collected values
                        if(discount == "no"):
                            statues_bool_discount = 0
                        else:
                            statues_bool_discount = 1

                        # Define the insert statement with ON CONFLICT clause
                        # Create a dictionary with the collected values
                        Order_food_values = (
                             int(order_id),
                             "state of art",
                             statues_bool,
                             float(price),
                             date,
                             int(table_id),
                      )
                        

                                                
                        insert_Order_food_query = """
                            INSERT INTO Order_food (
                                Order_id,
                                Table_condition,
                                is_paid,
                                price,
                                order_date,
                                table_id_ref
                            ) 
                            VALUES (?, ?, ?, ?, ?, ?)
                        """    
                        
                        Makes_order_values = (
                             int(customer_id),
                             int(order_id),
                             int(transaction_id),
                       )

                        insert_Makes_order_query ="""
                            INSERT INTO Makes_order (
                                Customer_id_ref,
                                Order_id_ref,
                                Transaction_id_ref
                                ) 
                            VALUES (?, ?, ?)
                        """   
                        
                        Receives_order_values = (
                             int(chef_id),
                             int(order_id),
                             int(waiter_id),
                        )     
                        
                        insert_Receives_order_query = """
                            INSERT INTO Receive_order (
                                Chef_id_ref,
                                Order_id_ref,
                                Waiter_id_ref
                                ) 
                            VALUES (?, ?, ?)
                        """
                            
                        transaction_values = (
                             int(transaction_id),
                             statues_bool_discount,
                             int(Type),
                             int(counter_id),
                        
                        ) 
                        insert_transaction_query ="""
                            INSERT INTO Transaction_ (
                                Id,
                                Is_discounter,
                                transaction_tyep,
                                Counter_id_ref
                                ) 
                            VALUES (?, ?, ?, ?)
                        """           
                        
                        update_availability_query = """
                            UPDATE Table_dine
                            SET Is_available = 0
                            WHERE Id = ?
                        """    
                        
                        update_table_values = (
                            int(table_id),
                         ) 
                        try:
                            s = conn.cursor()

                            s.execute(insert_Order_food_query, Order_food_values)
                            s.execute(insert_transaction_query, transaction_values)

                            s.execute(insert_Makes_order_query, Makes_order_values)
                            s.execute(insert_Receives_order_query, Receives_order_values)
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
                        Customer_values = (
                             int(customer_id),
                             first_name,
                             last_name
                        )
                        


                                                
                        insert_Customer_query = """
                            INSERT INTO Customer (
                                Customer_id,
                                First_name,
                                last_name
                            ) 
                            VALUES (?, ?, ?)
                        """          

  
                        try:
                            s = conn.cursor()
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
                     counter_values = (
                        int(counter_id),
                     )
                    
                     insert_counter_query = """
                        INSERT INTO Counter (
                            Id
                        ) 
                        VALUES (?)
                    """
                      
                     
                     try:
                         s = conn.cursor()
                         s.execute(insert_counter_query, counter_values)
                         s.commit()
                         st.success("Counter information inserted successfully")
                     except sqlite3.Error as err:
                         st.error(f"Error: {err}")

elif selected_option == 'create menu':
    st.empty()
    with st.container():
         with st.form(key='Counter_form'):

             col1, col2, col3 , col4 = st.columns(4)
             menu_id = col1.text_input("menu id: ")
             title = col2.text_input("title:")
             counter_id_label = "is_availaible:"

             is_availaible_options =  tuple(["no" , "yes"])
             is_availaible = col3.selectbox(counter_id_label , is_availaible_options)
             summery = col4.text_input("summery")
    ### query -> if counter id does not exist -> insert
                # Use the submit button inside the form context
             submit_button = st.form_submit_button(label='Submit')
             if submit_button:
                 # Validate the inputs (basic validation)
                 if not menu_id:
                     st.error("Please fill out all the fields.")
                 else:
                     ava = 0
                     if(is_availaible == "no"):
                         ava = 0
                     else:
                         ava = 1  
                     # Define the insert statement with ON CONFLICT clause
                     # Create a dictionary with the collected values
                     counter_values = (
                        int(menu_id),
                        title,
                        summery,
                        ava,
                        
                        
                     )
                    
                     insert_menu_query = '''
                        INSERT INTO Menu (Id, title, summery, is_availaible)
                        VALUES (?, ?, ?, ?)
                    '''
                      
                     
                     try:
                         s = conn.cursor()
                         s.execute(insert_menu_query, counter_values)
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
                    statues_bool = 0
                    # Define the insert statement with ON CONFLICT clause
                    # Create a dictionary with the collected values
                    if(is_booked == "no"):
                        statues_bool = 0
                    else:
                        statues_bool = 1

                    employee_values = (
                         int(table_id),
                         int(capacity),
                         statues_bool,
                         int(waiter_id)
                       )
                    
                    insert_employee_query = """
                        INSERT INTO Table_dine (
                            Id,
                            capacity,
                            Is_available,
                            Waiter_id_ref
                        ) 
                        VALUES (?, ?, ?, ?)
                    """         
                    
                    try:
                        s = conn.cursor()
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
            select_available_customer_query ="""
                    SELECT Customer_id
                    FROM Customer
                """
                
            with conn.cursor() as s:
                result = s.execute(select_available_customer_query)
                # Fetch all results and convert to a tuple of IDs
                customer_ids = tuple(row[0] for row in result)        
            
            customer_ids_id_label = "select customer id:"
        
            customer_id_options = customer_ids
            customer_id = col1.selectbox(customer_ids_id_label , customer_id_options)
            
            select_available_tables_query = """
                SELECT Id
                FROM Table_dine
                WHERE Is_available = 1
                    """
    
            with conn.cursor() as s:
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

                    Booking_values = (
                         int(customer_id),
                        int(table_id),
                         date,
                        )
                    
                    insert_Booking_query = """
                        INSERT INTO Booking (
                            Customer_id_ref,
                            Table_dine_id_ref,
                            book_date
                        ) 
                        VALUES (?, ?, ?)
                    """          
                    
                    try:
                        s = conn.cursor()
                        s.execute(insert_Booking_query, Booking_values)
                        s.commit()
                        st.success("booking information inserted successfully")
                    except sqlite3.Error as err:
                        st.error(f"Error: {err}")
         


# elif     un 3 ta
# retrieve order tuye Order anjam mishe.
