from random import choice


def get_jokes(n, *args):
    jokes_lists = []
    for number in range(n):
        full_joke = ""
        for input_list in args:
            full_joke += f' {choice(input_list)}'
        jokes_lists.append(full_joke)
    return jokes_lists


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes(5, nouns, adverbs, adjectives))
