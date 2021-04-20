from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Александр',
    'Михаил'
]
klasses = [
    '9А', '7В', '9Б', '9В',
    '8Б', '10А', '10Б', '9А'
]


def tutor_class_gen():
    for iterator, (tutor_name, klass_name) in enumerate(zip_longest(tutors, klasses)):
        if iterator < len(tutors):
            yield tutor_name, klass_name


if __name__ == '__main__':
    print(type(tutor_class_gen()))
    for tutor_klass_tuple in tutor_class_gen():
        print(tutor_klass_tuple)
