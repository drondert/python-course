"""
Реализовать класс Stationery (канцелярская принадлежность):
    определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
    создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
    в каждом классе реализовать переопределение метода draw.
    Для каждого класса метод должен выводить уникальное сообщение;
    создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Рисуем, чем попало')


class Pen(Stationery):
    def draw(self):
        print('Чернила повсюду')


class Pencil(Stationery):
    def draw(self):
        print('Грифелем по бумаге')


class Handle(Stationery):
    def draw(self):
        print('Такое и не сотрешь')


if __name__ == '__main__':
    for objects_to_check in [Stationery('Палка'), Pen('Батина ручка'), Pencil('Огрызок'), Handle('Неизвестный объект')]:
        print(f'Предмет для рисования: {objects_to_check.title}')
        objects_to_check.draw()
