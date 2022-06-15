import requests
import json

from config import keys


class APIException(Exception):
    pass


class Convertor:
    @staticmethod
    def get_price(base, sym, amount):
        try:
            base_key = keys[base.lower()]
        except KeyError:
            raise APIException(f"Не верно указана валюта - {base}! 👉 /start")

        try:
            sym_key = keys[sym.lower()]
        except KeyError:
            raise APIException(f"Не верно указана валюта - {sym}! 👉 /start")

        if base_key == sym_key:
            raise APIException(f'Невозможно конвертировать одинаковые валюты - {base}! 👉 /start')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не верно указано количество валюты - {amount}! 👉 /start')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_key}&tsyms={sym_key}')
        total_base = json.loads(r.content)[keys[sym.lower()]] * amount
        total_base = round(total_base, 3)
        return total_base
