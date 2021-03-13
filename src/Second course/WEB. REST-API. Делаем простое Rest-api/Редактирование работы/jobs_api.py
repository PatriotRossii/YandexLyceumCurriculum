import flask
from flask import jsonify, request

from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['PUT'])
def edit_jobs(jobs_id):
    if not request.json:
        return jsonify({"error": "Empty request"})
    elif not all(key in request.json for key in
                 ['id', 'team_leader', 'job', 'work_size',
                  'collaborators', 'start_date',
                  'end_date', 'is_finished']):
        return jsonify({"error": "Bad request"})

    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(jobs_id)

    if not jobs:
        return jsonify({'error': 'Not found'})

    jobs.update(request.json)
    db_sess.commit()
    return jsonify({'success': 'OK'})
