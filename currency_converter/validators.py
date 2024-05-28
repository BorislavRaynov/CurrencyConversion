from datetime import datetime


def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def is_valid_currency(currency):
    return len(currency) == 3 and currency.isalpha()
