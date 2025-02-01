# SQLite Chat Assistant

This project is a Python-based chat assistant that interacts with an SQLite database to answer user queries. It is built using **Flask** for the web interface and **SQLite** for the database. The assistant supports natural language queries and returns formatted answers based on the data in the database.

---

## How the Assistant Works

The chat assistant works as follows:

1. **Database Setup**:
   - The SQLite database (`database.db`) contains two tables:
     - `Employees`: Stores employee details like name, department, salary, and hire date.
     - `Departments`: Stores department details like name and manager.

2. **Query Handling**:
   - The assistant accepts natural language queries via a POST request to the `/chat` endpoint.
   - It converts the query into an SQL command and fetches data from the database.
   - It returns clear, formatted answers to the user.

3. **Supported Queries**:
   - `"Show me all employees in the [department] department."`
   - `"Who is the manager of the [department] department?"`
   - `"List all employees hired after [date]."`
   - `"What is the total salary expense for the [department] department?"`

4. **Error Handling**:
   - The assistant gracefully handles invalid queries, missing input, and database errors.
   - It returns meaningful error messages when no results are found or when the input is invalid.

---

## Steps to Run the Project Locally

### Prerequisites
- Python 3.x
- Flask (`pip install flask`)

### Step 1: Initialize the Database
1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Run the `initialize_db.py` script to create the database and insert sample data:
   ```bash
   python initialize_db.py
