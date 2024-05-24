-- insert menu item
CREATE PROCEDURE InsertMenuItem(
    IN itemName VARCHAR(255),
    IN itemType VARCHAR(50), -- Example: 'Appetizer', 'Entree', 'Dessert'
    IN price DECIMAL(10, 2),
    IN menuId INT
)
BEGIN
    DECLARE itemId INT;

    IF itemType = 'Appetizer' THEN
        INSERT INTO Appetizer_item (item_name, price, menu_id) 
        VALUES (itemName, price, menuId);
        SET itemId = LAST_INSERT_ID();
    ELSEIF itemType = 'Entree' THEN
        INSERT INTO Entree_item (item_name, price, menu_id) 
        VALUES (itemName, price, menuId);
        SET itemId = LAST_INSERT_ID();
    ELSEIF itemType = 'Dessert' THEN
        INSERT INTO Dessert_item (item_name, price, menu_id) 
        VALUES (itemName, price, menuId);
        SET itemId = LAST_INSERT_ID();
    END IF;
    
    SELECT itemId AS New_Item_Id;
END;

-- inserting new order
CREATE PROCEDURE InsertOrderDetails(
    IN p_order_id INT,
    IN p_table_id INT,
    IN p_is_paid BOOLEAN,
    IN p_date DATE,
    IN p_price FLOAT,
    IN p_waiter_id INT,
    IN p_chef_id INT,
    IN p_customer_id INT,
    IN p_transaction_id INT,
    IN p_discount BOOLEAN
)
BEGIN
    DECLARE v_statues_bool BOOL;
    DECLARE v_statues_bool_discount BOOL;
    
    -- if the order is paid
    IF p_is_paid = 0 THEN
        SET v_statues_bool = FALSE;
    ELSE
        SET v_statues_bool = TRUE;
    END IF;

    -- if a discount is applied
    IF p_discount = 0 THEN
        SET v_statues_bool_discount = FALSE;
    ELSE
        SET v_statues_bool_discount = TRUE;
    END IF;
    
    -- insert into Order_food table
    INSERT INTO Order_food (Order_id, Table_condition, is_paid, price, order_date, table_id_ref)
    VALUES (p_order_id, 'state of art', v_statues_bool, p_price, p_date, p_table_id)
    ON DUPLICATE KEY UPDATE Order_id = p_order_id;

    -- insert into Makes_order table
    INSERT INTO Makes_order (Customer_id_ref, Order_id_ref, Transaction_id_ref)
    VALUES (p_customer_id, p_order_id, p_transaction_id)
    ON DUPLICATE KEY UPDATE Customer_id_ref = p_customer_id, Transaction_id_ref = p_transaction_id;

    -- insert into Receive_order table
    INSERT INTO Receive_order (Chef_id_ref, Order_id_ref, Waiter_id_ref)
    VALUES (p_chef_id, p_order_id, p_waiter_id)
    ON DUPLICATE KEY UPDATE Chef_id_ref = p_chef_id, Waiter_id_ref = p_waiter_id;

    -- insert into Transaction_ table
    INSERT INTO Transaction_ (Id, Is_discounter, transaction_tyep, Counter_id_ref)
    VALUES (p_transaction_id, v_statues_bool_discount, 1, 1)
    ON DUPLICATE KEY UPDATE Is_discounter = v_statues_bool_discount;

    -- update Table_dine to mark the table as unavailable
    UPDATE Table_dine SET Is_available = FALSE WHERE Id = p_table_id;
END;


-- inserting new customer and transaction
CREATE PROCEDURE InsertCustomerTransaction(
    IN p_customer_id INT,
    IN p_first_name VARCHAR(255),
    IN p_last_name VARCHAR(255),
    IN p_transaction_id INT,
    IN p_discount BOOLEAN
)
BEGIN
    DECLARE v_statues_bool_discount BOOL;

    -- if a discount is applied
    IF p_discount = 0 THEN
        SET v_statues_bool_discount = FALSE;
    ELSE
        SET v_statues_bool_discount = TRUE;
    END IF;

    -- insert into Customer table
    INSERT INTO Customer (Customer_id, First_name, last_name)
    VALUES (p_customer_id, p_first_name, p_last_name)
    ON DUPLICATE KEY UPDATE First_name = p_first_name, last_name = p_last_name;

    -- insert into Transaction_ table
    INSERT INTO Transaction_ (Id, Is_discounter, transaction_tyep, Counter_id_ref)
    VALUES (p_transaction_id, v_statues_bool_discount, 2, 1)
    ON DUPLICATE KEY UPDATE Is_discounter = v_statues_bool_discount;
END;


-- Inserting a new counter
CREATE PROCEDURE InsertCounter(
    IN p_counter_id INT
)
BEGIN
    -- insert into Counter table
    INSERT INTO Counter (Id)
    VALUES (p_counter_id)
    ON DUPLICATE KEY UPDATE Id = p_counter_id;
END;


-- Inserting a new table
CREATE PROCEDURE InsertTable(
    IN p_table_id INT,
    IN p_capacity INT,
    IN p_is_booked BOOLEAN,
    IN p_waiter_id INT
)
BEGIN
    DECLARE v_statues_bool BOOL;

    -- if the table is booked
    IF p_is_booked = 0 THEN
        SET v_statues_bool = FALSE;
    ELSE
        SET v_statues_bool = TRUE;
    END IF;

    -- insert into Table_dine table
    INSERT INTO Table_dine (Id, capacity, Is_available, Waiter_id_ref)
    VALUES (p_table_id, p_capacity, v_statues_bool, p_waiter_id)
    ON DUPLICATE KEY UPDATE capacity = p_capacity, Is_available = v_statues_bool, Waiter_id_ref = p_waiter_id;
END;


-- inserting a new booking
CREATE PROCEDURE InsertBooking(
    IN p_customer_id INT,
    IN p_table_id INT,
    IN p_date DATE
)
BEGIN
    -- insert into Booking table
    INSERT INTO Booking (Customer_id_ref, Table_dine_id_ref, book_date)
    VALUES (p_customer_id, p_table_id, p_date);
END;

