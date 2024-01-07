from abc import ABC, abstractmethod

class DataFetcherInterface(ABC):

    @abstractmethod
    def fetch_data(self):
        pass
