from flask import Flask, render_template, redirect
from data import db_session
from data.users import User

from forms.register_form import RegisterForm
import hashlib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()

        if form.password.data != form.repeat_password.data:
            redirect("/register")

        new_user = User()

        new_user.surname = form.surname.data
        new_user.name = form.name.data
        new_user.age = form.age.data
        new_user.position = form.position.data
        new_user.speciality = form.speciality.data
        new_user.address = form.address.data
        new_user.email = form.email.data
        new_user.hashed_password = hashlib.md5(form.password.data.encode()).hexdigest()

        db_sess.add(new_user)
        db_sess.commit()
    return render_template("register.html", title="Регистрация", form=form)


def main():
    app.run()


if __name__ == '__main__':
    db_session.global_init("db/db.db")
    main()
