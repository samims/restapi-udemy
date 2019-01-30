import requests
import json

ENDPOINT = "http://127.0.0.1:8000/api/status/"


def do(method='get', data={}, is_json=True):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    # print(r.json())
    return r


# do(data={'id': 7})

do(method='delete', data={'id': 14})
# do(method='put', data={'id': 6, 'user': 1, 'content': 'Changing through script'})
# do(method='post', data={'user': 1, 'content': 'Posted through scriptsss'})
