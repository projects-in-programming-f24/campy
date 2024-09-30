# Campy B-Horror Movie Database

This is a simple command-line application for managing a database of campy B-horror movies. It allows users to add, view, update, and delete movie entries in a MongoDB database. There's no front end, just some CRUD functions.

## Amazing Features

- Add new movies to the database
- View all movies in the database
- Update existing movie information
- Delete movies from the database

## Prerequisites

- Python 3.11 or higher
- MongoDB Atlas account (or a local MongoDB installation if you'd like)
- pip (Python package manager)

## Setup

1. Clone this repository or download the source code. `git clone https://github.com/projects-in-programming-f24/campy.git`

2. Navigate to the project directory:
   ```
   cd path/to/campy-b-horror-movie-database
   ```

3. Create a virtual environemnt if you'd like
    ```
    python -m venv .venv 

    # On Windows:
    .venv\Scripts\activate

    # On macOS and Linux:
    source .venv/bin/activate

    ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the project root directory with your MongoDB connection string:
   ```
   MONGODB_URI=your_mongodb_connection_string_here
   ```
   Replace `your_mongodb_connection_string_here` with your actual MongoDB connection string from Atlas.

## Usage

To run the application:

```
python campy_app.py
```

Follow the on-screen prompts to interact with the database:

1. Add a movie
2. View all movies
3. Update a movie
4. Delete a movie
5. Exit the application

## Contributing

Contributions to improve the application are welcome. Please feel free to submit a Pull Request.

## License

Not that anyone really cares, but I'm modelling here for students! Available under the [MIT License](https://opensource.org/license/mit).