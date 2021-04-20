from pprint import pprint


def thesaurus_adv(*args):
    dictionary_of_last_names = {}
    for full_name in args:
        first_name, last_name = full_name.split()
        first_letter_of_last_name = last_name[0]
        first_letter_of_first_name = first_name[0]
        if first_letter_of_last_name not in dictionary_of_last_names:
            dictionary_of_last_names[first_letter_of_last_name] = {}
        if first_letter_of_first_name not in dictionary_of_last_names[first_letter_of_last_name]:
            dictionary_of_last_names[first_letter_of_last_name][first_letter_of_first_name] = []
        dictionary_of_last_names[first_letter_of_last_name][first_letter_of_first_name].append(full_name)
    return dictionary_of_last_names


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
pprint(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"), width=1)
