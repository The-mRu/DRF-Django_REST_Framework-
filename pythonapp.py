# 3rd party app to access database

import requests

URL="http://127.0.0.1:8000/demoInfo/4"

response = requests.get(url=URL)
data=response.json()
print(data)