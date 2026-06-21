import sqlite3

# This automatically creates a file called tasks.db on your computer
def get_connection():
    conn = sqlite3.connect("tasks.db")
    conn.row_factory = sqlite3.Row  # lets us get results as dictionaries
    return conn

# This creates the tasks table when app starts
def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT DEFAULT 'pending'
        )
    """)
    conn.commit()
    conn.close()