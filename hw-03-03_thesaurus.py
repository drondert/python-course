def thesaurus(*args):
    dictionary_of_names = {}
    for name in args:
        first_letter = name[0].upper()
        if first_letter not in dictionary_of_names:
            dictionary_of_names[first_letter] = [name]
        else:
            dictionary_of_names[first_letter].append(name)
    return dictionary_of_names


list_of_names = ['Иван', 'Мария', 'Петр', 'Илья', 'Павел', 'Яков', 'Михаил']
print(thesaurus(*list_of_names, 'Иоанн', 'Константин'))
print(dict(sorted(thesaurus(*list_of_names, 'Иоанн', 'Константин').items())))
