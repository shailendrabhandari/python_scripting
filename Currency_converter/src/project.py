import requests

# Global variables
API_URL = "http://apilayer.net/api/live"
API_KEY = "f479d95cf436f4e67446a015f25284ec"
VALID_CURRENCIES = ["USD", "EUR", "GBP", "INR", "AUD", "CAD", "SGD", "JPY", "CNY", "CHF"]


# Function to fetch conversion rate from one currency to another
def get_conversion_rate(from_currency, to_currency):
    if from_currency not in VALID_CURRENCIES or to_currency not in VALID_CURRENCIES:
        raise ValueError("Invalid currency code.")

    # Construct the URL for the API request
    params = {
        'access_key': API_KEY,
        'currencies': to_currency,
        'source': from_currency,
        'format': 1
    }
    print(f"Fetching data from: {API_URL} with params: {params}")  # Debugging step: Check the full URL and parameters

    response = requests.get(API_URL, params=params)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to fetch data: {response.status_code}, {response.text}")  # Print detailed error message
        raise Exception("Error fetching data from API")

    data = response.json()

    # Check if the response contains valid data
    if 'error' in data:
        print(f"Error in response: {data['error']}")
        raise Exception("API returned an error.")

    # Construct the key for the conversion rate (e.g., "USDEUR")
    rate_key = f"{from_currency}{to_currency}"

    return data['quotes'].get(rate_key)


# Function to convert the currency amount
def convert_currency(from_currency, to_currency, amount):
    rate = get_conversion_rate(from_currency, to_currency)
    if rate is None:
        raise ValueError(f"Cannot find conversion rate for {to_currency}")
    return amount * rate


# Main function to coordinate the program
def main():
    print("Welcome to the Currency Converter!")
    print("Supported currencies: ", ", ".join(VALID_CURRENCIES))

    from_currency = input("Enter the currency code you want to convert from: ").upper()
    to_currency = input("Enter the currency code you want to convert to: ").upper()
    amount = float(input("Enter the amount you want to convert: "))

    try:
        converted_amount = convert_currency(from_currency, to_currency, amount)
        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
