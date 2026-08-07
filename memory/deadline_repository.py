import sqlite3
from pathlib import Path 
DEADLINE_DB_PATH = Path(__file__).parent / 'deadlines.db'
def get_connection():
    return sqlite3.connect(DEADLINE_DB_PATH)
def initialize_database():
    con = get_connection()
    cur = con.cursor() 
    cur.execute(""" CREATE TABLE IF NOT EXISTS deadlines (
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,     
        email_id INTEGER NOT NULL,
        task_description TEXT NOT NULL,
        due_date TEXT NOT NULL,
        remind_at TEXT NOT NULL,
        current_tag TEXT NOT NULL,
        status TEXT NOT NULL
        )
        """)# foreign key relationship 
    con.commit()
    con.close()
def save_deadline(
    email_id, 
    task_description,
    due_date,
    remind_at, 
    current_tag,
    status
):
    con = get_connection()
    cur = con.cursor()
    cur.execute(""" INSERT INTO deadlines(
        email_id,
        task_description,
        due_date,
        remind_at, 
        current_tag,
        status) VALUES(?,?,?,?,?,?)""", 
        (
            email_id,
            task_description,
            due_date,
            remind_at,
            current_tag,
            status
        )
        )
    task_id = cur.lastrowid
    con.commit()
    con.close()
    return task_id
def get_deadline(task_id):
    con = get_connection()
    cur = con.cursor()
    cur.execute(""" SELECT * FROM deadlines WHERE task_id = ? """, (task_id,))
    row = cur.fetchall()
    con.close()
    return row 
def list_upcoming_deadlines(limit = 10):
    con = get_connection()
    cur = con.cursor()
    cur.execute("""
                SELECT email_id, task_description, due_date, remind_at
                FROM deadlines
                WHERE status = 'pending'
                ORDER BY due_date ASC
                LIMIT ?
                """, (limit,)
                )
    rows = cur.fetchall()
    con.close()
    return rows

if __name__ == '__main__':
    initialize_database()
    print(list_upcoming_deadlines())