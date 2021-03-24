import pandas as pd

class plant:
    def __init__(self, data_csv_file, name = "Nameless"):
        self.name = name
        self.data = pd.read_csv(data_csv_file)

    def get_name(self):
        return self.name

    def get_moisture(self):
        return self.moisture

    def get_temp(self):
        return self.temp