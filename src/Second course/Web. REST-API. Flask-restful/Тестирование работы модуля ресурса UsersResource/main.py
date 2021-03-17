import datetime
import unittest

from data import db_session
from data.users import User

import requests

db_sess = db_session.create_session()


class TestUsersListResource(unittest.TestCase):
    def test_get_all(self):
        resp = requests.get("127.0.0.1:8080/api/v2/users").json()

        users = db_sess.query(User).all()
        self.assertEqual(
            {
                'users':
                    [item.to_dict() for item in users]
            },
            resp
        )


class TestUserResource(unittest.TestCase):
    def test_get_invalid(self):
        resp = requests.get("127.0.0.1:8080/api/v2/users/5")

        self.assertEqual(
            {"error": "Bad request"},
            resp.json()
        )

    def test_get_valid(self):
        resp = requests.get("127.0.0.1:8080/api/v2/users/1")

        user = db_sess.query(User).get(1)
        self.assertEqual(
            {
                "users": user.to_dict()
            },
            resp.json()
        )

    def test_post_valid(self):
        resp = requests.post("127.0.0.1:8080/api/v2/users", params={
            "id": 2021, "surname": "Henry", "name": "James", "age": 18, "position": "True",
            "speciality": "False", "address": "Russia", "email": "email@com", "hashed_password": "hash",
            "modified_date": datetime.datetime.now()})

        self.assertEqual(
            {"success": "OK"},
            resp.json()
        )

    def test_post_empty(self):
        resp = requests.post("127.0.0.1:8080/api/v2/users")
        self.assertEqual(
            {"error": "Empty request"},
            resp.json()
        )

    def test_post_invalid(self):
        resp = requests.post("127.0.0.1:8080/api/v2/users", params={
            "id": 2021, "surname": "Henry", "name": "James", "age": 18, "position": "True",
            "speciality": "False", "address": "Russia", "email": "email@com", "hashed_password": "hash"})

        self.assertEqual(
            {"error": "Bad request"},
            resp.json()
        )

    def test_put_valid(self):
        resp = requests.put("127.0.0.1:8080/api/v2/users/1",
        {
            "id": 1,
            "surname": "Jane", "name": "Cooper", "age": 18,
            "position": "captain", "speciality": "research engineer",
            "address": "module_1", "email": "jane_chief@mars.org",
            "modified_date": datetime.datetime.now()
        })

        self.assertEqual(
            {"success": "OK"},
            resp.json()
        )

    def test_put_empty(self):
        resp = requests.put("127.0.0.1:8080/api/v2/users/1")

        self.assertEqual(
            {"error": "Empty request"},
            resp.json()
        )

    def test_put_invalid(self):
        resp = requests.put("127.0.0.1:8080/api/v2/users/1",
        {
            "id": 1,
            "surname": "Jane", "name": "Cooper", "age": 18,
            "position": "captain", "speciality": "research engineer",
            "address": "module_1", "email": "jane_chief@mars.org",
        })

        self.assertEqual(
            {"error": "Bad request"},
            resp.json()
        )

    def test_delete_invalid(self):
        resp = requests.delete("127.0.0.1:8080/api/v2/users/1012")
        self.assertEqual(
            {'error': 'Not found'},
            resp.json()
        )

    def test_delete_valid(self):
        resp = requests.delete("127.0.0.1:8080/api/v2/users/1")

        self.assertEqual(
            {"success": "OK"},
            resp.json()
        )


if __name__ == "__main__":
    db_session.global_init("db/test_database.db")

    captain = User()
    captain.surname = "Scott"
    captain.name = "Ridley"
    captain.age = 21
    captain.position = "captain"
    captain.speciality = "research engineer"
    captain.address = "module_1"
    captain.email = "scott_chief@mars.org"

    colonist = User()
    colonist.surname = "Washington"
    colonist.name = "George"
    colonist.age = 25
    colonist.position = "navigator"
    colonist.speciality = "engineer"
    colonist.address = "module_2"
    colonist.email = "washigton_george@mars.org"

    db_sess.add(captain)
    db_sess.add(colonist)
    db_sess.commit()

    unittest.main()
