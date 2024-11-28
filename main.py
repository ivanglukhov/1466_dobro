from flask import Flask
from flask import render_template
import database

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/advs")
def advs():
    rows = database.get_all_adverts()
    advs = []
    for adv in rows:
        d = {}
        d['id'] = adv[0]
        d['adress'] = adv[1]
        d['header'] = adv[2]
        d['description'] = adv[3]
        d['service_mode'] = adv[4]
        d['creator'] = adv[5]
        d['image'] = adv[6]

        advs.append(d)
    return render_template("board.html", advs=advs)

@app.route("/advs/<id>")
def adv(id):
    adv = database.get_advert(id)
    d = {}
    d['id'] = adv[0]
    d['adress'] = adv[1]
    d['header'] = adv[2]
    d['description'] = adv[3]
    d['service_mode'] = adv[4]
    d['creator'] = adv[5]
    d['image'] = adv[6]

    adv = d
    return render_template('adv.html', adv=adv)

app.run()
