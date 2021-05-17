class Cell:

    def __init__(self, num):
        if not isinstance(num, int):
            raise ValueError(f'{num} must be int')
        self.cells = num

    def __add__(self, other):
        if not isinstance(other, Cell):
            raise Exception(f'{other} is not a Cell')
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if not isinstance(other, Cell):
            raise Exception(f'{other} is not a Cell')
        if self.cells > other.cells:
            return Cell(self.cells - other.cells)
        else:
            return f'Невозможно выполнить вычитание'

    def __mul__(self, other):
        if not isinstance(other, Cell):
            raise Exception(f'{other} is not a Cell')
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        if not isinstance(other, Cell):
            raise Exception(f'{other} is not a Cell')
        return Cell(self.cells // other.cells)

    def __str__(self):
        return str(self.cells)

    def make_order(self, cells_in_row):
        return '\n'.join(['*' * cells_in_row for _ in range(self.cells // cells_in_row)]) \
            + '\n' + '*' * (self.cells % cells_in_row)


if __name__ == '__main__':
    big_cell = Cell(10)
    small_cell = Cell(3)
    print(big_cell.make_order(3))
    print(small_cell.make_order(2))
    print(big_cell + small_cell)
    print(big_cell - small_cell)
    print(small_cell - big_cell)
    print(big_cell / small_cell)
    print(big_cell * small_cell)
