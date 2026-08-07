import requests
print("Sending test request...")
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print("Status:", response.status_code)
if response.status_code == 200:
    data = response.json()
    print("title:", data['title'])
    print("completed", data['completed'])
else:
    print("Request failed")