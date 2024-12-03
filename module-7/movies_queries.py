#Amanda New
#CSD310-A311
#Module 7.2 Assignment
#Movies Queries

import mysql.connector
from mysql.connector import errorcode


config = {
    
    "user": "root",
    "password": "Gimmethembuns1!Manbob613!",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
        

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("The specified database does not exist")

    else:
                print(err)

def query():
    
    cursor = db.cursor()

    # Query 1: Select all fields from the studio table
    cursor.execute("SELECT * FROM studio")
    results1 = cursor.fetchall()
    print("Studio Table:")
    for row in results1:
        print(row)

    # Query 2: Select all fields from the genre table
    cursor.execute("SELECT * FROM genre")
    results2 = cursor.fetchall()
    print("\nGenre Table:")
    for row in results2:
        print(row)

    # Query 3: Select movie names with runtime less than 2 hours
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    results3 = cursor.fetchall()
    print("\nMovies with Runtime < 2 Hours:")
    for row in results3:
        print(row)

    # Query 4: Group movies by director
    cursor.execute("SELECT film_director, GROUP_CONCAT(film_name SEPARATOR '. ') AS films FROM film GROUP BY film_director") 
    results4 = cursor.fetchall()
    print("\nMovies Grouped by Director:")
    for row in results4:
        print(row)
query()




    



