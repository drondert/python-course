"""
Реализовать базовый класс Worker (работник):
    определить атрибуты: name, surname, position (должность), income (доход);
    последний атрибут должен
        быть защищённым
        ссылаться на словарь, содержащий элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
    создать класс Position (должность) на базе класса Worker;
    в классе Position реализовать методы
        получения полного имени сотрудника (get_full_name)
        дохода с учётом премии (get_total_income);
    проверить работу примера на реальных данных:
        создать экземпляры класса Position,
        передать данные,
        проверить значения атрибутов,
        вызвать методы экземпляров.
"""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            'wage': wage,
            'bonus': bonus
        }


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())


if __name__ == '__main__':
    employee_1 = Position('Kostya', 'Fedorov', 'peon', 30000, 5000)
    employee_2 = Position('Sasha', 'Susin', 'peasant', 35000, 1000)
    list_of_employees = [employee_1, employee_2]
    for employee in list_of_employees:
        print(
            employee.name,
            employee.surname,
            employee.position,
            employee.get_full_name(),
            employee.get_total_income()
        )
