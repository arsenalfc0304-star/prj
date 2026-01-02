import os

import requests
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv("API_KEY")


def convert_to_rub(amount: float, currency_from: str) -> float:
    """
    обращается к внешнему API (Exchange Rates Data API) для получения текущего курса валют
    и конвертации суммы операции из USD или EUR в рубли
    """
    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {"amount": float(amount), "from": currency_from, "to": "RUB"}
    headers = {"apikey": apikey}

    response = requests.get(url, headers=headers, params=payload)
    status_code = response.status_code
    result = response.json()
    if status_code == 200:
        return result["result"]
    else:
        return 0


# convert_to_rub(amount=100, currency_from="USD")
