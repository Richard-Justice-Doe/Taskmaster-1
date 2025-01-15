# Handles database logic
import sqlite3
import os

# Ensure the database directory exists
DB_DIR = 'db'
DB_PATH = os.path.join(DB_DIR, 'tasks.db')
if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR)

def initialize_db():
    """Initialize the database and create the tasks table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            category TEXT,
            priority TEXT,
            status TEXT DEFAULT 'Pending',
            deadline TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_task(title, description, category, priority, deadline):
    """Add a new task to the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (title, description, category, priority, deadline)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, description, category, priority, deadline))
    conn.commit()
    conn.close()

def list_tasks():
    """Retrieve all tasks from the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def delete_task(task_id):
    """Delete a task from the database by ID."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
# Handles database logic
import sqlite3
import os

# Ensure the database directory exists
DB_DIR = 'db'
DB_PATH = os.path.join(DB_DIR, 'tasks.db')
if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR)

def initialize_db():
    """Initialize the database and create the tasks table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            category TEXT,
            priority TEXT,
            status TEXT DEFAULT 'Pending',
            deadline TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_task(title, description, category, priority, deadline):
    """Add a new task to the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (title, description, category, priority, deadline)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, description, category, priority, deadline))
    conn.commit()
    conn.close()

def list_tasks():
    """Retrieve all tasks from the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def delete_task(task_id):
    """Delete a task from the database by ID."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
