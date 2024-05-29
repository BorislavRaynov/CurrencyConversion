from .validators import is_valid_date
from .conv_logging import save_conversion_log
from .converter import CurrencyConverter


class CurrencyConversionCLI:
    def __init__(self):
        self.converter = CurrencyConverter()

    def run(self):
        running = True

        while running:
            date = input("Enter date (YYYY-MM-DD) or 'END' to quit: ").strip()
            if date.upper() == 'END':
                break
            if not is_valid_date(date):
                print("Invalid date format. Please try again.")
                continue

            while running:
                available_currencies = self.converter.get_available_currencies()
                base_currency = input("Enter base currency (ISO 4217 code) or 'END' to quit: ").strip().upper()
                if base_currency == 'END':
                    running = False
                    break
                if base_currency not in available_currencies:
                    print("Invalid currency code. Please try again.")
                    continue

                while running:
                    target_currency = input("Enter target currency (ISO 4217 code) or 'END' to quit: ").strip().upper()
                    if target_currency == 'END':
                        running = False
                        break
                    if target_currency not in available_currencies:
                        print("Invalid currency code. Please try again.")
                        continue
                    if target_currency == base_currency:
                        print("Target currency is the same as base currency. Please enter different.")
                        continue

                    while running:
                        amount = input("Enter amount to convert: ").strip()
                        if isinstance(amount, str):
                            if amount.upper() == 'END':
                                running = False
                                break

                            else:
                                try:
                                    amount = round(float(amount), 2)
                                except ValueError:
                                    print("Invalid amount. Please enter a numeric value or 'END' to quit: .")
                                    continue

                                try:
                                    converted_amount = self.converter.convert(date, base_currency, target_currency, amount)
                                    print(f"{amount} {base_currency} = {converted_amount} {target_currency} on {date}")
                                    log_entry = {
                                        "date": date,
                                        "base_currency": base_currency,
                                        "target_currency": target_currency,
                                        "amount": amount,
                                        "converted_amount": converted_amount
                                    }
                                    save_conversion_log(log_entry)
                                except ValueError as e:
                                    print(e)
