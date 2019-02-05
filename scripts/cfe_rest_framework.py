import requests
import json
import os

ENDPOINT = "http://127.0.0.1:8000/api/status/"
AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/jwt/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + 'refresh/'
data = {'username': "admin", 'password': "pass1234"}
r = requests.post(AUTH_ENDPOINT, data=data)
token = r.json()['token']
print(token, r.headers)

# headers = {'content-type': "application/json"}
# r = requests.post(url=REFRESH_ENDPOINT, data=json.dumps({'token': token}), headers=headers)
# token = r.json()
# print(token)


# image_path = os.path.join(os.getcwd(), "logo.jpg")

# get_endpoint = ENDPOINT + str(14)
# r = requests.get(get_endpoint)
# print(r.status_code)

# post_data = json.dumps({"contents": "Some random contents"})
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
