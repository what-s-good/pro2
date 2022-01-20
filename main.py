from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
import json
import daten
from daten import pflanzen_laden
from daten import aufgaben_laden
import datetime as dt #wäre nur datetime, hätte es probleme gegeben mit Zeile 9 und 10. Quelle: https://stackoverflow.com/questions/15707532/import-datetime-v-s-from-datetime-import-datetime
from datetime import datetime
from datetime import date

app = Flask("Hello World")

#Quelle zum allgemeinen Verständnis: https://www.youtube.com/watch?v=GgS8-mn9zoM&list=PLNmsVeXQZj7otfP2zTa8AIiNIWVg0BRqs&index=12 & https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3-de

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
        return redirect(url_for("garten"))
    return render_template("index.html")


@app.route("/garten", methods=['GET'])
def garten():
    stockladen = pflanzen_laden() #lädt Daten aus pflanzendaten.json
    return render_template('garten.html', stockladen = stockladen)


@app.route("/aufgaben", methods=['GET', 'POST'])
def aufgaben():

    with open("pflanzendaten.json") as open_file:
        pflanzendaten = json.load(open_file)

    for pflanze in pflanzendaten:
        if request.method == "POST":
            if request.form.get(pflanze["Pflanze"]) == "Erledigt": #hier prüft es, ob der Button den gleichen "name" hat wie die Pflanze
                pflanze["Datum"] = str(dt.date.today()) #hier resetet es das datum im pflanzendaten.json auf den heutigen tag

    with open("pflanzendaten.json", "w") as open_file:
        json.dump(pflanzendaten, open_file, indent=4)

    aufgabe_inhalt = [] #macht leere liste, damit aufgaben nicht mehrmals erscheinen
    with open("aufgaben.json", "w") as open_file: #gibt leere liste ins aufgaben.json
        json.dump(aufgabe_inhalt, open_file, indent=4)

    for datum in pflanzen_laden(): #Mit Nicolas Steiger angeschaut
        #https://stackoverflow.com/questions/8419564/difference-between-two-dates-in-python
        format = "%Y-%m-%d"
        datum1 = datetime.strptime(datum["Datum"], format) #format formatiert dass Datum
        datum_heute = datetime.strptime(str(date.today()), format)
        datumberechnet = datum_heute - datum1
        print(datumberechnet) #0:00:00
        print(datumberechnet.days) #0
        if datumberechnet.days != 0: #die Pflanzen die heute eingegeben wurden werden nicht angezeigt
            if datumberechnet.days % float(datum["Giessen"]) == 0: #wenn rest null ergibt

                daten.aufgabe_speichern(datum["Pflanze"], datum["Wasser"], datum["Sonstiges"], datum_heute)

    with open("aufgaben.json") as open_file:
            aufgabe_inhalt = json.load(open_file)


    return render_template('aufgaben.html', aufgabe_inhalt=aufgabe_inhalt)


if __name__ == "__main__":
    app.run(debug=True, port=5000)