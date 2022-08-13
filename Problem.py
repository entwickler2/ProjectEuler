from abc import ABC, abstractmethod, abstractproperty


class AbsProblem(ABC):

    @abstractmethod
    def getinfo(self):
        pass

    @abstractmethod
    def result(self):
        pass
