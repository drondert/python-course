"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
чья прибыль ниже среднего.
"""
from collections import defaultdict


def return_lower_higher_avg(organizations):
    average_profit = sum([sum(org_profit) for org_profit in organizations.values()]) / len(organizations)
    lower_higher_avg = defaultdict(list)
    for k, v in organizations.items():
        if sum(v) > average_profit:
            lower_higher_avg['Прибыль выше средней'].append(k)
        else:
            lower_higher_avg['Прибыль ниже средней'].append(k)
    return lower_higher_avg


if __name__ == '__main__':
    organizations = defaultdict(list)
    while 1:
        org_name = input('Введите название организации: ')
        if org_name in ['', 'stop']:
            break
        org_profit = input('Введите прибыль поквартально через запятую: ').strip().split(',')
        for quarter in range(4):
            try:
                organizations[org_name].append(float(org_profit[quarter]))
            except IndexError:
                organizations[org_name].append(0)
    print(return_lower_higher_avg(organizations))
