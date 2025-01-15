import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="TaskMaster - A task management tool")
    parser.add_argument(
        "command", 
        help="The command to execute, e.g., 'add', 'delete', 'list', or 'initialize'",
        choices=["add", "delete", "list", "initialize"]
    )
    parser.add_argument("--title", help="Title of the task (required for 'add')", type=str)
    parser.add_argument("--description", help="Description of the task", type=str)
    parser.add_argument("--category", help="Category of the task", type=str)
    parser.add_argument("--priority", help="Priority of the task", type=str)
    parser.add_argument("--deadline", help="Deadline for the task", type=str)
    parser.add_argument("--id", help="ID of the task (required for 'delete')", type=int)

    # Handle missing arguments gracefully
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    # Parse arguments
    args = parser.parse_args()

    # Handle commands
    if args.command == "initialize":
        initialize_db()
        print("Database initialized.")
    elif args.command == "add":
        if not args.title:
            print("Error: '--title' is required for the 'add' command.")
            return
        add_task(args.title, args.description, args.category, args.priority, args.deadline)
        print("Task added successfully.")
    elif args.command == "list":
        tasks = list_tasks()
        for task in tasks:
            print(task)
    elif args.command == "delete":
        if not args.id:
            print("Error: '--id' is required for the 'delete' command.")
            return
        delete_task(args.id)
        print(f"Task with ID {args.id} deleted successfully.")

# Include database logic from previous code
import sqlite3
import os

DB_DIR = 'db'
DB_PATH = os.path.join(DB_DIR, 'tasks.db')
if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR)

def initialize_db():
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
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (title, description, category, priority, deadline)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, description, category, priority, deadline))
    conn.commit()
    conn.close()

def list_tasks():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def delete_task(task_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
