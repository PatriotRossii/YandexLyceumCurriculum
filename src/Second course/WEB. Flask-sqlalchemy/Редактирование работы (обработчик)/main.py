import datetime

from flask import app, abort, redirect, render_template, request
from flask_login import login_required


@app.route('/jobs/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_jobs(id):
    form = JobsForm()

    if request.method == "GET":
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter((Jobs.id == id,
                                           (Jobs.team_leader == current_user.id) | current_user.id == 1)
                                          ).first()
        if jobs:
            form.team_leader = jobs.team_leader
            form.job = jobs.job
            form.work_size = jobs.work_size
            form.collaborators = jobs.collaborators
            form.is_finished = jobs.is_finished
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter((Jobs.id == id,
                                           (Jobs.team_leader == current_user.id) | current_user.id == 1)
                                          ).first()
        if jobs:
            jobs.team_leader = form.team_leader.data
            jobs.job = form.job.data
            jobs.work_size = form.work_size.data
            jobs.collaborators = form.collaborators.data
            jobs.is_finished = form.is_finished.data

            if jobs.is_finished:
                jobs.end_date = datetime.datetime.now()

            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('jobs.html',
                           title='Редактирование работы',
                           form=form
                           )
