from flask import Flask
from flask import render_template
from flask import request
import daten

app = Flask("Hello World")


@app.route("/hello")
def hello():
    return render_template('index.html', name="Luca")

@app.route("/test")
def test():
    return "erfolgreich"

@app.route("/pflanzenformular", methods=['GET', 'POST'])
def pflanzenformular():
    if request.method == 'POST':
        ziel_pflanze = request.form['pflanze']

        ziel_giessen = request.form['giessen']

        ziel_wasser = request.form['wasser']

        daten.aktivitaet_speichern(ziel_pflanze, ziel_wasser, ziel_giessen)

        return render_template("index.html", pflanzenausgabe=ziel_pflanze + ", welche " + ziel_giessen + " mal gegossen werden muss, mit " + ziel_wasser + " Liter Wasser ")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)