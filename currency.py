import requests

API_KEY = "*****************" # Your own API_KEY, we added only for test purposes. Please use .env files.

# url = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}"

"""
curl --request GET \
--url 'https://api.apilayer.com/exchangerates_data/symbols' \
--header 'apikey: UinwoMMdbMWIwybSbAHi2TdH6oH4DRFG'
"""

url = "https://api.apilayer.com/exchangerates_data/symbols"
headers = {
    'apikey': 'UinwoMMdbMWIwybSbAHi2TdH6oH4DRFG'
}

response = requests.get(url, headers)
response.status_code
data = response.json()
data["symbols"]

currency_from = "TRY"
currency_to = "USD"
amount = 20
url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"

response = requests.get(url, headers)
response.status_code
data = response.json()
data
