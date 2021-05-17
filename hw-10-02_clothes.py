from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def fabric_expansion(self):
        pass


class Coat(Clothes):

    @property
    def fabric_expansion(self):
        return self.param / 6.5 + 0.5


class Suit(Clothes):

    @property
    def fabric_expansion(self):
        return 2 * self.param + 0.3


if __name__ == '__main__':
    my_clothes = [Coat(10), Suit(10)]
    for cloth in my_clothes:
        print(cloth.fabric_expansion)
