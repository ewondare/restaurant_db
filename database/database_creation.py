# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import streamlit as st
import sqlalchemy
# Create the SQL connection to pets_db as specified in your secrets file.
conn = st.connection('databaseprojphase2_db', type='sql')

# Insert some data with conn.session.
with conn.session as s:
    create_employee_table = '''
    CREATE TABLE IF NOT EXISTS Employee (
        SSN INT NOT NULL,
        First_Name VARCHAR(50),
        Last_Name VARCHAR(50),
        Home_Address TEXT,
        Date_Of_Birth DATE,
        Salary DECIMAL(15, 2),
        PRIMARY KEY (SSN)
    );
    '''

  
    table_Customer = '''CREATE TABLE IF NOT EXISTS Customer (
            Customer_id INT NOT NULL,
            First_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50),
            PRIMARY KEY(Customer_id)
        ); '''
    
    table_Manager = '''CREATE TABLE IF NOT EXISTS Manager (
            Id INT NOT NULL,
            Employee_id INT NOT NULL,
            PRIMARY KEY(Id),
            FOREIGN KEY(Employee_id) REFERENCES Employee(SSN)
        ); '''
 
    table_Cashier = '''CREATE TABLE IF NOT EXISTS Cashier (
            Id INT NOT NULL,
            Employee_id INT NOT NULL,
            Counter_id INT NOT NULL,
            PRIMARY KEY(Id),
            FOREIGN KEY(Employee_id) REFERENCES Employee(SSN),
            FOREIGN KEY(Counter_id) REFERENCES Counter(Id)
        ); '''
    
    
    table_Waiter = '''CREATE TABLE IF NOT EXISTS Waiter (
            Id INT NOT NULL,
            Employee_id INT NOT NULL,
            PRIMARY KEY(Id),
            FOREIGN KEY(Employee_id) REFERENCES Employee(SSN)
        ); '''    
    
    table_Chef = '''CREATE TABLE IF NOT EXISTS Chef (
            Id INT NOT NULL,
            Employee_id INT NOT NULL,
            PRIMARY KEY(Id),
            FOREIGN KEY(Employee_id) REFERENCES Employee(SSN)
        ); '''    
    
    table_Food = '''CREATE TABLE IF NOT EXISTS Food (
            Id INT NOT NULL,
            name VARCHAR(100) NOT NULl,
            Is_available BOOLEAN, 
            PRIMARY KEY(Id)
        ); '''
    
    table_Counter = '''CREATE TABLE IF NOT EXISTS Counter (
            Id INT NOT NULL,
            PRIMARY KEY(Id)
        ); '''
    
    table_Transaction = '''CREATE TABLE IF NOT EXISTS Transaction_ (
            Id INT NOT NULL,
            Is_discounter BOOLEAN,
            transaction_tyep INT NOT NULL, 
            Counter_id_ref INT,
            PRIMARY KEY(Id),
            FOREIGN KEY(Counter_id_ref) REFERENCES Counter(Id)
        ); '''
    
    table_Table_dine = '''CREATE TABLE IF NOT EXISTS Table_dine (
            Id INT NOT NULL,
            capacity INT NOT NULL,
            Is_available BOOLEAN, 
            Waiter_id_ref INT,
            PRIMARY KEY(Id),
            FOREIGN KEY(Waiter_id_ref) REFERENCES Waiter(Id)
        ); '''
    
    table_Booking = '''CREATE TABLE IF NOT EXISTS Booking (
            Customer_id_ref INT NOT NULL,
            Table_dine_id_ref INT NOT NULL,
            book_date DATE, 
            PRIMARY KEY(Customer_id_ref,Table_dine_id_ref),
            FOREIGN KEY(Customer_id_ref) REFERENCES Customer(Customer_id),
            FOREIGN KEY(Table_dine_id_ref) REFERENCES Table_dine(Id)
        ); '''
    
    table_Order = '''CREATE TABLE IF NOT EXISTS Order_food (
            Order_id INT NOT NULL,
            Table_condition TEXT,
            is_paid BOOLEAN, 
            price DOUBLE,
            order_date DATE,
            table_id_ref INT,
            PRIMARY KEY(Order_id),
            FOREIGN KEY(table_id_ref) REFERENCES Table_dine(Id)
        ); '''   
    
    table_Makes_order = '''CREATE TABLE IF NOT EXISTS Makes_order (
            Customer_id_ref INT NOT NULL,
            Order_id_ref INT NOT NULL,
            Transaction_id_ref INT,
            PRIMARY KEY(Customer_id_ref,Order_id_ref,Transaction_id_ref),
            FOREIGN KEY(Customer_id_ref) REFERENCES Customer(Customer_id),
            FOREIGN KEY(Order_id_ref) REFERENCES Order_food(Order_id),
            FOREIGN KEY(Transaction_id_ref) REFERENCES Transaction_(Id)
        ); '''
    
    table_Receive_order = '''CREATE TABLE IF NOT EXISTS Receive_order (
            Chef_id_ref INT NOT NULL,
            Order_id_ref INT NOT NULL,
            Waiter_id_ref INT NOT NULL,
            PRIMARY KEY(Chef_id_ref,Order_id_ref,Waiter_id_ref),
            FOREIGN KEY(Chef_id_ref) REFERENCES Chef(Id),
            FOREIGN KEY(Waiter_id_ref) REFERENCES Waiter(Id),
            FOREIGN KEY(Order_id_ref) REFERENCES  Order_food(Order_id)
        ); '''
    
    table_Deliver_food = '''CREATE TABLE IF NOT EXISTS Deliver_food (
            Food_id_ref INT NOT NULL,
            Table_dine_id_ref INT NOT NULL,
            Waiter_id_ref INT NOT NULL,
            PRIMARY KEY(Food_id_ref,Table_dine_id_ref,Waiter_id_ref),
            FOREIGN KEY(Food_id_ref) REFERENCES Food(Id),
            FOREIGN KEY(Table_dine_id_ref) REFERENCES Table_dine(Id),
            FOREIGN KEY(Waiter_id_ref) REFERENCES Waiter(Id)
        ); '''
    
    table_Menu = '''CREATE TABLE IF NOT EXISTS Menu (
            Id INT NOT NULL,
            title TEXT,
            summery TEXT, 
            is_availaible BOOLEAN,
            PRIMARY KEY(Id)
        ); '''   
    

    table_Appetizer_item = '''CREATE TABLE IF NOT EXISTS Appetizer_item (
            Id INT NOT NULL,
            name TEXT,
            price DOUBLE, 
            description TEXT,
            recipie TEXT,
            menu_id INT NOT NULL,
            PRIMARY KEY(Id),
            FOREIGN KEY(menu_id) REFERENCES Menu(Id)

        ); '''   
    
    table_Entree_item = '''CREATE TABLE IF NOT EXISTS Entree_item (
            Id INT NOT NULL,
            name TEXT,
            price DOUBLE, 
            description TEXT,
            recipie TEXT,
            menu_id INT NOT NULL,
            PRIMARY KEY(Id),
            FOREIGN KEY(menu_id) REFERENCES Menu(Id)
        ); '''   
    
    table_Desert_item = '''CREATE TABLE IF NOT EXISTS Desert_item (
            Id INT NOT NULL,
            name TEXT,
            price DOUBLE, 
            description TEXT,
            recipie TEXT,
            menu_id INT NOT NULL,
            PRIMARY KEY(Id),
            FOREIGN KEY(menu_id) REFERENCES Menu(Id)

        ); '''

    table_Appetizer_order = '''CREATE TABLE IF NOT EXISTS Appetizer_order (
            Id INT NOT NULL,
            order_id INT NOT NULL,
            appetizer_id INT NOT NULL,
            PRIMARY KEY(Id),
            FOREIGN KEY(order_id) REFERENCES Order_food(Order_id),
            FOREIGN KEY(appetizer_id) REFERENCES Appetizer_item(Id)
        ); '''   
    table_Entree_order = '''CREATE TABLE IF NOT EXISTS Entree_order (
            Id INT NOT NULL,
            order_id INT NOT NULL,
            Entree_id INT NOT NULL,
            PRIMARY KEY(Id),
            FOREIGN KEY(order_id) REFERENCES Order_food(Order_id),
            FOREIGN KEY(Entree_id) REFERENCES Entree_item(Id)
        ); '''   
    table_Desert_order = '''CREATE TABLE IF NOT EXISTS Desert_order (
            Id INT NOT NULL,
            order_id INT NOT NULL,
            Desert_id INT NOT NULL,
            PRIMARY KEY(Id),
            FOREIGN KEY(order_id) REFERENCES Order_food(Order_id),
            FOREIGN KEY(Desert_id) REFERENCES Desert_item(Id)
        ); '''   
    
    # Define the values to be inserted as a dictionary
    employee_values = {'SSN': 1351351365, 'Home_Address': 'qghafhafh', 'Date_Of_Birth': '2000-03-03', 'Salary': 270000.0, 'First_Name': 'dgahafh', 'Last_Name': 'fhafhafh'}
    
    # Define the insert statement
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
    #s.execute(insert_employee_query, employee_values)                
    #s.execute(insert_manager_query, manager_values)
              
    #s.execute("DROP TABLE Receive_order")
    s.execute(create_employee_table);
    s.execute(table_Customer);
    s.execute(table_Cashier);
    s.execute(table_Manager);
    s.execute(table_Waiter);
    s.execute(table_Chef);
    s.execute(table_Food);
    s.execute(table_Counter);
    s.execute(table_Transaction);
    s.execute(table_Table_dine);
    s.execute(table_Booking);
    s.execute(table_Order);
    s.execute(table_Makes_order);
    s.execute(table_Receive_order);
    s.execute(table_Deliver_food);
    s.execute(table_Menu);
    s.execute(table_Appetizer_item);
    s.execute(table_Entree_item);
    s.execute(table_Desert_item);
    s.execute(table_Appetizer_order);
    s.execute(table_Entree_order);
    s.execute(table_Desert_order);
    
    s.commit()

# Query and display the data you inserted
pet_owners = conn.query('select * from Employee')
st.dataframe(pet_owners)
# Query and display the data you inserted
pet_ownersE = conn.query('select * from Manager')
st.dataframe(pet_ownersE)

pet_ownersEe = conn.query('select * from Counter')
st.dataframe(pet_ownersEe)

pet_ownersEee = conn.query('select * from Waiter')
st.dataframe(pet_ownersEee)

pet_ownersEeee = conn.query('select * from Chef')
st.dataframe(pet_ownersEeee)

pet_ownersEeeEe = conn.query('select * from Cashier')
st.dataframe(pet_ownersEeeEe)