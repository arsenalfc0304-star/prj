import json

from external_api import convert_to_rub

# import convert_to_rub


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
        print(convert_to_rub(transaction["amount"], transaction["currency"]["code"]))
    else:
        return float(transaction["operationAmount"]["amount"]) * float(transaction["operationAmount"]["currency"]["code"])

transaction_rub(
    {
        "id": 560813069,
        "state": "CANCELED",
        "date": "2019-12-03T04:27:03.427014",
        "operationAmount": {
            "amount": "17628.50",
            "currency": {
                "name": "USD",
                "code": "USD"
                }
            }
    }
)
