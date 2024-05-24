import streamlit as st
import pypyodbc as odbc 

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

if selected_option == 'Update Employee':
    st.empty()
    with st.container():
        
        employee_item_options = ("Manager", "Cashier", "Chef" , "Waiter")  
        employee_item_selection = st.selectbox("Choose an item option:", employee_item_options)
        
        if employee_item_selection == 'Manager':
            update_options = ("home address" , "date of birth" , "first name" , "last name" , "salary" , "ssn")
            employee_item_update = st.selectbox("which item do you want to update" , update_options)
            if(employee_item_update == "home address"):
                home_address_label = "home address: "
                id = st.text_input("Manager id: ")
                home_address = st.text_input(home_address_label)
                #if id exists -> update (cascade)
                
            if(employee_item_update == "date of birth"):
                birthday_label = "date of birth: "
                id = st.text_input("Manager id: ")
                date_of_birth = st.text_input(birthday_label)
                #if id exists -> update (cascade)
            if(employee_item_update == "first name"):
                name_label = "first name: "
                id = st.text_input("Manager id: ")
                first_name = st.text_input(name_label)
                #if id exists -> update (cascade)
            if(employee_item_update == "last name"):
                name_label = "last name: "
                id = st.text_input("Manager id: ")
                last_name = st.text_input(name_label)
                #if id exists -> update (cascade)
            if(employee_item_update == "salary"):
                salary_label = "salary: "
                id = st.text_input("Manager id: ")
                salary = st.text_input(salary_label)
                #if id exists -> update (cascade)
            if(employee_item_update == "ssn"):
                ssn_label = "ssn: "
                id = st.text_input("Manager id: ")
                ssn = st.text_input(ssn_label)
                #if id exists -> update (cascade)
    
        elif employee_item_selection == 'Cashier':
            
            update_options = ("home address" , "date of birth" , "first name" , "last name" , "salary" , "ssn" , "counter id")
            employee_item_update = st.selectbox("which item do you want to update" , update_options)
            
            if(employee_item_update == "home address"):
                home_address_label = "home address: "
                id = st.text_input("Cashier id: ")
                home_address = st.text_input(home_address_label)
                #if id exists -> update (cascade)
            if(employee_item_update == "date of birth"):
                birthday_label = "date of birth: "
                id = st.text_input("Cashier id: ")
                date_of_birth = st.text_input(birthday_label)
                #if id exists -> update (cascade)
            if(employee_item_update == "first name"):
                name_label = "first name: "
                id = st.text_input("Cashier id: ")
                first_name = st.text_input(name_label)
                #if id exists -> update (cascade)
            if(employee_item_update == "last name"):
                name_label = "last name: "
                id = st.text_input("Cashier id: ")
                last_name = st.text_input(name_label)
                #if id exists -> update (cascade)
            if(employee_item_update == "salary"):
                salary_label = "salary: "
                id = st.text_input("Cashier id: ")
                salary = st.text_input(salary_label)
                #if id exists -> update (cascade)
            if(employee_item_update == "ssn"):
                ssn_label = "ssn: "
                id = st.text_input("Cashier id: ")
                ssn = st.text_input(ssn_label)
                #if id exists -> update (cascade)
            if(employee_item_update == "counter id"):
                 counter_id_label = "counter id: "
                 id = st.text_input("Cashier id: ")
                 counter_id = st.text_input(counter_id_label)
                 #if id exists -> update (cascade)
                
        elif employee_item_selection == 'Chef':
            update_options = ("home address" , "date of birth" , "first name" , "last name" , "salary" , "ssn")
            employee_item_update = st.selectbox("which item do you want to update" , update_options)
            if(employee_item_update == "home address"):
                home_address_label = "home address: "
                id = st.text_input("Chef id: ")
                home_address = st.text_input(home_address_label)
                #if id exists -> update (cascade)
            if(employee_item_update == "date of birth"):
                birthday_label = "date of birth: "
                id = st.text_input("Chef id: ")
                date_of_birth = st.text_input(birthday_label)
                #if id exists -> update (cascade)
            if(employee_item_update == "first name"):
                name_label = "first name: "
                id = st.text_input("Chef id: ")
                first_name = st.text_input(name_label)
                #if id exists -> update (cascade)
            if(employee_item_update == "last name"):
                name_label = "last name: "
                id = st.text_input("Chef id: ")
                last_name = st.text_input(name_label)
                #if id exists -> update (cascade)
            if(employee_item_update == "salary"):
                salary_label = "salary: "
                id = st.text_input("Chef id: ")
                salary = st.text_input(salary_label)
                #if id exists -> update (cascade)
            if(employee_item_update == "ssn"):
                ssn_label = "ssn: "
                id = st.text_input("Chef id: ")
                ssn = st.text_input(ssn_label)
                #if id exists -> update (cascade)
                
        elif employee_item_selection == 'Waiter':
            update_options = ("home address" , "date of birth" , "first name" , "last name" , "salary" , "ssn")
            employee_item_update = st.selectbox("which item do you want to update" , update_options)
            if(employee_item_update == "home address"):
                home_address_label = "home address: "
                id = st.text_input("Waiter id: ")
                home_address = st.text_input(home_address_label)
                #if id exists -> update (cascade)
            if(employee_item_update == "date of birth"):
                birthday_label = "date of birth: "
                id = st.text_input("Waiter id: ")
                date_of_birth = st.text_input(birthday_label)
                #if id exists -> update (cascade)
            if(employee_item_update == "first name"):
                name_label = "first name: "
                id = st.text_input("Waiter id: ")
                first_name = st.text_input(name_label)
                #if id exists -> update (cascade)
            if(employee_item_update == "last name"):
                name_label = "last name: "
                id = st.text_input("Waiter id: ")
                last_name = st.text_input(name_label)
                #if id exists -> update (cascade)
            if(employee_item_update == "salary"):
                salary_label = "salary: "
                id = st.text_input("Waiter id: ")
                salary = st.text_input(salary_label)
                #if id exists -> update (cascade)
            if(employee_item_update == "ssn"):
                ssn_label = "ssn: "
                id = st.text_input("Waiter id: ")
                ssn = st.text_input(ssn_label)
                #if id exists -> update (cascade)

        
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


if selected_option == 'Customer and Transaction':
    st.empty()
    with st.container():
        update_options = ("first name" , "last name" ,  "transaction type" , "discount")
        customer_item_update = st.selectbox("which item do you want to update" , update_options)
        if(customer_item_update == "first name"):
                first_name_label = "first name: "
                id = st.text_input("Customer id: ")
                first_name = st.text_input(first_name_label)
                #if id exists -> update (cascade)
        if(customer_item_update == "last name"):
                last_name_label = "last name: "
                id = st.text_input("Customer id: ")
                last_name = st.text_input(last_name_label)
                #if id exists -> update (cascade)
        if(customer_item_update == "transaction type"):
                transaction_type_label = "transaction type: "
                id = st.text_input("Transaction id: ")
                transaction_type = st.text_input(transaction_type_label)
                #if id exists -> update (cascade)
        if(customer_item_update == "discount"):
                discount_label = "discount: "
                id = st.text_input("Customer id: ")
                transaction_id = st.text_input("Transaction id: ")
                discount = st.text_input(discount_label)
                #if id exists -> update (cascade)
                

if selected_option == 'Counter':
    st.empty()
    with st.container():
        update_options = ("counter id" , )
        counter_item_update = st.selectbox("which item do you want to update" , update_options)
        if(counter_item_update == "counter id"):
            id = st.text_input("Initial Counter id: ")
            counter_id = st.text_input("Changed Counter id: ")
        #if id exists -> update (cascade)   

if selected_option == 'Table':
    st.empty()
    with st.container():
        update_options = ("capacity" , "is booked" , "waiter id")
        table_item_update = st.selectbox("which item do you want to update" , update_options)
        if(table_item_update == "capacity"):
                capacity_label = "capacity: "
                id = st.text_input("Table id: ")
                capacity = st.text_input(capacity_label)
                #if id exists -> update (cascade)
        if(table_item_update == "is booked"):
                is_booked_label = "is booked: "
                id = st.text_input("Table id: ")
                is_booked = st.text_input(is_booked_label)
                #if id exists -> update (cascade)
        if(table_item_update == "waiter id"):
                waiter_id_label = "waiter id: "
                id = st.text_input("Table id: ")
                waiter_id = st.text_input(waiter_id_label)
                #if id exists -> update (cascade)

if selected_option == 'Booking':
    st.empty()
    with st.container():
        update_options = ("customer id" , "table id" , "date")
        booking_item_update = st.selectbox("which item do you want to update" , update_options)
        if(booking_item_update == "customer id"):
                customer_id_label = "changed customer id: "
                customer_id = st.text_input("Initial Customer id: ")
                table_id = st.text_input("Table id: ")
                customer = st.text_input(customer_id_label)
                #if id exists -> update (cascade)
                
        if(booking_item_update == "table id"):
                table_id_label = "changed table id: "
                customer_id = st.text_input("Customer id: ")
                table_id = st.text_input("Initial Table id: ")
                table = st.text_input(table_id_label)
                #if id exists -> update (cascade) 
                       
        if(booking_item_update == "date"):
                date_label = "date: "
                customer_id = st.text_input("Customer id: ")
                table_id = st.text_input("Table id: ")
                date = st.text_input(date_label)
                #if id exists -> update (cascade)
