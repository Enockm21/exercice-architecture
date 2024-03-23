import abc

    
class Vocabulary(abc.ABC):
    """
    Abstract class that represnete a vocabulary
    @author : ahmed.bouzidia@ecoles-epsi.net
    @version : 20-03-2024

    """
    # Méthodes abstraites
    @abc.abstractmethod
    def getMorningSalutation(self):
        pass

    @abc.abstractmethod
    def getAfternoonSalutation(self):
        pass

    @abc.abstractmethod
    def getNightSalutation(self):
        pass

    @abc.abstractmethod
    def sayGoodbye(self):
        pass
    @abc.abstractmethod
    def congratulate(self):
        pass   

    @abc.abstractmethod
    def blame(self):
        pass   