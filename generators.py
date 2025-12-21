def filter_by_currency(transactions, currency):
    """
    принимает на вход список словарей, представляющих транзакции,
    возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной
    """
    #if currency in transactions:
    return filter(lambda item: item["operationAmount"]["currency"]["code"] == currency, transactions)


def transaction_descriptions(transactions):
    """
    принимает список словарей с транзакциями,
    возвращает описание каждой операции по очереди
    """
    for x in transactions:
        yield x["description"]


def card_number_generator(start, stop):
    """
    принимает начальное и конечное значения для генерации диапазона номеров карт.
    выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    """
    x = start
    while 1 <= x <= stop <= 9999999999999999:
        str1 = ""
        for y in range(0, 16 - len(str(x))):
            str1 += "0"
        str1 += str(x)
        yield str1
        x += 1
for card_number in card_number_generator(5, 1):
    print(card_number)
