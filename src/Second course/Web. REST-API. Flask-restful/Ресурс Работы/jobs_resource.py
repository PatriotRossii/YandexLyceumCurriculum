from flask_restful import reqparse, abort, Api, Resource
from flask import jsonify

from . import db_session
from .jobs import Jobs

from parser import parser


class JobsListResource(Resource):
    def get(self):
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).all()
        return jsonify(
            {
                'jobs':
                    [item.to_dict() for item in jobs]
            }
        )


class JobsResource(Resource):
    def get(self):
        args = parser.parse_args()

        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).get(args["job_id"])
        if not jobs:
            return jsonify({"error": "Not found"})
        return jsonify(
            {
                'jobs': jobs.to_dict()
            }
        )

    def post(self):
        args = parser.parse_args()

        if not args:
            return jsonify({"error": "Empty request"})
        elif not all(key in args for key in
                     ['id', 'team_leader', 'job', 'work_size',
                      'collaborators', 'start_date',
                      'end_date', 'is_finished']):
            return jsonify({"error": "Bad request"})

        db_sess = db_session.create_session()
        jobs = Jobs(
            **args
        )
        db_sess.add(jobs)
        db_sess.commit()
        return jsonify({"success": "OK"})

    def delete(self):
        args = parser.parse_args()

        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).get(args["job_id"])

        if not jobs:
            return jsonify({'error': 'Not found'})
        db_sess.delete(jobs)
        db_sess.commit()
        return jsonify({'success': 'OK'})

    def put(self):
        args = parser.parse_args()

        if not args:
            return jsonify({"error": "Empty request"})
        elif not all(key in args for key in
                     ['id', 'team_leader', 'job', 'work_size',
                      'collaborators', 'start_date',
                      'end_date', 'is_finished']):
            return jsonify({"error": "Bad request"})

        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).get(args["job_id"])

        if not jobs:
            return jsonify({'error': 'Not found'})

        jobs.update(args)
        db_sess.commit()
        return jsonify({'success': 'OK'})
