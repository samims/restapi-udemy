import json
import requests
import os


AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/register/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"
ENDPOINT = "http://127.0.0.1:8000/api/status/"

image_path = os.path.join(os.getcwd(), "logo.jpg")

headers = {
    "Content-Type": "application/json",
    #"Authorization": "JWT " + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImNmZSIsImV4cCI6MTUxMzIwNjEwOSwiZW1haWwiOiIiLCJvcmlnX2lhdCI6MTUxMzIwNTgwOX0.JCIM7Es7-pJpKVv4-OrEjCFVYsIegRxELu6YATayu7k',
}

data = {
    'username': 'ab2',
    'email': 'ab2@example.com',
    'password': 'learncode',
    'password2': 'learncode'
}

r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
print(r.text)
# import requests
# import json
# import os
#
# AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/register/"
# REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"
# ENDPOINT = "http://127.0.0.1:8000/api/status/"
# # AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/register"
# data = {'username': "sam1",'email': "sam1@example.com", 'password': "pass1234", "password2": "pass1234"}
# headers = {
#     "content-type": "application/json",
# }
# r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
# print(r)
# print(r.json())