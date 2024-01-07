from data_fetcher_interface import DataFetcherInterface

class DataFetcherBridge(DataFetcherInterface):
    def __init__(self, fetcher: DataFetcherInterface):
        self.fetcher = fetcher

    def fetch_data(self):
        return self.fetcher.fetch_data()
