from vocabulary import Vocabulary


class FrenchVocabulary(Vocabulary):
    """
    French Vocabulary 
    Inherits from the class Vocabulary
    @author: Ahmed Bouzidia
    @author : ahmed.bouzidia@ecoles-epsi.net
    @version : 20-03-2024
    """

    def getMorningSalutation(self):
        return "Bonjour"

    def getAfternoonSalutation(self):
        return "Bon après-midi"

    def getNightSalutation(self):
        return "Bonne nuit"

    def sayGoodbye(self):
        return "Au revoir"
    
    def congratulate(self):
        return "Bien dit !"

    def blame(self):
        return "Ce n'est pas un palindrome !" 