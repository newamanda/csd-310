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
    "DROP TABLE IF EXISTS Role;",
    "DROP TABLE IF EXISTS SupplyInventory;",
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
        BottlesSold INT DEFAULT 0
    );
    """,
    """
    CREATE TABLE Orders (
        OrderID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        WineID INT,
        DistributorID INT,
        Inventory INT
    );
    """,
    #"""
    #CREATE TABLE Reports (
        #ReportID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        #ReportType VARCHAR(255) NOT NULL 
    #);
    #""",
    #"""
    #CREATE TABLE DistQuarterReport (
       # DistQuarterID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        #ReportID INT NOT NULL,
        #DistributorID INT,
        #WineID INT,
        #BottlesSold INT
    #);
    #""",
    #"""
    #CREATE TABLE SalesQuarterReport (
        #SalesQuarterID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        #ReportID INT,
        #WineID INT,
        #BottlesSoldQuarter INT,
        #BottlesSoldTotal INT
    #);
    #""",
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
        SupplierID INT,
        SupplyItemID INT,
        ExpectedDeliveryDate DATE NOT NULL,
        ActualDeliveryDate DATE NOT NULL,
        SupInventory INT
    );
    """,
    #"""
    #CREATE TABLE SupplyQuarterReport (
        #SupQuarterReportID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        #ReportID INT,
        #SupplierID INT,
        #SupplyID INT,
        #AverageDeliveryGap INT,
        #InventoryTotal INT
    #);
    #""",
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
        HoursQ1 INT,
        HoursQ2 INT,
        HoursQ3 INT,
        HoursQ4 INT
    );
    """,
    """
    CREATE TABLE SupplyInventory (
        SupplyItemID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        SupplyType VARCHAR(255),
        SupplierID INT,
        TotalInventory INT
    );
    """,
    """
    CREATE TABLE Role (
        RoleID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        RoleName VARCHAR(255) NOT NULL
    );
    """
    #"""
    #CREATE TABLE DeptQuarterReport (
       # DeptQuarterID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        #ReportID INT,
        #DepartmentID INT,
        #HoursWorked INT
    #);
    #"""
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
    ADD FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID),
    ADD FOREIGN KEY (SupplyItemID) REFERENCES SupplyItem(SupplyItemID);
    """,
    """
    ALTER TABLE SupplyQuarterReport
    ADD FOREIGN KEY (ReportID) REFERENCES Reports(ReportID),
    ADD FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID);
    """,
    """
    ALTER TABLE Employee
    ADD FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID);
    """,
    """
    ALTER TABLE SupplyInventory
    ADD FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID);
    """

]

distributor = [
    (51234, "Walmart", "Email: wm@walmart.com Phone: 111-1111"),
    (61234, "Target", "Email: tg@target.com Phone: 222-2222"),
    (71234, "Costco", "Email: ct@costco.com Phone: 333-3333"),
    (81234, "Tesco", "Email: tc@tesco.com Phone: 444-4444"),
    (91234, "Foodland", "Email: fl@foodland.com Phone: 555-5555"),
    (52345, "Safeway", "Email: sf@safe.com Phone: 666-6666")
]

wine = [
    (1234, "Merlot", 23000),
    (1235, "Cabernet", 30000),
    (1236, "Chablis", 41000),
    (1237, "Chardonnay", 32000)
]

orders = [
    (1000, 1234, 51234, 500),
    (2000, 1235, 61234, 300),
    (3000, 1236, 71234, 200),
    (4000, 1237, 81234, 350),
    (5000, 1236, 91234, 100),
    (6000, 1235, 52345, 200)
]

reports = [
    (1, "Distributor Report"),
    (2, "Sales Report")
]

supplyinventory = [
    (1, "Bottles", 1033, 800),
    (2, "Corks", 1033, 1000),
    (3, "Labels", 1044, 1200),
    (4, "Boxes", 1044, 1000),
    (5, "Vats", 1055, 40),
    (6, "Tubing", 1055, 150)
]
#distquarterreport = [
    #(1, 1, 1, 1, 20),
    #(2, 1, 2, 2, 15)
#]

#salesquarterreport = [
    #(1, 2, 1, 20, 100),
    #(2, 2, 2, 15, 80)
#]

supplier = [
    (1033, "Oregon Supplies", "Email: os@ogsup.com Phone: 111-2222"),
    (1044, "California Supplies", "Email: cs@calisup.com Phone: 222-3333"),
    (1055, "Nebraska Supplies", "Email: ns@nebsup.com Phone: 333-4444")
]

supplyshipment = [
    (12345, 1033, 1, "2024-9-5", "2024-9-10", 700),
    (67891, 1033, 2, "2024-10-6", "2024-10-6", 300),
    (11121, 1044, 3, "2024-9-7", "2024-9-27", 800),
    (14151, 1044, 4, "2024-10-8", "2024-10-28", 500),
    (17181, 1055, 5, "2024-9-1", "2024-9-6", 20),
    (20212, 1055, 6, "2024-10-10", "2024-10-15", 90)
]

#supplyquarterreport = [
    #(1, 3, 1, 17, 5, 1),
    #(2, 4, 2, 18, 6, 2)
#]

department = [
    (1, "Finance"),
    (2, "Marketing"),
    (3, "Production"),
    (4, "Distribution")
]

employee = [
    (199424, "Janet", "Collins", 1, "Leader of Finance/Payroll", 480, 500, 513, 495),
    (199525, "Roz", "Murphy", 2, "Leader of Marketing", 560, 512, 540, 578),
    (199626, "Bob", "Ulrich", 2, "Marketing Assistant", 570, 530, 541, 580),
    (199727, "Henry", "Doyle", 3, "Production Line Manager", 480, 480, 480, 480),
    (199828, "Maria", "Costanza", 4, "Leader of Distribution", 480, 480, 480, 480),
    (199929, "John", "Johnson", 3, "Production Worker", 500, 500, 500, 500)    
]

role = [
    (1, "Leader of Finance/Payroll"),
    (2, "Leader of Marketing"),
    (3, "Marketing Assistant"),
    (4, "Production Line Manager"),
    (5, "Leader of Distribution"),
    (6, "Production Worker")

]

#deptquarterreport = [
    #(1, 2, 3, 4),
    #(5, 6, 7, 8)
#]

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
    cursor.executemany("INSERT INTO Wine (WineID, WineName, BottlesSold) VALUES (%s, %s, %s);", wine)
    cursor.executemany("INSERT INTO Orders (OrderID, WineID, DistributorID, Inventory) VALUES (%s, %s, %s, %s);", orders)
    cursor.executemany("INSERT INTO SupplyInventory (SupplyItemID, SupplyType, SupplierID, TotalInventory) VALUES (%s, %s, %s, %s);", supplyinventory)
    #cursor.executemany("INSERT INTO Reports (ReportID, ReportType) VALUES (%s, %s);", reports)
    #cursor.executemany("INSERT INTO DistQuarterReport (DistQuarterID, ReportID, DistributorID, WineID, BottlesSold) VALUES (%s, %s, %s, %s, %s);", distquarterreport)
    #cursor.executemany("INSERT INTO SalesQuarterReport (SalesQuarterID, ReportID, WineID, BottlesSoldQuarter, BottlesSoldTotal) VALUES (%s, %s, %s, %s, %s);", salesquarterreport)
    cursor.executemany("INSERT INTO Supplier (SupplierID, SupplierName, ContactInfo) VALUES (%s, %s, %s);", supplier)
    cursor.executemany("INSERT INTO SupplyShipment (SupplyShipmentID, SupplierID, SupplyItemID, ExpectedDeliveryDate, ActualDeliveryDate, SupInventory) VALUES (%s, %s, %s, %s, %s, %s);", supplyshipment)
    #cursor.executemany("INSERT INTO SupplyQuarterReport (SupQuarterReportID, ReportID, SupplierID, SupplyID, AverageDeliveryGap, InventoryTotal) VALUES (%s, %s, %s, %s, %s, %s);", supplyquarterreport)
    cursor.executemany("INSERT INTO Department (DepartmentID, DepartmentName) VALUES (%s, %s);", department)
    cursor.executemany("INSERT INTO Role (RoleID, RoleName) VALUES (%s, %s);", role)
    cursor.executemany("INSERT INTO Employee (EmployeeID, FirstName, LastName, DepartmentID, Role, HoursQ1, HoursQ2, HoursQ3, HoursQ4) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);", employee)
    #cursor.executemany("INSERT INTO DeptQuarterReport (DeptQuarterID, ReportID, DepartmentID, HoursWorked) VALUES (%s, %s, %s, %s);", deptquarterreport)

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