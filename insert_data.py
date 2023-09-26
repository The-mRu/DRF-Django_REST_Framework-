# 3rd party app to access database

import requests
import json

URL= "http://127.0.0.1:8000/demoCreate/"


data={
    'Name':'Rifat',
    'course_name':'Sound Box',
    'course_duration':30,
    'seat':20,
}

json_data=json.dumps(data)
r= requests.post(url=URL, data=json_data)

data=r.json()
print(data)

