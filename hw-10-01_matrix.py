class Matrix:

    @staticmethod
    def is_nested_list(obj_to_check):
        if obj_to_check:
            if isinstance(obj_to_check, list):
                for nested_list in obj_to_check:
                    if not isinstance(nested_list, list):
                        raise Exception(f'{nested_list} is not a list')
                return True
            raise Exception(f'{obj_to_check} is not a list')
        raise Exception(f'{obj_to_check} is empty')

    def __init__(self, list_of_lists):
        if self.is_nested_list(list_of_lists):
            self.content = list_of_lists

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.content])

    def __add__(self, other):
        result_list = []
        if not isinstance(other, Matrix):
            raise Exception(f'{other} is not of Matrix class')
        if len(self.content) == len(other.content):
            for row_1, row_2 in zip(self.content, other.content):
                if len(row_1) != len(row_2):
                    raise Exception(f'Cannot sum elements of Matrix class with different dimensions')

                result_list.append([elem_1 + elem_2 for elem_1, elem_2 in zip(row_1, row_2)])
        else:
            raise Exception(f'Cannot sum elements of Matrix class with different dimensions')

        return Matrix(result_list)


if __name__ == '__main__':
    mtx_1 = Matrix([[1, 2], [3, 4]])
    mtx_2 = Matrix([[5, 6], [7, 8]])
    print(mtx_1, '\n')
    print(mtx_2, '\n')
    print(mtx_1 + mtx_2)
