
from systemlanguagedetector import SystemLanguageDetector
from vocabulary import Vocabulary
from frenchvocabulary import FrenchVocabulary
from englishvocabulary import EnglishVocabulary
from clock import Clock

from host import Host


class HostBuilder:
    """
    - A class that implements a Builder Design Pattern
        - It's used to create an instance of the class Host
    @author : ahmed.bouzidia@ecoles-epsi.net
    @version : 23-03-2024
    """

    def __init__(self):
        self.system_lang_detector = SystemLanguageDetector()
        self.vocab: Optional[Vocabulary] = None
        self.clock = Clock()


    def build(self) -> "HostBuilder":
        """"
         Function: create new Host instance
          - Prepare argument for the Receptionist constructor:
             - Instance of Vocabulary  child class
             - Instance of  Clock
          - Return :
                - Host instance
        """
        if self.vocab is None:
            system_lang = self.system_lang_detector.get_system_language()
            if system_lang.startswith("fr"):
                self.vocab = FrenchVocabulary()
            else:
                self.vocab = EnglishVocabulary()

        return Host(self.vocab, self.clock)
