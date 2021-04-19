import requests

CURRENCY_API_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


def currency_rates(char_code):
    char_code = char_code.upper()
    response = requests.get(CURRENCY_API_URL).text
    try:
        return float(response[response.find('<Value>', response.find(char_code)) + 7:response.find('</Value>',
                              response.find(char_code))].replace(',', '.'))
    except ValueError:
        return None


print(currency_rates('usd'))
print(currency_rates('qwe'))
