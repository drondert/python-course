import random


class LotoCard:
    NUMBER_OF_SPACES = 4
    NUMBER_OF_DIGITS = 5
    MAX_NUMBER_OF_DIGITS = 15
    MAX_POSSIBLE_DIGIT = 90
    MAX_CELL_LEN = 3

    def __init__(self):
        def check_sort_item(item):
            if isinstance(item, int):
                return item
            else:
                return random.randint(1, LotoCard.MAX_POSSIBLE_DIGIT)

        self._numbers_stroked = 0
        self._card_content = [
            [],
            [],
            []
        ]
        numbers_pool = random.sample(range(1, 1 + LotoCard.MAX_POSSIBLE_DIGIT), LotoCard.MAX_NUMBER_OF_DIGITS)
        for row in self._card_content:
            for _ in range(LotoCard.NUMBER_OF_SPACES):
                row.append('')
            for _ in range(LotoCard.NUMBER_OF_DIGITS):
                row.append(numbers_pool.pop())

        for index, row in enumerate(self._card_content):
            self._card_content[index] = sorted(row, key=check_sort_item)

    def __str__(self):
        body = '\n'
        for row in self._card_content:
            for cell in row:
                body += str(cell).ljust(LotoCard.MAX_CELL_LEN)
            body += '\n'
        return body

    def has_number(self, number):
        for row in self._card_content:
            if number in row:
                return True
        return False


class LotoPlayer:
    def __init__(self, name, is_cpu=False):
        if not isinstance(is_cpu, bool):
            raise ValueError('bool only')
        self.is_cpu = is_cpu
        self.name = name
        self.loto_card = LotoCard()

    def __str__(self):
        return f'{"-" * ((26 - len(self.name)) // 2)} {self.name} {"-" * ((26 - len(self.name)) // 2)}'\
               + self.loto_card.__str__()

    def try_stroke_number(self, number):
        for index, row in enumerate(self.loto_card._card_content):
            for num_index, number_in_card in enumerate(row):
                if number == number_in_card:
                    self.loto_card._card_content[index][num_index] = '-'
                    self.loto_card._numbers_stroked += 1
                    return True
        return False


class LotoGame:
    MAX_NUMBER_OF_TURNS = 90

    def __init__(self, human, cpu):
        self.human = human
        self.cpu = cpu

    def start(self):
        game_is_running = True
        for turn, number in enumerate(random.sample(range(1, 1 + LotoCard.MAX_POSSIBLE_DIGIT), LotoCard.MAX_POSSIBLE_DIGIT)):
            number = random.randint(1, LotoCard.MAX_POSSIBLE_DIGIT)
            print(f'Новый бочонок: {number} (осталось {LotoGame.MAX_NUMBER_OF_TURNS - turn - 1})')
            for player in [self.human, self.cpu]:
                print(player)

            user_input = ''
            while user_input != 'y' and user_input != 'n':
                user_input = input('Зачеркнуть цифру? (y/n)\n')
            if user_input == 'y':
                if not self.human.try_stroke_number(number):
                    msg = 'Вы проиграли! Удачи в следующий раз!'
                    break
            elif user_input == 'n':
                if self.human.loto_card.has_number(number):
                    msg = 'Вы проиграли! Удачи в следующий раз!'
                    break
            if self.human.loto_card._numbers_stroked == LotoCard.MAX_NUMBER_OF_DIGITS:
                msg = 'Победа за Вами!'

            if self.cpu.loto_card.has_number(number):
                self.cpu.try_stroke_number(number)
        else:
            msg = 'Закончились бочонки?!'
        print(msg)


if __name__ == '__main__':
    LotoGame(LotoPlayer(name='Костя'), LotoPlayer(name='CPU-1', is_cpu=True)).start()
