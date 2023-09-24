import requests
import json

URL= "http://127.0.0.1:8000/demoCreate/"


data={
    'id':4,
    'Name':'Md Sayeem',
    'course_name':'Web development' ,
    'seat':'50'
    
    
}

json_data=json.dumps(data)
r= requests.put(url=URL, data=json_data)

data=r.json()
print(data)

