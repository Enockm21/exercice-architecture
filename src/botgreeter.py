from typing import Any
from Vocabulary import Vocabulary
from PeriodeChecker import PeriodeChecker

class BotGreeter:
"""
This class  represents a greeter  
It will be used in the Dashboard (console or API) to say hello and goodbye
@author : Ahmed Bouzidia
"""
    def __init__(self, vocab: Vocabulary, periodeChecker: PeriodeChecker):
        self.vocab: Vocabulary = vocab
        self.periodeChecker: PeriodeChecker = periodeChecker

    def greet(self) -> str:
        period = self.periodeChecker.get_day_period()
        if period == DayPeriodGrammar.MORNING:
            return f"{self.vocab.getMorningSalutation()}!"
        elif period == DayPeriodGrammar.AFTERNOON:
            return f"{self.vocab.getAfternoonSalutation()}!"
        elif period == DayPeriodGrammar.EVENING:
            return f"{self.vocab.getNightSalutation()}!"
        else:
            return "Bonjour, monde!"  # Fallback greeting if period is unknown

    def say_goodbye(self) -> str:
        return f"{self.vocab.sayGoodbye()}!"
