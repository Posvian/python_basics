# Сделайте эту же задачу для интервала
# от 1 до 200. Подумайте над тем почему
# такая задача - усложненная? В чем сложность?

number = 0
while number <= 200:
    if number % 10 == 0 or 4 < number % 10 <= 9 or 10 < number % 100 < 20:
        print(number, 'процентов')
    elif number % 10 == 1:
        print(number, 'процент')
    elif 1 < number % 10 < 5:
        print(number, 'процента')
    number += 1
