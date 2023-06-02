import tkinter as tk
import random
import sqlite3
import pytest
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

class VierGewinnt:
    def __init__(self, zeile=6, spalte=7):
        self.zeile = zeile
        self.spalte = spalte
        self.spielfeld = [[' ' for _ in range(spalte)] for _ in range(zeile)]

        self.conn = sqlite3.connect('Spieler.db')
        self.db_cursour = self.conn.cursor()

        self.spieler_name = ""

        self.root = tk.Tk()
        self.root.title("Vier Gewinnt")

        self.mode = tk.StringVar()

        self.db_cursour.execute("SELECT name FROM Player")
        rows = self.db_cursour.fetchall()
        options = [row[0] for row in rows]

        spieler_label = tk.Label(self.root, text="Spieler: ")
        spieler_label.grid(row=0, column=0, pady=10, padx=5)

        ausgewhaehlter_spieler = tk.StringVar()
        dropdown = tk.OptionMenu(self.root, ausgewhaehlter_spieler, *options)
        dropdown.grid(row=0, column=1, pady=10)

        mode_label = tk.Label(self.root, text="Spielmodus:")
        mode_label.grid(row=1, column=1, pady=5, padx=100)

        pvp_button = tk.Button(self.root, text="Spieler vs. Spieler", command=lambda: self.spiel_starten('P'))
        pvp_button.grid(row=2, column=1, pady=5, padx=20)

        pvc_button = tk.Button(self.root, text="Spieler vs. Computer", command=lambda: self.spiel_starten('C'))
        pvc_button.grid(row=3, column=1, pady=5, padx=20)

        load_button = tk.Button(self.root, text="Spielstand laden", command=self.load_game)
        load_button.grid(row=4, column=1, pady=5, padx=20)

        exit_button = tk.Button(self.root, text="Programm beenden", command=self.root.quit)
        exit_button.grid(row=5, column=1, pady=5, padx=20)

    def spiel_starten(self, modus):
        self.mode.set(modus)
        self.root.destroy()

        self.root = tk.Tk()
        self.root.title("Vier Gewinnt")

        self.buttons = []
        for zeile in range(self.zeile):
            button_zeile = []
            for spalte in range(self.spalte):
                button = tk.Button(self.root, text=' ', width=6, height=3, command=lambda c=spalte: self.spielzug_spieler(c))
                button.grid(row=zeile, column=spalte, padx=2, pady=2)
                button_zeile.append(button)
            self.buttons.append(button_zeile)

        self.turn = 'X'
        self.game_over = False

        if self.mode.get() == 'C' and self.turn == 'O':
            self.root.after(500, self.spielzug_computer)  # Warte 500 Millisekunden vor Computer-Zug
            # Deaktiviere Spieler-Buttons während des Computer-Zugs
            for zeile in range(self.zeile):
                for spalte in range(self.spalte):
                    if self.spielfeld[zeile][spalte] == ' ':
                        self.buttons[zeile][spalte].config(state='disabled')

        back_button = tk.Button(self.root, text="Zurück zum Menü", command=self.zurueck_zum_menue)
        back_button.grid(row=self.zeile + 1, columnspan=self.spalte, pady=10)

        self.turn_label = tk.Label(self.root, text="Aktueller Zug: Spieler X")
        self.turn_label.grid(row=self.zeile + 2, columnspan=self.spalte, pady=10)

        save_button = tk.Button(self.root, text="Spielstand speichern", command=self.spiel_speichern)
        save_button.grid(row=self.zeile + 3, columnspan=self.spalte, pady=10)

        self.update_spielzug_label()  # Aktualisiere den Text der Zug-Anzeige

    def spiel_speichern(self):
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if filename:
            with open(filename, "w") as file:
                for zeile in self.spielfeld:
                    file.write(" ".join(zeile) + "\n")
            tk.messagebox.showinfo("Spielstand gespeichert", "Der Spielstand wurde erfolgreich gespeichert.")

    def load_game(self):
        filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if filename:
            with open(filename, "r") as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    row = line.strip().split()
                    self.spielfeld[i] = row
            self.update_spielfeld()

    def update_spielfeld(self):
        pass

    def update_spielzug_label(self):
        """
        Aktualisiert den Text der Zug-Anzeige basierend auf dem aktuellen Spieler.
        """
        self.turn_label.config(text=f"Aktueller Zug: Spieler {self.turn}")

    def zurueck_zum_menue(self):
        self.root.destroy()
        # Starten Sie das Spiel erneut
        game = VierGewinnt()
        game.run()

    def spielzug_spieler(self, spalte):
        """
        Diese Methode wird aufgerufen, wenn ein Spieler einen Zug macht.
        Sie überprüft die Gültigkeit des Zuges, aktualisiert das Spielfeld,
        überprüft auf Gewinn oder Unentschieden und wechselt den Zug zum nächsten Spieler.
        """
        if not self.game_over and self.spielzug_valide(spalte):
            if self.mode.get() == 'C' and self.turn == 'O':
                return  # Ignoriert Spieler Spielzuege waehrend Computer am Zug ist

            for zeile in range(self.zeile - 1, -1, -1):
                if self.spielfeld[zeile][spalte] == ' ':
                    self.spielfeld[zeile][spalte] = self.turn
                    self.buttons[zeile][spalte].config(text=self.turn, bg='purple' if self.turn == 'X' else 'blue', state='disabled')
                    if self.check_gewinner(self.turn):
                        self.game_over = True
                        self.endstand_anzeigen(self.turn)
                    elif self.check_unentschieden():
                        self.game_over = True
                        self.endstand_anzeigen('draw')
                    else:
                        if self.mode.get() == 'C' and self.turn == 'X':
                            self.spielzug_wechseln()
                            self.root.after(500, self.spielzug_computer)  # Wait 500 milliseconds before computer move
                            # Disable player buttons during computer move
                            for zeile in range(self.zeile):
                                for spalte in range(self.spalte):
                                    if self.spielfeld[zeile][spalte] == ' ':
                                        self.buttons[zeile][spalte].config(state='disabled')
                        else:
                            self.spielzug_wechseln()
                    break
        self.update_spielzug_label()

    def spielzug_computer(self):
        """
        Diese Methode wird aufgerufen, wenn der Computer einen Zug macht.
        Sie wählt einen zufälligen gültigen Zug aus und aktualisiert das Spielfeld.
        Dann überprüft sie auf Gewinn oder Unentschieden und wechselt den Zug zum nächsten Spieler.
        """
        spalte = random.randint(0, self.spalte - 1)
        while not self.spielzug_valide(spalte):
            spalte = random.randint(0, self.spalte - 1)

        for zeile in range(self.zeile - 1, -1, -1):
            if self.spielfeld[zeile][spalte] == ' ':
                self.spielfeld[zeile][spalte] = 'O'
                self.buttons[zeile][spalte].config(text='O', bg='blue')
                if self.check_gewinner('O'):
                    self.game_over = True
                    self.endstand_anzeigen('O')
                elif self.check_unentschieden():
                    self.game_over = True
                    self.endstand_anzeigen('draw')
                else:
                    # Buttons werden reaktiviert, nachdem Computer Zug gemacht hat
                    for zeile in range(self.zeile):
                        for spalte in range(self.spalte):
                            if self.spielfeld[zeile][spalte] == ' ':
                                self.buttons[zeile][spalte].config(state='normal')
                    self.spielzug_wechseln()
                break
        self.update_spielzug_label()

    def spielzug_wechseln(self):
        """
        Diese Methode wechselt den Zug zum nächsten Spieler.
        """
        self.turn = 'O' if self.turn == 'X' else 'X'

    def spielzug_valide(self, spalte):
        """
        Diese Methode überprüft, ob ein Zug in einer bestimmten Spalte gültig ist.
        """
        return spalte >= 0 and spalte < self.spalte and self.spielfeld[0][spalte] == ' '

    def check_gewinner(self, symbol):
        """
        Diese Methode überprüft, ob ein Spieler gewonnen hat.
        """
        for zeile in range(self.zeile):
            for spalte in range(self.spalte):
                if self.spielfeld[zeile][spalte] == symbol:
                    # Horizontal
                    if spalte + 3 < self.spalte and all(self.spielfeld[zeile][spalte + i] == symbol for i in range(4)):
                        return True
                    # Vertical
                    if zeile + 3 < self.zeile and all(self.spielfeld[zeile + i][spalte] == symbol for i in range(4)):
                        return True
                    # Diagonal /
                    if zeile + 3 < self.zeile and spalte + 3 < self.spalte and all(self.spielfeld[zeile + i][spalte + i] == symbol for i in range(4)):
                        return True
                    # Diagonal \
                    if zeile + 3 < self.zeile and spalte - 3 >= 0 and all(self.spielfeld[zeile + i][spalte - i] == symbol for i in range(4)):
                        return True
        return False

    def check_unentschieden(self):
        """
        Diese Methode überprüft, ob das Spiel unentschieden ist.
        """
        return all(self.spielfeld[zeile][spalte] != ' ' for zeile in range(self.zeile) for spalte in range(self.spalte))

    def endstand_anzeigen(self, ergebnis):
        """
        Diese Methode zeigt eine Nachricht an, wenn das Spiel vorbei ist.
        """
        if ergebnis == 'X':
            messagebox.showinfo("Spiel vorbei", "Herzlichen Glückwunsch! Spieler X hat gewonnen!")
        elif ergebnis == 'O':
            if self.mode.get() == 'P':
                messagebox.showinfo("Spiel vorbei", "Herzlichen Glückwunsch! Spieler O hat gewonnen!")
            else:
                messagebox.showinfo("Spiel vorbei", "Schade! Der Computer hat gewonnen!")
        else:
            messagebox.showinfo("Spiel vorbei", "Das Spiel ist unentschieden!")

    def run(self):
        self.root.mainloop()

# Spiel starten
game = VierGewinnt()
game.run()
game.conn.close()


def test_check_gewinner():
    spiel = VierGewinnt(7, 6)

    # Horizontale Gewinnbedingung
    spiel.spielfeld[3][1] = 'X'
    spiel.spielfeld[3][2] = 'X'
    spiel.spielfeld[3][3] = 'X'
    spiel.spielfeld[3][4] = 'X'
    assert spiel.check_gewinner('X') == True

    # Vertikale Gewinnbedingung
    spiel.spielfeld[2][4] = 'O'
    spiel.spielfeld[3][4] = 'O'
    spiel.spielfeld[4][4] = 'O'
    spiel.spielfeld[5][4] = 'O'
    assert spiel.check_gewinner('O') == True

    # Diagonale (/) Gewinnbedingung
    spiel.spielfeld[2][2] = 'X'
    spiel.spielfeld[3][3] = 'X'
    spiel.spielfeld[4][4] = 'X'
    spiel.spielfeld[5][5] = 'X'
    assert spiel.check_gewinner('X') == True

    # Diagonale (\) Gewinnbedingung
    spiel.spielfeld[1][4] = 'O'
    spiel.spielfeld[2][3] = 'O'
    spiel.spielfeld[3][2] = 'O'
    spiel.spielfeld[4][1] = 'O'
    assert spiel.check_gewinner('O') == True

    # Kein Gewinner
    assert spiel.check_gewinner('X') == False
    assert spiel.check_gewinner('O') == False


def test_spielzug_valide():
    spiel = VierGewinnt(7, 6)
    spiel.spielfeld[0][5] = 'X'  # Beispiel für bereits belegte Spalte

    assert spiel.spielzug_valide(2) == False  # Erwartet: False (Spalte bereits belegt)
    assert spiel.spielzug_valide(4) == True  # Erwartet: True (Spalte frei)
    assert spiel.spielzug_valide(7) == False  # Erwartet: False (Spalte außerhalb des Spielfelds)
    assert spiel.spielzug_valide(-1) == False  # Erwartet: False (Spalte außerhalb des Spielfelds)
