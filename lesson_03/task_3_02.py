# усложненный вариант задания 1. Написать
# функцию num_translate_adv, которая
# корректно обработает числительные,
# начинающиеся с заглавной буквы. Если
# перевод сделать невозможно, вернуть объект None.

def num_translate_adv(number):
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
    if f'{number}'.istitle():
        number = number.lower()
        return nums_dict.get(number).capitalize()
    else:
        return nums_dict.get(number)


print(num_translate_adv('One'))

print(num_translate_adv('two'))

print(num_translate_adv('twelve'))
