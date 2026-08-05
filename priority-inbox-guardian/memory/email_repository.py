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
    "2026-08-05T12:00:00",
))

con.commit()

res = cur.execute("SELECT email_id, subject, summary, urgency FROM emails")
print(res.fetchall())

con.close() 