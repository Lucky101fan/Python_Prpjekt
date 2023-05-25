import tkinter as tk
import sqlite3

class Menue:
    def __init__(self):
        self.db = sqlite3.connect('spielstand.db')
        self.db.execute('''CREATE TABLE IF NOT EXISTS spieler (name TEXT, gewinne INT)''')

        self.root = tk.Tk()
        self.root.title("Vier Gewinnt - Menü")
        self.root.geometry("600x400")

        #design
        label_font = ("Arial", 18)
        button_font = ("Arial", 14)

        self.label_name = tk.Label(self.root, text="Spielername:", font=label_font)
        self.label_name.pack(pady=20)

        self.eingabe_name = tk.Entry(self.root, font=button_font)
        self.eingabe_name.pack()

        self.button_computer = tk.Button(self.root, text="Gegen Computer", font=button_font, command=self.starte_gegen_computer)
        self.button_computer.pack(pady=10)

        self.button_spieler = tk.Button(self.root, text="Gegen Spieler", font=button_font, command=self.starte_gegen_spieler)
        self.button_spieler.pack(pady=10)
        self.root.mainloop()

    def spieler_eintragen(self):
        print("Methode spieler_eintragen")
        name = self.eingabe_name.get()
        self.db.execute("INSERT INTO spieler (name) VALUES (?)", (name,))
        self.db.commit()

    def starte_gegen_computer(self):
        self.spieler_eintragen()
        self.db.close()  # Schließen der Datenbankverbindung
        self.root.destroy()
        spiel = Spielbrett(gegen_computer=True)
        spiel.spiel_starten()

    def starte_gegen_spieler(self):
        self.spieler_eintragen()
        self.db.close()  # Schließen der Datenbankverbindung
        self.root.destroy()
        spiel = Spielbrett(gegen_computer=False)
        spiel.spiel_starten()


start = Menue()