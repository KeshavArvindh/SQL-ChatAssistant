# app.py
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Function to execute SQL queries
def execute_query(query):
    """
    Executes a SQL query and returns the result.
    Handles database errors gracefully.
    """
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except sqlite3.Error as e:
        result = f"An error occurred: {e}"
    finally:
        conn.close()
    return result

# Function to handle chat queries
def chat_assistant(query):
    """
    Processes user queries and returns appropriate responses.
    Handles invalid queries, missing input, and database errors.
    """
    try:
        query = query.lower().strip()

        if "show me all employees in the" in query:
            department = query.split("department")[0].split("in the")[-1].strip()
            if not department:
                return "Please specify a department."
            sql_query = f"SELECT * FROM Employees WHERE Department = '{department}'"
            result = execute_query(sql_query)
            if not result:
                return f"No employees found in the {department} department."
            return result

        elif "who is the manager of the" in query:
            department = query.split("department")[0].split("of the")[-1].strip()
            if not department:
                return "Please specify a department."
            sql_query = f"SELECT Manager FROM Departments WHERE Name = '{department}'"
            result = execute_query(sql_query)
            if not result:
                return f"No manager found for the {department} department."
            return result[0][0]  # Return the manager's name

        elif "list all employees hired after" in query:
            date = query.split("after")[-1].strip()
            if not date:
                return "Please specify a date."
            sql_query = f"SELECT * FROM Employees WHERE Hire_Date > '{date}'"
            result = execute_query(sql_query)
            if not result:
                return f"No employees hired after {date}."
            return result

        elif "what is the total salary expense for the" in query:
            department = query.split("department")[0].split("for the")[-1].strip()
            if not department:
                return "Please specify a department."
            sql_query = f"SELECT SUM(Salary) FROM Employees WHERE Department = '{department}'"
            result = execute_query(sql_query)
            if not result or result[0][0] is None:
                return f"No salary data found for the {department} department."
            return f"Total salary expense for {department}: ${result[0][0]}"

        else:
            return "Sorry, I don't understand that query. Please try again."

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Flask route for the chat endpoint
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    """
    Handles GET and POST requests to the /chat endpoint.
    GET: Returns a welcome message.
    POST: Processes user queries and returns responses.
    """
    if request.method == 'GET':
        return "Welcome to the Chat Assistant! Send a POST request with your query."
    elif request.method == 'POST':
        user_query = request.json.get('query')
        if not user_query:
            return jsonify({"error": "No query provided"}), 400
        response = chat_assistant(user_query)
        return jsonify({"response": response})

# Run the Flask app
if __name__ == '__main__':
    print("The chat-assistant can be accessed on http://localhost:5000/chat")
    app.run(debug=True)