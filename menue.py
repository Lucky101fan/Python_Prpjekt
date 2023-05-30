import tkinter as tk
import sqlite3
from gui import SpielbrettGUI
import random

class Menue:


    def __init__(self):
        self.db = sqlite3.connect('datenbank/spielstand.db')
        self.db.execute('''CREATE TABLE IF NOT EXISTS spieler (spieler_1_name TEXT, spieler_2_name TEXT, gewinne INT)''')
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
        
    def choose_bot_name(self):
        bot_names = [
            "AlphaBot", "BetaAI", "GammaChat", "DeltaBot", "EpsilonAI", "ZetaChat",
            "EtaBot", "ThetaAI", "IotaChat", "KappaBot", "LambdaAI", "MuChat",
            "NuBot", "XiAI", "OmicronChat", "PiBot", "RhoAI", "SigmaChat",
            "TauBot", "UpsilonAI", "PhiChat", "ChiBot", "PsiAI", "OmegaChat",
            "Bot-2000", "AI-X", "ChatMaster", "RoboBrain", "CogniBot", "MegaAI",
            "SuperChat", "UltimateBot", "IntelliAI", "GeniusChat", "SmartBot", "HyperAI",
            "QuickChat", "SpeedyBot", "SwiftAI", "AgileChat", "NimbleBot", "DexterAI",
            "ChatterBot", "BrainiacAI", "WiseChat", "SageBot", "OracleAI", "KnowBot",
            "DigitalAssistant", "TechAI", "VirtualChat", "CyberBot", "LogicAI", "SynthChat",
            "RoboFriend", "AIPal", "ChatBuddy", "CleverBot", "MindfulAI", "FriendlyChat",
            "MasterBot", "AIWizard", "ChatGuru", "SavvyBot", "EinsteinAI", "EnigmaChat",
            "NeuralBot", "AIScribe", "ChatWhiz", "BrainWaveAI", "ConverseBot", "ThoughtfulChat",
            "SynapseBot", "AIProdigy", "TalkativeChat", "BotGenie", "CerebralAI", "InsightfulChat",
            "MegaBot", "AICommander", "ChatPro", "RoboThinker", "IntelAI", "LivelyChat",
            "VirtualFriend", "AICompanion", "ChatCaptain", "RoboSage", "MindBot", "JoyfulAI",
            "WhisperingChat", "AIProphet", "BotSquad", "GeniusAI", "ConversantChat", "VividBot",
            "SparkyAI", "ChatExpert", "BotAdvocate", "BrightChat", "AIChampion", "HappyBot",
            "DreamyChat", "AIPioneer", "BotStrategist", "WittyAI", "InsiderChat", "KindBot"
        ]

        return random.choice(bot_names)

    def spieler_eintragen(self):
        print("Methode spieler_eintragen")
        name = self.eingabe_name.get()
        bot_name = self.choose_bot_name()
        self.db.execute("INSERT INTO spieler (spieler_1_name, spieler_2_name) VALUES (?),(?)", (name,)(bot_name,))
        self.db.commit()

    def starte_gegen_computer(self):
        self.db.close()  # Schließen der Datenbankverbindung
        self.root.destroy()


    def starte_gegen_spieler(self):
        self.spieler_eintragen()
        self.db.close()  # Schließen der Datenbankverbindung
        self.root.destroy()
        spielbrett_gui = SpielbrettGUI()
        spielbrett_gui.start()
    



start = Menue()