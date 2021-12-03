from flask import Flask
from flask import render_template
from flask import request

app = Flask("Hello World")


@app.route("/hello")
def hello():
    return render_template('index.html', name="Luca")

@app.route("/test")
def test():
    return "erfolgreich"

@app.route("/luca", methods=['GET', 'POST'])
def luca():
    if request.method == 'POST':
        ziel_pflanze = request.form['pflanze']
        rueckgabe_string1 = ziel_pflanze

        ziel_giessen = request.form['giessen']
        rueckgabe_string2 = ziel_giessen

        ziel_wasser = request.form['wasser']
        rueckgabe_string3 = ziel_wasser

        return render_template("index.html", pflanzenausgabe=rueckgabe_string1 + ", welche " + rueckgabe_string2 + " mal gegossen werden muss, mit " + rueckgabe_string3 + " Liter Wasser ")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)