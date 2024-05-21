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



options = ("Menu item", "New worker", "New Details of an order", "Customer and Transaction")
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


        

elif selected_option ==  "New worker":
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





elif selected_option == "Customer and Transaction":
    st.empty()
    st.write("please update all the details relating to the order and its transaction.")
    
    customer_id_label = "Customer ID:"
    first_name_label = "First Name:"
    last_name_label = "Last Name:"
    col1, col2, col3 = st.columns(3)
    customer_id = col1.text_input(customer_id_label)
    first_name = col2.text_input(first_name_label)
    last_name = col3.text_input(last_name_label)

    col1, col2, col3, col4 = st.columns(4)
    id = col1.text_input("Transaction id:")
    Type = col2.text_input("Transaction type:")
    discount = col3.text_input("discount:")
    
    # 1.insert into order
    # 2.insert into transaction
    # 3.insert into  makes order
    

    if customer_id and first_name and last_name:
        st.write("Customer Information:")
        st.write(f"- Customer ID: {customer_id}")
        st.write(f"- First Name: {first_name}")
        st.write(f"- Last Name: {last_name}")


# elif  counter / table / booking / retrieve order / un 3 ta



        