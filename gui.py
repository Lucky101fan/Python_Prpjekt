import tkinter as tk
import random

class SpielbrettGUI:
    def __init__(self):
        self.fenster = tk.Tk()
        self.fenster.title("Vier gewinnt")

        self.breite = 7
        self.hoehe = 6
        self.brett = [[' ' for _ in range(self.breite)] for _ in range(self.hoehe)]
        self.felder = []

        self.spieler = random.choice(['lila', 'blau'])
        self.farbe = 'purple' if self.spieler == 'lila' else 'blue'

        for spalte in range(self.breite):
            feld_spalte = []
            for zeile in range(self.hoehe):
                button = tk.Button(self.fenster, width=10, height=5, bg='white', command=lambda s=spalte: self.feldKlick(s))
                button.grid(row=self.hoehe - zeile, column=spalte, padx=5, pady=5)
                feld_spalte.append(button)
            self.felder.append(feld_spalte)
            

    def feldKlick(self, spalte):
        for r in range(self.hoehe-1, -1, -1):
            if self.brett[r][spalte] == ' ':
                self.brett[r][spalte] = self.spieler
                self.felder[spalte][self.hoehe-1-r].config(bg=self.farbe)
                break

        winner = self.überpruefe_gewinner(self.spieler)

        if self.spieler == 'lila':
            self.spieler = 'blau'
            self.farbe = 'blue'
        else:
            self.spieler = 'lila'
            self.farbe = 'purple'
       
        if winner:
         self.neues_spiel()
         print(f"Spieler {winner} hat gewonnen!")
         

    def überpruefe_gewinner(self, symbol):
        zeilen = len(self.brett)
        spalten = len(self.brett[0])

        for spalte in range(spalten):
            for zeile in range(zeilen - 3):
                if self.brett[zeile][spalte] != ' ' and \
                   self.brett[zeile][spalte] == self.brett[zeile + 1][spalte] == self.brett[zeile + 2][spalte] == self.brett[zeile + 3][spalte]:
                    return symbol

        for zeile in range(zeilen):
            for spalte in range(spalten - 3):
                if self.brett[zeile][spalte] != ' ' and \
                   self.brett[zeile][spalte] == self.brett[zeile][spalte + 1] == self.brett[zeile][spalte + 2] == self.brett[zeile][spalte + 3]:
                    return symbol

        return None  
    
    def start(self):
        self.fenster.mainloop()

    def neues_spiel(self):
        for spalte in self.felder:
            for button in spalte:
                button.config(bg='white')
        self.brett = [[' ' for _ in range(self.breite)] for _ in range(self.hoehe)]
        self.spieler = random.choice(['lila', 'blau'])
        self.farbe = 'purple' if self.spieler == 'lila' else 'blue'

spielbrett_gui = SpielbrettGUI()
spielbrett_gui.start()