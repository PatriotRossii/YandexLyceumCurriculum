from flask_restful import reqparse, abort, Api, Resource
from flask import jsonify

from . import db_session
from .users import User

from parser import parser

USER_FIELDS = ["id", "surname", "name", "age",
               "position", "speciality", "address",
               "email", "hashed_password", "modified_date"]


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    news = session.query(User).get(user_id)
    if not news:
        return jsonify({'error': 'Not found'})


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


class UsersResource(Resource):
    def get(self):
        args = parser.parse_args()
        user_id = args['user_id']

        return abort_if_user_not_found(user_id)

        db_sess = db_session.create_session()
        users = db_sess.query(User).get(user_id)
        return jsonify(
            {
                'users': users.to_dict()
            }
        )

    def put(self):
        args = parser.parse_args()
        user_id = args['user_id']

        if not args:
            return jsonify({"error": "Empty request"})
        elif not all(key in args for key in
                     USER_FIELDS):
            return jsonify({"error": "Bad request"})

        return abort_if_user_not_found(user_id)

        db_sess = db_session.create_session()
        user = db_sess.query(User).get(user_id)

        user.update(args)
        db_sess.commit()
        return jsonify({'success': 'OK'})

    def delete(self):
        args = parser.parse_args()
        user_id = args['user_id']

        return abort_if_user_not_found(user_id)

        db_sess = db_session.create_session()
        user = db_sess.query(User).get(user_id)

        db_sess.delete(user)
        db_sess.commit()
        return jsonify({'success': 'OK'})

    def post(self):
        args = parser.parse_args()

        if not args:
            return jsonify({"error": "Empty request"})
        elif not all(key in args for key in
                     USER_FIELDS):
            return jsonify({"error": "Bad request"})

        db_sess = db_session.create_session()
        user = User(
            **args
        )
        db_sess.add(user)
        db_sess.commit()
        return jsonify({"success": "OK"})
