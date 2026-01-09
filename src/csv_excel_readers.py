import pandas as pd


def read_data_from_csv(path: str) -> list:
    """
    Функция для считывания финансовых операций из CSV принимает путь к файлу CSV в качестве аргумента,
    выдает список словарей с транзакциями
    """
    data = pd.read_csv(path).head()
    print(data.to_dict(orient='list'))


def read_data_from_excel(path: str) -> list:
    """
    Функция для считывания финансовых операций из Excel принимает путь к файлу Excel в качестве аргумента,
    выдает список словарей с транзакциями
    """
    data = pd.read_excel(path)
    print(data.to_dict(orient='records'))


#read_data_from_csv("data/transactions.csv")

read_data_from_excel("data/transactions_excel.xlsx")