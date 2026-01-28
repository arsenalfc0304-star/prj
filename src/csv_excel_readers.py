import pandas as pd


def read_data_from_csv(path: str) -> list:
    """
    Функция для считывания финансовых операций из CSV принимает путь к файлу CSV в качестве аргумента,
    выдает список словарей с транзакциями
    """
    data = pd.read_csv(path, delimiter=";")
    return data.to_dict(orient="records")


def read_data_from_excel(path: str) -> list:
    """
    Функция для считывания финансовых операций из Excel принимает путь к файлу Excel в качестве аргумента,
    выдает список словарей с транзакциями
    """
    data = pd.read_excel(path)
    return data.to_dict(orient="records")
