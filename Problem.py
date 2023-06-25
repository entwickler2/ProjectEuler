from abc import ABC, abstractmethod


class AbsProblem(ABC):

    @abstractmethod
    def getinfo(self):
        pass

    @abstractmethod
    def result(self):
        pass
