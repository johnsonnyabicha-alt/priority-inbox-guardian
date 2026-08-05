import sqlite3
con = sqlite3.connect('email.db')
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

res = cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
print(res.fetchall())

con.close() 