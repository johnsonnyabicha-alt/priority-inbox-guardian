from memory.email_repository import (
    initialize_database,
    email_exists,
    save_email,
    get_email_summary,
    get_email
)
from memory.deadline_repository import(
    initialize_database as initialize_deadline_database,
    save_deadline,
    list_upcoming_deadlines 
)
from services.featherless_service import(
    classify_email_with_llm
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
    classification = classify_email_with_llm(subject, body)
    email_id = save_email(
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
    if classification["urgency"] == "action":
        save_deadline(
            email_id=email_id,
            task_description=classification["task_description"],
            due_date=classification["due_date"],
            remind_at=classification["remind_at"],
            current_tag="future_action",
            status="pending"
        )
    return {
        "stored": True,
        "summary": classification["summary"],
        "urgency": classification["urgency"],
        "tag": classification["tag"]
    }
    
def telegram_command(command_text):
    parts = command_text.split()
    # Handle empty inputs
    if not parts:
        return "Empty command"
    # First word in the command 
    command = parts[0].lower()
    # summary <email_id>
    if command == "summary":
        if len(parts) != 2:
            return "Usage: summary <email_id>"
        
        try:
            email_id = int(parts[1])
        except ValueError:
            return "Email ID must be a number."
        email = get_email_summary(email_id)

        if not email:
            return "Email not found."
        
        subject, summary, tag, urgency = email 
        return (
            f"Subject: {subject}\n"
            f"Summary: {summary}\n"
            f"Tag: {tag}\n"
            f"Urgency: {urgency}"
        )
    # deadlines
    if command == "deadlines":
        deadlines = list_upcoming_deadlines()
        if not deadlines:
            return "No upcoming deadlines."
        
        return "\n".join(
            f"[{task_id}] {description} - {due_date}"
            for task_id, description, due_date, _ in deadlines
        )
    # full email
    if command == "full":
        if len(parts) != 2:
            return "Usage: full <email_id>"
        try:
            email_id = int(parts[1])
        except ValueError:
            return "Email ID must be a number."
        
        email = get_email(email_id)
        
        if not email:
            return "Email not Found."
        
        (email_id,
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
        processed_at) = email  
        return(
            f"From: {sender_name} <{sender_email}>\n"
            f"Subject: {subject}\n\n"
            f"Body:\n{body}"
            )
    if command == "help":
        return(
            "Available commands:\n"
            "summary <email_id> - Show email summary\n"
            "full <email_id> - Show full email body\n"
            "deadlines - List upcoming deadlines\n"
            "help - Show this message"
        )        
    return "Unknown command."
    

if __name__ == '__main__':
    # initializing database 
    initialize_database()
    initialize_deadline_database()
    # stimulating incoming email
    test_email = {
        "message_id": "msg_006",
        "sender_name": "BlackRock Early Careers",
        "sender_email": "careers@blackrock.com",
        "subject": "Application Deadline Reminder",
        "body": "Please complete your application before 10 August."
    }
    
    result = process_incoming_email(test_email)
    print("=== Workflow Result ===")
    print(result)
    # telegram command test
    print("\n=== Telegram Command Tests ===")
    print(telegram_command("summary 1"))
    print()
    print(telegram_command("deadlines"))
    print()
    print(telegram_command("full 1"))
    print()
    print(telegram_command("help"))