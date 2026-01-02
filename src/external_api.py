import requests


def convert_to_rub(amount: float, currency_from: str) -> float:
    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {
        "amount": float(amount),
        "from": currency_from,
        "to": "RUB"
        }
    headers = {
        "apikey": "Sa5AQJe8Ko8JXKWBVMuTRS9OhiRrNoOK"
        }

    response = requests.get(url, headers=headers, params=payload)
    status_code = response.status_code
    result = response.json()
    if status_code == 200:
        print(result["result"])

#convert_to_rub(amount=100, currency_from="USD")