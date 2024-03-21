from palindrome import Palindrome
from receptionistbuilder import ReceptionistBuilder
from console import Console

# Obsolete : on a remplacé par un code dans le main.py
class ConsoleBuilder:
    """
    This class is a builder
    Implement a Builder Design Pattern
    It builds a Dashboard
    @author : ahmed.bouzidia@ecoles-epsi.net
    @version : 20-03-2024
    """
    def build(self):  # mettre tout dans le constructeur car c'est simple 
        receptionistBuilder = ReceptionistBuilder()
        receptionist = receptionistBuilder.build()
        palindrome = Palindrome(" ")
        console = Console(palindrome, receptionist)
        return console
