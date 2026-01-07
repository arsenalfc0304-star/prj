import pandas as pd


def read_data_from_csv(path: str) -> list:
    data = pd.read_csv(path).head()
    print(data.to_dict(orient='list'))


read_data_from_csv("data/transactions.csv")