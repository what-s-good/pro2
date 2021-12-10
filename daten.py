from datetime import datetime
import json


def speichern(datei, key, pflanze, giessen, wasser):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(key)] = {
        "Pflanze": pflanze,
        "Giessen": giessen,
        "Wasser": wasser
    }

    # print(datei_inhalt)

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)


def aktivitaet_speichern(pflanze, giessen, wasser):
    datei_name = "pflanzendaten.json"
    zeitpunkt = datetime.now()
    speichern(datei_name, zeitpunkt, pflanze, giessen, wasser)
    return zeitpunkt, pflanze, giessen, wasser


def aktivitaeten_laden():
    datei_name = "aktivitaeten_2.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt
