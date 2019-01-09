import requests
import json

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/updates/"


def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    status_code = r.status_code
    print(status_code)
    if status_code != 404:
        print("Probably good enough!")
    data = r.json()
    print(type(json.dumps(data)))
    for obj in data:
        print(obj["id"])
        if obj['id'] == 1:
            r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']))
            # print(dir(r2))
            print(r2.json())
    return data


def create_update():
    new_data = {
        "user": 1,
        "content": "another new content"
    }
    r = requests.delete(BASE_URL + ENDPOINT,  data=new_data)
    print(r.status_code)
    print(r.headers)
    if r.status_code == requests.codes.ok:
        print(r.text)


get_list()
create_update()
