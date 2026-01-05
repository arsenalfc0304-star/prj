import os

import requests
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv("API_KEY")


def get_api_convertion_to_rub(transaction: dict) -> float:
    """
    обращается к внешнему API (Exchange Rates Data API) для получения текущего курса валют
    и конвертации суммы операции из USD или EUR в рубли
    """
    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {
        "amount": float(transaction["operationAmount"]["amount"]),
        "from": transaction["operationAmount"]["currency"]["code"],
        "to": "RUB",
    }
    headers = {"apikey": apikey}

    response = requests.get(url, headers=headers, params=payload)
    status_code = response.status_code
    result = response.json()["result"]
    if status_code == 200:
        return float(result)
    else:
        return 0.0
