from flask_restful import Resource, abort
from flask import jsonify

from . import db_session
from .users import User

from .users_parser import parser

USER_FIELDS = ["id", "surname", "name", "age",
               "position", "speciality", "address",
               "email", "hashed_password"]


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    users = session.query(User).get(user_id)
    if not users:
        abort(404, message="Not Found")


def bad_request():
    abort(404, message="Bad Request")


def empty_request():
    abort(404, message="Empty Request")


class UsersListResource(Resource):
    def get(self):
        db_sess = db_session.create_session()
        users = db_sess.query(User).all()
        return jsonify(
            {
                'users':
                    [item.to_dict() for item in users]
            }
        )

    def post(self):
        args = parser.parse_args()

        if not args:
            empty_request()
        elif not all(key in args for key in
                     USER_FIELDS):
            bad_request()

        db_sess = db_session.create_session()
        user = User(
            **args
        )
        db_sess.add(user)
        db_sess.commit()
        return jsonify({"success": "OK"})


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)

        db_sess = db_session.create_session()
        users = db_sess.query(User).get(user_id)
        return jsonify(
            {
                'users': users.to_dict()
            }
        )

    def put(self, user_id):
        args = parser.parse_args()

        if not args:
            empty_request()
        elif not all(key in args for key in
                     USER_FIELDS):
            bad_request()

        abort_if_user_not_found(user_id)

        db_sess = db_session.create_session()
        user = db_sess.query(User).get(user_id)

        for key, value in args.items():
            setattr(user, key, value)

        db_sess.commit()
        return jsonify({'success': 'OK'})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)

        db_sess = db_session.create_session()
        user = db_sess.query(User).get(user_id)

        db_sess.delete(user)
        db_sess.commit()
        return jsonify({'success': 'OK'})

