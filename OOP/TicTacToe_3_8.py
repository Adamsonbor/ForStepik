class Cell:
    
    def __init__(self):
        self.value = 0
        self.is_free = True


    def __bool__(self):
        return self.is_free


    def __repr__(self):
        return str(self.value)


class TicTacToe:

    def __init__(self):
        self.pole = tuple(tuple(Cell() for row in range(3)) for col in range(3))


    def clear(self):
        for row in self.pole:
            for col in row:
                col.value = 0


    def __is_valid_idxs(self, *idxs):
        if any(i > 2 for i in idxs):
            raise IndexError('неверный индекс клетки')


    def __getitem__(self, keys):
        row, col = keys
        if type(row) is int and type(col) is int:
            self.__is_valid_idxs(row, col)
            return self.pole[row][col].value
        if type(row) is int:
            self.__is_valid_idxs(row)
            return tuple(i.value for i in self.pole[row][col])
        else:
            self.__is_valid_idxs(col)
            return tuple(i[col].value for i in self.pole)


    def __setitem__(self, keys, value):
        self.__is_valid_idxs(*keys)
        row, col = keys
        if not self.pole[row][col]:
            raise ValueError('клетка уже занята')
        row, col = keys
        self.pole[row][col].value = value


    def __str__(self):
        for row in self.pole:
            print()
            for col in row:
                print(col.value, end=' ')
        return ''

        







g = TicTacToe()
g.clear()
assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"
g[1, 1] = 1
g[2, 1] = 2
assert g[1, 1] == 1 and g[2, 1] == 2, "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"

try:
    res = g[3, 0]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"

    
try:
    g[3, 0] = 5
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"


g.clear()
g[0, 0] = 1
g[1, 0] = 2
g[2, 0] = 3
print(g)

assert g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (1, 2, 3), "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"

cell = Cell()
assert cell.value == 0, "начальное значение атрибута value класса Cell должно быть равно 0"
res = cell.is_free
cell.is_free = True
assert bool(cell), "функция bool вернула False для свободной клетки"
 
