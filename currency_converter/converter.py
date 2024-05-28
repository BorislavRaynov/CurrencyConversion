import requests
from .api_utils import load_api_key
from .cash_handler import load_cache, save_cache


class CurrencyConverter:
    def __init__(self):
        self.api_key = load_api_key()
        self.cache = load_cache()

    def fetch_exchange_rates(self, date, base_currency):
        if date not in self.cache:
            self.cache[date] = {}

        if base_currency not in self.cache[date]:
            url = f"https://api.fastforex.io/historical?date={date}&api_key={self.api_key}&from={base_currency}"
            response = requests.get(url)
            response.raise_for_status()
            self.cache[date][base_currency] = response.json()['results']
            save_cache(self.cache)

        return self.cache[date][base_currency]

    def convert(self, date, base_currency, target_currency, amount):
        rates = self.fetch_exchange_rates(date, base_currency)
        if target_currency in rates:
            return round(amount * rates[target_currency], 2)
        else:
            raise ValueError(f"No exchange rate available for {target_currency} on {date}")
