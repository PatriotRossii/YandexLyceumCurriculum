from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index/<title>')
@app.route('/<title>')
def index(title):
    return render_template('base.html', title=title,)


@app.route("/distribution")
def answer():
    user_list = [{"name": "Ридли", "surname": "Скот"}, {"name": "Энди", "surname": "Уир"},
                 {"name": "Марк", "surname": "Уотни"}, {"name": "Венката", "surname": "Капур"},
                 {"name": "Тедди", "surname": "Сандерс"}, {"name": "Шон", "surname": "Бин"}]
    return render_template('distribution.html', title="Распределение", user_list=user_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
