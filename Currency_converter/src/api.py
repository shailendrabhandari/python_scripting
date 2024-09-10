import requests

API_URL = "http://apilayer.net/api/live"
API_KEY = "f479d95cf436f4e67446a015f25284ec"
VALID_CURRENCIES = ["USD", "EUR", "GBP", "INR", "AUD", "CAD", "SGD", "JPY", "CNY", "CHF"]

def get_conversion_rate(from_currency, to_currency):
    if from_currency not in VALID_CURRENCIES or to_currency not in VALID_CURRENCIES:
        raise ValueError("Invalid currency code.")

    params = {
        'access_key': API_KEY,
        'currencies': to_currency,
        'source': from_currency,
        'format': 1
    }

    response = requests.get(API_URL, params=params)

    if response.status_code != 200:
        print(f"Failed to fetch data: {response.status_code}, {response.text}")
        raise Exception("Error fetching data from API")

    data = response.json()

    if 'error' in data:
        print(f"Error in response: {data['error']}")
        raise Exception("API returned an error.")

    rate_key = f"{from_currency}{to_currency}"
    return data['quotes'].get(rate_key)
