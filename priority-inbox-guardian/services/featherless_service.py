import os
from dotenv import load_dotenv
# load environment 
load_dotenv()
# read api key
API_KEY = os.getenv("FEATHERLESS_API_KEY")

def classify_email_with_llm(subject, body):
    print(f"Using API key: {API_KEY is not None}")
    text = (subject + " " + body).lower()
    if "urgent" in text or "deadline" in text:
        return{
            "summary": "Complete application before 10 August",
            "tag": "career",
            "urgency": "action",
            "status": "classified",
            "task_description": "Complete BlackRock application",
            "due_date": "2026-08-10",
            "remind_at": "2026-08-08"
        }
        
    return{
        "summary": "General informational email",
        "tag": "general",
        "urgency": "info",
        "status": "classified",
        "task_description": None,
        "due_date": None,
        "remind_at": None
    }