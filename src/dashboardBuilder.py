from palindrome import Palindrome
from botgreeter import BotGreeter
from  botgreeterbuilder import BotGreeterBuilder
from dashboard import Dashboard

class DashboardBuilder:
    def build(self):
        botBuilder = BotGreeterBuilder()
        botGreeter = botBuilder.build()
        palindrome = Palindrome(" ")
        dashboard = Dashboard(palindrome,botGreeter)
        return dashboard