import requests
import requests.utils
import datetime


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


def currency_rates_advanced(url, currency_code):
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
            result = datetime.datetime.now().date(), float(rate)
            return result


if __name__ == '__main__':
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    print(currency_rates(url, "USd"))
    print(currency_rates(url, "EuR"))
    print(currency_rates(url, "GBP"))
    print(currency_rates(url, "GBP2"))
    print(currency_rates_advanced(url, "USd"))
    print(currency_rates_advanced(url, "EuR"))
    print(currency_rates_advanced(url, "GBP"))
    print(currency_rates_advanced(url, "GBP2"))