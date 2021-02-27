from flask import Flask, render_template

app = Flask(__name__, template_folder="")


@app.route('/list_prof/<type>')
def profession_list(type):
    if type not in ["ul", "ol"]:
        return render_template("invalid.html")

    profession_list = [
        "инженер-исследователь", "пилот", "строитель",
        "экзобиолог", "врач", "инженер по терраформированию",
        "климатолог", "специалист по радиацинной защите", "астрогеолог",
        "гляциолог", "инженер жизнеобеспечения", "метеоролог",
        "оператор марсохода", "киберинженер", "штурман",
        "пилот дронов"
    ]

    return render_template('base.html', type_=type,
                           profession_list=profession_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
