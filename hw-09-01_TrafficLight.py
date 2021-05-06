"""
Создать класс TrafficLight (светофор):
    определить у него один атрибут color (цвет) и метод running (запуск);
    атрибут реализовать как приватный;
    в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
    продолжительность
        первого состояния (красный) составляет 7 секунд,
        второго (жёлтый) — 2 секунды,
        третьего (зелёный) — на ваше усмотрение;
    переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
    проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов.
При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

import time


class TrafficLight:
    color_time = {
        'red': 7,
        'yellow': 2,
        'green': 4
    }

    def __init__(self):
        self.__color = 'red'

    def running(self):
        time_tick = 0
        timers_sum = sum(self.color_time.values())
        while True:
            print(f'{time_tick} second(s), Traffic light is {self.__color}')
            time_tick += 1
            time.sleep(1)
            if time_tick % timers_sum < self.color_time['red']:
                self.__color = 'red'
            elif time_tick % timers_sum < self.color_time['red'] + self.color_time['yellow']:
                self.__color = 'yellow'
            else:
                self.__color = 'green'


if __name__ == '__main__':
    post_1 = TrafficLight()
    post_1.running()
