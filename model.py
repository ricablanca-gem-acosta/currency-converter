import requests


def currencies():
    response = requests.get(
        "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json")
    return response.json()


def rate(date, from_currency, to_currency):
    response = requests.get(
        "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{date}/currencies/eur.json".format(date=date)).json()
    from_euro = response["eur"][from_currency]
    to_euro = response["eur"][to_currency]
    return round(to_euro / from_euro, 4)
