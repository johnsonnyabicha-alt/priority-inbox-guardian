import requests
import os
from dotenv import load_dotenv
import json
# load environment 
load_dotenv()
# read api key
API_KEY = os.getenv("FEATHERLESS_API_KEY")
print("API key loaded:", API_KEY is not None)
print("API key preview:", API_KEY[:8] + "...")
# featherless ai endpoint
API_URL = "https://api.featherless.ai/v1/chat/completions"
def build_payload(subject,body):
    prompt = f"""
You are an email classification assistant.

Assume the current year is 2026.

Use these tagging rules:
- career: jobs, internships, placements, applications, recruiters, companies
- academic: coursework, exams, assignments, lectures, university administration
- finance: payments, invoices, subscriptions, rent, banking
- general: everything else

Return ONLY valid JSON with the exact structure:
{{
    "summary": "one sentence summary",
    "tag": "career | finance | academic | general",
    "urgency": "action | info",
    "status": "classified",
    "task_description": "future task or null",
    "due_date": "YYYY-MM-DD or null",
}}
Email subject = {subject}

Email body:
{body}
"""
    
    return {
        "model": "deepseek-ai/DeepSeek-V3-0324",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.2
    }   
def send_request_to_ai(payload):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type":"application/json"
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    print(f"HTTP status: {response.status_code}")
    try:
        response.raise_for_status()
    except requests.HTTPError:
        print("Server response:")
        print(response.text)
        raise
    
    data = response.json()
    content = data["choices"][0]["message"]["content"].strip()

    print("Raw model response:")
    print(content)

    # Remove Markdown code fences if present
    if content.startswith("```"):
        content = (
            content.replace("```json", "")
                .replace("```", "")
                .strip()
        )

    return json.loads(content)
def generate_reply_draft(subject, body):
    prompt = f"""
You are a professional email assistant.

Write a concise, polite reply to this email.

Do not include placeholders such as [Sender's Name] or [Your Name].
Sign the email as:

Johnson Nyabicha

Email subject: {subject}

Email body:
{body}

Return only the draft text.
"""

    payload = {
        "model": "deepseek-ai/DeepSeek-V3-0324",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.4
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()

    data = response.json()
    return data["choices"][0]["message"]["content"].strip()    
def classify_email_with_llm(subject, body):
    print(f"Using API key: {API_KEY is not None}")
    payload = build_payload(subject, body)

    print("Payload being sent to AI service:")
    print(payload)
    
    return send_request_to_ai(payload)

if __name__ == '__main__':
    result = classify_email_with_llm(
        "Application Deadline Reminder",
        "Please complete your application before 10 August."
    )

    print("\nClassification Result:")
    print(result)