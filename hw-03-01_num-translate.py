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
    return NUM_TRANSLATION_DICTIONARY_EN_RU.get(num.lower())


test_list = ['one', 'two', 'too', 'three', 'free', 'four', 'FOR', 'five', 'fIvE',
             'six', 'seven', 'eight', 'nine', 'ten']
for elem in test_list:
    print(num_translate(elem))
