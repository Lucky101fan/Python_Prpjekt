import random

class VierGewinnt:
    def spielzug_computer(self):
        """
        Diese Methode wird aufgerufen, wenn der Computer einen Zug macht.
        Sie wählt einen zufälligen gültigen Zug aus und aktualisiert das Spielfeld.
        Dann überprüft sie auf Gewinn oder Unentschieden und wechselt den Zug zum nächsten Spieler.
        """
        spalte = random.randint(0, self.spalten - 1)
        while not self.spielzug_valide(spalte):
            spalte = random.randint(0, self.spalten - 1)

        for zeile in range(self.zeilen - 1, -1, -1):
            if self.board[zeile][spalte] == ' ':
                self.board[zeile][spalte] = 'O'
                self.buttons[zeile][spalte].config(text='O', bg='yellow')
                if self.ueberpruefe_gewinner('O'):
                    self.game_over = True
                    self.endstand_anzeigen('O')
                elif self.ueberpruefe_unentschieden():
                    self.game_over = True
                    self.endstand_anzeigen('draw')
                else:
                    # Buttons werden reaktiviert, nachdem Computer Zug gemacht hat
                    for zeile in range(self.zeilen):
                        for spalte in range(self.spalten):
                            if self.board[zeile][spalte] == ' ':
                                self.buttons[zeile][spalte].config(state='normal')
                    self.spielzug_wechseln()
                break

    def spielzug_wechseln(self):
        """
        Diese Methode wechselt den Zug zum nächsten Spieler.
        """
        self.turn = 'O' if self.turn == 'X' else 'X'