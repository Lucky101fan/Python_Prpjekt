import sqlite3

spielbrett = [
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "o", "", ""],
    ["", "x", "o", "x", "", "", ""]
]

spieler_1_name = "lukas"
spieler_2_name = "bot"
gewinner = 1


def array_to_string(arr):
    string = ""
    for row in arr:
        string += ",".join(row) + "\n"
    return string


def string_to_array(string):
    spielbrett = []
    rows = string.strip().split("\n")
    for row in rows:
        spielbrett.append(row.split(","))
    return spielbrett


def Spielstand_speichern(spieler1, spieler2, gewinner, spielbrett):
    # Array in einen String umwandeln
    string = array_to_string(spielbrett)

    # Datenbankverbindung herstellen
    conn = sqlite3.connect('datenbank/spielstand.db')
    cursor = conn.cursor()

    # Spielstand in die Datenbank einfügen
    cursor.execute("INSERT INTO spieler (spieler_1_name, spieler_2_name, gewinner, spielstand) VALUES (?, ?, ?, ?)",
                   (spieler1, spieler2, gewinner, string))

    # Datenbankverbindung schließen
    conn.commit()
    conn.close()


def Spielstand_auslesen(id):
    conn = sqlite3.connect('datenbank/spielstand.db')
    cursor = conn.cursor()

    cursor.execute("SELECT spielstand FROM spieler WHERE id=?", (id,))
    ergebnis = cursor.fetchone()

    if ergebnis is not None:
        spielbrett_string = ergebnis[0]
        spielbrett = string_to_array(spielbrett_string)

        return spielbrett

    conn.close()
    return None


def Spiele_ausgeben():
    conn = sqlite3.connect('datenbank/spielstand.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS "spieler" (
    "spieler_1_name"	TEXT,
	"spieler_2_name"	TEXT,
	"gewinner"	INT,
	"spielstand"	TEXT,
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT''')
    cursor.execute("SELECT spieler_1_name, spieler_2_name, gewinner FROM spieler")
    ergebnis = cursor.fetchall()

    spieler_historie = []
    for row in ergebnis:
        spieler_1_name = row[0]
        spieler_2_name = row[1]
        gewinner = row[2]
        spieler_historie.append((spieler_1_name, spieler_2_name, gewinner))

    conn.close()
    return spieler_historie

def Spieler_ausgabe():
    conn = sqlite3.connect('datenbank/spielstand.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS"spieler_liste" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"name"	TEXT,
	"gewinne"	INTEGER,
	"verloren"	INTEGER
    cursor.execute("SELECT * FROM spieler_liste")''')
    
    ergebnis = cursor.fetchall()

    for row in ergebnis:
        

    conn.close()
    return 


Spielstand_speichern(spieler_1_name, spieler_2_name, gewinner, spielbrett)
arr = Spielstand_auslesen(2)
historie = Spiele_ausgeben()

print(arr[5][1])
# print(historie)
