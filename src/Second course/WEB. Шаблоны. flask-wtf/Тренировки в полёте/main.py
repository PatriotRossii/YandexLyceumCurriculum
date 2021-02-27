from flask import Flask, render_template, url_for
import random

app = Flask(__name__, template_folder="")


@app.route("/training/<prof>")
def training(prof):
    words = prof.split()
    src = url_for('static', filename="img/" + ("ing.jpg" if "инженер" in words or "строитель" in words else "sci.jpg"))
    return render_template('training.html', title="Симуляторы", source=src)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
