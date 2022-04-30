# Реализовать склонение слова «процент»
# во фразе «N процентов».
number = 0
while number <= 101:
    if number % 10 == 0 or 4 < number % 10 <= 9 or 10 < number < 20:
        print(number, 'процентов')
    elif number % 10 == 1:
        print(number, 'процент')
    elif 1 < number % 10 < 5:
        print(number, 'процента')
    number += 1
