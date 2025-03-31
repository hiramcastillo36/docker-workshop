from flask import Flask, jsonify, request, render_template_string
import os
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.environ.get('MYSQL_HOST', 'mysql'),
            database=os.environ.get('MYSQL_DATABASE', 'flaskdb'),
            user=os.environ.get('MYSQL_USER', 'flaskuser'),
            password=os.environ.get('MYSQL_PASSWORD', 'flaskpassword'),
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

@app.route('/')
def index():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask MySQL Docker Demo</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            h1 { color: #333; }
            form { margin: 20px 0; }
            input, button { padding: 8px; margin: 5px 0; }
            ul { list-style-type: none; padding: 0; }
            li { padding: 10px; margin: 5px 0; background-color: #f5f5f5; border-radius: 4px; }
        </style>
    </head>
    <body>
        <h1>Task Manageeer</h1>
        <form action="/add_task" method="POST">
            <input type="text" name="task" placeholder="Enter a task" required>
            <button type="submit">Add Taskeed</button>
        </form>
        <h2>Tasks:</h2>
        <ul>
            {% for task in tasks %}
                <li>{{ task[1] }}</li>
            {% endfor %}
        </ul>
    </body>
    </html>
    '''

    connection = get_db_connection()
    tasks = []

    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM tasks")
            tasks = cursor.fetchall()
            cursor.close()
            connection.close()
        except Error as e:
            print(f"Error fetching tasks: {e}")

    return render_template_string(html, tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("INSERT INTO tasks (description) VALUES (%s)", (task,))
                connection.commit()
                cursor.close()
                connection.close()
            except Error as e:
                print(f"Error adding task: {e}")

    return index()

@app.route('/health')
def health():
    connection = get_db_connection()
    status = 'OK' if connection else 'Database connection failed'
    if connection:
        connection.close()
    return jsonify({'status': status})

if __name__ == '__main__':
    app.run()
