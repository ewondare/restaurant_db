-- Deleting an employee
CREATE PROCEDURE DeleteEmployee(IN empSSN VARCHAR(11))
BEGIN
    DELETE FROM Waiter WHERE Employee_id = empSSN;
    SELECT 'Deleted from Waiter' AS Status, * FROM Waiter;

    DELETE FROM Chef WHERE Employee_id = empSSN;
    SELECT 'Deleted from Chef' AS Status, * FROM Chef;

    DELETE FROM Cashier WHERE Employee_id = empSSN;
    SELECT 'Deleted from Cashier' AS Status, * FROM Cashier;

    DELETE FROM Manager WHERE Employee_id = empSSN;
    SELECT 'Deleted from Manager' AS Status, * FROM Manager;

    DELETE FROM Employee WHERE SSN = empSSN;
    SELECT 'Deleted from Employee' AS Status, * FROM Employee;
END;

-- deleting a menu item
CREATE PROCEDURE DeleteMenu(IN menuId INT)
BEGIN
    DELETE FROM Appetizer_item WHERE menu_id = menuId;
    SELECT 'Deleted from Appetizer_item' AS Status, * FROM Appetizer_item;

    DELETE FROM Desert_item WHERE menu_id = menuId;
    SELECT 'Deleted from Desert_item' AS Status, * FROM Desert_item;

    DELETE FROM Entree_item WHERE menu_id = menuId;
    SELECT 'Deleted from Entree_item' AS Status, * FROM Entree_item;

    DELETE FROM Menu WHERE Id = menuId;
    SELECT 'Deleted from Menu' AS Status, * FROM Menu;
END;

-- deleting a table dine
CREATE PROCEDURE DeleteTableDine(IN tableId INT)
BEGIN
    DELETE FROM Booking WHERE Table_dine_id_ref = tableId;
    SELECT 'Deleted from Booking' AS Status, * FROM Booking;

    DELETE FROM Order_food WHERE table_id_ref = tableId;
    SELECT 'Deleted from Order_food' AS Status, * FROM Order_food;

    DELETE FROM Deliver_food WHERE Table_dine_id_ref = tableId;
    SELECT 'Deleted from Deliver_food' AS Status, * FROM Deliver_food;

    DELETE FROM Table_dine WHERE Id = tableId;
    SELECT 'Deleted from Table_dine' AS Status, * FROM Table_dine;
END;

-- deleting a customer
CREATE PROCEDURE DeleteCustomer(IN customerId INT)
BEGIN
    DELETE FROM Booking WHERE Customer_id_ref = customerId;
    SELECT 'Deleted from Booking' AS Status, * FROM Booking;

    DELETE FROM Makes_order WHERE Customer_id_ref = customerId;
    SELECT 'Deleted from Makes_order' AS Status, * FROM Makes_order;

    DELETE FROM Customer WHERE Customer_id = customerId;
    SELECT 'Deleted from Customer' AS Status, * FROM Customer;
END;

-- deleting an order
CREATE PROCEDURE DeleteOrder(IN orderId INT)
BEGIN
    DELETE FROM Appetizer_order WHERE order_id = orderId;
    SELECT 'Deleted from Appetizer_order' AS Status, * FROM Appetizer_order;

    DELETE FROM Desert_order WHERE order_id = orderId;
    SELECT 'Deleted from Desert_order' AS Status, * FROM Desert_order;

    DELETE FROM Entree_order WHERE order_id = orderId;
    SELECT 'Deleted from Entree_order' AS Status, * FROM Entree_order;

    DELETE FROM Makes_order WHERE Order_id_ref = orderId;
    SELECT 'Deleted from Makes_order' AS Status, * FROM Makes_order;

    DELETE FROM Order_food WHERE Order_id = orderId;
    SELECT 'Deleted from Order_food' AS Status, * FROM Order_food;
END;

-- deleting a counter
CREATE PROCEDURE DeleteCounter(IN counterId INT)
BEGIN
    DELETE FROM Cashier WHERE Counter_id = counterId;
    SELECT 'Deleted from Cashier' AS Status, * FROM Cashier;

    DELETE FROM Transaction_ WHERE Counter_id_ref = counterId;
    SELECT 'Deleted from Transaction_' AS Status, * FROM Transaction_;

    DELETE FROM Counter WHERE Id = counterId;
    SELECT 'Deleted from Counter' AS Status, * FROM Counter;
END;
