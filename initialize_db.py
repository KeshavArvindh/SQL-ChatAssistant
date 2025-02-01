# initialize_db.py
import sqlite3

def initialize_database():
    """
    Initializes the SQLite database with the required tables and sample data.
    """
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create Employees table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employees (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Department TEXT NOT NULL,
        Salary INTEGER,
        Hire_Date TEXT
    )
    ''')

    # Create Departments table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Departments (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Manager TEXT NOT NULL
    )
    ''')

    # Insert sample data into Employees table
    cursor.execute('''
    INSERT OR IGNORE INTO Employees (Name, Department, Salary, Hire_Date)
    VALUES 
        ('Alice', 'Sales', 50000, '2021-01-01'),
        ('Bob', 'Engineering', 70000, '2020-06-10'),
        ('Charlie', 'Marketing', 60000, '2022-03-20')
    ''')

    # Insert sample data into Departments table
    cursor.execute('''
    INSERT OR IGNORE INTO Departments (Name, Manager)
    VALUES 
        ('Sales', 'Alice'),
        ('Engineering', 'Bob'),
        ('Marketing', 'Charlie')
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    initialize_database()
    print("Database initialized successfully!")