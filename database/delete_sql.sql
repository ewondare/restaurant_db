-- Deleting an employee
CREATE PROCEDURE DeleteEmployee(IN empSSN VARCHAR(11))
BEGIN
    DELETE FROM Waiter WHERE Employee_id = empSSN;
    DELETE FROM Chef WHERE Employee_id = empSSN;
    DELETE FROM Cashier WHERE Employee_id = empSSN;
    DELETE FROM Manager WHERE Employee_id = empSSN;
    DELETE FROM Employee WHERE SSN = empSSN;
END;

-- deleting a menu item
CREATE PROCEDURE DeleteMenu(IN menuId INT)
BEGIN
    DELETE FROM Appetizer_item WHERE menu_id = menuId;
    DELETE FROM Desert_item WHERE menu_id = menuId;
    DELETE FROM Entree_item WHERE menu_id = menuId;
    DELETE FROM Menu WHERE Id = menuId;
END;

-- deleting a table dine
CREATE PROCEDURE DeleteTableDine(IN tableId INT)
BEGIN
    DELETE FROM Booking WHERE Table_dine_id_ref = tableId;
    DELETE FROM Order_food WHERE table_id_ref = tableId;
    DELETE FROM Deliver_food WHERE Table_dine_id_ref = tableId;
    DELETE FROM Table_dine WHERE Id = tableId;
END;

-- deleting a customer
CREATE PROCEDURE DeleteCustomer(IN customerId INT)
BEGIN
    DELETE FROM Booking WHERE Customer_id_ref = customerId;
    DELETE FROM Makes_order WHERE Customer_id_ref = customerId;
    DELETE FROM Customer WHERE Customer_id = customerId;
END;

-- deleting an order
CREATE PROCEDURE DeleteOrder(IN orderId INT)
BEGIN
    DELETE FROM Appetizer_order WHERE order_id = orderId;
    DELETE FROM Desert_order WHERE order_id = orderId;
    DELETE FROM Entree_order WHERE order_id = orderId;
    DELETE FROM Makes_order WHERE Order_id_ref = orderId;
    DELETE FROM Order_food WHERE Order_id = orderId;
END;

-- deleting a counter
CREATE PROCEDURE DeleteCounter(IN counterId INT)
BEGIN
    DELETE FROM Cashier WHERE Counter_id = counterId;
    DELETE FROM Transaction_ WHERE Counter_id_ref = counterId;
    DELETE FROM Counter WHERE Id = counterId;
END;
