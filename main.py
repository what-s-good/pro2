from flask import Flask
from flask import render_template
from flask import request
import daten
from daten import pflanzen_laden
from datetime import datetime
from datetime import date

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

        ziel_sonstig = request.form['sonstig']

        daten.aktivitaet_speichern(ziel_pflanze, ziel_wasser, ziel_giessen, ziel_sonstig)

        return render_template("index.html", pflanzenausgabe="Du hast " + ziel_pflanze + ", welche " + ziel_giessen + " mal mit " + ziel_wasser + " Deziliter Wasser gegossen werden muss.")

    return render_template("index.html")


@app.route("/garten", methods=['GET'])
def garten():
    stockladen = pflanzen_laden()
    return render_template('garten.html', stockladen = stockladen)

@app.route("/aufgaben", methods=['GET'])
def aufgaben():
    stockaufgaben = []
    for datum in pflanzen_laden():
        format = "%Y-%m-%d"
        datum1 = datetime.strptime(datum["Datum"], format) #format formatiert dass Datum
        datum_heute = datetime.strptime(str(date.today()), format)
        datumberechnet = datum_heute - datum1
        print(datumberechnet.days)
        if datumberechnet.days != 0: #die Pflanzen die heute eingegeben wurden werden nicht angezeigt
            if datumberechnet.days % int(datum["Wasser"]) == 0:
                stockaufgaben.append(datum["Pflanze"])
    return render_template('aufgaben.html', stockaufgaben = stockaufgaben)


if __name__ == "__main__":
    app.run(debug=True, port=5000)