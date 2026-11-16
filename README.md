# Students Database – PostgreSQL CRUD Application

A Python application that connects to a PostgreSQL database and performs
CRUD operations.

## Video Demonstration

[Demonstration Video](https://youtu.be/4Z07sT0XjNw)

## Requirements

- PostgreSQL (with pgAdmin 4)
- Python 3
- psycopg2

## Database Setup

1. In pgAdmin, right-click **Databases > Create > Database** and name it `students_db`.
2. Open the **Query Tool** on `students_db`.
3. Open `create_students.sql` and execute it. This creates the `students` table
   and inserts the three initial records.

## Running the Application

1. Install psycopg2:

   ```bash
   sudo apt install python3-psycopg2
   ```

2. Open `main.py` and set the connection details (host, port, database name,
   user, and password) to match your PostgreSQL setup.

3. Run the application:

   ```bash
   python3 main.py
   ```
