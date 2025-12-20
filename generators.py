transactions = [{"description": 1, "currency": "USB"}, {"description": 2, "currency": "USB"}]
def filter_by_currency(transactions, currency):
    return filter(lambda item: item["currency"] == currency, transactions)


transaction_descriptions = (x["description"] for x in transactions)
transactions = [{"description": 1, "currency": "USB"}, {"description": 2, "currency": "USB"}]
descriptions = transaction_descriptions(transactions)
for _ in range(2):
  print(next(descriptions))

huy = filter_by_currency(transactions, "USB")
for _ in range(2):
    print(next(huy))

#print(next(transaction_descriptions))
#print(next(transaction_descriptions))