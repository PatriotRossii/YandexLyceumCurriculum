import os

from flask import Flask
from flask_restful import Api

from app.data.users_resource import UsersListResource, UsersResource
from app.data import db_session

app = Flask(__name__)

api = Api(app)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

api.add_resource(UsersListResource, '/api/v2/users')
api.add_resource(UsersResource, '/api/v2/users/<int:user_id>')

if __name__ == "__main__":
    db_session.global_init("app/db/people.db")
    app.run("127.0.0.1", 8080)
