import requests
import json
from config import keys

class ConvertionExeption(Exception):
    pass

class Converter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionExeption(f'невозмодно перевести одинаковые валюты {base}.')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExeption(f'не удалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExeption(f'не удалось обработать валюту {base}')
        try:
            amount = str(amount)
        except ValueError:
            raise ConvertionExeption(f'не удалось обработать количество {amount}')

        url = (f"https://api.apilayer.com/exchangerates_data/convert?to={base_ticker}&from={quote_ticker}&amount={amount}")


        headers = {
            "apikey": "zT3eAh70YXEz8dJWF6D4ekl5hGxJKE5P"
        }
        payload = {}
        response = requests.request("GET", url, headers=headers, data = payload )
        status_code = response.status_code
        data = json.loads(response.text)
        total = (data["result"])


        return total
