import datetime
import unittest

from data import db_session
from data.jobs import Jobs

import requests

db_sess = db_session.create_session()


class TestJobsListResource(unittest.TestCase):
    def test_get_all(self):
        resp = requests.get("127.0.0.1:8080/api/jobs").json()

        jobs = db_sess.query(Jobs).all()
        self.assertEqual(
            {
                'jobs':
                    [item.to_dict() for item in jobs]
            },
            resp
        )


class TestJobsResource(unittest.TestCase):
    def test_get_invalid(self):
        resp = requests.get("127.0.0.1:8080/api/jobs/5")

        self.assertEqual(
            {"error": "Not found"},
            resp.json()
        )

    def test_get_valid(self):
        resp = requests.get("127.0.0.1:8080/api/jobs/1")

        jobs = db_sess.query(Jobs).get(1)
        self.assertEqual(
            {
                "jobs": jobs.to_dict()
            },
            resp.json()
        )

    def test_post_valid(self):
        resp = requests.post("127.0.0.1:8080/api/jobs", params={
            "id": 3, "team_leader": 1, "job": "Fix all", "work_size": 2,
            "collaborators": "1,2", "start_date": datetime.datetime.now(),
            "end_date": datetime.datetime.now() + datetime.timedelta(1), "is_finished": False
        })

        self.assertEqual(
            {"success": "OK"},
            resp.json()
        )

    def test_post_empty(self):
        resp = requests.post("127.0.0.1:8080/api/jobs")
        self.assertEqual(
            {"error": "Empty request"},
            resp.json()
        )

    def test_post_invalid(self):
        resp = requests.post("127.0.0.1:8080/api/jobs", params={
            "id": 3, "team_leader": 1, "job": "Fix all", "work_size": 2,
            "collaborators": "1,2", "start_date": datetime.datetime.now(),
            "end_date": datetime.datetime.now() + datetime.timedelta(1),
        })

        self.assertEqual(
            {"error": "Bad request"},
            resp.json()
        )

    def test_put_valid(self):
        resp = requests.put("127.0.0.1:8080/api/jobs/1", params={
            "id": 1, "team_leader": 1, "job": "Fix all", "work_size": 2,
            "collaborators": "1,2", "start_date": datetime.datetime.now(),
            "end_date": datetime.datetime.now() + datetime.timedelta(1),
        })

        self.assertEqual(
            {"success": "OK"},
            resp.json()
        )

    def test_put_empty(self):
        resp = requests.put("127.0.0.1:8080/api/jobs")

        self.assertEqual(
            {"error": "Empty request"},
            resp.json()
        )

    def test_put_invalid(self):
        resp = requests.put("127.0.0.1:8080/api/jobs/1", params={
            "id": 1, "team_leader": 1, "job": "Fix all", "work_size": 2,
            "collaborators": "1,2", "start_date": datetime.datetime.now(),
        })

        self.assertEqual(
            {"error": "Bad request"},
            resp.json()
        )

    def test_delete_invalid(self):
        resp = requests.delete("127.0.0.1:8080/api/jobs/2020")
        self.assertEqual(
            {'error': 'Not found'},
            resp.json()
        )

    def test_delete_valid(self):
        resp = requests.delete("127.0.0.1:8080/api/jobs/1")

        self.assertEqual(
            {"success": "OK"},
            resp.json()
        )


if __name__ == "__main__":
    db_session.global_init("db/test_database.db")

    job_1 = Jobs()

    job_1.id = 1
    job_1.team_leader = 2
    job_1 = "Repair broken TV"
    job_1.work_size = 1
    job_1.collaborators = "1,2,3"

    job_1.start_date = datetime.datetime.now()
    job_1.end_date = datetime.datetime.now() + datetime.timedelta(1, 2, 3)

    job_1.is_finished = False

    job_2 = Jobs()
    job_1.id = 2
    job_1.team_leader = 1
    job_1 = "Repair broken spaceship"
    job_1.work_size = 5
    job_1.collaborators = "2,3,4"

    job_1.start_date = datetime.datetime.now()
    job_1.end_date = datetime.datetime.now() + datetime.timedelta(1, 2, 3)

    job_1.is_finished = True

    db_sess.add(job_1)
    db_sess.add(job_2)
    db_sess.commit()

    unittest.main()
