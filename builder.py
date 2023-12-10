# builder.py
class AnalyticsBuilder:
    def __init__(self):
        self.data = {}

    def add_data(self, name, data_type):
        self.data[name] = data_type

    def get_built_data(self):
        return self.data
