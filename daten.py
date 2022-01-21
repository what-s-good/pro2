import json
import datetime


def speichern(datei, key, pflanze, giessen, wasser, sonstig): #hier werden die Daten von aktivitaet_speichern ins jsonfile geladen, als Dics (einzelne Datensaetze) in einer Liste
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = []

    datei_inhalt.append ({ #form (dic), wie die Daten gespeichert werden soll
        "Pflanze": pflanze,
        "Datum": str(key),
        "Giessen": giessen,
        "Wasser": wasser,
        "Sonstiges": sonstig
    })

    with open("pflanzendaten.json", "w") as open_file: #öffnet json und dumped datei_inhalt
        json.dump(datei_inhalt, open_file, indent=4)

def aufgabe_speichern(pflanze, wasser, sonstiges, datum): #hier werden die Daten aus dem pflanzendaten.json geholt
    try:
        with open("aufgaben.json") as open_file: #json als aufgabe_inhalt setzen (variable)
            aufgabe_inhalt = json.load(open_file)
    except FileNotFoundError:
        aufgabe_inhalt = []

    aufgabe_inhalt.append ({
        "Pflanze": pflanze,
        "Datum": str(datum),
        "Wasser": wasser,
        "Sonstiges": sonstiges
    })

    # print(datei_inhalt)

    with open("aufgaben.json", "w") as open_file: #öffnet json und dumped aufgabe_inhalt
        json.dump(aufgabe_inhalt, open_file, indent=4)


def aktivitaet_speichern(pflanze, giessen, wasser, sonstig): #hier werden die Daten aus dem Formular empfangen
    datei_name = "pflanzendaten.json"
    zeitpunkt = str(datetime.date.today()) #das Datum wird erfasst
    speichern(datei_name, zeitpunkt, pflanze, giessen, wasser, sonstig)
    return zeitpunkt, pflanze, giessen, wasser, sonstig


def pflanzen_laden():
    datei_name = "pflanzendaten.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt

def aufgaben_laden():
    datei_name = "aufgaben.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt
