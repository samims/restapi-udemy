import json
import requests
import os


# AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/register/"
AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"
ENDPOINT = "http://127.0.0.1:8000/api/status/"

image_path = os.path.join(os.getcwd(), "logo.jpg")

headers = {
    "Content-Type": "application/json",
    # "Authorization": "JWT " + "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyNiwidXNlcm5hbWUiOiJhYjExIiwiZXhwIjoxNTQ5NzM0Mjk3LCJlbWFpbCI6ImFiMTFAZXhhbXBsZS5jb20iLCJvcmlnX2lhdCI6MTU0OTczMzk5N30.HLpgKTXPhze51sxl9YbWC0YY9oH_1cSHzL4L3YI6mOo"
}

data = {
    'username': 'admin',
    'email': 'admin@example.com',
    'password': 'pass1234',
    'password2': 'pass1234'
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