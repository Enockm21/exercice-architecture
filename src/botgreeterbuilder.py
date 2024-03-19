#from Vocabulary import Vocabulary, EngVocab, FrenchVocab

from PeriodeChecker import PeriodeChecker
from SystemLanguageDetector import SystemLanguageDetector

class BotGreeterBuilder:
    def __init__(self):
        self.system_lang_detector = SystemLanguageDetector()
        self.vocab: Optional[Vocabulary] = None
        self.periode_checker: Optional[PeriodeChecker] = None

    def set_vocab(self, vocab: Vocabulary) -> "BotGreeterBuilder":
        self.vocab = vocab
        return self

    def set_periode_checker(self, periode_checker: PeriodeChecker) -> "BotGreeterBuilder":
        self.periode_checker = periode_checker
        return self

    def build(self) -> "BotGreeter":
        if self.vocab is None:
            system_lang = self.system_lang_detector.get_system_language()
            if system_lang.startswith("fr"):
                self.vocab = FrenchVocab()
            else:
                self.vocab = EngVocab()
        if self.periode_checker is None:
            raise ValueError("PeriodeChecker is not set")
        return BotGreeter(self.vocab, self.periode_checker)
