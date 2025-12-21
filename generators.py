#from tests.test_generators import transactions_list

def filter_by_currency(transactions, currency):
    """
    принимает на вход список словарей, представляющих транзакции,
    возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной
    """
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
        for y in range(0, 16-len(str(x))):
            str1 += "0"
        str1 += str(x)
        yield str1
        x += 1

#descriptions = transaction_descriptions(transactions_list)

#huy = filter_by_currency(transactions_list, "USB")
#for _ in range(2):
#    print(next(huy))

#for card_number in card_number_generator(9999999999999987, 9999999999999999):
#    print(card_number)
#print(next(card_number))
#print(next(card_number))

# for _ in range(3):
#   print(next(descriptions))
#
