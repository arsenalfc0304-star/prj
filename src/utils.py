import json

from external_api import convert_to_rub


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


# print(load_json("data/operations.json"))


def transaction_rub(transaction: dict) -> float:
    """
    принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float.
    Если транзакция была в USD или EUR,
    происходит обращение к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли
    """
    if (
        transaction["operationAmount"]["currency"]["code"] == "USD"
        or transaction["operationAmount"]["currency"]["code"] == "EUR"
    ):
        convert_to_rub(
            float(transaction["operationAmount"]["amount"]), transaction["operationAmount"]["currency"]["code"]
        )
    elif transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])


# transaction1 = {
#     "id": 560813069,
#     "state": "CANCELED",
#     "date": "2019-12-03T04:27:03.427014",
#     "operationAmount": {"amount": "17628.50", "currency": {"name": "USD", "code": "USD"}},
# }
#
# transaction_rub(transaction1)
