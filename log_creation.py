# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:36:14 2024

@author: LENOVO
"""

import streamlit as st
import pypyodbc as odbc 
import sqlite3
import sqlalchemy


Parinaz_SERVER_NAME = 'DESKTOP-0S9785Q\SQLEXPRESS'
Nazanin_SERVER_NAME = 'DESKTOP-LMGNA9O\DEFAULT2023'
Dorsa_SERVER_NAME = 'DESKTOP-CEC2DIQ'
Taha_SERVER_NAME = 'DESKTOP-PS5PSLJ\SQLEXPRESS'

Parinaz_DB = 'GroupAssignment1'
Nazanin_DB = 'proj'
Dorsa_DB = 'GroupAssignment2(1)'
Taha_DB = 'GroupAssignment1'

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = Taha_SERVER_NAME
DATABASE_NAME = Taha_DB

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""

conn = odbc.connect(connectString=connection_string)
print(conn)

create_employee_log_table = """
                if not exists (select * from sysobjects where name='EmployeeLog' and xtype='U')
                    CREATE TABLE  EmployeeLog (
                        log_id INTEGER IDENTITY(1,1) PRIMARY KEY,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                        operation TEXT,
                        ssn CHAR(10),
                        home_address varchar(250),
                        date_of_birth date,
                        salary REAL,
                        first_name varchar(250),
                        last_name varchar(250),
                        old_home_address varchar(250),
                        old_date_of_birth DATE,
                        old_salary REAL,
                        old_first_name varchar(250),
                        old_last_name varchar(250)
                    );
                    """
create_Manager_log_table = """
                    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='ManagerLog' AND xtype='U')
                        CREATE TABLE ManagerLog (
                            log_id INT IDENTITY(1,1) PRIMARY KEY,
                            timestamp DATETIME DEFAULT GETDATE(),
                            operation VARCHAR(50),
                            manager_id bigINT,
                            employee_id char(10),
                            old_manager_id bigINT,
                            old_employee_id char(10)
                        );
                   """
                   
create_Cashier_log_table = """
                        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='CashierLog' AND xtype='U')
                        BEGIN
                            CREATE TABLE CashierLog (
                                log_id INT IDENTITY(1,1) PRIMARY KEY,
                                timestamp DATETIME DEFAULT GETDATE(),
                                operation VARCHAR(50),
                                cashier_id bigINT,
                                employee_id char(10),
                                counter_id INT,
                                old_cashier_id bigINT,
                                old_employee_id char(10),
                                old_counter_id INT
                            );
                        END;
                   """         
                   
 
create_ChefLog_log_table = """
                      IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='ManagerLog' AND xtype='U')
                          CREATE TABLE ChefLog (
                              log_id INT IDENTITY(1,1) PRIMARY KEY,
                              timestamp DATETIME DEFAULT GETDATE(),
                              operation VARCHAR(50),
                              Chef_id bigINT,
                              employee_id char(10),
                              Chef_manager_id bigINT,
                              old_employee_id char(10)
                          );
                     """
                 
create_Order_log_table = """
                IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='OrderLog' AND xtype='U')
                BEGIN
                    CREATE TABLE OrderLog (
                        log_id INT IDENTITY(1,1) PRIMARY KEY,
                        timestamp DATETIME DEFAULT GETDATE(),
                        operation VARCHAR(50),
                        order_id bigint,
                        table_id INT,
                        is_paid BIT,
                        price bigint,
                        counter_id INT,
                        date DATE,
                        old_order_id bigint,
                        old_table_id INT,
                        old_is_paid BIT,
                        old_price bigint,
                        old_counter_id INT,
                        old_date DATE
                    );
                END;                     """
                 
create_Makes_order_log_table = """
                    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Makes_orderLog' AND xtype='U')
                    BEGIN
                        CREATE TABLE Makes_orderLog (
                            log_id INT IDENTITY(1,1) PRIMARY KEY,
                            timestamp DATETIME DEFAULT GETDATE(),
                            operation VARCHAR(50),
                            customer_id bigint,
                            order_id bigint,
                            transaction_id bigint,
                            old_customer_id bigint,
                            old_order_id bigint,
                            old_transaction_id bigint
                        );
                    END;
                """
create_Receive_order_log_table = """
                    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Receive_orderLog' AND xtype='U')
                    BEGIN
                        CREATE TABLE Receive_orderLog (
                            log_id INT IDENTITY(1,1) PRIMARY KEY,
                            timestamp DATETIME DEFAULT GETDATE(),
                            operation VARCHAR(50),
                            chef_id bigint,
                            waiter_id bigint,
                            order_id bigint,
                            old_chef_id bigint,
                            old_waiter_id bigint,
                            old_order_id bigint
                        );
                    END;

                """
create_Transaction_order_log_table = """
                    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='TransactionLog' AND xtype='U')
                    BEGIN
                        CREATE TABLE TransactionLog (
                            log_id INT IDENTITY(1,1) PRIMARY KEY,
                            timestamp DATETIME DEFAULT GETDATE(),
                            operation VARCHAR(50),
                            transaction_id bigint,
                            type VARCHAR(50),
                            discount bit,
                            counter_id int,
                            old_transaction_id bigint,
                            old_type VARCHAR(50),
                            old_discount bit,
                            old_counter_id INT
                        );
                    END;

                 """        
                 
create_Customer_order_log_table = """
                    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='CustomerLog' AND xtype='U')
                    BEGIN
                        CREATE TABLE CustomerLog (
                            log_id INT IDENTITY(1,1) PRIMARY KEY,
                            timestamp DATETIME DEFAULT GETDATE(),
                            operation VARCHAR(50),
                            customer_id bigint,
                            first_name VARCHAR(250),
                            last_name VARCHAR(250),
                            old_customer_id bigint,
                            old_first_name VARCHAR(250),
                            old_last_name VARCHAR(250)
                        );
                    END;


                 """    
create_Table_order_log_table = """
                    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='TableLog' AND xtype='U')
                    BEGIN
                        CREATE TABLE TableLog (
                            log_id INT IDENTITY(1,1) PRIMARY KEY,
                            timestamp DATETIME DEFAULT GETDATE(),
                            operation VARCHAR(50),
                            table_id INT,
                            capacity INT,
                            is_booked BIT,
                            waiter_id bigint,
                            old_table_id INT,
                            old_capacity INT,
                            old_is_booked BIT,
                            old_waiter_id bigint
                        );
                    END;


                 """    
create_DessertItems_log_table = """
                    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='DessertItemsLog' AND xtype='U')
                    BEGIN
                        CREATE TABLE DessertItemsLog (
                            log_id INT IDENTITY(1,1) PRIMARY KEY,
                            timestamp DATETIME DEFAULT GETDATE(),
                            operation VARCHAR(50),
                            dessert_item_id INT,
                            name VARCHAR(250),
                            price bigint,
                            recipe VARCHAR(MAX),
                            description VARCHAR(MAX),
                            menu_id INT,
                            old_dessert_item_id INT,
                            old_name VARCHAR(250),
                            old_price bigint,
                            old_recipe VARCHAR(MAX),
                            old_description VARCHAR(MAX),
                            old_menu_id INT
                        );
                    END;

                  """    
create_Entreeitems_log_table = """
                     IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='EntreeitemsLog' AND xtype='U')
                     BEGIN
                         CREATE TABLE EntreeitemsLog (
                             log_id INT IDENTITY(1,1) PRIMARY KEY,
                             timestamp DATETIME DEFAULT GETDATE(),
                             operation VARCHAR(50),
                             entree_item_id INT,
                             name VARCHAR(250),
                             price bigint,
                             recipe VARCHAR(MAX),
                             description VARCHAR(MAX),
                             menu_id INT,
                             old_entree_item_id INT,
                             old_name VARCHAR(250),
                             old_price bigint,
                             old_recipe VARCHAR(MAX),
                             old_description VARCHAR(MAX),
                             old_menu_id INT
                         );
                     END;

                   """        
create_Appetizeritems_log_table = """
                    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='AppetizeritemsLog' AND xtype='U')
                    BEGIN
                        CREATE TABLE AppetizeritemsLog (
                            log_id INT IDENTITY(1,1) PRIMARY KEY,
                            timestamp DATETIME DEFAULT GETDATE(),
                            operation VARCHAR(50),
                            appetizer_item_id INT,
                            name VARCHAR(250),
                            price bigint,
                            recipe VARCHAR(MAX),
                            description VARCHAR(MAX),
                            menu_id INT,
                            old_appetizer_item_id INT,
                            old_name VARCHAR(250),
                            old_price bigint,
                            old_recipe VARCHAR(MAX),
                            old_description VARCHAR(MAX),
                            old_menu_id INT
                        );
                    END;

                  """               
                  
                  
                  
cursor = conn.cursor()
cursor.execute(create_employee_log_table)
cursor.execute(create_Manager_log_table)
cursor.execute(create_Cashier_log_table)
cursor.execute(create_ChefLog_log_table)
cursor.execute(create_Order_log_table)
cursor.execute(create_Makes_order_log_table)
cursor.execute(create_Receive_order_log_table)
cursor.execute(create_Transaction_order_log_table)
cursor.execute(create_Customer_order_log_table)

cursor.execute(create_Table_order_log_table)
cursor.execute(create_DessertItems_log_table)
cursor.execute(create_Entreeitems_log_table)
cursor.execute(create_Appetizeritems_log_table)


create_insert_trigger = """
CREATE TRIGGER trg_Insert_Employee
ON Employee
AFTER INSERT
AS
BEGIN
    INSERT INTO EmployeeLog (
        operation,
        ssn,
        home_address,
        date_of_birth,
        salary,
        first_name,
        last_name
    )
    SELECT 
        'INSERT', 
        i.ssn,
        i.home_address,
        i.date_of_birth,
        i.salary,
        i.first_name,
        i.last_name
        
    FROM 
        inserted i;
    
END;
"""

create_update_trigger = """  
CREATE TRIGGER trg_update_Employee
ON Employee
AFTER UPDATE
AS
BEGIN
    INSERT INTO EmployeeLog (
        operation,
        ssn,
        home_address,
        date_of_birth,
        salary,
        first_name,
        last_name,
        old_home_address,
        old_date_of_birth,
        old_salary,
        old_first_name,
        old_last_name
    )
    SELECT 
        'Update', 
        i.ssn,
        i.home_address,
        i.date_of_birth,
        i.salary,
        i.first_name,
        i.last_name,
        d.home_address,
        d.date_of_birth,
        d.salary,
        d.first_name,
        d.last_name
    FROM 
        inserted i 
    INNER JOIN
        Deleted d on i.ssn = d.ssn
    
END;
"""

create_delete_trigger = """
CREATE TRIGGER trg_Delete_Employee
ON Employee
AFTER DELETE
AS
BEGIN
    INSERT INTO EmployeeLog (
        operation,
        ssn,
        home_address,
        date_of_birth,
        salary,
        first_name,
        last_name,
        old_home_address,
        old_date_of_birth,
        old_salary,
        old_first_name,
        old_last_name
    )
    SELECT 
        'DELETE', 
        d.ssn,
        d.home_address,
        d.date_of_birth,
        d.salary,
        d.first_name,
        d.last_name,
        d.home_address,
        d.date_of_birth,
        d.salary,
        d.first_name,
        d.last_name
    FROM 
        deleted d;
END;
"""

cursor.execute(create_insert_trigger)
cursor.execute(create_update_trigger)
cursor.execute(create_delete_trigger)

create_insert_trigger_manager = """
CREATE TRIGGER trg_Insert_Manager
ON Manager
AFTER INSERT
AS
BEGIN
    INSERT INTO ManagerLog (
        operation,
        manager_id,
        employee_id
    )
    SELECT 
        'INSERT', 
        i.id,
        i.id
    FROM 
        inserted i;
END;
"""
create_update_trigger_manager = """  
CREATE TRIGGER trg_update_Manager
ON Manager
AFTER UPDATE
AS
BEGIN
    INSERT INTO ManagerLog (
        operation,
        manager_id,
        employee_id,
        old_manager_id,
        old_employee_id
    )
    SELECT 
        'UPDATE', 
        i.id,
        i.employee_id,
        d.id,
        d.employee_id
    FROM 
        inserted i
    INNER JOIN
        Deleted d on i.id = d.id
    
END;
"""

create_delete_trigger_manager = """
CREATE TRIGGER trg_Delete_Manager
ON Manager
AFTER DELETE
AS
BEGIN
    INSERT INTO ManagerLog (
        operation,
        manager_id,
        employee_id,
        old_manager_id,
        old_employee_id
    )
    SELECT 
        'DELETE', 
        d.id,
        d.employee_id,
        d.id,
        d.employee_id
    FROM 
        deleted d;
END;
"""
cursor.execute(create_insert_trigger_manager)
cursor.execute(create_update_trigger_manager)
cursor.execute(create_delete_trigger_manager)


create_cashier_trigger = """
CREATE TRIGGER trg_Insert_Cashier
ON Cashier
AFTER INSERT
AS
BEGIN
    INSERT INTO CashierLog (
        operation,
        cashier_id,
        employee_id,
        counter_id
    )
    SELECT 
        'INSERT', 
        i.id,
        i.employee_id,
        i.counter_id
    FROM 
        inserted i;
END;
"""
create_update_trigger_cashier = """  
CREATE TRIGGER trg_update_cashier
ON Cashier
AFTER UPDATE
AS
BEGIN
    INSERT INTO CashierLog (
        operation,
        cashier_id,
        employee_id,
        counter_id,
        old_cashier_id,
        old_employee_id,
        old_counter_id
    )
    SELECT 
        'UPDATE', 
        i.id,
        i.employee_id,
        i.counter_id,
        d.id,
        d.employee_id,
        d.counter_id
    FROM 
        inserted i
    INNER JOIN
        Deleted d on i.id = d.id
    
END;
"""
create_delete_trigger_cashier = """
CREATE TRIGGER trg_Delete_Cashier
ON Cashier
AFTER DELETE
AS
BEGIN
    INSERT INTO CashierLog (
        operation,
        cashier_id,
        employee_id,
        counter_id,
        old_cashier_id,
        old_employee_id,
        old_counter_id
    )
    SELECT 
        'DELETE', 
        d.id,
        d.employee_id,
        d.counter_id,
        d.id,
        d.employee_id,
        d.counter_id
    FROM 
        deleted d;
END;
"""

cursor.execute(create_cashier_trigger)
cursor.execute(create_update_trigger_cashier)
cursor.execute(create_delete_trigger_cashier)

create_chef_trigger = """
CREATE TRIGGER trg_Insert_Chef
ON Chef
AFTER INSERT
AS
BEGIN
    INSERT INTO ChefLog (
        operation,
        chef_id,
        employee_id
        )
    SELECT 
        'INSERT', 
        i.id,
        i.employee_id
    FROM 
        inserted i;
END;
"""

create_update_trigger_chef = """  
CREATE TRIGGER trg_update_Chef
ON Chef
AFTER UPDATE
AS
BEGIN
    INSERT INTO ChefLog (
        operation,
        chef_id,
        employee_id,
        old_chef_id,
        old_employee_id
        )
    SELECT 
        'UPDATE', 
        i.id,
        i.employee_id,
        d.id,
        d.employee_id
    FROM 
        inserted i
    INNER JOIN
        Deleted d on i.id = d.id
    
END;
"""
create_delete_trigger_chef = """
CREATE TRIGGER trg_Delete_Chef
ON Chef
AFTER DELETE
AS
BEGIN
    INSERT INTO ChefLog (
        operation,
        chef_id,
        employee_id,
        old_chef_id,
        old_employee_id
    )
    SELECT 
        'DELETE', 
        d.id,
        d.employee_id,
        d.id,
        d.employee_id
    FROM 
        deleted d;
END;
"""

cursor.execute(create_chef_trigger)
cursor.execute(create_update_trigger_chef)
cursor.execute(create_delete_trigger_chef)


create_insert_trigger_order = """
CREATE TRIGGER trg_Insert_Order
ON [Order]
AFTER INSERT
AS
BEGIN
    INSERT INTO OrderLog (
        operation,
        order_id,
        table_id,
        is_paid,
        price,
        counter_id,
        date
    )
    SELECT 
        'INSERT', 
        i.id,
        i.table_id,
        i.is_paid,
        i.price,
        i.counter_id,
        i.date
    FROM 
        inserted i;
END;
"""
create_update_trigger_order = """  
CREATE TRIGGER trg_update_order
ON [Order]
AFTER UPDATE
AS
BEGIN
    INSERT INTO OrderLog (
        operation,
        order_id,
        table_id,
        is_paid,
        price,
        counter_id,
        date,
        old_order_id,
        old_table_id,
        old_is_paid,
        old_price,
        old_counter_id,
        old_date
    )
    SELECT 
        'UPDATE', 
        i.id,
        i.table_id,
        i.is_paid,
        i.price,
        i.counter_id,
        i.date,
        d.id,
        d.table_id,
        d.is_paid,
        d.price,
        d.counter_id,
        d.date
    FROM 
        inserted i
    INNER JOIN
        Deleted d on i.id = d.id
    
END;
"""
create_delete_trigger_order = """
CREATE TRIGGER trg_Delete_Order
ON [Order]
AFTER DELETE
AS
BEGIN
    INSERT INTO OrderLog (
        operation,
        order_id,
        table_id,
        is_paid,
        price,
        counter_id,
        date,
        old_order_id,
        old_table_id,
        old_is_paid,
        old_price,
        old_counter_id,
        old_date
    )
    SELECT 
        'DELETE', 
        d.id,
        d.table_id,
        d.is_paid,
        d.price,
        d.counter_id,
        d.date,
        d.id,
        d.table_id,
        d.is_paid,
        d.price,
        d.counter_id,
        d.date
    FROM 
        deleted d;
END;
"""
cursor.execute(create_update_trigger_order)
cursor.execute(create_insert_trigger_order)
cursor.execute(create_delete_trigger_order)


create_insert_trigger_makes_order = """
CREATE TRIGGER trg_Insert_Makes_order
ON Makes_order
AFTER INSERT
AS
BEGIN
    INSERT INTO Makes_orderLog (
        operation,
        customer_id,
        order_id,
        transaction_id
    )
    SELECT 
        'INSERT', 
        i.customer_id,
        i.order_id,
        i.transaction_id
    FROM 
        inserted i;
END;
"""
create_update_trigger_makes_order = """  
CREATE TRIGGER trg_update_makes_order
ON Makes_order
AFTER UPDATE
AS
BEGIN
    INSERT INTO Makes_orderLog (
        operation,
        customer_id,
        order_id,
        transaction_id,
        old_customer_id,
        old_order_id,
        old_transaction_id
    )
    SELECT 
        'UPDATE', 
        i.customer_id,
        i.order_id,
        i.transaction_id,
        d.customer_id,
        d.order_id,
        d.transaction_id
    FROM 
        inserted i
    INNER JOIN
        Deleted d on i.order_id = d.order_id and i.customer_id = d.customer_id and i.transaction_id = d.transaction_id
    
END;
"""
create_delete_trigger_makes_order = """
CREATE TRIGGER trg_Delete_Makes_order
ON Makes_order
AFTER DELETE
AS
BEGIN
    INSERT INTO Makes_orderLog (
        operation,
        customer_id,
        order_id,
        transaction_id,
        old_customer_id,
        old_order_id,
        old_transaction_id
    )
    SELECT 
        'DELETE', 
        d.customer_id,
        d.order_id,
        d.transaction_id,
        d.customer_id,
        d.order_id,
        d.transaction_id
    FROM 
        deleted d;
END;
"""

cursor.execute(create_insert_trigger_makes_order)
cursor.execute(create_update_trigger_makes_order)
cursor.execute(create_delete_trigger_makes_order)

create_insert_trigger_receive_order = """
CREATE TRIGGER trg_Insert_Receive_order
ON Receive_order
AFTER INSERT
AS
BEGIN
    INSERT INTO Receive_orderLog (
        operation,
        chef_id,
        waiter_id,
        order_id
    )
    SELECT 
        'INSERT', 
        i.chef_id,
        i.waiter_id,
        i.order_id
    FROM 
        inserted i;
END;
"""

create_update_trigger_receive_order = """
CREATE TRIGGER trg_update_Receive_order
ON Receive_order
AFTER UPDATE
AS
BEGIN
    INSERT INTO Receive_orderLog (
        operation,
        chef_id,
        waiter_id,
        order_id,
        old_chef_id,
        old_waiter_id,
        old_order_id
    )
    SELECT 
        'UPDATE', 
        i.chef_id,
        i.waiter_id,
        i.order_id,
        d.chef_id,
        d.waiter_id,
        d.order_id
    FROM 
        inserted i
    INNER JOIN
        Deleted d on i.chef_id = d.chef_id and i.waiter_id = d.waiter_id and i.order_id = d.order_id
END;
"""

create_delete_trigger_receive_order = """
CREATE TRIGGER trg_Delete_Receive_order
ON Receive_order
AFTER DELETE
AS
BEGIN
    INSERT INTO Receive_orderLog (
        operation,
        chef_id,
        waiter_id,
        order_id,
        old_chef_id,
        old_waiter_id,
        old_order_id
    )
    SELECT 
        'DELETE', 
        d.chef_id,
        d.waiter_id,
        d.order_id,
        d.chef_id,
        d.waiter_id,
        d.order_id
    FROM 
        deleted d;
END;
"""

cursor.execute(create_insert_trigger_receive_order)
cursor.execute(create_update_trigger_receive_order)
cursor.execute(create_delete_trigger_receive_order)


create_insert_trigger_transaction = """
CREATE TRIGGER trg_Insert_Transaction
ON [Transaction]
AFTER INSERT
AS
BEGIN
    INSERT INTO TransactionLog (
        operation,
        transaction_id,
        type,
        discount,
        counter_id
    )
    SELECT 
        'INSERT', 
        i.id,
        i.type,
        i.discount,
        i.counter_id
    FROM 
        inserted i;
END;
"""

create_update_trigger_transaction = """
CREATE TRIGGER trg_update_Transaction
ON [Transaction]
AFTER UPDATE
AS
BEGIN
    INSERT INTO TransactionLog (
        operation,
        transaction_id,
        type,
        discount,
        counter_id,
        old_transaction_id,
        old_type,
        old_discount,
        old_counter_id
    )
    SELECT 
        'UPDATE', 
        i.id,
        i.type,
        i.discount,
        i.counter_id,
        d.id,
        d.type,
        d.discount,
        d.counter_id
    FROM 
        inserted i
    INNER JOIN
        Deleted d on i.counter_id = d.counter_id and i.id = d.id 
END;
"""
create_delete_trigger_transaction = """
CREATE TRIGGER trg_Delete_Transaction
ON [Transaction]
AFTER DELETE
AS
BEGIN
    INSERT INTO TransactionLog (
        operation,
        transaction_id,
        type,
        discount,
        counter_id,
        old_transaction_id,
        old_type,
        old_discount,
        old_counter_id
    )
    SELECT 
        'DELETE', 
        d.id,
        d.type,
        d.discount,
        d.counter_id,
        d.id,
        d.type,
        d.discount,
        d.counter_id
    FROM 
        deleted d;
END;
"""

cursor.execute(create_insert_trigger_transaction)
cursor.execute(create_update_trigger_transaction)
cursor.execute(create_delete_trigger_transaction)


create_insert_trigger_customer = """
CREATE TRIGGER trg_Insert_Customer
ON Customer
AFTER INSERT
AS
BEGIN
    INSERT INTO CustomerLog (
        operation,
        customer_id,
        first_name,
        last_name
    )
    SELECT 
        'INSERT', 
        i.Customer_id,
        i.First_name,
        i.Last_name
    FROM 
        inserted i;
END;
"""

create_update_trigger_customer = """
CREATE TRIGGER trg_update_Customer
ON Customer
AFTER UPDATE
AS
BEGIN
    INSERT INTO CustomerLog (
        operation,
        customer_id,
        first_name,
        last_name,
        old_customer_id,
        old_first_name,
        old_last_name
    )
    SELECT 
        'UPDATE', 
        i.Customer_id,
        i.First_name,
        i.Last_name,
        d.customer_id,
        d.first_name,
        d.last_name
    FROM 
        inserted i
    INNER JOIN
        Deleted d on i.customer_id = d.customer_id
    
END;
"""
create_delete_trigger_customer = """
CREATE TRIGGER trg_Delete_Customer
ON Customer
AFTER DELETE
AS
BEGIN
    INSERT INTO CustomerLog (
        operation,
        customer_id,
        first_name,
        last_name,
        old_customer_id,
        old_first_name,
        old_last_name
    )
    SELECT 
        'DELETE', 
        d.customer_id,
        d.first_name,
        d.last_name,
        d.customer_id,
        d.first_name,
        d.last_name
    FROM 
        deleted d;
END;
"""

cursor.execute(create_update_trigger_customer)
cursor.execute(create_insert_trigger_customer)
cursor.execute(create_delete_trigger_customer)

create_insert_trigger_table = """
CREATE TRIGGER trg_Insert_Table
ON [Table]
AFTER INSERT
AS
BEGIN
    INSERT INTO TableLog (
        operation,
        table_id,
        capacity,
        is_booked,
        waiter_id
    )
    SELECT 
        'INSERT', 
        i.id,
        i.capacity,
        i.is_booked,
        i.waiter_id
    FROM 
        inserted i;
END;
"""

create_update_trigger_table = """
CREATE TRIGGER trg_update_Table
ON [Table]
AFTER UPDATE
AS
BEGIN
    INSERT INTO TableLog (
        operation,
        table_id,
        capacity,
        is_booked,
        waiter_id,
        old_table_id,
        old_capacity,
        old_is_booked,
        old_waiter_id
    )
    SELECT 
        'UPDATE', 
        i.id,
        i.capacity,
        i.is_booked,
        i.waiter_id,
        d.id,
        d.capacity,
        d.is_booked,
        d.waiter_id
    FROM 
        inserted i
    INNER JOIN
        Deleted d on i.id = d.id
END;
"""
create_delete_trigger_table = """
CREATE TRIGGER trg_Delete_Table
ON [Table]
AFTER DELETE
AS
BEGIN
    INSERT INTO TableLog (
        operation,
        table_id,
        capacity,
        is_booked,
        waiter_id,
        old_table_id,
        old_capacity,
        old_is_booked,
        old_waiter_id
    )
    SELECT 
        'DELETE', 
        d.id,
        d.capacity,
        d.is_booked,
        d.waiter_id,
        d.id,
        d.capacity,
        d.is_booked,
        d.waiter_id
    FROM 
        deleted d;
END;
"""
cursor.execute(create_update_trigger_table)
cursor.execute(create_insert_trigger_table)
cursor.execute(create_delete_trigger_table)

create_insert_trigger_dessert_items = """
CREATE TRIGGER trg_Insert_DessertItems
ON dessert_items
AFTER INSERT
AS
BEGIN
    INSERT INTO DessertItemsLog (
        operation,
        dessert_item_id,
        name,
        price,
        recipe,
        description,
        menu_id
    )
    SELECT 
        'INSERT', 
        i.Id,
        i.name,
        i.price,
        i.recipe,
        i.description,
        i.menu_id
    FROM 
        inserted i;
END;
"""

create_update_trigger_dessert_items = """
CREATE TRIGGER trg_update_DessertItems
ON dessert_items
AFTER Update
AS
BEGIN
    INSERT INTO DessertItemsLog (
        operation,
        dessert_item_id,
        name,
        price,
        recipe,
        description,
        menu_id,
        old_dessert_item_id,
        old_name,
        old_price,
        old_recipe,
        old_description,
        old_menu_id
    )
    SELECT 
        'UPDATE', 
        i.Id,
        i.name,
        i.price,
        i.recipe,
        i.description,
        i.menu_id,
        d.Id,
        d.name,
        d.price,
        d.recipe,
        d.description,
        d.menu_id
    FROM 
        inserted i
    INNER JOIN
        Deleted d on i.Id = d.Id
END;
"""
create_delete_trigger_dessert_items = """
CREATE TRIGGER trg_Delete_DessertItems
ON dessert_items
AFTER DELETE
AS
BEGIN
    INSERT INTO DessertItemsLog (
        operation,
        dessert_item_id,
        name,
        price,
        recipe,
        description,
        menu_id,
        old_dessert_item_id,
        old_name,
        old_price,
        old_recipe,
        old_description,
        old_menu_id
    )
    SELECT 
        'DELETE', 
        d.Id,
        d.name,
        d.price,
        d.recipe,
        d.description,
        d.menu_id,
        d.Id,
        d.name,
        d.price,
        d.recipe,
        d.description,
        d.menu_id
    FROM 
        deleted d;
END;
"""
cursor.execute(create_update_trigger_dessert_items)
cursor.execute(create_insert_trigger_dessert_items)
cursor.execute(create_delete_trigger_dessert_items)

create_insert_trigger_Entree_items = """
CREATE TRIGGER trg_Insert_Entreeitems
ON Entree_items
AFTER INSERT
AS
BEGIN
    INSERT INTO EntreeitemsLog (
        operation,
        entree_item_id,
        name,
        price,
        recipe,
        description,
        menu_id
    )
    SELECT 
        'INSERT', 
        i.Id,
        i.name,
        i.price,
        i.recipe,
        i.description,
        i.menu_id
    FROM 
        inserted i;
END;
"""

create_update_trigger_Entree_items = """
CREATE TRIGGER trg_update_Entreeitems
ON Entree_items
AFTER UPDATE
AS
BEGIN
    INSERT INTO EntreeitemsLog (
        operation,
        entree_item_id,
        name,
        price,
        recipe,
        description,
        menu_id,
        old_entree_item_id,
        old_name,
        old_price,
        old_recipe,
        old_description,
        old_menu_id
    )
    SELECT 
        'UPDATE', 
        i.Id,
        i.name,
        i.price,
        i.recipe,
        i.description,
        i.menu_id,
        d.Id,
        d.name,
        d.price,
        d.recipe,
        d.description,
        d.menu_id
    FROM 
        inserted i
    INNER JOIN
        Deleted d on i.Id = d.Id
END;
"""
create_delete_trigger_entree_items = """
CREATE TRIGGER trg_Delete_EntreeItems
ON Entree_items
AFTER DELETE
AS
BEGIN
    INSERT INTO EntreeitemsLog (
        operation,
        entree_item_id,
        name,
        price,
        recipe,
        description,
        menu_id,
        old_entree_item_id,
        old_name,
        old_price,
        old_recipe,
        old_description,
        old_menu_id
    )
    SELECT 
        'DELETE', 
        d.Id,
        d.name,
        d.price,
        d.recipe,
        d.description,
        d.menu_id,
        d.Id,
        d.name,
        d.price,
        d.recipe,
        d.description,
        d.menu_id
    FROM 
        deleted d;
END;
"""

cursor.execute(create_update_trigger_Entree_items)
cursor.execute(create_insert_trigger_Entree_items)
cursor.execute(create_delete_trigger_entree_items)


create_insert_trigger_Appetizer_items = """
CREATE TRIGGER trg_Insert_Appetizeritems
ON Appetizer_items
AFTER INSERT
AS
BEGIN
    INSERT INTO AppetizeritemsLog (
        operation,
        appetizer_item_id,
        name,
        price,
        recipe,
        description,
        menu_id
    )
    SELECT 
        'INSERT', 
        i.Id,
        i.name,
        i.price,
        i.recipe,
        i.description,
        i.menu_id
    FROM 
        inserted i;
END;
"""
create_update_trigger_Appetizer_items = """
CREATE TRIGGER trg_update_Appetizeritems
ON Appetizer_items
AFTER UPDATE
AS
BEGIN
    INSERT INTO AppetizeritemsLog (
        operation,
        appetizer_item_id,
        name,
        price,
        recipe,
        description,
        menu_id,
        old_appetizer_item_id,
        old_name,
        old_price,
        old_recipe,
        old_description,
        old_menu_id
    )
    SELECT 
        'UPDATE', 
        i.Id,
        i.name,
        i.price,
        i.recipe,
        i.description,
        i.menu_id,
        d.Id,
        d.name,
        d.price,
        d.recipe,
        d.description,
        d.menu_id
    FROM 
        inserted i
    INNER JOIN
        Deleted d on i.Id = d.Id
END;
"""
create_delete_trigger_appetizer_items = """
CREATE TRIGGER trg_Delete_AppetizerItems
ON Appetizer_items
AFTER DELETE
AS
BEGIN
    INSERT INTO AppetizeritemsLog (
        operation,
        appetizer_item_id,
        name,
        price,
        recipe,
        description,
        menu_id,
        old_appetizer_item_id,
        old_name,
        old_price,
        old_recipe,
        old_description,
        old_menu_id
    )
    SELECT 
        'DELETE', 
        d.Id,
        d.name,
        d.price,
        d.recipe,
        d.description,
        d.menu_id,
        d.Id,
        d.name,
        d.price,
        d.recipe,
        d.description,
        d.menu_id
    FROM 
        deleted d;
END;
"""

cursor.execute(create_update_trigger_Appetizer_items)
cursor.execute(create_insert_trigger_Appetizer_items)
cursor.execute(create_delete_trigger_appetizer_items)


conn.commit()
