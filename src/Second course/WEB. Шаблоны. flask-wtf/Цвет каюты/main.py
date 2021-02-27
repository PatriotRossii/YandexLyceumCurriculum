from flask import Flask, render_template, url_for
import random

app = Flask(__name__)


@app.route("/table/<sex>/<int:age>")
def table(sex, age):
    colors = {
        "male": ["#03254c", "#1167b1", "#187bcd", "#2a9df4", "#d0efff"],
        "female": ["#fc6600", "#ff7417", "#f9812a", "#d772c", "#f79862"]
    }
    return render_template('table.html', title="Таблица", color=random.choice(colors[sex]),
                           source=url_for('static', filename="img/" + ("young.jpg" if age < 21 else "old.jpg")))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
