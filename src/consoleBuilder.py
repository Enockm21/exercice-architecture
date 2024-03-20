from palindrome import Palindrome
from botgreeter import BotGreeter
from receptionistbuilder import ReceptionistBuilder
from console import Console

		#Ahmed Service
class ConsoleBuilder:
	"""
	This class is a builder
	Implement a Bilder Design Patter
	It builds a Dashboard
	@author : ahmed.bouzidia@ecoles-epsi.net
    @version : 20-03-2024
	"""
    def build(self):
        receptionistBuilder = ReceptionistBuilder()
        receptionist = receptionistBuilder.build()
        palindrome = Palindrome(" ")
        console  = Console(palindrome,receptionist)
        return console