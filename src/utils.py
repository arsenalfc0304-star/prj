import json


def load_json(path):
    """
    принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
            return data
    except Exception:
        return []


print(load_json("data/operations.json"))


def transaction_rub(transaction: dict) -> float:
    """
    принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float.
    Если транзакция была в USD или EUR,
    происходит обращение к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли
    """
    if transaction["currency"] == "USD" or transaction["currency"] == "EUR":


    return float(transaction["amount"]) * float(transaction["currency"])
