# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

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
    Trusted_Connection=yes;
"""
conn = odbc.connect(connectString=connection_string)
s = conn.cursor()
print(conn)
print()
# Insert some data with conn.session.
create_employee_table = '''
    CREATE TABLE Employee (
        SSN INT NOT NULL,
        First_Name VARCHAR(50),
        Last_Name VARCHAR(50),
        Home_Address TEXT,
        Date_Of_Birth DATE,
        Salary DECIMAL(15, 2),
        PRIMARY KEY (SSN)
    );
    '''

  
table_Customer = '''CREATE TABLE  Customer (
            Customer_id INT NOT NULL,
            First_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50),
            PRIMARY KEY(Customer_id)
        ); '''
    
table_Manager = '''CREATE TABLE  Manager (
            Id INT NOT NULL,
            Employee_id INT NOT NULL,
            PRIMARY KEY(Id),
            FOREIGN KEY(Employee_id) REFERENCES Employee(SSN)
        ); '''
 
table_Cashier = '''CREATE TABLE  Cashier (
            Id INT NOT NULL,
            Employee_id INT NOT NULL,
            Counter_id INT NOT NULL,
            PRIMARY KEY(Id),
            FOREIGN KEY(Employee_id) REFERENCES Employee(SSN),
            FOREIGN KEY(Counter_id) REFERENCES Counter(Id)
        ); '''
    
    
table_Waiter = '''CREATE TABLE Waiter (
            Id INT NOT NULL,
            Employee_id INT NOT NULL,
            PRIMARY KEY(Id),
            FOREIGN KEY(Employee_id) REFERENCES Employee(SSN)
        ); '''    
    
table_Chef = '''CREATE TABLE  Chef (
            Id INT NOT NULL,
            Employee_id INT NOT NULL,
            PRIMARY KEY(Id),
            FOREIGN KEY(Employee_id) REFERENCES Employee(SSN)
        ); '''    
    
table_Food = '''CREATE TABLE  Food (
            Id INT NOT NULL,
            name VARCHAR(100) NOT NULl,
            Is_available BIT, 
            PRIMARY KEY(Id)
        ); '''
    
table_Counter = '''CREATE TABLE  Counter (
            Id INT NOT NULL,
            PRIMARY KEY(Id)
        ); '''
    
table_Transaction = '''CREATE TABLE  Transaction_ (
            Id INT NOT NULL,
            Is_discounter BIT ,
            transaction_tyep INT NOT NULL, 
            Counter_id_ref INT,
            PRIMARY KEY(Id),
            FOREIGN KEY(Counter_id_ref) REFERENCES Counter(Id)
        ); '''
    
table_Table_dine = '''CREATE TABLE  Table_dine (
            Id INT NOT NULL,
            capacity INT NOT NULL,
            Is_available BIT, 
            Waiter_id_ref INT,
            PRIMARY KEY(Id),
            FOREIGN KEY(Waiter_id_ref) REFERENCES Waiter(Id)
        ); '''
    
table_Booking = '''CREATE TABLE  Booking (
            Customer_id_ref INT NOT NULL,
            Table_dine_id_ref INT NOT NULL,
            book_date DATE, 
            PRIMARY KEY(Customer_id_ref,Table_dine_id_ref),
            FOREIGN KEY(Customer_id_ref) REFERENCES Customer(Customer_id),
            FOREIGN KEY(Table_dine_id_ref) REFERENCES Table_dine(Id)
        ); '''
    
table_Order = '''CREATE TABLE Order_food (
    Order_id INT NOT NULL PRIMARY KEY,
    Table_condition NVARCHAR(MAX),
    is_paid BIT,
    price FLOAT,
    order_date DATE,
    table_id_ref INT,
    FOREIGN KEY (table_id_ref) REFERENCES Table_dine(Id)
        ); '''   
    
table_Makes_order = '''CREATE TABLE  Makes_order (
            Customer_id_ref INT NOT NULL,
            Order_id_ref INT NOT NULL,
            Transaction_id_ref INT,
            PRIMARY KEY(Customer_id_ref,Order_id_ref,Transaction_id_ref),
            FOREIGN KEY(Customer_id_ref) REFERENCES Customer(Customer_id),
            FOREIGN KEY(Order_id_ref) REFERENCES Order_food(Order_id),
            FOREIGN KEY(Transaction_id_ref) REFERENCES Transaction_(Id)
        ); '''
    
table_Receive_order = '''CREATE TABLE  Receive_order (
            Chef_id_ref INT NOT NULL,
            Order_id_ref INT NOT NULL,
            Waiter_id_ref INT NOT NULL,
            PRIMARY KEY(Chef_id_ref,Order_id_ref,Waiter_id_ref),
            FOREIGN KEY(Chef_id_ref) REFERENCES Chef(Id),
            FOREIGN KEY(Waiter_id_ref) REFERENCES Waiter(Id),
            FOREIGN KEY(Order_id_ref) REFERENCES  Order_food(Order_id)
        ); '''
    
table_Deliver_food = '''CREATE TABLE  Deliver_food (
            Food_id_ref INT NOT NULL,
            Table_dine_id_ref INT NOT NULL,
            Waiter_id_ref INT NOT NULL,
            PRIMARY KEY(Food_id_ref,Table_dine_id_ref,Waiter_id_ref),
            FOREIGN KEY(Food_id_ref) REFERENCES Food(Id),
            FOREIGN KEY(Table_dine_id_ref) REFERENCES Table_dine(Id),
            FOREIGN KEY(Waiter_id_ref) REFERENCES Waiter(Id)
        ); '''
    
table_Menu = '''CREATE TABLE  Menu (
            Id INT NOT NULL,
            title NVARCHAR(MAX),
            summery NVARCHAR(MAX), 
            is_availaible BIT,
            PRIMARY KEY(Id)
        ); '''   
    

table_Appetizer_item = '''CREATE TABLE Appetizer_item (
    Id INT NOT NULL PRIMARY KEY,
    name NVARCHAR(MAX),
    price FLOAT,
    description NVARCHAR(MAX),
    recipie NVARCHAR(MAX),
    menu_id INT NOT NULL,
    FOREIGN KEY (menu_id) REFERENCES Menu(Id)
);'''   
    
table_Entree_item = '''CREATE TABLE  Entree_item (
    Id INT NOT NULL PRIMARY KEY,
    name NVARCHAR(MAX),
    price FLOAT,
    description NVARCHAR(MAX),
    recipie NVARCHAR(MAX),
    menu_id INT NOT NULL,
    FOREIGN KEY (menu_id) REFERENCES Menu(Id)
        ); '''   
    
table_Desert_item = '''CREATE TABLE  Desert_item (
    Id INT NOT NULL PRIMARY KEY,
    name NVARCHAR(MAX),
    price FLOAT,
    description NVARCHAR(MAX),
    recipie NVARCHAR(MAX),
    menu_id INT NOT NULL,
    FOREIGN KEY (menu_id) REFERENCES Menu(Id)
        ); '''

table_Appetizer_order = '''CREATE TABLE  Appetizer_order (
            Id INT NOT NULL,
            order_id INT NOT NULL,
            appetizer_id INT NOT NULL,
            PRIMARY KEY(Id),
            FOREIGN KEY(order_id) REFERENCES Order_food(Order_id),
            FOREIGN KEY(appetizer_id) REFERENCES Appetizer_item(Id)
        ); '''   
table_Entree_order = '''CREATE TABLE  Entree_order (
            Id INT NOT NULL,
            order_id INT NOT NULL,
            Entree_id INT NOT NULL,
            PRIMARY KEY(Id),
            FOREIGN KEY(order_id) REFERENCES Order_food(Order_id),
            FOREIGN KEY(Entree_id) REFERENCES Entree_item(Id)
        ); '''   
table_Desert_order = '''CREATE TABLE  Desert_order (
            Id INT NOT NULL,
            order_id INT NOT NULL,
            Desert_id INT NOT NULL,
            PRIMARY KEY(Id),
            FOREIGN KEY(order_id) REFERENCES Order_food(Order_id),
            FOREIGN KEY(Desert_id) REFERENCES Desert_item(Id)
        ); '''   
    

              
    #s.execute("DROP TABLE Receive_order")


              
    #s.execute("DROP TABLE Receive_order")
s.execute(create_employee_table);
s.execute(table_Customer);
s.execute(table_Counter);

s.execute(table_Cashier);
s.execute(table_Manager);
s.execute(table_Waiter);
s.execute(table_Chef);
s.execute(table_Food);
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


s.commit();
