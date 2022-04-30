from utils import currency_rates_advanced, currency_rates

print(currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', "USd"))
print(currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', "EuR"))
print(currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', "GBP"))
print(currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', "GBP2"))
print(currency_rates_advanced('http://www.cbr.ru/scripts/XML_daily.asp', "USd"))
print(currency_rates_advanced('http://www.cbr.ru/scripts/XML_daily.asp', "EuR"))
print(currency_rates_advanced('http://www.cbr.ru/scripts/XML_daily.asp', "GBP"))
print(currency_rates_advanced('http://www.cbr.ru/scripts/XML_daily.asp', "GBP2"))