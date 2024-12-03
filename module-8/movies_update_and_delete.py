#Amanda New
#CSD310-A311
#Module 8 - Movies: Update and Deletes

import mysql.connector
from mysql.connector import errorcode


config = {
    
    "user": "root",
    "password": "Gimmethembuns1!Manbob613!",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

#define show_films function
def show_films(cursor,title):
    
    #inner join query 
    select_query = "select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film \
    INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id"
    
    #insert, update, and delete query - comment out line to run independently 
    insert_query = "INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES ('Back to the Future', '1985', 116, 'Robert Zemeckis', 3 , 2)"
    update_query = "UPDATE film SET genre_id = 1 WHERE film_name = 'Alien'"
    delete_query = "DELETE FROM film WHERE film_name = 'Gladiator'"

    #*** commented lines are combined queries for select and update only***
    #combined_query = select_query + ";" + insert_query + ";" + select_query
    #combined_query = select_query + ";" + insert_query + ';' + update_query + ";" + select_query 
    combined_query = select_query + ";" + insert_query + ';' + update_query + ";" + delete_query + ';' + select_query 
    
    generator = cursor.execute(combined_query, multi=True)
    
    #iterate over generator 
    for cur in generator:
        print('cursor:', cur)
        if cur.with_rows:
            print("\n == {} ==".format(title))                
            for film in cur.fetchall():
                print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film [1], film[2], film[3]))

#***show_films call is under try vvv***

try:
    db = mysql.connector.connect(**config)
        

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue...")
    cursor = db.cursor()

    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")
    #db.commit() <-- remove comment to commit to sql

except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("The specified database does not exist")

    else:
                print(err)







    



