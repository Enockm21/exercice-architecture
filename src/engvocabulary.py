from vocabulary import Vocabulary

class EngVocab(Vocabulary):
    """
    English Vocabulary 
    Inherits from the class Vocabulary
    @author: Ahmed Bouzidia
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