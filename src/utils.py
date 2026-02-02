import json

from src.external_api import get_api_convertion_to_rub

from src.loggers import utils_logger


def load_json(path):
    """
    принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
            utils_logger.info(f"возвращаем список словарей с данными о финансовых транзакциях из файла {path}")
            return data
    except Exception as e:
        utils_logger.error(f"произошла ошибка получения данных о транзакции {e}")
        return []


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
        utils_logger.info(
            "выдаем сумму транзакции после конвертации из"
            f'{transaction["operationAmount"]["currency"]["code"]} в рубли по текущему курсу валют'
        )
        return float(get_api_convertion_to_rub(transaction))
    elif transaction["operationAmount"]["currency"]["code"] == "RUB":
        utils_logger.info("выдаем сумму транзакции в рублях")
        return float(transaction["operationAmount"]["amount"])
    else:
        utils_logger.error("валюта транзакции не определена")
        return 0.0
