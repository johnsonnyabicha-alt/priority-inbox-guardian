import sqlite3
from pathlib import Path 
DB_PATH = Path(__file__).parent / 'email.db'
def get_connection():
    return sqlite3.connect(DB_PATH)
def initialize_database():
    con = get_connection()
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS emails(
        email_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        message_id TEXT UNIQUE, 
        sender_name TEXT NOT NULL, 
        sender_email TEXT NOT NULL, 
        subject TEXT, 
        body TEXT, 
        summary TEXT,
        tag TEXT, 
        urgency TEXT, 
        status TEXT, 
        received_at TEXT,
        processed_at TEXT
    )
    """)
    con.commit()
    con.close()
def save_email(
    message_id,
    sender_name,
    sender_email, 
    subject, 
    body, 
    summary,
    tag,
    urgency,
    status, 
    received_at,
    processed_at
    ):
        con = get_connection()
        cur = con.cursor()
        cur.execute(""" INSERT OR IGNORE INTO emails(
            message_id,
            sender_name,
            sender_email, 
            subject, 
            body, 
            summary,
            tag,
            urgency,
            status, 
            received_at,
            processed_at
        )  VALUES(?,?,?,?,?,?,?,?,?,?,?)
        """, (
            message_id,
            sender_name,
            sender_email, 
            subject, 
            body, 
            summary,
            tag,
            urgency,
            status, 
            received_at,
            processed_at
        ))
        con.commit()
        con.close()
def get_email(email_id):
    con = get_connection()
    cur = con.cursor()
    cur.execute(""" SELECT * FROM emails WHERE email_id = ?""", (email_id,))
    row = cur.fetchone()
    con.close()
    return row
def email_exists(message_id):
    con = get_connection()
    cur = con.cursor()
    cur.execute(""" SELECT 1 FROM emails WHERE message_id = ?""",(message_id,))
    exists = cur.fetchone() is not None
    con.close() 
    return exists 
def list_recent_emails(limit = 10):
    con = get_connection()
    cur = con.cursor()
    cur.execute(""" SELECT email_id, subject, summary, urgency 
                FROM emails 
                ORDER BY email_id DESC
                LIMIT ?""",(limit,))
    rows = cur.fetchall()
    con.close()
    return rows

if __name__ == '__main__':
    initialize_database()
    save_email(
        "msg_001",
        "Exeter Accommodation",
        "rent.accommodation@exeter.ac.uk",
        "URGENT: Rent Reminder",
        "Please pay rent by 15th August or a late fee of 50 pounds will added to your tenant ledger.",
        "Pay August rent before 15th August",
        "finance",
        "action",
        "classified",
        "2026-08-05T12:00:00",
        "2026-08-05T12:00:00"
    )
    print(list_recent_emails())
    print(get_email(1))
    print(email_exists('msg_001'))