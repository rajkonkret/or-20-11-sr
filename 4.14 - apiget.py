# json  -> {"name" : "Radek"}
from typing import List

import requests
from pydantic import BaseModel

url = 'http://api.nbp.pl/api/exchangerates/rates/A/USD/'

response = requests.get(url)
print(response)
# <Response [200]> ok
# 3XX - błedy np.: przekierowania
# 4XX - błedy po stronie uzytkownika
# 5xx - błedy pp ostronie serwera

table = response.json()
print(table)
# {'table': 'A', 'currency': 'dolar amerykański', 'code': 'USD',
#  'rates': [{'no': '227/A/NBP/2023', 'effectiveDate': '2023-11-23', 'mid': 3.9969}]}

print(table['rates'][0]['mid'])


class Rate(BaseModel):
    no: str
    effectiveDate: str
    mid: float


class ExchangeRate(BaseModel):
    table: str
    currency: str
    code: str
    rates: List[Rate]


ex_rate = ExchangeRate.parse_raw(response.text)
print(ex_rate)
# table='A' currency='dolar amerykański' code='USD'
# rates=[Rate(no='227/A/NBP/2023', effectiveDate='2023-11-23', mid=3.9969)]
print(ex_rate.rates)  # [Rate(no='227/A/NBP/2023', effectiveDate='2023-11-23', mid=3.9969)]
for i in ex_rate.rates:
    print(f"{i.no}, {i.effectiveDate} {i.mid}")
# [Rate(no='227/A/NBP/2023', effectiveDate='2023-11-23', mid=3.9969)]
