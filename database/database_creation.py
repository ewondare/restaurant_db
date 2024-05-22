# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import streamlit as st

# Create the SQL connection to pets_db as specified in your secrets file.
conn = st.connection('databaseprojphase2_db', type='sql')

# Insert some data with conn.session.
with conn.session as s:
    table_Employee = '''CREAT TABLE IF NOT EXISTS Employee (
            SSN INT NOT NULL,
            Home_Adress TEXT,
            Date_of_birth DATE,
            Salary DOUBLE,
            PRIMARY KEY(SSN)
        ); '''
  
    table_Customer = '''CREAT TABLE IF NOT EXISTS Customer (
            Customer_id INT NOT NULL,
            First_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50),
            PRIMARY KEY(Customer_id)
        ); '''
    
    table_Manager = '''CREAT TABLE IF NOT EXISTS Manager (
            Id INT NOT NULL,
            Employee_id INT NOT NULL,
            PRIMARY KEY(Id),
            FOREIGN KEY(Employee_id) REFERENCES Employee(SSN)
        ); '''
 
    table_Cashier = '''CREAT TABLE IF NOT EXISTS Cashier (
            Id INT NOT NULL,
            Employee_id INT NOT NULL,
            Counter_id INT NOT NULL,
            PRIMARY KEY(Id),
            FOREIGN KEY(Employee_id) REFERENCES Employee(SSN),
            FOREIGN KEY(Counter_id) REFERENCES Counter(Id)
        ); '''
    
    
    table_Waiter = '''CREAT TABLE IF NOT EXISTS Waiter (
            Id INT NOT NULL,
            Employee_id INT NOT NULL,
            PRIMARY KEY(Id),
            FOREIGN KEY(Employee_id) REFERENCES Employee(SSN)
        ); '''    
    
    table_Chef = '''CREAT TABLE IF NOT EXISTS Chef (
            Id INT NOT NULL,
            Employee_id INT NOT NULL,
            PRIMARY KEY(Id),
            FOREIGN KEY(Employee_id) REFERENCES Employee(SSN)
        ); '''    
    
    table_Food = '''CREAT TABLE IF NOT EXISTS Food (
            Id INT NOT NULL,
            name VARCHAR(100) NOT NULl,
            Is_available BOOLEAN, 
            PRIMARY KEY(Id)
        ); '''
    
    table_Counter = '''CREAT TABLE IF NOT EXISTS Counter (
            Id INT NOT NULL,
            PRIMARY KEY(Id)
        ); '''
    
    table_Transaction = '''CREAT TABLE IF NOT EXISTS Transaction (
            Id INT NOT NULL,
            Is_discounter BOOLEAN,
            transaction_tyep INT NOT NULL, 
            Counter_id_ref INT,
            PRIMARY KEY(Id),
            FOREIGN KEY(Counter_id_ref) REFERENCES Counter(Id)
        ); '''
    
    table_Table_dine = '''CREAT TABLE IF NOT EXISTS Table_dine (
            Id INT NOT NULL,
            capacity INT NOT NULL,
            Is_available BOOLEAN, 
            Waiter_id_ref INT,
            PRIMARY KEY(Id),
            FOREIGN KEY(Waiter_id_ref) REFERENCES Waiter(Id)
        ); '''
    
    table_Booking = '''CREAT TABLE IF NOT EXISTS Booking (
            Customer_id_ref INT NOT NULL,
            Table_dine_id_ref INT NOT NULL,
            book_date DATE, 
            PRIMARY KEY(Customer_id_ref,Table_dine_id_ref),
            FOREIGN KEY(Customer_id_ref) REFERENCES Customer(Customer_id),
            FOREIGN KEY(Table_dine_id_ref) REFERENCES Table_dine(Id)
        ); '''
    
    table_Order = '''CREAT TABLE IF NOT EXISTS Order (
            Order_id INT NOT NULL,
            Table_condition TEXT,
            is_paid BOOLEAN, 
            price DOUBLE,
            order_date DATE,
            table_id_ref INT,
            PRIMARY KEY(Order_id),
            FOREIGN KEY(table_id_ref) REFERENCES Table_dine(Id)
        ); '''   
    
    table_Makes_order = '''CREAT TABLE IF NOT EXISTS Makes_order (
            Customer_id_ref INT NOT NULL,
            Order_id_ref INT NOT NULL,
            Transaction_id_ref INT,
            PRIMARY KEY(Customer_id_ref,Order_id_ref,Transaction_id_ref),
            FOREIGN KEY(Customer_id_ref) REFERENCES Customer(Customer_id),
            FOREIGN KEY(Order_id_ref) REFERENCES Order(Order_id),
            FOREIGN KEY(Transaction_id_ref) REFERENCES Transaction(Id)
        ); '''
    
    table_Receive_order = '''CREAT TABLE IF NOT EXISTS Makes_order (
            Chef_id_ref INT NOT NULL,
            Order_id_ref INT NOT NULL,
            Waiter_id_ref INT,
            PRIMARY KEY(Chef_id_ref,Order_id_ref,Waiter_id_ref),
            FOREIGN KEY(Chef_id_ref) REFERENCES Chef(Id),
            FOREIGN KEY(Waiter_id_ref) REFERENCES Waiter(Id),
            FOREIGN KEY(Order_id_ref) REFERENCES  Order(Order_id)
        ); '''
    
    table_Deliver_food = '''CREAT TABLE IF NOT EXISTS Deliver_food (
            Food_id_ref INT NOT NULL,
            Table_dine_id_ref INT NOT NULL,
            Waiter_id_ref INT NOT NULL,
            PRIMARY KEY(Food_id_ref,Table_dine_id_ref,Waiter_id_ref),
            FOREIGN KEY(Food_id_ref) REFERENCES Food(Id),
            FOREIGN KEY(Table_dine_id_ref) REFERENCES Table_dine(Id),
            FOREIGN KEY(Waiter_id_ref) REFERENCES Waiter(Id)
        ); '''
    
    table_Menu = '''CREAT TABLE IF NOT EXISTS Menu (
            Id INT NOT NULL,
            title TEXT,
            summery TEXT, 
            is_availaible BOOLEAN,
            PRIMARY KEY(Id),

        ); '''   
    

    table_Appetizer_item = '''CREAT TABLE IF NOT EXISTS Appetizer_item (
            Id INT NOT NULL,
            name TEXT,
            price DOUBLE, 
            description TEXT,
            recipie TEXT,
            menu_id INT NOT NULL,
            PRIMARY KEY(Id),
            FOREIGN KEY(menu_id) REFERENCES Menu(Id),

        ); '''   
    
    table_Entree_item = '''CREAT TABLE IF NOT EXISTS Entree_item (
            Id INT NOT NULL,
            name TEXT,
            price DOUBLE, 
            description TEXT,
            recipie TEXT,
            menu_id INT NOT NULL,
            PRIMARY KEY(Id),
            FOREIGN KEY(menu_id) REFERENCES Menu(Id),

        ); '''   
    
    table_Desert_item = '''CREAT TABLE IF NOT EXISTS Desert_item (
            Id INT NOT NULL,
            name TEXT,
            price DOUBLE, 
            description TEXT,
            recipie TEXT,
            menu_id INT NOT NULL,
            PRIMARY KEY(Id),
            FOREIGN KEY(menu_id) REFERENCES Menu(Id),

        ); '''

    table_Appetizer_order = '''CREAT TABLE IF NOT EXISTS Appetizer_order (
            Id INT NOT NULL,
            order_id INT NOT NULL,
            appetizer_id INT NOT NULL,
            PRIMARY KEY(Id),
            FOREIGN KEY(order_id) REFERENCES Order(Order_id),
            FOREIGN KEY(appetizer_id) REFERENCES Appetizer_item(Id)
        ); '''   
    table_Entree_order = '''CREAT TABLE IF NOT EXISTS Entree_order (
            Id INT NOT NULL,
            order_id INT NOT NULL,
            Entree_id INT NOT NULL,
            PRIMARY KEY(Id),
            FOREIGN KEY(order_id) REFERENCES Order(Order_id),
            FOREIGN KEY(Entree_id) REFERENCES Entree_item(Id)
        ); '''   
    table_Desert_order = '''CREAT TABLE IF NOT EXISTS Desert_order (
            Id INT NOT NULL,
            order_id INT NOT NULL,
            Desert_id INT NOT NULL,
            PRIMARY KEY(Id),
            FOREIGN KEY(order_id) REFERENCES Order(Order_id),
            FOREIGN KEY(Desert_id) REFERENCES Desert_item(Id)
        ); '''   
           
    
    
    s.commit()

# Query and display the data you inserted
#pet_owners = conn.query('select * from pet_owners')
#st.dataframe(pet_owners)