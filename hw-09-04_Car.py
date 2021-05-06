"""
Реализуйте базовый класс Car:
    у класса должны быть следующие атрибуты:
        speed,
        color,
        name,
        is_police (булево).
    А также методы:
    go,
    stop,
    turn(direction),
    которые должны сообщать, что машина поехала, остановилась, повернула (куда);
    опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
    добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
    для классов TownCar и WorkCar переопределите метод show_speed.
        При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

    Создайте экземпляры классов, передайте значения атрибутов.
    Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина тронулась')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина разворачивается {direction}')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')
        if self.speed > 60:
            print('Превышение скорости!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')
        if self.speed > 60:
            print('Превышение скорости!')


class PoliceCar(Car):
    pass


if __name__ == '__main__':
    car_1 = Car(61, 'blue', 'DullName', False)
    car_2 = TownCar(100, 'red', 'RedIsFaster', False)
    car_3 = SportCar(120, 'red', 'Fancy', False)
    car_4 = WorkCar(59, 'gray', 'Work-Work', False)
    car_5 = PoliceCar(90, 'white', 'Hot Fuzz', True)
    list_of_cars = [
        car_1,
        car_2,
        car_3,
        car_4,
        car_5,
    ]
    for car in list_of_cars:
        print(car.name, car.color, type(car))
        car.show_speed()
