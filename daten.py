import json
import datetime


def speichern(datei, key, pflanze, giessen, wasser, sonstig):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = []

    datei_inhalt.append ({
        "Pflanze": pflanze,
        "Datum": str(key),
        "Giessen": giessen,
        "Wasser": wasser,
        "Sonstiges": sonstig
    })

    with open("pflanzendaten.json", "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)

def aufgabe_speichern(pflanze, wasser, sonstiges, datum):
    try:
        with open("aufgaben.json") as open_file:
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

    with open("aufgaben.json", "w") as open_file:
        json.dump(aufgabe_inhalt, open_file, indent=4)


def aktivitaet_speichern(pflanze, giessen, wasser, sonstig):
    datei_name = "pflanzendaten.json"
    zeitpunkt = str(datetime.date.today())
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
