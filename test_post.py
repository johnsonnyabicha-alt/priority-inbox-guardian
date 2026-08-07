import requests
payload = {
    "subject": "Application Deadline Reminder",
    "body": "Please complete your application before 10 August.",
    "requested_output": "summary, tag, urgency"
}
print("Sending POST request...")
response = requests.post("https://jsonplaceholder.typicode.com/posts", json = payload)
print("status", response.status_code)

if response.status_code in (200,201):
    data = response.json()
    print(data)
else:
    print("Request failed:", response.text)