-- updating employee
CREATE PROCEDURE UpdateEmployee(
    IN empSSN VARCHAR(11),
    IN newFirstName VARCHAR(50),
    IN newLastName VARCHAR(50),
    IN newHomeAddress TEXT,
    IN newDateOfBirth DATE,
    IN newSalary DECIMAL(15, 2)
)
BEGIN
    UPDATE Employee
    SET 
        First_Name = newFirstName,
        Last_Name = newLastName,
        Home_Address = newHomeAddress,
        Date_Of_Birth = newDateOfBirth,
        Salary = newSalary
    WHERE SSN = empSSN;

    SELECT 'Updated Employee' AS Status, * FROM Employee WHERE SSN = empSSN;
END;

-- updating menu
CREATE PROCEDURE UpdateMenu(
    IN menuId INT,
    IN newTitle TEXT,
    IN newSummary TEXT,
    IN newIsAvailable BOOLEAN
)
BEGIN
    UPDATE Menu
    SET 
        title = newTitle,
        summery = newSummary,
        is_availaible = newIsAvailable
    WHERE Id = menuId;

    SELECT 'Updated Menu' AS Status, * FROM Menu WHERE Id = menuId;
END;

-- updating table_dine
CREATE PROCEDURE UpdateTableDine(
    IN tableId INT,
    IN newCapacity INT,
    IN newIsAvailable BOOLEAN,
    IN newWaiterIdRef INT
)
BEGIN
    UPDATE Table_dine
    SET 
        capacity = newCapacity,
        Is_available = newIsAvailable,
        Waiter_id_ref = newWaiterIdRef
    WHERE Id = tableId;

    SELECT 'Updated Table_dine' AS Status, * FROM Table_dine WHERE Id = tableId;
END;

-- updating customer
CREATE PROCEDURE UpdateCustomer(
    IN customerId INT,
    IN newFirstName VARCHAR(50),
    IN newLastName VARCHAR(50)
)
BEGIN
    UPDATE Customer
    SET 
        First_name = newFirstName,
        last_name = newLastName
    WHERE Customer_id = customerId;

    SELECT 'Updated Customer' AS Status, * FROM Customer WHERE Customer_id = customerId;
END;

-- updating order
CREATE PROCEDURE UpdateOrder(
    IN orderId INT,
    IN newTableCondition TEXT,
    IN newIsPaid BOOLEAN,
    IN newPrice DOUBLE,
    IN newOrderDate DATE,
    IN newTableIdRef INT
)
BEGIN
    UPDATE Order_food
    SET 
        Table_condition = newTableCondition,
        is_paid = newIsPaid,
        price = newPrice,
        order_date = newOrderDate,
        table_id_ref = newTableIdRef
    WHERE Order_id = orderId;

    SELECT 'Updated Order_food' AS Status, * FROM Order_food WHERE Order_id = orderId;
END;

-- updating counter
CREATE PROCEDURE UpdateCounter(
    IN counterId INT,
    IN newId INT
)
BEGIN
    UPDATE Counter
    SET 
        Id = newId
    WHERE Id = counterId;

    SELECT 'Updated Counter' AS Status, * FROM Counter WHERE Id = newId;
END;
