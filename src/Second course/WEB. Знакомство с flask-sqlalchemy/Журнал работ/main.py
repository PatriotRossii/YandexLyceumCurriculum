import datetime

from flask import Flask, render_template
from data import db_session
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    db_sess = db_session.create_session()
    data = []

    for element in db_sess.query(Jobs).all():
        team_leader = db_sess.query(User).filter(User.id == element.team_leader).first()
        representation = f"{team_leader.surname} {team_leader.name}"
        data.append((element,
                     representation))

    return render_template("jobs.html", jobs=data)


def main():
    app.run()


if __name__ == '__main__':
    db_session.global_init("db/database.db")

    captain = User()
    captain.surname = "Scott"
    captain.name = "Ridley"
    captain.age = 21
    captain.position = "captain"
    captain.speciality = "research engineer"
    captain.address = "module_1"
    captain.email = "scott_chief@mars.org"

    colonist = User()
    colonist.surname = "Washington"
    colonist.name = "George"
    colonist.age = 25
    colonist.position = "navigator"
    colonist.speciality = "engineer"
    colonist.address = "module_2"
    colonist.email = "washigton_george@mars.org"

    doctor = User()
    doctor.surname = "Smith"
    doctor.name = "Will"
    doctor.age = 30
    doctor.position = "doctor"
    doctor.speciality = "neurobiologist"
    doctor.address = "module_3"
    doctor.email = "will_smith@mars.org"

    lead_research = User()
    lead_research.surname = "Wright"
    lead_research.name = "Apollo"
    lead_research.age = 21
    lead_research.position = "scientist"
    lead_research.speciality = "lead researcher"
    lead_research.address = "module_4"
    lead_research.email = "apollo_wright@mars.org"

    job = Jobs()
    job.team_leader = 1
    job.job = "deployment of residental modules 1 and 2"
    job.work_size = 15
    job.collaborators = "2, 3"
    job.start_date = datetime.datetime.now()
    job.is_finished = False

    db_sess = db_session.create_session()

    db_sess.add(captain)
    db_sess.add(colonist)
    db_sess.add(doctor)
    db_sess.add(lead_research)
    db_sess.add(job)

    db_sess.commit()

    main()
