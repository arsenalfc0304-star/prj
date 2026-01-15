import re
from collections import Counter

def filter_by_state(dict_list: list, state: str = "EXECUTED") -> list:
    """
    принимает список словарей и опционально значение для ключа state (по умолчанию "EXECUTED"),
    возвращает новый список словарей, содержащий только словари, у которых ключ state соответствует указанному значению
    """
    return list(filter(lambda x: x["state"] == state, dict_list))


def sort_by_date(dict_list: list, descending: bool = True) -> list:
    """
    принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание),
    возвращает новый список, отсортированный по дате (date)
    """
    return sorted(dict_list, key=lambda x: x["date"], reverse=descending)


def process_bank_search(dict_list:list[dict], search:str)->list[dict]:
    """
    принимает список словарей с данными о банковских операциях и строку поиска,
    возвращает список словарей, у которых в описании есть данная строка
    """
    filtered_dict_list = []
    for transaction in dict_list:
        if not re.search(search, transaction["description"]) == None:
            filtered_dict_list.append(transaction)
    return filtered_dict_list


def process_bank_operations(dict_list:list[dict], categories:list)->dict:
    """
    принимает список словарей с данными о банковских операциях и список категорий операций,
    возвращает словарь (ключи — это названия категорий, значения — это количество операций в каждой категории)
    """
    categories_counting = []
    for category in categories:
        for transaction in dict_list:
            if transaction["description"] == category:
                categories_counting.append(category)
    result = Counter(categories_counting)
    return dict(result)
