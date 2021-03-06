import datetime

from flask import app, redirect, render_template, request, make_response


@app.route("/jobs", methods=['GET', 'POST'])
def jobs():
    form = JobsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()

        new_job = Jobs()

        new_job.team_leader = form.team_leader.data
        new_job.job = form.job.data
        new_job.work_size = form.work_size.data
        new_job.collaborators = form.collaborators.data

        new_job.start_date = datetime.datetime.now()
        new_job.end_date = None

        new_job.is_finished = form.is_finished.data

        db_sess.add(new_job)
        db_sess.commit()

        return redirect("/")
    return render_template("jobs.html", title="Создание работы", form=form)
