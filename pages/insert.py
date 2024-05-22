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

conn = odbc.connect(connectString=connection_string)
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
            #home_address, birthday , salary, first_name, last_name = None

            col1,col2,col3 = st.columns(3)
            ssn = col1.text_input("ssn:")
            home_address = col2.text_input("home address:")
            birthday = col3.text_input("date of birthday:")

            col4, col5, col6, col7 = st.columns(4)
            salary = col4.text_input("salary: ")
            first_name = col5.text_input("first name:")
            last_name = col6.text_input("last name:")
            # 1.insert into employee if ssn doesn not already exist

            id = col7.text_input("Manager id:")
            # 2.insert id, ssn into manager if id does not already exist

        elif employee_item_selection == 'Cashier':
            #home_address, birthday , salary, first_name, last_name = None
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

            id = col7.text_input("Cashier id:")
            ########
            ### query = "Select id from counter"
            ### df = 
            ###Names = df['id]
            counter_id_options = tuple([1 , 2 , 3]) # = id
            counter_id = col0.selectbox("counter id: " , counter_id_options)
            # 2.insert id, ssn, counter_id  into cashier if id does not already exist

        elif employee_item_selection == 'Chef':
            #home_address, birthday , salary, first_name, last_name = None

            col1,col2,col3 = st.columns(3)
            ssn = col1.text_input("ssn:")
            home_address = col2.text_input("home address:")
            birthday = col3.text_input("date of birthday:")

            col4, col5, col6, col7 = st.columns(4)
            salary = col4.text_input("salary: ")
            first_name = col5.text_input("first name:")
            last_name = col6.text_input("last name:")
            # 1.insert into employee if ssn doesn not already exist

            id = col7.text_input("Chef id:")
            # 2.insert id, ssn into chef if id does not already exist      
        elif employee_item_selection == 'Waiter':
            #home_address, birthday , salary, first_name, last_name = None

            col1,col2,col3 = st.columns(3)
            ssn = col1.text_input("ssn:")
            home_address = col2.text_input("home address:")
            birthday = col3.text_input("date of birthday:")

            col4, col5, col6, col7 = st.columns(4)
            salary = col4.text_input("salary: ")
            first_name = col5.text_input("first name:")
            last_name = col6.text_input("last name:")
            # 1.insert into employee if ssn doesn not already exist

            id = col7.text_input("Waiter id:")
            # 2.insert id, ssn into waiter if id does not already exist      




elif selected_option == "New Details of an order":
    st.empty()
    with st.container():

        order_id_label = "order id:"
        table_id_label = "table id:"
        is_paid_label = "is paid:"
        date_label = "date:"
        counter_id_label = "select counter id:"
        col1, col2, col3 = st.columns(3)
        order_id = col1.text_input(order_id_label)
        table_id = col2.text_input(table_id_label)
        is_paid = col3.text_input(is_paid_label)


        col4, col5 = st.columns(2)
        date  = col4.text_input(date_label)

        

        ########
        ### query = "Select id from counter"
        ### df = 
        ###Names = df['id]
        counter_id_options = tuple([1 , 2 , 3]) # = id
        counter_id = col5.selectbox(counter_id_label , counter_id_options)

        st.write("for also entering details for [Recieve Order] table, please fill the following setions.")
        col6,col7 = st.columns(2)
        chef_id = col6.text_input("Chef id: ")
        waiter_id = col7.text_input("Waiter id:")

        ######
        ## if chef_id and waiter_id exist => chef_id , waiter_id , order_id insert into [Recieve Order]






elif selected_option == "Customer and Transaction":
    st.empty()
    with st.container():
        st.write("please update all the details relating to the order and its transaction.")
        
        customer_id_label = "Customer ID:"
        first_name_label = "First Name:"
        last_name_label = "Last Name:"
        col1, col2, col3, col4 = st.columns(4)
        customer_id = col1.text_input(customer_id_label)
        first_name = col2.text_input(first_name_label)
        last_name = col3.text_input(last_name_label)
        order_id = col4.text_input("Customer id:")

        col1, col2, col3, col4 = st.columns(4)
        id = col1.text_input("Transaction id:")
        Type = col2.text_input("Transaction type:")
        discount = col3.text_input("discount:")
        
        # 1.insert into order
        # 2.insert into transaction
        # 3.insert into  makes order
        



elif selected_option == 'Counter':
    st.empty()
    with st.container():
        counter_id = st.text_input("Counter id: ")
    ### query -> if counter id does not exist -> insert

elif selected_option == 'Table':
    st.empty()
    with st.container():
        col1, col2, col3 , col4 = st.columns(4)
        table_id = col1.text_input("Table id: ")
        capacity = col2.text_input("Capacty:")
        is_booked = col3.text_input("Is it booked?")
        waiter_id = col4.text_input("Waiter id:")
    ### query -> if table id does not exist and id waiter id exist -> insert


elif selected_option == 'Booking':
    st.empty()
    with st.container():
        col1 , col2 , col3 = st.columns(3)
        customer_id = col1.text_input("Customer id: ")
        table_id = col2.text_input("Table id:")
        date = col3.text_input("Date: ")
        # if customer id and table id already exist -> insert

         


# elif     un 3 ta
# retrieve order tuye Order anjam mishe.