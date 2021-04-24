import datetime

import requests
from data import db_session

from data.jobs import Jobs
from data.users import User
from flask import jsonify

db_session.global_init("database.db")
db_sess = db_session.create_session()

captain = User()
captain.id = 1
captain.surname = "Scott"
captain.name = "Ridley"
captain.age = 21
captain.position = "captain"
captain.speciality = "research engineer"
captain.address = "module_1"
captain.email = "scott_chief@mars.org"

job = Jobs()
job.id = 1
job.team_leader = 1
job.job = "deployment of residental modules 1 and 2"
job.work_size = 15
job.collaborators = "2, 3"
job.start_date = datetime.datetime.now()
job.is_finished = False

db_sess.add(captain)
db_sess.add(job)
db_sess.commit()

r = requests.put("http://127.0.0.1:8080/api/jobs/1",
                 params=
                 {
                     "id": 1, "team_leader": 1, "job": "new job",
                     "work_size": 3, "collaborators": "1,2",
                     "start_date": datetime.datetime.now(),
                     "end_date": datetime.datetime.now() + datetime.timedelta(1),
                     "is_finished": False
                 })
assert r.json() == jsonify({"success": "OK"})

r = requests.put("http://127.0.0.1:8080/api/jobs/2020")
assert r.json() == jsonify({"error": "Not found"})

r = requests.put("http://127.0.0.1:8080/api/jobs/1")
assert r.json() == jsonify({"error": "Empty request"})

r = requests.put("http://127.0.0.1:8080/api/jobs/1",
                 params=
                 {
                     "id": 1, "team_leader": 1, "job": "new job",
                     "work_size": 3, "collaborators": "1,2",
                     "start_date": datetime.datetime.now(),
                     "end_date": datetime.datetime.now() + datetime.timedelta(1),
                 })
assert r.json() == jsonify({"error": "Bad request"})

r = requests.get("http://127.0.0.1:8080/api/jobs")
assert r.json() == jsonify(
    {
        "jobs": [
            {
                "id": 1, "team_leader": 1, "job": "new job",
                "work_size": 3, "collaborators": "1,2",
                "start_date": datetime.datetime.now(),
                "end_date": datetime.datetime.now() + datetime.timedelta(1),
            }
        ]
    }
)
