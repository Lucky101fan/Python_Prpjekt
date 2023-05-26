import random


def choose_bot_name():
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
print(choose_bot_name())