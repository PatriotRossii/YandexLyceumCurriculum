from datetime import datetime

import requests
from flask import jsonify

r = requests.post(
    "http://127.0.0.1:8080/api/jobs"
)  # Некорректный запрос. Ибо пустой.
assert r.json() == jsonify({"error": "Empty request"})

r = requests.post(
    "http://127.0.0.1:8080/api/jobs",
    params={
        "id": 1, "team_leader": 2, "job": "description",
        "work_size": 1, "collaborators": "1,2",
        "start_date": datetime.now(), "end_date": datetime.now(),
    }
)  # Некорректный запрос. Ибо не передано поле is_finished.
assert r.json() == jsonify({"error": "Bad request"})

r = requests.post(
    "http://127.0.0.1:8080/api/jobs",
    params={
        "id": 1, "team_leader": 2, "job": "description",
        "work_size": 1, "collaborators": "1,2",
        "start_date": datetime.now(), "end_date": datetime.now(),
        "is_finished": False
    }
)  # Корректный запрос. Переданы все необходимые поля
assert r.json() == jsonify({"success": "OK"})

r = requests.post(
    "http://127.0.0.1:8080/api/jobs",
    params={
        "id": 1, "team_leader": 2, "job": "description",
        "work_size": 1, "collaborators": "1,2",
        "start_date": datetime.now(), "end_date": datetime.now(),
        "is_finished": False
    }
)  # Некорректный запрос. Работа с таким id уже существует
assert r.json() == jsonify({"error": "Id already exists"})
