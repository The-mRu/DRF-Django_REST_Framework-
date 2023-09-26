# 3rd party app to access database

import requests
import json

URL= "http://127.0.0.1:8000/demoCreate/"


data={
    #add only update fields name
    'id':10,
    'Name':'GS Tasin',
    
    
}

json_data=json.dumps(data)
r= requests.put(url=URL, data=json_data)

data=r.json()
print(data)

