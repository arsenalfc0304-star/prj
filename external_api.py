import requests

url = "https://api.apilayer.com/exchangerates_data/convert"

payload = {
    "amount": "1200",
    "from": "EUR",
    "to": "RUB"
}
headers = {
    "apikey": "Sa5AQJe8Ko8JXKWBVMuTRS9OhiRrNoOK"
}

response = requests.get(url, headers=headers, params=payload)

status_code = response.status_code
result = response.json()

print(status_code)
print(result)