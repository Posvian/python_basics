# Реализовать класс Matrix (матрица)

class Matrix:
    def __init__(self, matrix):
        lst_length = []
        for el in range(len(matrix)):
            lst_length.append(len(matrix[el]))
        if len(set(lst_length)) == 1:
            self.matrix = matrix
        else:
            raise ValueError("Incorrect data for Matrix initialization: not equal lenght of lists")

    def __str__(self):
        matrix = ''
        for el in self.matrix:
            matrix += '| '
            for i in el:
                matrix += '{:>3}'.format(i)
            matrix += ' |\n'
        return matrix

    def __add__(self, other):
        rez = []
        for i in range(len(self.matrix)):
            rez1 = []
            if len(self.matrix) == len(other.matrix):
                for el in range(len(self.matrix[i])):
                    if len(self.matrix[i]) == len(other.matrix[i]):
                        rez1.append(self.matrix[i][el] + other.matrix[i][el])
                    else:
                        raise ValueError('Incorrect dimensions for add method')
                rez.append(rez1)
            else:
                raise ValueError('Incorrect dimensions for add method')
        return Matrix(rez)


if __name__ == '__main__':
    m1 = Matrix([[11,2,3],[4,5,6],[117,8,9]])
    m2 = Matrix([[1,1,1],[1,1,1],[1,1,1]])
    print(m1)
    print(m2)

    m4 = m1 + m2
    print(m4)
    print(type(m4))

    m3 = Matrix([[1, 1], [1, 1], [1, 1]])
    print(m3)

    # Подтверждение работы ValueError при сложении матриц разной длины
    # m5 = m1 + m3

    # Подтверждения работы ValueError при создании некорректной матрицы
    # m6 = Matrix([[1, 1, 1, 1], [1, 1, 1], [1, 1, 1]])
