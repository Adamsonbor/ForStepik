from operator import add, sub

class Matrix:
    __operator = {'+':add, '-':sub}

    def __init__(self, *args):
        if len(args) == 1:
            self.__is_valid_lst(args[0])
            self.__matrix = args[0]
            self.__rows = len(args[0])
            self.__cols = len(args[0][0])
        else:
            self.__matrix = [[args[2] for col in range(args[1])] for col in range(args[0])]
            self.__rows = args[0]
            self.__cols = args[1]


    @property
    def rows(self):
        return self.__rows


    @property
    def cols(self):
        return self.__cols


    def __is_valid_value(self, value):
        if type(value) not in (int, float):
            raise TypeError('список должен быть прямоугольным, состоящим из чисел')


    def __is_valid_idxs(self, idxs):
        if idxs[0] > self.__rows or idxs[1] > self.__cols:
            raise IndexError('недопустимые значения индексов')


    def __is_valid_lst(self, lst):
        if any(len(lst[0]) != len(i) for i in lst) or any(type(i) not in (int, float) for row in lst for i in row):
            raise TypeError('список должен быть прямоугольным, состоящим из чисел')


    def __is_valid_dimensions(self, other):
        if self.__rows != other.rows or self.__cols != other.cols:
            raise ValueError('операции возможны только с матрицами равных размеров')


    def __do(self, other, operator='+'):
        op = self.__operator[operator]
        if type(other) is type(self):
            self.__is_valid_dimensions(other)
            out = Matrix(self.__rows, self.__cols, 0)
            for row in range(self.__rows):
                for col in range(self.__cols):
                        out[row, col] = op(self[row, col], other[row, col])
        else:
            self.__is_valid_value(other)
            out = Matrix([[op(self[row, col], other) for col in range(self.__cols)] for row in range(self.__rows)])

        return out


    def __getitem__(self, idxs):
        self.__is_valid_idxs(idxs)
        return self.__matrix[idxs[0]][idxs[1]]


    def __setitem__(self, idxs, value):
        self.__is_valid_idxs(idxs)
        self.__is_valid_value(value)
        self.__matrix[idxs[0]][idxs[1]] = value


    def __add__(self, other):
       return self.__do(other)


    def __sub__(self, other):
        return self.__do(other, '-')



    def __repr__(self):
        for row in self.__matrix:
            print()
            for col in row:
                print(col, end=' ')
        return ''







mt = Matrix([[1, 2], [3, 4]])
res = mt[0, 0] # 1
print(res)
res = mt[0, 1] # 2
print(res)
res = mt[1, 0] # 3
print(res)
res = mt[1, 1] # 4
print(res)
res = mt + mt
print(res)
res = mt + 10
print(res)
res = mt - 10
print(res)
res = mt - mt
print(res)

