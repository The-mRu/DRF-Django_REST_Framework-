import requests

URL="http://127.0.0.1:8000/demoInfo/"

response = requests.get(url=URL)
data=response.json()
print(data)