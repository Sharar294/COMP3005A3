-- create_students.sql
-- Sets up the students table and loads the initial data.
--
-- Step 1 (run once, separately): create the database itself.
--   In pgAdmin: right-click Databases > Create > Database, name it "students_db"
--
-- Step 2: connect to students_db and run the rest of this script.

-- Remove any existing copy so the script can be re-run from a clean state
DROP TABLE IF EXISTS students;

-- Create the students table as per the assignment schema
CREATE TABLE students (
    student_id      SERIAL PRIMARY KEY,     -- auto-incrementing integer primary key
    first_name      TEXT NOT NULL,
    last_name       TEXT NOT NULL,
    email           TEXT NOT NULL UNIQUE,   -- no two students may share an email
    enrollment_date DATE
);

-- Insert the initial data provided in the assignment
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');

