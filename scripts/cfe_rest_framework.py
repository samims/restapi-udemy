import requests
import json
import os

AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/register/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"
ENDPOINT = "http://127.0.0.1:8000/api/status/"
# AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/register"
data = {'username': "sam1",'email': "sam1@example.com", 'password': "pass1234", "password2": "pass1234"}
headers = {
    "content-type": "application/json",
    # "Authorization": "JWT " + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTQ5NjI2MTA3LCJlbWFpbCI6ImFkbWluQGV4YW1wbGUuY29tIiwib3JpZ19pYXQiOjE1NDk2MjU4MDd9.Q7PwzubNN6YcFmk3fqiuxpc1xVX0eYnfdyCDxj5kN3w'}
}
r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
# token = r.json()['token']
print(r)
print(r.json())

# REFRESH_ENDPOINT = AUTH_ENDPOINT + 'refresh/'

# r = requests.post(url=REFRESH_ENDPOINT, data=json.dumps({'token': token}), headers=headers)
# token = r.json()
# print(token)


image_path = os.path.join(os.getcwd(), "logo.jpg")

# get_endpoint = ENDPOINT + str(14)
# r = requests.get(get_endpoint)
# print(r.status_code)

# headers = {"Authorization": "JWT " + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTQ5NjIxMzUzLCJlbWFpbCI6ImFkbWluQGV4YW1wbGUuY29tIiwib3JpZ19pYXQiOjE1NDk2MjEwNTN9.S36KymSxMXuQYxczpjKB1E4Jl9tcEhBiILnHr42UtE8', 'user': 'admin', 'expires': '2019-02-15T10:14:13.476219Z'}
#
# post_data = {"content": "Updated random contents"}
# with open(image_path, 'rb') as image:
#     file_data = {
#         'image': image
#     }
#     # posted_response = requests.post(ENDPOINT, data=post_data, files=file_data, headers=headers)
#     posted_response = requests.put(ENDPOINT +"25/", data=post_data, files=file_data, headers=headers)
#     print(posted_response.text)
#     get_endpoint = ENDPOINT + str(12)

# post_headers = json.dumps({'content-type': 'application/json'})
# r = requests.post(ENDPOINT, data=post_data)
# print(r.text, "status: ", r.status_code)

# def do_img(method='get', data=dict(), is_json=True, image_path=None):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     if image_path is not None:
#         with open(image_path, 'rb') as image:
#             file_data = {
#                 'image': image
#             }
#             r = requests.request(method, ENDPOINT, data=data, files=file_data, headers=headers)
#     else:
#         r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r
#
#
# do_img(method='put', data={'user': 1, 'id': 1, 'content': 'First post', }, is_json=False, image_path=image_path)
#
#
# def do(method='get', data={}, is_json=True):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     # print(r.json())
#     return r
#
# # do(data={'id': 7})
#
# # do(method='delete', data={'id': 7})
# # do(method='put', data={'id': 6, 'user': 1, 'content': 'Changing through script'})
# # do(method='post', data={'user': 1, 'content': 'Posted through scriptsss'})
