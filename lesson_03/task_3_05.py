#Реализовать функцию get_jokes(),
# возвращающую n шуток, сформированных
# из трех случайных слов, взятых из трёх
# заданных списков.

import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(joke_amount, first_list, second_list, third_list):
    """make amount of random jokes from three lists"""
    joke_number = 1
    jokes = []
    while joke_number <= joke_amount:
        first_word = random.choice(first_list)
        second_word = random.choice(second_list)
        third_word = random.choice(third_list)
        joke = f'{first_word} {second_word} {third_word}'
        jokes.append(joke)
        joke_number += 1
    return jokes


print(get_jokes(5, nouns, third_list = ['яркий'], second_list = ['вчера']))
print(get_jokes(3, nouns, adverbs, adjectives))

