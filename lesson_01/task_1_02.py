# Для кубов нечётных чисел от 1 до 1000.
# Вычислить сумму чисел, сумма цифр кубов
# которых делится нацело на 7.

number = 1
number_sum = 0
while number <= 1000:
    digit = number**3
    numeric_sum = 0
    while digit > 0:
        numeric = digit % 10
        numeric_sum += numeric
        digit = digit // 10
    if numeric_sum % 7 == 0:
        number_sum += number
        print(number, '^3 =', number**3, [numeric_sum], 'накоп. сумма:', number_sum)
    number += 2
