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

# Funktion zum Konvertieren eines Arrays in einen String
def array_to_string(arr):
    string = ""
    for row in arr:
        string += ",".join(row) + "\n"
    return string


# Funktion zum Konvertieren eines Strings in ein Array
def string_to_array(string):
    spielbrett = []
    rows = string.strip().split("\n")
    for row in rows:
        spielbrett.append(row.split(","))
    return spielbrett


# Funktion zum Speichern des Spielstands in der Datenbank
def Spielstand_speichern(spieler1, spieler2, gewinner, spielbrett):
    string = array_to_string(spielbrett)  # Array in einen String umwandeln

    conn = sqlite3.connect('datenbank/spielstand.db')  # Datenbankverbindung herstellen
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS spieler (
        spieler_1_name TEXT,
        spieler_2_name TEXT,
        gewinner INT,
        spielstand TEXT
    )''')  # Tabelle erstellen, falls sie nicht existiert

    cursor.execute("INSERT INTO spieler (spieler_1_name, spieler_2_name, gewinner, spielstand) VALUES (?, ?, ?, ?)",
                   (spieler1, spieler2, gewinner, string))  # Spielstand in die Datenbank einfügen

    conn.commit()  # Änderungen in der Datenbank speichern
    conn.close()  # Datenbankverbindung schließen


# Funktion zum Auslesen des Spielstands aus der Datenbank
def Spielstand_auslesen(id):
    conn = sqlite3.connect('datenbank/spielstand.db')  # Datenbankverbindung herstellen
    cursor = conn.cursor()

    cursor.execute("SELECT spielstand FROM spieler WHERE id=?", (id,))  # Spielstand basierend auf der ID abrufen
    ergebnis = cursor.fetchone()

    if ergebnis is not None:
        spielbrett_string = ergebnis[0]
        spielbrett = string_to_array(spielbrett_string)  # String in ein Array umwandeln
        conn.close()
        return spielbrett

    conn.close()
    return None


# Funktion zum Ausgeben der Spielerhistorie aus der Datenbank
def Spiele_ausgeben():
    conn = sqlite3.connect('datenbank/spielstand.db')  # Datenbankverbindung herstellen
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS spieler (
        spieler_1_name TEXT,
        spieler_2_name TEXT,
        gewinner INT,
        spielstand TEXT,
        id INTEGER PRIMARY KEY AUTOINCREMENT
    )''')  # Tabelle erstellen, falls sie nicht existiert

    cursor.execute("SELECT spieler_1_name, spieler_2_name, gewinner FROM spieler")  # Spielerhistorie abrufen
    ergebnis = cursor.fetchall()

    spieler_historie = []
    for row in ergebnis:
        spieler_1_name = row[0]
        spieler_2_name = row[1]
        gewinner = row[2]
        spieler_historie.append((spieler_1_name, spieler_2_name, gewinner))

    conn.close()
    return spieler_historie


# Funktion zum Ausgeben der Spielerliste aus der Datenbank
def Spieler_ausgabe():
    conn = sqlite3.connect('datenbank/spielstand.db')  # Datenbankverbindung herstellen
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS spieler_liste (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        gewinne INTEGER,
        verloren INTEGER
    )''')  # Tabelle erstellen, falls sie nicht existiert

    cursor.execute("SELECT * FROM spieler_liste")  # Spielerliste abrufen
    ergebnis = cursor.fetchall()

    for row in ergebnis:
        print(row)

    conn.close()


def neuer_Spieler(name):
    conn = sqlite3.connect('datenbank/spielstand.db')  # Datenbankverbindung herstellen
    cursor = conn.cursor()

    cursor.execute("Select name from spieler_liste")
    ergebnis = cursor.fetchall()

    for row in ergebnis:
        if(row == name):
            cursor.execute('''CREATE TABLE IF NOT EXISTS spieler_liste (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
        	name TEXT,
            gewinne INTEGER,
            verloren INTEGER
            )''')  # Tabelle erstellen, falls sie nicht existiert

            cursor.execute("INSERT INTO spieler (name, gewinne, verloren) VALUES (?, ?, ?)",
                (name, 0, 0))  # Spielstand in die Datenbank einfügen
            break


    conn.close()
    

# Spielstand speichern
Spielstand_speichern(spieler_1_name, spieler_2_name, gewinner, spielbrett)

# Spielstand auslesen
arr = Spielstand_auslesen(1)
print(arr[5][1])

# Spielerhistorie ausgeben
historie = Spiele_ausgeben()
print(historie)

# Spielerliste ausgeben
Spieler_ausgabe()
