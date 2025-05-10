import sqlite3
from rich.console import Console
from rich.table import Table

console = Console()

import sqlite3

def get_connection():
    conn = sqlite3.connect("todos.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, task TEXT, status TEXT DEFAULT 'todo')")
    # Check if status column exists, if not add it (for existing DBs)
    cursor.execute("PRAGMA table_info(todos)")
    columns = [col[1] for col in cursor.fetchall()]
    if "status" not in columns:
        cursor.execute("ALTER TABLE todos ADD COLUMN status TEXT DEFAULT 'todo'")
        conn.commit()
    return conn, cursor

def get_tasks():
    conn, cursor = get_connection()
    tasks = cursor.execute("SELECT * FROM todos WHERE status IN ('todo', 'doing')").fetchall()
    conn.close()
    return tasks

def add_task(task, status="todo"):
    conn, cursor = get_connection()
    if status not in ("todo", "doing", "done"):
        status = "todo"
    cursor.execute("INSERT INTO todos (task, status) VALUES (?, ?)", (task, status))
    conn.commit()
    conn.close()

def update_task(task_id, new_task, new_status=None):
    conn, cursor = get_connection()
    if new_status and new_status not in ("todo", "doing", "done"):
        new_status = None
    if new_status:
        cursor.execute("UPDATE todos SET task = ?, status = ? WHERE id = ?", (new_task, new_status, task_id))
    else:
        cursor.execute("UPDATE todos SET task = ? WHERE id = ?", (new_task, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn, cursor = get_connection()
    cursor.execute("DELETE FROM todos WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def manage_todo():
    while True:
        console.print("\n[bold blue]To-Do List Manager[/bold blue]")
        tasks = get_tasks()
        if tasks:
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("ID", style="dim", width=6)
            table.add_column("Task")
            table.add_column("Status", width=10)
            for task in tasks:
                table.add_row(str(task[0]), task[1], task[2])
            console.print(table)
        else:
            console.print("[green]No tasks found.[/green]")

        console.print("\nOptions:")
        console.print("1. Add Task")
        console.print("2. Update Task")
        console.print("3. Delete Task")
        console.print("4. Exit To-Do Manager")

        choice = console.input("\nEnter your choice (1-4): ")

        if choice == "1":
            task_desc = console.input("Enter task description: ")
            add_task(task_desc)
            console.print("[green]Task added successfully![/green]")
        elif choice == "2":
            task_id = console.input("Enter task ID to update: ")
            new_desc = console.input("Enter new task description: ")
            new_status = console.input("Enter new status (todo, doing, done) or leave blank: ")
            if new_status.strip() == "":
                new_status = None
            update_task(int(task_id), new_desc, new_status)
            console.print("[green]Task updated successfully![/green]")
        elif choice == "3":
            task_id = console.input("Enter task ID to delete: ")
            delete_task(int(task_id))
            console.print("[red]Task deleted successfully![/red]")
        elif choice == "4":
            break
        else:
            console.print("[red]Invalid choice. Please try again.[/red]")
