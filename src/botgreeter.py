from typing import Any

from dayperiodchecker   import DayPeriodChecker
from vocabulary import Vocabulary
from engvocabulary import EngVocab
from frenchvocabulary  import FrenchVocab
from dayperiodegrammar import DayPeriodGrammar



class BotGreeter:
    """
    This class  represents a greeter  : comme un receptionnniste qui acceuil l'utilisateur 
    It will be used in the Dashboard (console or API) to say hello and goodbye
    @author : Ahmed Bouzidia
    @author : ahmed.bouzidia@ecoles-epsi.net
    @version : 20-03-2024
    """
    def __init__(self, vocab: Vocabulary, periodeChecker: DayPeriodChecker):
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

    def blam(self):
        return  f"{self.vocab.blam()}!"

    def feliciter(self):
        return  f"{self.vocab.feliciter()}!"

