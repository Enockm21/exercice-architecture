from palindrome import Palindrome
from botgreeter import BotGreeter
from  botgreeterbuilder import BotGreeterBuilder
from dashboard import Dashboard

class DashboardBuilder:
	"""
	This class is a builder
	Implement a Bilder Design Patter
	It builds a Dashboard
	@author : ahmed.bouzidia@ecoles-epsi.net
    @version : 20-03-2024
	"""
    def build(self):
        botBuilder = BotGreeterBuilder()
        botGreeter = botBuilder.build()
        palindrome = Palindrome(" ")
        dashboard = Dashboard(palindrome,botGreeter)
        return dashboard