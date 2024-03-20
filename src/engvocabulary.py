from vocabulary import Vocabulary

    #Ahmed Service
    
class EngVocab(Vocabulary):
    """
    English Vocabulary 
    Inherits from the class Vocabulary
    @author: Ahmed Bouzidia
    @author : ahmed.bouzidia@ecoles-epsi.net
    @version : 20-03-2024
    """

    def getMorningSalutation(self):
        return "Good Morning"

    def getAfternoonSalutation(self):
        return "Good Afternoon"

    def getNightSalutation(self):
        return "Good Night"

    def sayGoodbye(self):
        return "Goodbye"
    
    def feliciter(self):
        return  "Well Said "


    def blam(self):
        return "It is not palindrome!" 