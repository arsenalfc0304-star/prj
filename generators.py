transactions = [{"description": 1, "currency": "USB"}, {"description": 2, "currency": "USB"}]
def filter_by_currency(transactions, currency):
    return filter(lambda item: item["currency"] == currency, transactions)


transaction_descriptions = (x["description"] for x in transactions)

huy = filter_by_currency(transactions, "USB")
print(next(huy))
print(next(huy))
print(next(transaction_descriptions))
print(next(transaction_descriptions))