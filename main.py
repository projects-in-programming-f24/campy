import os
from dotenv import load_dotenv
import pymongo
from bson.objectid import ObjectId

load_dotenv()
mongodb_uri = os.getenv('MONGODB_URI')
print(mongodb_uri)

# note: you could put this db code in another file if you're feeling fancy
try:
    client = pymongo.MongoClient(mongodb_uri) # this creates a client that can connect to our DB
    print("Databases available:")
    print(client.list_database_names()) # just to make sure you are connecting to the right server...
    db = client.get_database("campy") # this gets the database named 'campy'
    movies = db.get_collection("movies") # this gets the collection named 'movies'
    
    client.server_info() # this is a hack to force the client to connect to the server so we can error out
    print("Connected successfully to the 'campy' database!")
except pymongo.errors.ConnectionFailure as e:
    print(f"Could not connect to MongoDB: {e}")
    exit(1)

def add_movie():
    title = input("Enter movie title: ")
    year = int(input("Enter release year: "))
    director = input("Enter director name: ")
    plot = input("Enter brief plot summary: ")
    budget = float(input("Enter movie budget: "))
    
    movie = {
        "title": title,
        "year": year,
        "director": director,
        "plot": plot,
        "budget": budget
    }
    
    try:
        result = movies.insert_one(movie)
        print(f"Movie added with ID: {result.inserted_id}")
    except pymongo.errors.PyMongoError as e:
        print(f"An error occurred while adding the movie: {e}")

def view_movies():
    try:
        movie_count = movies.count_documents({})
        if movie_count == 0:
            print("No movies found in the database.")
        else:
            for movie in movies.find():
                print(f"\nID: {movie['_id']}")
                print(f"Title: {movie['title']}")
                print(f"Year: {movie['year']}")
                print(f"Director: {movie['director']}")
                print(f"Plot: {movie['plot']}")
                print(f"Budget: ${movie['budget']}")
    except pymongo.errors.PyMongoError as e:
        print(f"An error occurred while retrieving movies: {e}")

def add_movie():
    title = input("Enter movie title: ")
    year = int(input("Enter release year: "))
    director = input("Enter director name: ")
    plot = input("Enter brief plot summary: ")
    budget = float(input("Enter movie budget: "))
    
    movie = {
        "title": title,
        "year": year,
        "director": director,
        "plot": plot,
        "budget": budget
    }
    
    result = movies.insert_one(movie)
    print(f"Movie added with ID: {result.inserted_id}")

def view_movies():
    for movie in movies.find():
        print(f"\nID: {movie['_id']}")
        print(f"Title: {movie['title']}")
        print(f"Year: {movie['year']}")
        print(f"Director: {movie['director']}")
        print(f"Plot: {movie['plot']}")
        print(f"Budget: ${movie['budget']}")

# a note on updating in MongoDB: you can update one document or many documents at a time
# I used the $set operator here for a few important reasons:
    # $set allows us to update only the specified field(s) without affecting other fields in the document. cheaper, faster.
    # If the field doesn't exist, $set will add it to the document without altering the structure of existing fields.
    # Without $set, you might accidentally replace the entire document with just the updated field. I do this all the time by accident
def update_movie():
    movie_id = input("Enter the ID of the movie to update: ")
    field = input("Enter the field to update (title/year/director/plot/budget): ")
    value = input("Enter the new value: ")
    
    if field == 'year' or field == 'budget':
        value = float(value)
    
    result = movies.update_one(
        {"_id": ObjectId(movie_id)},
        {"$set": {field: value}}
    )
    
    if result.modified_count:
        print("Movie updated successfully!")
    else:
        print("No movie found with that ID.")

def delete_movie():
    movie_id = input("Enter the ID of the movie to delete: ")
    
    result = movies.delete_one({"_id": ObjectId(movie_id)})
    
    if result.deleted_count:
        print("Movie deleted successfully!")
    else:
        print("No movie found with that ID.")
def main():
    while True:
        print("\nCampy B-Horror Movie Database")
        print("1. Add a movie")
        print("2. View all movies")
        print("3. Update a movie")
        print("4. Delete a movie")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_movie()
        elif choice == '2':
            view_movies()
        elif choice == '3':
            update_movie()
        elif choice == '4':
            delete_movie()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

    client.close()
    print("Goodbye!")

if __name__ == "__main__":
    main()