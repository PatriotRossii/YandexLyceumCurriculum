import datetime

import sqlalchemy
from flask_restful import reqparse

USER_FIELDS = ["id", "team_leader", "job", "work_size",
               "collaborators", "start_date", "end_date",
               "is_finished"]


parser = reqparse.RequestParser()
parser.add_argument("id", required=True, type=int)
parser.add_argument("team_leader", required=True, type=int)
parser.add_argument("job", required=True, type=str)
parser.add_argument("work_size", required=True, type=int)
parser.add_argument("collaborators", required=True, type=str)
parser.add_argument("start_date", required=True, type=datetime.datetime)
parser.add_argument("end_date", required=True, type=datetime.datetime)
parser.add_argument("is_finished", required=True, type=bool)
