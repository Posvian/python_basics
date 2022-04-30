# Написать функцию currency_rates(), принимающую в качестве
# аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю.
import requests
import requests.utils

url = 'http://www.cbr.ru/scripts/XML_daily.asp'


def currency_rates(url, currency_code):
    response = requests.get(url)
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    content = content.split('ID=')[1:]
    currency_code = currency_code.upper()
    for cell in content:
        if currency_code in cell:
            cell = cell.split('<Value>')
            rate = cell[1][:7]
            rate = rate.replace(',', '.')
            return float(rate)


print(currency_rates(url, "USd"))
print(currency_rates(url, "EuR"))
print(currency_rates(url, "GBP"))
print(currency_rates(url, "GBP2"))
