# Написать функцию num_translate,
# переводящую числительные от 0 до 10
# c английского на русский язык.
def num_translate(number):
    nums_dict = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    number = number.lower()
    return nums_dict.get(number)


print(num_translate("one"))

print(num_translate("eight"))

print(num_translate("twelv"))
