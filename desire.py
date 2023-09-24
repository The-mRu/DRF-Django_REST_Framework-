import requests
import json

URL= "http://127.0.0.1:8000/demoCreate/"


data={
    'Name':'kasfi',
    'course_name':'ML',
    'course_duration':30,
    'seat':'20',
}

json_data=json.dumps(data)
r= requests.post(url=URL, data=json_data)

data=r.json()
print(data)

