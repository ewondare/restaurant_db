import streamlit as st
import pypyodbc as odbc 
import sqlite3

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

    
options = ("Menu item", "Update Employee", "Update Details of an order", "Customer and Transaction", "Table" , "Booking")
selected_option = st.selectbox("What update you going to make?", options)


if selected_option == 'Menu item':
    st.empty()
    with st.container():
        with st.form(key='menu_form'):
            menu_item_options = ("Appetizer", "Entree", "Dessert")  
            menu_item_selection = st.selectbox("Choose a menu item option:", menu_item_options)
        
            if menu_item_selection == 'Appetizer':
                update_options = ("name" , "price" , "description" , "recipe")
                menu_item_update = st.multiselect("which item do you want to update" , update_options)
                id = st.text_input("Appetizer id:" , key = 1)
                t = []
                for i in menu_item_update:
                     if(i == "name"):
                        name_label = "name: "
                        name = st.text_input(name_label)
                        t.append(1)
                        #if id exists -> update (cascade)
                     if(i == "price"):
                        price_label = "price: "
                        price = int(st.text_input(price_label))
                        t.append(2)
                        #if id exists -> update (cascade)
                     if(i == "description"):
                        description_label = "description: "
                        description = st.text_area(description_label)
                        t.append(3)
                        #if id exists -> update (cascade)
                     if(i == "recipe"):
                        recipe_label = "recipe: "
                        recipe = st.text_area(recipe_label)
                        t.append(4)
                        #if id exists -> update (cascade)
                menu_id = 1

            if menu_item_selection == 'Entree':
               update_options = ("name" , "price" , "description" , "recipe")
               menu_item_update = st.multiselect("which item do you want to update" , update_options)
               id = st.text_input("Entree id:" , key = 1)
               t = []
               for i in menu_item_update:
                   if(i == "name"):
                        name_label = "name: "
                        name = st.text_input(name_label)
                        t.append(1)
                        #if id exists -> update (cascade)
                   if(i == "price"):
                        price_label = "price: "
                        price = int(st.text_input(price_label))
                        t.append(2)
                        #if id exists -> update (cascade)
                   if(i == "description"):
                        description_label = "description: "
                        description = st.text_area(description_label)
                        t.append(3)
                       #if id exists -> update (cascade)
                   if(i == "recipe"):
                        recipe_label = "recipe: "
                        recipe = st.text_area(recipe_label)
                        t.append(4)
                        #if id exists -> update (cascade)
               menu_id = 2
            
            if menu_item_selection == 'Dessert':
                update_options = ("name" , "price" , "description" , "recipe")
                menu_item_update = st.multiselect("which item do you want to update" , update_options)
                id = st.text_input("Dessert id:" , key = 1)
                t = []
                for i in menu_item_update:
                    if(i == "name"):
                         name_label = "name: "
                         name = st.text_input(name_label)
                         t.append(1)
                         #if id exists -> update (cascade)
                    if(i == "price"):
                        price_label = "price: "
                        price = int(st.text_input(price_label))
                        t.append(2)
                        #if id exists -> update (cascade)
                    if(i == "description"):
                         description_label = "description: "
                         description = st.text_area(description_label)
                         t.append(3)
                         #if id exists -> update (cascade)
                    if(i == "recipe"):
                        recipe_label = "recipe: "
                        recipe = st.text_area(recipe_label)
                        t.append(4)
                         #if id exists -> update (cascade)
                menu_id = 3
                    
            submit_button = st.form_submit_button(label='Submit')

            if submit_button:
                if(not id):
                    st.error("Please fill out all the fields.")
                # Validate the inputs (basic validation)
                else:
                    try:
                        if(menu_id == 1):
                            for i in t:
                                if(i == 1):
                                  if(name):
                                    s = conn.cursor()
                                    s.execute("Update Appetizer_items SET name = '{}' WHERE Id = '{}'".format(name,id))
                                    s.commit()
                                    st.success("name information updated successfully")

                                if(i == 2):
                                    if(price):
                                        s = conn.cursor()
                                        s.execute("Update Appetizer_items SET price = '{}' WHERE Id = '{}'".format(price,id))
                                        s.commit()
                                        st.success("price information updated successfully")
                                if(i == 3):
                                    if(description):
                                        s = conn.cursor()
                                        s.execute("Update Appetizer_items SET description = '{}' WHERE Id = '{}'".format(description,id))
                                        s.commit()
                                        st.success("description information updated successfully")
                                if(i == 4):
                                    if(recipe):
                                        s = conn.cursor()
                                        s.execute("Update Appetizer_items SET recipe = '{}' WHERE Id = '{}'".format(recipe,id))
                                        s.commit()
                                        st.success("recipe information updated successfully")
                        if(menu_id ==2):
                            for i in t:
                                if(i == 1):
                                  if(name):
                                    s = conn.cursor()
                                    s.execute("Update Entree_items SET name = '{}' WHERE Id = '{}'".format(name,id))
                                    s.commit()
                                    st.success("name information updated successfully")

                                if(i == 2):
                                    if(price):
                                        s = conn.cursor()
                                        s.execute("Update Entree_items SET price = '{}' WHERE Id = '{}'".format(price,id))
                                        s.commit()
                                        st.success("price information updated successfully")
                                if(i == 3):
                                    if(description):
                                        s = conn.cursor()
                                        s.execute("Update Entree_items SET description = '{}' WHERE Id = '{}'".format(description,id))
                                        s.commit()
                                        st.success("description information updated successfully")
                                if(i == 4):
                                    if(recipe):
                                        s = conn.cursor()
                                        s.execute("Update Entree_items SET recipe = '{}' WHERE Id = '{}'".format(recipe,id))
                                        s.commit()
                                        st.success("recipe information updated successfully")
                        if(menu_id ==3):
                            for i in t:
                                if(i == 1):
                                   if(name):
                                    s = conn.cursor()
                                    s.execute("Update Dessert_items SET name = '{}' WHERE Id = '{}'".format(name,id))
                                    s.commit()
                                    st.success("name information updated successfully")

                                if(i == 2):
                                    if(price):
                                        s = conn.cursor()
                                        s.execute("Update Dessert_items SET price = '{}' WHERE Id = '{}'".format(price,id))
                                        s.commit()
                                        st.success("price information updated successfully")
                                if(i == 3):
                                    if(description):
                                        s = conn.cursor()
                                        s.execute("Update Dessert_items SET description = '{}' WHERE Id = '{}'".format(description,id))
                                        s.commit()
                                        st.success("description information updated successfully")
                                if(i == 4):
                                    if(recipe):
                                        s = conn.cursor()
                                        s.execute("Update Dessert_items SET recipe = '{}' WHERE Id = '{}'".format(recipe,id))
                                        s.commit()
                                        st.success("recipe information updated successfully")
                    except sqlite3.Error as err:
                        st.error(f"Error: {err}")

if selected_option == 'Update Employee':
    st.empty()
    with st.container():
            employee_item_options = ("Manager", "Cashier", "Chef" , "Waiter", "Employee")  
            employee_item_selection = st.selectbox("Choose an item option:", employee_item_options)
            if employee_item_selection == 'Employee':
                with st.form(key='employee_form'):
                    update_options = ("home address" , "date of birth" , "first name" , "last name" , "salary" , "ssn")
                    employee_item_update = st.multiselect("which item do you want to update" , update_options)
                    id = st.text_input("Employee ssn: ")
                    t = []
                    for i in employee_item_update:
                        if(i == "home address"):
                            home_address_label = "home address: "
                            home_address = st.text_input(home_address_label)
                            t.append(1)
                            #if id exists -> update (cascade)
                        if(i == "date of birth"):
                            birthday_label = "date of birth: "
                            date_of_birth = st.date_input(birthday_label,value=None)
                            t.append(2)
                            #if id exists -> update (cascade)
                        if(i == "first name"):
                            name_label = "first name: "
                            first_name = st.text_input(name_label)
                            t.append(3)
                            #if id exists -> update (cascade)
                        if(i == "last name"):
                            name_label = "last name: "
                            last_name = st.text_input(name_label)
                            t.append(4)
                            #if id exists -> update (cascade)
                        if(i == "salary"):
                            salary_label = "salary: "
                            salary = st.number_input(salary_label)
                            t.append(5)
                            #if id exists -> update (cascade)
                            
                    submit_button = st.form_submit_button(label='Submit')
                    if submit_button:
                        if(not id):
                            st.error("Please fill out all the fields.") 
                        else:
                            try:
                                for i in t:
                                    if(i == 1):
                                        if(home_address):
                                            s = conn.cursor()
                                            s.execute("Update Employee SET home_address = '{}' WHERE ssn = '{}'".format(home_address,id))
                                            s.commit()
                                            st.success("home address information updated successfully")
                                    if(i == 2):
                                        if(date_of_birth):
                                            s = conn.cursor()
                                            s.execute("Update Employee SET date_of_birth = '{}' WHERE ssn = '{}'".format(date_of_birth,id))
                                            s.commit()
                                            st.success("date of birth information updated successfully")
                                    if(i == 3):
                                        if(first_name):
                                            s = conn.cursor()
                                            s.execute("Update Employee SET first_name = '{}' WHERE ssn = '{}'".format(first_name,id))
                                            s.commit()
                                            st.success("first name information updated successfully")
                                    if(i == 4):
                                        if(last_name):
                                            s = conn.cursor()
                                            s.execute("Update Employee SET last_name = '{}' WHERE ssn = '{}'".format(last_name,id))
                                            s.commit()
                                            st.success("last name information updated successfully")
                                    if(i == 5):
                                        if(salary):
                                            s = conn.cursor()
                                            s.execute("Update Employee SET salary = '{}' WHERE ssn = '{}'".format(salary,id))
                                            s.commit()
                                            st.success("salary information updated successfully")
                            except sqlite3.Error as err:
                                st.error(f"Error: {err}")
                            
            if employee_item_selection == 'Manager':
                with st.form(key='manger_form'):
                    update_options = ("employee ssn",)
                    employee_item_update = st.selectbox("which item do you want to update" , update_options)
                    id = st.text_input("Manager id: ")
                    if (employee_item_update == "employee ssn"):
                        ssn_label = "ssn: "
                        employee_id = st.text_input(ssn_label)
                        #if id exists -> update (cascade)
                    submit_button = st.form_submit_button(label='Submit')
                    if submit_button:
                        try:
                            if(not id):
                                st.error("Please fill out all the fields.") 
                            else:
                                if(employee_id):
                                    s = conn.cursor()
                                    s.execute("Update Manager SET employee_id = '{}' WHERE id = '{}'".format(employee_id,id))
                                    s.commit()
                                    st.success("employee id information updated successfully")
                        except sqlite3.Error as err:
                                st.error(f"Error: {err}")
                            
            elif employee_item_selection == 'Cashier':
                with st.form(key='cashier_form'):
                    update_options = ("employee ssn" , "counter id")
                    employee_item_update = st.multiselect("which item do you want to update" , update_options)
                    id = st.text_input("Cashier id: ")
                    t = []
                    for i in employee_item_update:
                        if(i == "employee ssn"):
                            ssn_label = "ssn: "
                            employee_id = st.text_input(ssn_label)
                            t.append(1)
                            #if id exists -> update (cascade)
                        if(i == "counter id"):
                            counter_id_label = "counter id: "
                            counter_id = st.text_input(counter_id_label)
                            t.append(2)
                            #if id exists -> update (cascade)
                    submit_button = st.form_submit_button(label='Submit')
                    if submit_button:
                        try:
                            if(not id):
                                st.error("Please fill out all the fields.") 
                            else:
                                for i in t:
                                    if(i == 1):
                                        if(employee_id):
                                            s = conn.cursor()
                                            s.execute("Update Cashier SET employee_id = '{}' WHERE id = '{}'".format(employee_id,id))
                                            s.commit()
                                            st.success("employee id  information updated successfully")
                                    if(i == 2):
                                        if(counter_id):
                                            s = conn.cursor()
                                            s.execute("Update Cashier SET counter_id = '{}' WHERE id = '{}'".format(counter_id,id))
                                            s.commit()
                                            st.success("counter id information updated successfully")
                        except sqlite3.Error as err:
                                st.error(f"Error: {err}")
                            
            elif employee_item_selection == 'Chef':
                with st.form(key='chef_form'):
                    update_options = ("employee ssn",)
                    employee_item_update = st.selectbox("which item do you want to update" , update_options)
                    id = st.text_input("Chef id: ")
                    if(employee_item_update == "employee ssn"):
                        ssn_label = "ssn: "
                        employee_id = st.text_input(ssn_label)
                        #if id exists -> update (cascade)
                    submit_button = st.form_submit_button(label='Submit')
                    if submit_button:
                        try:
                            if(not id):
                                st.error("Please fill out all the fields.") 
                            else:
                                if(employee_id):
                                    s = conn.cursor()
                                    s.execute("Update Chef SET employee_id = '{}' WHERE id = '{}'".format(employee_id,id))
                                    s.commit()
                                    st.success("employee id information updated successfully")
                        except sqlite3.Error as err:
                                st.error(f"Error: {err}")  
                              
            elif employee_item_selection == 'Waiter':
                with st.form(key='waiter_form'):
                    update_options = ("employee ssn",)
                    employee_item_update = st.selectbox("which item do you want to update" , update_options)
                    id = st.text_input("Waiter id: ")
                    if(employee_item_update == "employee ssn"):
                        ssn_label = "ssn: "
                        employee_id = st.text_input(ssn_label)
                        #if id exists -> update (cascade)
                    submit_button = st.form_submit_button(label='Submit')
                    if submit_button:
                        try:
                            if(not id):
                                st.error("Please fill out all the fields.") 
                            else:
                                if(employee_id):
                                    s = conn.cursor()
                                    s.execute("Update Waiter SET employee_id = '{}' WHERE id = '{}'".format(employee_id,id))
                                    s.commit()
                                    st.success("employee id information updated successfully")
                        except sqlite3.Error as err:
                                st.error(f"Error: {err}")  

        
if selected_option == 'Update Details of an order':
    st.empty()
    with st.container():
        with st.form(key='order_form'):
                update_options = ("is paid" , "date" , "counter id" , "table id" , "chef id" , "waiter id","order status","order appetizer","order entree","order dessert")
                order_item_update = st.multiselect("which item do you want to update" , update_options)
                id = st.text_input("Order id: " , key = 1)
                t = []
                for i in order_item_update:
                    if(i == "is paid"):
                            is_paid_label = "is paid: "
                            is_paid = st.text_input(is_paid_label)
                            t.append(1)
                            #if id exists -> update (cascade)
                    if(i == "date"):
                            day_label = "date: "
                            date = st.date_input(day_label , value = None)
                            t.append(2)
                            #if id exists -> update (cascade)
                    if(i == "counter id"):
                            counter_id_label = "counter id: "
                            counter_id = st.text_input(counter_id_label)
                            t.append(3)
                            #if id exists -> update (cascade)
                    if(i == "table id"):
                            table_id_label = "table id: "
                            table_id = st.text_input(table_id_label)
                            t.append(4)
                            #if id exists -> update (cascade)
                            
                    if(i == "chef id"):
                            chef_id = st.text_input("chef id: ") 
                            t.append(5)
                            #if id exists -> update (cascade)
                    if(i == "waiter id"):
                            waiter_id = st.text_input("waiter id: ")  
                            t.append(6)
                            #if id exists -> update (cascade)  
                    if(i == "order status"):
                            counter_status_lable = "order status: "
                            order_status = st.text_input(counter_status_lable)
                            t.append(7)
                    if(i == "order appetizer"):
                            order_appetizer_id = st.text_input("Order Appeitizer id: ")
                            counter_appetizer_lable = "Appetizer id: "
                            order_appetizer = st.text_input(counter_appetizer_lable)
                            t.append(8)
                    if(i == "order entree"):
                            order_entree_id = st.text_input("Order Entree id: ")
                            counter_entree_lable = "Entree id: "
                            order_entree = st.text_input(counter_entree_lable)
                            t.append(9)
                    if(i == "order dessert"):
                            order_appetizer_id = st.text_input("Order Desert id: ")
                            counter_desert_lable = "Desert id: "
                            order_desert = st.text_input(counter_desert_lable)
                            t.append(10)
                            
                submit_button = st.form_submit_button(label='Submit')
                if submit_button:
                    try:
                        if(not id):
                            st.error("Please fill out all the fields.") 
                        else:
                            for i in t:
                                if(i == 1):
                                    if(is_paid):
                                        s = conn.cursor()
                                        s.execute("Update [Order] SET is_paid = '{}' WHERE id = '{}'".format(is_paid,id))
                                        s.commit()
                                        st.success("is paid information updated successfully")
                                if(i == 2):
                                    if(date):
                                        s = conn.cursor()
                                        s.execute("Update [Order] SET date = '{}' WHERE id = '{}'".format(date,id))
                                        s.commit()
                                        st.success("date information updated successfully")
                                if(i == 3):
                                    if(counter_id):
                                        s = conn.cursor()
                                        s.execute("Update [Order] SET counter_id = '{}' WHERE id = '{}'".format(counter_id,id))
                                        s.commit()
                                        st.success("counter id information updated successfully")
                                if(i == 4):
                                    if(table_id):
                                        s = conn.cursor()
                                        s.execute("Update [Order] SET table_id = '{}' WHERE id = '{}'".format(table_id,id))
                                        s.commit()
                                        st.success("table id information updated successfully")
                                if(i == 5):
                                    if(chef_id):
                                        s = conn.cursor()
                                        s.execute("Update Receive_order SET chef_id = '{}' WHERE order_id = '{}'".format(chef_id,id))
                                        s.commit()
                                        st.success("chef id information updated successfully")
                                if(i == 6):
                                    if(waiter_id):
                                        s = conn.cursor()
                                        s.execute("Update Receive_order SET waiter_id = '{}' WHERE order_id = '{}'".format(waiter_id,id))
                                        s.commit()
                                        st.success("waiter id information updated successfully")
                                if(i == 7):
                                       if(order_status):
                                            s = conn.cursor()
                                            s.execute("Update [Order] SET order_status = '{}' WHERE id = '{}'".format(order_status,id))
                                            s.commit()
                                            st.success("order status information updated successfully")
                                if(i == 8):
                                    if(order_appetizer):
                                            s = conn.cursor()
                                            s.execute("Update order_appetizer SET appetizer_id = '{}'  WHERE id = '{}'".format(order_appetizer,order_appetizer_id))
                                            s.commit()
                                            st.success("order appetizer information updated successfully")
                                if(i == 9):
                                    if(order_entree):
                                            s = conn.cursor()
                                            s.execute("Update Order_entree SET entree_id = '{}'  WHERE id = '{}'".format(order_entree,order_entree_id))
                                            s.commit()
                                            st.success("order entree information updated successfully")
                                if(i == 10):
                                    if(order_desert):
                                            s = conn.cursor()
                                            s.execute("Update Order_desert SET dessert_id = '{}'  WHERE id = '{}'".format(order_desert,order_desert_id))
                                            s.commit()
                                            st.success("order dessert information updated successfully")
                                        
                    except sqlite3.Error as err:
                        st.error(f"Error: {err}")    


if selected_option == 'Customer and Transaction':
    st.empty()
    with st.container():
            update_options = ("customer" ,  "transaction")
            customer_item_update = st.selectbox("which item do you want to update" , update_options)
            if(customer_item_update == "customer"):
                    with st.form(key='customer_form'):
                        update = ("first name" , "last name")
                        item_update = st.multiselect("which item do you want to update",update)
                        id = st.text_input("Customer id: ")
                        t = []
                        for i in item_update:
                                if(i == "first name"):
                                        first_name_label = "first name: "
                                        first_name = st.text_input(first_name_label)
                                        t.append(1)
                                        #if id exists -> update (cascade)
                                if(i == "last name"):
                                        last_name_label = "last name: "
                                        last_name = st.text_input(last_name_label)
                                        t.append(2)
                                        #if id exists -> update (cascade)
                        submit_button = st.form_submit_button(label='Submit')
                        if submit_button:
                            if(not id):
                                st.error("Please fill out all the fields.") 
                            else:
                                try:
                                    for i in t:
                                        if(i == 1):
                                            if(first_name):
                                                s = conn.cursor()
                                                s.execute("Update Customer SET first_name = '{}' WHERE customer_id = '{}'".format(first_name,id))
                                                s.commit()
                                                st.success("first name information updated successfully")
                                        if(i == 2):
                                            if(last_name):
                                                s = conn.cursor()
                                                s.execute("Update Customer SET last_name = '{}' WHERE customer_id = '{}'".format(last_name,id))
                                                s.commit()
                                                st.success("last name information updated successfully")
                                except sqlite3.Error as err:
                                     st.error(f"Error: {err}")
            if(customer_item_update == "transaction"):
                with st.form(key='transaction_form'):
                        update = ("transaction type" , "discount" , "counter id")
                        item_update = st.multiselect("which item do you want to update",update)
                        id = st.text_input("Transaction id: ")
                        t = []
                        for i in item_update:
                            if(i == "transaction type"):
                                    transaction_type_label = "transaction type: "
                                    transaction_type = st.text_input(transaction_type_label)
                                    t.append(1)
                                    #if id exists -> update (cascade)
                            if(i == "discount"):
                                    discount_label = "discount: "
                                    discount = st.text_input(discount_label)
                                    t.append(2)
                                    #if id exists -> update (cascade)
                            if(i == "counter id"):
                                    counter_id = st.text_input("Counter id: ")
                                    t.append(3)
                        submit_button = st.form_submit_button(label='Submit')
                        if submit_button:
                            if(not id):
                                st.error("Please fill out all the fields.") 
                            else:
                                try:
                                    for i in t:
                                        if(i == 1):
                                            if(transaction_type):
                                                s = conn.cursor()
                                                s.execute("Update [Transaction] SET type = '{}' WHERE id = '{}'".format(transaction_type,id))
                                                s.commit()
                                                st.success("transaction type information updated successfully")
                                        if(i == 2):
                                            if(discount):
                                                s = conn.cursor()
                                                s.execute("Update [Transaction] SET discount = '{}' WHERE id = '{}'".format(discount,id))
                                                s.commit()
                                                st.success("discount information updated successfully")
                                        if(i == 3):
                                           if(counter_id):
                                                s = conn.cursor()
                                                s.execute("Update [Transaction] SET counter_id = '{}' WHERE id = '{}'".format(counter_id,id))
                                                s.commit()
                                                st.success("counter id information updated successfully")
                                except sqlite3.Error as err:
                                     st.error(f"Error: {err}")
                    

if selected_option == 'Table':
    st.empty()
    with st.container():
        with st.form(key='customer_form'):
            update_options = ("capacity" , "is booked" , "waiter id")
            table_item_update = st.multiselect("which item do you want to update" , update_options)
            id = st.text_input("Table id: ")
            t = []
            for i in table_item_update:
                if(i == "capacity"):
                        capacity_label = "capacity: "
                        capacity = st.text_input(capacity_label)
                        t.append(1)
                        #if id exists -> update (cascade)
                if(i == "is booked"):
                        is_booked_label = "is booked: "
                        is_booked = st.text_input(is_booked_label)
                        t.append(2)
                        #if id exists -> update (cascade)
                if(i == "waiter id"):
                        waiter_id_label = "waiter id: "
                        waiter_id = st.text_input(waiter_id_label)
                        t.append(3)
                        #if id exists -> update (cascade)
            submit_button = st.form_submit_button(label='Submit')
            if submit_button:
                if(not id):
                    st.error("Please fill out all the fields.") 
                else:
                    try:
                       for i in t:
                           if(i == 1):
                                if(capacity):
                                        s = conn.cursor()
                                        s.execute("Update [Table] SET capacity = '{}' WHERE id = '{}'".format(capacity,id))
                                        s.commit()
                                        st.success("counter id information updated successfully")    
                           if(i == 2):
                                if(is_booked):
                                        s = conn.cursor()
                                        s.execute("Update [Table] SET is_booked = '{}' WHERE id = '{}'".format(is_booked,id))
                                        s.commit()
                                        st.success("counter id information updated successfully")
                           if(i == 3):
                                if(waiter_id):
                                        s = conn.cursor()
                                        s.execute("Update [Table] SET waiter_id = '{}' WHERE id = '{}'".format(waiter_id,id))
                                        s.commit()
                                        st.success("counter id information updated successfully")
                    except sqlite3.Error as err:
                        st.error(f"Error: {err}") 

if selected_option == 'Booking':
    st.empty()
    with st.container():
        with st.form(key='customer_form'):
            update_options = ("customer id" , "table id" , "date")
            booking_item_update = st.multiselect("which item do you want to update" , update_options)
            customer_id = st.text_input("Customer id: ")
            table_id = st.text_input("Table id: ")
            t = []
            for i in booking_item_update:
                if(i == "customer id"):
                        customer_id_label = "changed customer id: "
                        customer = st.text_input(customer_id_label)
                        t.append(1)
                        #if id exists -> update (cascade)
                        
                if(i == "table id"):
                        table_id_label = "changed table id: "
                        table = st.text_input(table_id_label)
                        t.append(2)
                        #if id exists -> update (cascade) 
                            
                if(i == "date"):
                        date_label = "date: "
                        date = st.date_input(date_label,value=None)
                        t.append(3)
                        #if id exists -> update (cascade)
            submit_button = st.form_submit_button(label='Submit')
            if submit_button:
                if(not id):
                    st.error("Please fill out all the fields.") 
                else:
                    try:
                       for i in t:
                           if(i == 1):
                                if(customer):
                                        s = conn.cursor()
                                        s.execute("Update Booking SET customer_id = '{}' WHERE customer_id = '{}' and table_id = '{}'".format(customer,customer_id,table_id))
                                        s.commit()
                                        st.success("customer id information updated successfully")    
                           if(i == 2):
                                if(table):
                                        s = conn.cursor()
                                        s.execute("Update Booking SET table_id = '{}' WHERE customer_id = '{}' and table_id = '{}'".format(table,customer_id,table_id))
                                        s.commit()
                                        st.success("table id information updated successfully")
                           if(i == 3):
                                if(date):
                                        s = conn.cursor()
                                        s.execute("Update Booking SET date = '{}' WHERE customer_id = '{}' and table_id = '{}'".format(date,customer_id,table_id))
                                        s.commit()
                                        st.success("date information updated successfully")
                    except sqlite3.Error as err:
                        st.error(f"Error: {err}")
