import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

load_dotenv()

def create_connection():
    connection = None
    try:
        # Print connection details (be careful with this in production!)
        print(f"Attempting to connect to:")
        print(f"Host: {os.getenv('DB_HOST')}")
        print(f"User: {os.getenv('DB_USER')}")
        print(f"Database: {os.getenv('DB_NAME')}")
        
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            database=os.getenv('DB_NAME')
        )
        print("Successfully connected to the database")
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        print(f"Error Code: {e.errno}")
        print(f"SQL State: {e.sqlstate}")
        print(f"Error Message: {e.msg}")
    return connection

# Create table if it doesn't exist
def create_table(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS movies (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        year INT,
        director VARCHAR(255),
        plot TEXT,
        budget DECIMAL(10, 2)
    )
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute(create_table_query)
            connection.commit()
            print("Table 'movies' created successfully")
    except Error as e:
        print(f"Error creating table: {e}")

def add_movie(connection):
    title = input("Enter movie title: ")
    year = int(input("Enter release year: "))
    director = input("Enter director name: ")
    plot = input("Enter brief plot summary: ")
    budget = float(input("Enter movie budget: "))
    
    query = """
    INSERT INTO movies (title, year, director, plot, budget)
    VALUES (%s, %s, %s, %s, %s)
    """
    values = (title, year, director, plot, budget)
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, values)
            connection.commit()
            print(f"Movie added with ID: {cursor.lastrowid}")
    except Error as e:
        print(f"Error adding movie: {e}")

def view_movies(connection):
    query = "SELECT * FROM movies"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
            if not results:
                print("No movies found in the database.")
            else:
                for movie in results:
                    print(f"\nID: {movie[0]}")
                    print(f"Title: {movie[1]}")
                    print(f"Year: {movie[2]}")
                    print(f"Director: {movie[3]}")
                    print(f"Plot: {movie[4]}")
                    print(f"Budget: ${movie[5]}")
    except Error as e:
        print(f"Error retrieving movies: {e}")

def update_movie(connection):
    movie_id = input("Enter the ID of the movie to update: ")
    field = input("Enter the field to update (title/year/director/plot/budget): ")
    value = input("Enter the new value: ")
    
    query = f"UPDATE movies SET {field} = %s WHERE id = %s"
    values = (value, movie_id)
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, values)
            connection.commit()
            if cursor.rowcount:
                print("Movie updated successfully!")
            else:
                print("No movie found with that ID.")
    except Error as e:
        print(f"Error updating movie: {e}")

def delete_movie(connection):
    movie_id = input("Enter the ID of the movie to delete: ")
    
    query = "DELETE FROM movies WHERE id = %s"
    value = (movie_id,)
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, value)
            connection.commit()
            if cursor.rowcount:
                print("Movie deleted successfully!")
            else:
                print("No movie found with that ID.")
    except Error as e:
        print(f"Error deleting movie: {e}")

def main():
    connection = create_connection()
    if connection is None:
        return
    
    create_table(connection)
    
    while True:
        print("\nCampy B-Horror Movie Database")
        print("1. Add a movie")
        print("2. View all movies")
        print("3. Update a movie")
        print("4. Delete a movie")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_movie(connection)
        elif choice == '2':
            view_movies(connection)
        elif choice == '3':
            update_movie(connection)
        elif choice == '4':
            delete_movie(connection)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

    connection.close()
    print("Goodbye!")

if __name__ == "__main__":
    main()