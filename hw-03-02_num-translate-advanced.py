NUM_TRANSLATION_DICTIONARY_EN_RU = {
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


def num_translate(num):
    translated_num = NUM_TRANSLATION_DICTIONARY_EN_RU.get(num.lower())
    if num == num.capitalize() and translated_num is not None:
        return translated_num.capitalize()
    else:
        return translated_num


test_list = ['one', 'Two', 'too', 'three', 'Free', 'four', 'FOR', 'Five', 'fIvE',
             'six', 'Seven', 'eight', 'nine', 'Ten']
for elem in test_list:
    print(f'{elem} {num_translate(elem)}')
