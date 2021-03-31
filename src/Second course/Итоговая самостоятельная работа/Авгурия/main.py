import requests
import json


def creatures_accounting(host, port, **kwargs):
    r = requests.get(f"http://{host}:{port}")
    data = json.loads(r.text)

    exists = False
    for element in data:
        if element.keys() == kwargs.keys():
            exists = True

    if not exists:
        data.append(
            kwargs
        )

    return data
