import flask
from flask import jsonify, request

from . import db_session
from .users import User

blueprint = flask.Blueprint(
    'users_api',
    __name__,
    template_folder='templates'
)

USER_FIELDS = ["id", "surname", "name", "age",
               "position", "speciality", "address",
               "email", "hashed_password", "modified_date"]


@blueprint.route('/api/users')
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify(
        {
            'users':
                [item.to_dict() for item in users]
        }
    )


@blueprint.route('/api/users/<int:user_id>')
def get_user(user_id):
    db_sess = db_session.create_session()
    users = db_sess.query(User).get(user_id)
    if not users:
        return jsonify({"error": "Not found"})
    return jsonify(
        {
            'users': users.to_dict()
        }
    )


@blueprint.route('/api/users/<int:user_id>', methods=['PUT'])
def edit_user(user_id):
    if not request.json:
        return jsonify({"error": "Empty request"})
    elif not all(key in request.json for key in
                 USER_FIELDS):
        return jsonify({"error": "Bad request"})

    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)

    if not user:
        return jsonify({'error': 'Not found'})

    user.update(request.json)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)

    if not user:
        return jsonify({'error': 'Not found'})
    db_sess.delete(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users', methods=['POST'])
def add_user():
    if not request.json:
        return jsonify({"error": "Empty request"})
    elif not all(key in request.json for key in
                 USER_FIELDS):
        return jsonify({"error": "Bad request"})

    db_sess = db_session.create_session()
    user = User(
        **request.json
    )
    db_sess.add(user)
    db_sess.commit()
    return jsonify({"success": "OK"})
