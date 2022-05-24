# Написать свой модуль utils и перенести в него функцию
# currency_rates и currency_rates_advanced, если вы
# решали задание 2. Создать скрипт, импортировать в
# него модуль utils и выполнить несколько вызовов функции
# currency_rates. Убедиться, что ничего лишнего не происходит.
from utils import currency_rates_advanced, currency_rates

print(currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', "USd"))
print(currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', "EuR"))
print(currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', "GBP"))
print(currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', "GBP2"))
print(currency_rates_advanced('http://www.cbr.ru/scripts/XML_daily.asp', "USd"))
print(currency_rates_advanced('http://www.cbr.ru/scripts/XML_daily.asp', "EuR"))
print(currency_rates_advanced('http://www.cbr.ru/scripts/XML_daily.asp', "GBP"))
print(currency_rates_advanced('http://www.cbr.ru/scripts/XML_daily.asp', "GBP2"))