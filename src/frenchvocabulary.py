from vocabulary import Vocabulary

class FrenchVocab(Vocabulary):
    """
    French Vocabulary 
    Inherits from the class Vocabulary
    @author: Ahmed Bouzidia
    """

    def getMorningSalutation(self):
        return "Bonjour"

    def getAfternoonSalutation(self):
        return "Bon après-midi"

    def getNightSalutation(self):
        return "Bonne nuit"

    def sayGoodbye(self):
        return "Au revoir"
    
    def feliciter(self):
        return "Bien dit !"

    def blam(self):
        return "Ce n'est pas un palindrome !" 