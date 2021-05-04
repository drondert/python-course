"""
Написать функцию email_parse(<email_address>),
которая при помощи регулярного выражения извлекает
имя пользователя и почтовый домен из email адреса
и возвращает их в виде словаря.
Если адрес не валиден, выбросить исключение ValueError.
"""

import re

EXAMPLES = [
    'someone@geekbrains.ru',
    'drondert@mail.ru',
    'invalid_address',
    'invalid@address'
]
RE_EMAIL = re.compile(r'(.+)@(.+\..+)')


def email_parse(email_address):
    reg_find = RE_EMAIL.findall(email_address)
    if reg_find:
        return {'username': reg_find[0][0], 'domain': reg_find[0][1]}
    else:
        raise ValueError(f'wrong email: {email_address}')


if __name__ == '__main__':
    for email in EXAMPLES:
        # try:
        #     print(email_parse(email))
        # except ValueError:
        #     print(email)
        print(email_parse(email))
