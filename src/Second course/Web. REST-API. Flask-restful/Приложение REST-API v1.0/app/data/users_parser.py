import datetime

import sqlalchemy
from flask_restful import reqparse

USER_FIELDS = ["id", "surname", "name", "age",
               "position", "speciality", "address",
               "email", "hashed_password", "modified_date"]


parser = reqparse.RequestParser()
parser.add_argument("id", required=True, type=int)
parser.add_argument("surname", required=True, type=str)
parser.add_argument("name", required=True, type=str)
parser.add_argument("age", required=True, type=int)
parser.add_argument("position", required=True, type=str)
parser.add_argument("speciality", required=True, type=str)
parser.add_argument("address", required=True, type=str)
parser.add_argument("email", required=True, type=str)
parser.add_argument("hashed_password", required=True, type=str)