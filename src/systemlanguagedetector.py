import locale

class SystemLanguageDetector:
    """
    This class defines the system languages.
    It will be used in BotGreeterBuilder.
    @author: Ahmed Bouzidia
    """

    def __init__(self):
        pass

    def get_system_language(self):
        # Retrieve the system language
        system_lang = locale.getdefaultlocale()[0]
        return system_lang
