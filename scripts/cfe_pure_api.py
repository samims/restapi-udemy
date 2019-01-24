import requests
import json

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/updates/"


def get_list(id=None):
    data = json.dumps({})
    if id is not None:
        data = json.dumps({"id": id})
    data = json.dumps({"id":id})
    r = requests.get(BASE_URL + ENDPOINT, data=data)
    status_code = r.status_code
    if status_code != 200:
        print("Not good. status code is ->", status_code)
    data = r.json()
    return data


def create_update():
    new_data = {
        "user": 1,
        "content": "This is the third article"
    }
    r = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text


# print(get_list())
# print(create_update())


# print(get_object())

def do_obj_update():
    new_data = {
        "id": 6,
        "content": "New object updated data"
    }
    r = requests.put(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text


def do_obj_delete():
    new_data = {"id": 6, "content": "Some new awesome content"}
    r = requests.delete(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text


# print(do_obj_update())
# print(do_obj_update())
# print(do_obj_delete())
ENDPOINT = 'api/books/'


def create_book():
    url =  BASE_URL + ENDPOINT
    data = {
        "title": "First Book",
        "isbn": "xbcnd,d"
    }
    r = requests.post(url, data=data)# json.dumps(data))
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text

print(create_book())