#Amanda New

#Katie Hilliard
#Keanu Foltz
#Amit Rizal

import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'root',
    'password': 'Gimmethembuns1!Manbob613!', 
    'host': '127.0.0.1',  # Replace with your host if not localhost
}

database_name = "BacchusWine"

def create_database(cursor):
    try:
        cursor.execute(f"CREATE DATABASE {database_name}")
        print(f"{database_name} database was established")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print(f"{database_name} already exists")
        else:
            print(f"Database not created: {err}, please try again!")
            exit(1)

sql_schema = [

    "DROP TABLE IF EXISTS DeptQuarterReport;",
    "DROP TABLE IF EXISTS Employee;",
    "DROP TABLE IF EXISTS Department;",
    "DROP TABLE IF EXISTS SupplyQuarterReport;",
    "DROP TABLE IF EXISTS SupplyShipment;",
    "DROP TABLE IF EXISTS Supplier;",
    "DROP TABLE IF EXISTS SalesQuarterReport;",
    "DROP TABLE IF EXISTS DistQuarterReport;",
    "DROP TABLE IF EXISTS Reports;",
    "DROP TABLE IF EXISTS Orders;",
    "DROP TABLE IF EXISTS Wine;",
    "DROP TABLE IF EXISTS Distributor;",
    """
    CREATE TABLE Distributor (
        DistributorID INT PRIMARY KEY AUTO_INCREMENT,
        DistributorName VARCHAR(100) NOT NULL,
        ContactInfo TEXT
    );
    """,
    """
    CREATE TABLE Wine (
        WineID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        WineName VARCHAR(255) NOT NULL,
        Inventory INT
    );
    """,
    """
    CREATE TABLE Orders (
        OrderID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        WineID INT,
        DistributorID INT
    );
    """,
    """
    CREATE TABLE Reports (
        ReportID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        ReportType VARCHAR(255) NOT NULL 
    );
    """,
    """
    CREATE TABLE DistQuarterReport (
        DistQuarterID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        ReportID INT NOT NULL,
        DistributorID INT,
        WineID INT,
        BottlesSold INT
    );
    """,
    """
    CREATE TABLE SalesQuarterReport (
        SalesQuarterID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        ReportID INT,
        WineID INT,
        BottlesSoldQuarter INT,
        BottlesSoldTotal INT
    );
    """,
    """
    CREATE TABLE Supplier (
        SupplierID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        SupplierName VARCHAR(100) NOT NULL,
        ContactInfo VARCHAR(255) NOT NULL
    );
    """,
    """
    CREATE TABLE SupplyShipment (
        SupplyShipmentID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        Type VARCHAR(255),
        SupplierID INT,
        ExpectedDelivery DATE NOT NULL,
        ActualDelivery DATE NOT NULL,
        DeliveryGap INT,
        Inventory INT
    );
    """,
    """
    CREATE TABLE SupplyQuarterReport (
        SupQuarterReportID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        ReportID INT,
        SupplierID INT,
        SupplyID INT,
        AverageDeliveryGap INT,
        InventoryTotal INT
    );
    """,
    """
    CREATE TABLE Department (
        DepartmentID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        DepartmentName VARCHAR(255) NOT NULL
    );
    """,
    """
    CREATE TABLE Employee (
        EmployeeID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        FirstName VARCHAR(255) NOT NULL,
        LastName VARCHAR(255) NOT NULL,
        DepartmentID INT,
        Role VARCHAR(255) NOT NULL,
        HoursWorked INT
    );
    """,
    """
    CREATE TABLE DeptQuarterReport (
        DeptQuarterID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        ReportID INT,
        DepartmentID INT,
        HoursWorked INT
    );
    """
]

foreign_key = [
    """
    ALTER TABLE Orders
    ADD FOREIGN KEY (WineID) REFERENCES Wine(WineID),
    ADD FOREIGN KEY (DistributorID) REFERENCES Distributor(DistributorID);
    """,
    """
    ALTER TABLE DistQuarterReport
    ADD FOREIGN KEY (WineID) REFERENCES Wine(WineID),
    ADD FOREIGN KEY (ReportID) REFERENCES Reports(ReportID),
    ADD FOREIGN KEY (DistributorID) REFERENCES Distributor(DistributorID);
    """,
    """
    ALTER TABLE SalesQuarterReport
    ADD FOREIGN KEY (ReportID) REFERENCES Reports(ReportID),
    ADD FOREIGN KEY (WineID) REFERENCES Wine(WineID);
    """,
    """
    ALTER TABLE SupplyShipment
    ADD FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID);
    """,
    """
    ALTER TABLE SupplyQuarterReport
    ADD FOREIGN KEY (ReportID) REFERENCES Reports(ReportID),
    ADD FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID);
    """,
    """
    ALTER TABLE Employee
    ADD FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID);
    """

]

distributor = [
    (1, "Wine Distributor A", "contactA@example.com"),
    (2, "Wine Distributor A", "contactA@example.com")
]

wine = [
    (1, "Red Wine", 50),
    (2, "White Wine", 30)
]

orders = [
    (1,1,1),
    (2,2,2)
]

reports = [
    (1, "Distributor Report"),
    (2, "Sales Report")
]

distquarterreport = [
    (1, 1, 1, 1, 20),
    (2, 1, 2, 2, 15)
]

salesquarterreport = [
    (1, 2, 1, 20, 100),
    (2, 2, 2, 15, 80)
]

supplier = [
    (1, "Supplier A", "supplierA@example.com"),
    (2, "Supplier B", "supplierB@example.com")
]

supplyshipment = [
    (1, "Type A", 1, "2024-1-1", "2024-1-2", 1, 100),
    (2, "Type B", 2, "2024-1-5", "2024-1-6", 1, 50)
]

supplyquarterreport = [
    (1, 3, 1, 17, 5, 1),
    (2, 4, 2, 18, 6, 2)
]

department = [
    (1, "Sales"),
    (2, "Operations")
]

employee = [
    (1, "John", "Doe", 1, "Manager", 40),
    (2, "Jane", "Smith", 2, "Analyst", 35)
]

deptquarterreport = [
    (1, 2, 3, 4),
    (5, 6, 7, 8)
]

try:
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # Create database if it doesn't exist
    create_database(cursor)

    # Switch to the new database
    connection.database = database_name

    # Execute the schema (tables and foreign keys)
    for statement in sql_schema:
        cursor.execute(statement)
    
    for fk in foreign_key:
        cursor.execute(fk, multi=True)

    # Insert data into the tables
    cursor.executemany("INSERT INTO Distributor (DistributorID, DistributorName, ContactInfo) VALUES (%s, %s, %s);", distributor)
    cursor.executemany("INSERT INTO Wine (WineID, WineName, Inventory) VALUES (%s, %s, %s);", wine)
    cursor.executemany("INSERT INTO Orders (OrderID, WineID, DistributorID) VALUES (%s, %s, %s);", orders)
    cursor.executemany("INSERT INTO Reports (ReportID, ReportType) VALUES (%s, %s);", reports)
    cursor.executemany("INSERT INTO DistQuarterReport (DistQuarterID, ReportID, DistributorID, WineID, BottlesSold) VALUES (%s, %s, %s, %s, %s);", distquarterreport)
    cursor.executemany("INSERT INTO SalesQuarterReport (SalesQuarterID, ReportID, WineID, BottlesSoldQuarter, BottlesSoldTotal) VALUES (%s, %s, %s, %s, %s);", salesquarterreport)
    cursor.executemany("INSERT INTO Supplier (SupplierID, SupplierName, ContactInfo) VALUES (%s, %s, %s);", supplier)
    cursor.executemany("INSERT INTO SupplyShipment (SupplyShipmentID, Type, SupplierID, ExpectedDelivery, ActualDelivery, DeliveryGap, Inventory) VALUES (%s, %s, %s, %s, %s, %s, %s);", supplyshipment)
    cursor.executemany("INSERT INTO SupplyQuarterReport (SupQuarterReportID, ReportID, SupplierID, SupplyID, AverageDeliveryGap, InventoryTotal) VALUES (%s, %s, %s, %s, %s, %s);", supplyquarterreport)
    cursor.executemany("INSERT INTO Department (DepartmentID, DepartmentName) VALUES (%s, %s);", department)
    cursor.executemany("INSERT INTO Employee (EmployeeID, FirstName, LastName, DepartmentID, Role, HoursWorked) VALUES (%s, %s, %s, %s, %s, %s);", employee)
    cursor.executemany("INSERT INTO DeptQuarterReport (DeptQuarterID, ReportID, DepartmentID, HoursWorked) VALUES (%s, %s, %s, %s);", deptquarterreport)

    connection.commit()
    print("All data inserted into tables successfully.")

    # Fetch and print all tables in the database
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()

    print("\nSHOW TABLES:")
    for table in tables:
        print(f"- {table[0]}")

    print("\nTable Content:")

    # For each table, select and display its contents
    for table in tables:
        table_name = table[0]
        print(f"\nTable: {table_name}")
        
        # Fetch all rows from the current table
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()

        # Get column names
        cursor.execute(f"DESCRIBE {table_name};")
        columns = cursor.fetchall()
        column_names = [column[0] for column in columns]

        # Print column names
        print(f"Columns: {', '.join(column_names)}")

        # Print rows
        if rows:
            for row in rows:
                print(row)
        else:
            print("No data found.")


except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()