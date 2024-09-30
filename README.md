# Campy B-Horror Movie Database (SQL Version)

This is a simple command-line application for managing a database of campy B-horror movies. It allows users to add, view, update, and delete movie entries in a MySQL database. There's no front end, just some CRUD functions.

## Amazing Features

- Add new movies to the database
- View all movies in the database
- Update existing movie information
- Delete movies from the database

## Prerequisites

- Python 3.11 or higher
- MySQL server - provided for you
- pip (Python package manager)

## Setup

1. Clone this repository or download the source code.
   ```
   git clone https://github.com/projects-in-programming-f24/campy.git
   ```

2. Navigate to the project directory:
   ```
   cd path/to/campy-b-horror-movie-database
   ```

3. Create a virtual environment if you'd like:
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

5. Set up your .env file:
   a. Create a new file in the project root directory and name it `.env`
   b. Open the `.env` file in a text editor
   c. Add your MySQL connection details in the following format:
      ```
      DB_HOST=your_mysql_host
      DB_USER=your_mysql_username
      DB_PASS=your_mysql_password
      DB_NAME=your_database_name
      ```
   d. Replace the placeholders with your actual MySQL connection details (provided for you on Slack). For example:
      ```
      DB_HOST=34.123.45.67
      DB_USER=myuser
      DB_PASS=mypassword
      DB_NAME=campy_movies
      ```
   e. Save and close the `.env` file

   Note: The `.env` file contains sensitive information. Make sure it's included in your `.gitignore` file to prevent it from being committed to version control. PLEASE DO NOT LEAK THIS!!!

## Usage

To run the application:

```
python main.py
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