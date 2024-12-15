#Amanda New
#Katie Hilliard
#Keanu Foltz
#Amit Rizal

#Module 11
#Milestone 3

#import mysql
import mysql.connector

#establish connection
connection = mysql.connector.connect(
    user='root', #Replace with your user
    password='Gimmethembuns1!Manbob613!', #Replace with your password
    host='127.0.0.1', #Replace with your host
    database='BacchusWine' #Replace with your database name
)

#define employee productivity report
def employee_productivity_report():
    query = """
    SELECT FirstName, LastName AS EmployeeName, Role, HoursQ1, HoursQ2, HoursQ3, HoursQ4, (HoursQ1 + HoursQ2 + HoursQ3 + HoursQ4) AS TotalHoursWorked
    FROM Employee
    ORDER BY TotalHoursWorked DESC;
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()

    #print and format results:
    print(f"{'Employee Name':<15} {'Role':<5} {'':<20} {'Q1':<5} {'Q2':<5} {'Q3':<5} {'Q4':<5} {'2024 Total':<0}")
    print("-" * 80)

    for row in results:
        print(f"{row[0]:<5} {row[1]:<10} {row[2]:<25} {row[3]:<5} {row[4]:<5} {row[5]:<5} {row[6]:<5} {row[7]:<5}")

#run function
if __name__ == "__main__":
    try:
        employee_productivity_report()
    finally:
        connection.close()