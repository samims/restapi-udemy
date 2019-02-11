import json
import os
import requests


AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"

image_path = os.path.join(os.getcwd(), "logo.jpg")
print(image_path, "###")

headers = {
    "Content-Type": "application/json",
}

data = {
    'username': 'admin',
    'password': 'pass1234'
}

r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json()['token']
print(token)


ENDPOINT = 'http://127.0.0.1:8000/api/status/'
headers = {
    # "Content-Type": "application/json",
    "Authorization": "JWT " + token
}

data2 = {
    'content': "First post using authorization"
}
if image_path is not None:
    with open(image_path, 'rb') as image:
        file_data = {
            'image': image
        }
        r = requests.post(ENDPOINT, data=data2, files=file_data, headers=headers)
        print(r.text)
