import psycopg2
import os


DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "students_db",
    "user": "postgres",
    "password": "postgres",
}


def get_connection():
    """Open and return a new connection to the PostgreSQL database."""
    return psycopg2.connect(**DB_CONFIG)

def getAllStudents():
    """Retrieve and display all records from the students table."""
    try:
        # 'with' commits on success and rolls back on error
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute("SELECT * FROM students ORDER BY student_id;")
            # Print each row returned by the query
            for row in cur.fetchall():
                print(row)
    except psycopg2.Error as e:
        print(f"Error retrieving students: {e}")

    
def addStudent(first_name, last_name, email, enrollment_date):
    """Insert a new student record into the students table."""
    try:
        with get_connection() as conn, conn.cursor() as cur:
            # %s placeholders let psycopg2 safely insert the values
            cur.execute(
                "INSERT INTO students (first_name, last_name, email, enrollment_date) "
                "VALUES (%s, %s, %s, %s);",
                (first_name, last_name, email, enrollment_date),
            )
        print("Student added.")
    except psycopg2.Error as e:
        print(f"Error adding student: {e}")


def updateStudentEmail(student_id, new_email):
    """Update the email address of the student with the given student_id."""
    try:
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute(
                "UPDATE students SET email = %s WHERE student_id = %s;",
                (new_email, student_id),
            )
        print("Email updated.")
    except psycopg2.Error as e:
        print(f"Error updating email: {e}")


def deleteStudent(student_id):
    """Delete the record of the student with the given student_id."""
    try:
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
        print("Student deleted.")
    except psycopg2.Error as e:
        print(f"Error deleting student: {e}")


if __name__ == "__main__":
    getAllStudents()
    addStudent("Alice", "Wong", "alice.wong@example.com", "2023-09-03")
    getAllStudents()
    updateStudentEmail(1, "john.new@example.com")
    getAllStudents()
    deleteStudent(3)
    getAllStudents()
    

