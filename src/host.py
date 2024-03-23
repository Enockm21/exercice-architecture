from typing import Any
from clock  import Clock
from vocabulary import Vocabulary
from englishvocabulary import EnglishVocabulary 
from frenchvocabulary  import FrenchVocabulary

from clockgrammar import ClockGrammar

                
class Host:
    """
    This class  represents a greeter  : comme un receptionnniste qui acceuil l'utilisateur 
    It will be used in the Dashboard (console or API) to say hello and goodbye
    @author : Ahmed Bouzidia
    @author : ahmed.bouzidia@ecoles-epsi.net
    @version : 20-03-2024
    """
    def __init__(self, vocabulary: Vocabulary, clock: Clock):
        self.vocabulary: Vocabulary = vocabulary
        self.clock : Clock = clock

    def greet(self) -> str:
        period = self.clock.get_day_period()
        if period == ClockGrammar.MORNING:
            return f"{self.vocabulary.getMorningSalutation()}!"
        elif period == ClockGrammar.AFTERNOON:
            return f"{self.vocabulary.getAfternoonSalutation()}!"
        elif period == ClockGrammar.EVENING:
            return f"{self.vocabulary.getNightSalutation()}!"
        else:
            return "Bonjour, monde!"  # Fallback greeting if period is unknown

    def say_goodbye(self) -> str:
        return f"{self.vocabulary.sayGoodbye()}!"

    def blame(self):
        return  f"{self.vocabulary.blame()}!"

    def congratulate(self):
        return  f"{self.vocabulary.congratulate()}!"

