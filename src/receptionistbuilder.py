
from systemlanguagedetector import SystemLanguageDetector
from vocabulary import Vocabulary
from frenchvocabulary import FrenchVocab
from engvocabulary import EngVocab
from dayperiodchecker import DayPeriodChecker

from receptionist import Receptionist

    #Ahmed Service : repository

class ReceptionistBuilder:
    """
    A class that implements a Builder Design Pattern
    It's used to creat an instance of the class BotGreeter
    @author : ahmed.bouzidia@ecoles-epsi.net
    @version : 20-03-2024
    """

    def __init__(self):
        self.system_lang_detector = SystemLanguageDetector()
        self.vocab: Optional[Vocabulary] = None
        self.periode_checker = DayPeriodChecker()
    
   # def set_vocab(self, vocab: Vocabulary) -> "ReceptionistBuilder":
    #    self.vocab = vocab
     #   return self

#    def set_periode_checker(self, periode_checker: DayPeriodChecker) -> "ReceptionistBuilder":
 #       self.periode_checker = periode_checker
  #      return self

    def build(self) -> "ReceptionistBuilder":
        if self.vocab is None:
            system_lang = self.system_lang_detector.get_system_language()
            if system_lang.startswith("fr"):
                self.vocab = FrenchVocab()
            else:
                self.vocab = EngVocab()
        if self.periode_checker is None:
            raise ValueError("PeriodeChecker is not set")
        return Receptionist(self.vocab, self.periode_checker)
