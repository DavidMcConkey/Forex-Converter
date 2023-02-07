from forex_python.converter import CurrencyRates, CurrencyCodes, Decimal, RatesNotAvailableError

curr = CurrencyRates(force_decimal=True)
cd = CurrencyCodes()

def result(start,end,amt):
    """Returns string that states beginning and ending currency and final amount"""
    amt_dec = Decimal(amt) #Allows input to be float or int
    end_amt = round(curr.convert(start.upper(),end.upper(), amt_dec), 2)
    curr_symbol = cd.get_symbol(end)
    res = f"""{curr_symbol}{end_amt}"""
    return res

def code_validity(code):
    """Returns true if valid currency, otherwise false"""
    valid_currency_codes = ["EUR", "IDR", "BGN", "ILS", "GBP", "DKK", "CAD",
                        "JPY", "HUF", "RON", "MYR", "SEK", "SGD", "HKD",
                        "AUD", "CHF", "KRW", "CNY", "TRY", "HRK", "NZD",
                        "THB", "USD", "NOK", "RUB", "INR", "MXN", "CZK",
                        "BRL", "PLN", "PHP", "ZAR"]
    if code in valid_currency_codes:
        return True
    else:
        return False


def num_validity(num):
    """Returns true if arg is an integer or float, returns false if else"""
    try:
        num_float = float(num)
        if num_float <= 0:
            return False
        return True
    except ValueError:
        return False