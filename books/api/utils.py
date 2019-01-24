import json


def is_json(json_data):
    print("==========================================")
    try:
        json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    print(is_valid)
    return is_valid
