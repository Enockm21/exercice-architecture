import abc

class Vocabulary(abc.ABC):
"""
Abstract class that represnete a vocabulary
@author : Ahmed Bouzidia
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