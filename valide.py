def spielzug_valide(spielbrett,spalte: int, zeile: int) -> bool:
    breite = 7
    hoehe = 6
    

    # Überprüfung, ob die Spalte im erlaubten Bereich liegt
    if spalte < 0 or spalte >= hoehe:
        return False

    # Überprüfung, ob die Zeile im erlaubten Bereich liegt
    if zeile < 0 or zeile >= breite:
        return False

    # Überprüfung, ob das Feld noch nicht besetzt ist
    if spielbrett[spalte][zeile] != "":
        return True

    if spielbrett[zeile][spalte] == "blau" or spielbrett[zeile][spalte] == "lila":
        return False
    else:
        return True


    







spielbrett = [
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", "blau", " ", " ", " "],
    [" ", " ", " ", " ", "lila", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "]
    ]
spalte = 9
zeile = 1
print("Zug Valide:")
print(spielzug_valide(spielbrett,spalte, zeile))



