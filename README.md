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

4. This will create a database.db file in the project directory.

### Step 2: Run the Flask App
1. Start the Flask app by running:
```bash

python app.py
```
2. The app will start running at http://localhost:5000/.

### Step 3: Test the Chat Assistant
1. Use Postman, curl, or a browser to interact with the /chat endpoint.
2. Send a POST request to http://localhost:5000/chat with a JSON payload like:

```json

{
    "query": "Show me all employees in the Sales department"
}
```
3. The assistant will return a response in JSON format.

### Example Queries and Responses
# 1. Show Employees in a Department
Query:
```json

{
    "query": "Show me all employees in the Sales department"
}
```

Response:
```json

{
    "response": [
        [1, "Alice", "Sales", 50000, "2021-01-01"]
    ]
}
```
# Known Limitations
### Limited Query Support:
The assistant currently supports only a few types of queries. Adding more query types would improve its functionality.

### Natural Language Processing (NLP):
The assistant uses simple string matching to process queries. Integrating an NLP library (e.g., spaCy or NLTK) could make it more robust and flexible.

### Error Handling:
While the assistant handles common errors, some edge cases (e.g., complex invalid queries) may not be handled gracefully.

### Scalability:
The current implementation is designed for small datasets. For larger datasets, performance optimizations (e.g., indexing) would be necessary.

# Suggestions for Improvement
### 1. Add More Query Types:
Support additional queries like:
`"What is the average salary in the [department] department?"`
`"How many employees are there in the [department] department?"`

### 2. Improve Query Parsing:
Use regular expressions or an NLP library to handle more complex queries.

### 3. Enhance Error Handling:
Add more detailed error messages and logging for debugging.

### 4. Deploy to the Cloud:
Deploy the app to a cloud platform like Heroku, AWS, or Google Cloud for public access.

### 5.Add a Web Interface:
Create a simple web interface for users to interact with the chat assistant without using Postman or curl.



