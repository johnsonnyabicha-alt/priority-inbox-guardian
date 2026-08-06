from memory.email_repository import (
    initialize_database,
    email_exists,
    save_email
)
# stimulating workflow using Python logic
def process_incoming_email(email_event):
    message_id = email_event["message_id"]
    subject = email_event["subject"]
    body = email_event["body"]
    
    if email_exists(message_id):
        return {
            "reason": "duplicate email",
            "stored": False
        }
    classification = classify_email(subject, body)
    save_email(
        message_id=message_id,
        sender_name=email_event["sender_name"],
        sender_email=email_event["sender_email"],
        subject=subject,
        body=body,
        summary=classification["summary"],
        tag=classification["tag"],
        urgency=classification["urgency"],
        status=classification["status"],
        received_at="2026-08-05T12:00:00",
        processed_at="2026-08-05T12:00:01"
    )
    return {
    "stored": True,
    "summary": classification["summary"],
    "urgency": classification["urgency"],
    "tag": classification["tag"]
    }
def classify_email(subject, body):
    text = (subject + " " + body).lower()

    if "urgent" in text or "deadline" in text:
        return {
            "summary": "Complete application before 10 August",
            "tag": "career",
            "urgency": "action",
            "status": "classified"
        }

    return {
        "summary": "General informational email",
        "tag": "general",
        "urgency": "info",
        "status": "classified"
    }
    
def telegram_command(command_text):
    pass

if __name__ == '__main__':
    initialize_database()
    test_email = {
        "message_id": "msg_002",
        "sender_name": "BlackRock Early Careers",
        "sender_email": "careers@blackrock.com",
        "subject": "Application Deadline Reminder",
        "body": "Please complete your application before 10 August."
    }
    result = process_incoming_email(test_email)
    print(result)