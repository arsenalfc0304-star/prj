import pandas as pd


def get_csv_data(path: str) -> list:
   result = pd.read_csv(path)
   print(result.head())

get_csv_data("data/transactions.csv")