import datetime
import os
import unittest

from app.data import db_session
from app.data.users import User

import requests

db_session.global_init("app/db/test_database.db")
db_sess = db_session.create_session()

empty_request_message = {'message': {'id': 'Missing required parameter in the JSON body or the post '
                                           'body or the query string'}}
bad_request_message = {'message': {'hashed_password': 'Missing required parameter in the JSON body '
                                                          'or the post body or the query string'}}


class Test01_UsersListResource(unittest.TestCase):
    def test_get_all(self):
        resp = requests.get("http://127.0.0.1:8080/api/v2/users").json()

        users = db_sess.query(User).all()
        self.assertEqual(
            {
                'users':
                    [item.to_dict() for item in users]
            },
            resp
        )

    def test_post_valid(self):
        resp = requests.post("http://127.0.0.1:8080/api/v2/users", params={
            "id": 2021, "surname": "Henry", "name": "James", "age": 18, "position": "True",
            "speciality": "False", "address": "Russia", "email": "email@com", "hashed_password": "hash"})

        self.assertEqual(
            {"success": "OK"},
            resp.json()
        )

    def test_post_empty(self):
        resp = requests.post("http://127.0.0.1:8080/api/v2/users")
        self.assertEqual(
            empty_request_message,
            resp.json()
        )

    def test_post_invalid(self):
        resp = requests.post("http://127.0.0.1:8080/api/v2/users", params={
            "id": 2021, "surname": "Henry", "name": "James", "age": 18, "position": "True",
            "speciality": "False", "address": "Russia", "email": "email@com"})

        self.assertEqual(
            bad_request_message,
            resp.json()
        )


class Test02_UserResource(unittest.TestCase):
    def test_01_get_invalid(self):
        resp = requests.get("http://127.0.0.1:8080/api/v2/users/5")

        self.assertEqual(
            {"message": "Not Found"},
            resp.json()
        )

    def test_02_get_valid(self):
        resp = requests.get("http://127.0.0.1:8080/api/v2/users/2")

        user = db_sess.query(User).get(2).to_dict()
        self.assertEqual(
            {
                "users": user
            },
            resp.json()
        )

    def test_03_put_valid(self):
        resp = requests.put("http://127.0.0.1:8080/api/v2/users/2",
                            {
                                "id": 2,
                                "surname": "Jane", "name": "Cooper", "age": 18,
                                "position": "captain", "speciality": "research engineer",
                                "address": "module_1", "email": "jane_chief@mars.org",
                                "hashed_password": "correct_hash",
                            })

        self.assertEqual(
            {"success": "OK"},
            resp.json()
        )

    def test_04_put_empty(self):
        resp = requests.put("http://127.0.0.1:8080/api/v2/users/1")

        self.assertEqual(
            empty_request_message,
            resp.json()
        )

    def test_05_put_invalid(self):
        resp = requests.put("http://127.0.0.1:8080/api/v2/users/1",
                            {
                                "id": 1,
                                "surname": "Jane", "name": "Cooper", "age": 18,
                                "position": "captain", "speciality": "research engineer",
                                "address": "module_1", "email": "jane_chief@mars.org",
                            })

        self.assertEqual(
            bad_request_message,
            resp.json()
        )

    def test_06_delete_invalid(self):
        resp = requests.delete("http://127.0.0.1:8080/api/v2/users/1012")
        self.assertEqual(
            {'message': 'Not Found'},
            resp.json()
        )

    def test_07_delete_valid(self):
        resp = requests.delete("http://127.0.0.1:8080/api/v2/users/1")

        self.assertEqual(
            {"success": "OK"},
            resp.json()
        )


if __name__ == "__main__":
    for user in db_sess.query(User).all():
        db_sess.delete(user)
    db_sess.commit()

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
