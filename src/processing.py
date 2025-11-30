def filter_by_state(dict_list: list, state: str="EXECUTED") -> list:
    """
    принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED'),
    возвращает новый список словарей, содержащий только словари, у которых ключ state соответствует указанному значению
    """
    return list(filter(lambda x: x["state"] == state, dict_list))


def sort_by_date(dict_list: list, descending: bool=True) -> list:
    """
    принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание),
    возвращает новый список, отсортированный по дате (date)
    """
    return sorted(dict_list, key=lambda x: x["date"], reverse=descending)

