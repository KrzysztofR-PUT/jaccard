import pandas as pd


class Reader:
    csvPath = "facts.csv"

    def read_data(self):
        return pd.read_csv(self.csvPath, usecols=["user_id", "song_id"], nrows=100)