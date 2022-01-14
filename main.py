from flask import Flask
from flask import render_template
from flask import request
import daten
from daten import pflanzen_laden

app = Flask("Hello World")


@app.route("/")
def hello():
    return render_template('start.html', name="Luca")


@app.route("/pflanzenformular", methods=['GET', 'POST'])
def pflanzenformular():
    if request.method == 'POST':
        ziel_pflanze = request.form['pflanze']

        ziel_giessen = request.form['giessen']

        ziel_wasser = request.form['wasser']

        daten.aktivitaet_speichern(ziel_pflanze, ziel_wasser, ziel_giessen)

        return render_template("index.html", pflanzenausgabe="Du hast " + ziel_pflanze + ", welche " + ziel_giessen + " mal mit " + ziel_wasser + " Deziliter Wasser gegossen werden muss.")

    return render_template("index.html")


@app.route("/garten", methods=['GET'])
def garten():
    stockladen = pflanzen_laden()
    return render_template('garten.html', stockladen = stockladen)

@app.route("/aufgaben")
def aufgaben():
    return render_template('aufgaben.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)