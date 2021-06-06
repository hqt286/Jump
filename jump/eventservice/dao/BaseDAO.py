from abc import ABC, abstractmethod


class BaseDAO(ABC):
    """
    This interface class is set up a basic methods for each DAO class
    """

    @abstractmethod
    def getById(self, id):
        pass

    @abstractmethod
    def removeById(self, id):
        pass

    @abstractmethod
    def create(self, item):
        pass

    @abstractmethod
    def update(self, item):
        pass

    @abstractmethod
    def getByIds(self, ids):
        pass

    @abstractmethod
    def removeByIds(self, ids):
        pass

    @abstractmethod
    def createOrUpdateBatch(self, item):
        pass
