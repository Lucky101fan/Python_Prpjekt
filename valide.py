def spielzug_valide(spalte: int, zeile: int) -> bool:
    breite = 7
    hoehe = 6
    spielbrett = [
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", "x", " ", " ", " "],
    [" ", " ", " ", " ", "o", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "]
]

    # Überprüfung, ob die Spalte im erlaubten Bereich liegt
    if spalte < 0 or spalte >= hoehe:
        return False

    # Überprüfung, ob die Zeile im erlaubten Bereich liegt
    if zeile < 0 or zeile >= breite:
        return False

    # Überprüfung, ob das Feld noch nicht besetzt ist
    if spielbrett[spalte][zeile] != " ":
        return False

    if spielbrett[zeile][spalte] == "x" or spielbrett[zeile][spalte] == "o":
        return True
    else:
        return False


    








spalte = 4
zeile = 3
print("Zug Valide:")
print(spielzug_valide(spalte, zeile))



