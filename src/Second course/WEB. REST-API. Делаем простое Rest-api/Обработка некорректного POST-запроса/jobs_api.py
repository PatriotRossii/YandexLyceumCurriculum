import flask
from flask import jsonify, request

from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs', methods=['POST'])
def add_job():
    if not request.json:
        return jsonify({"error": "Empty request"})
    elif not all(key in request.json for key in
                 ['id', 'team_leader', 'job', 'work_size',
                  'collaborators', 'start_date',
                  'end_date', 'is_finished']):
        return jsonify({"error": "Bad request"})

    db_sess = db_session.create_session()

    if db_sess.query(Jobs).get(request.json['id']):
        return jsonify({"error": "Id already exists"})

    jobs = Jobs(
        **request.json
    )
    db_sess.add(jobs)
    db_sess.commit()
    return jsonify({"success": "OK"})
