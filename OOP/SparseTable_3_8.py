class Cell:
    
    def __init__(self, data: any):
        self.value = data



class SparseTable:

    def __init__(self):
        self.__rows = 0
        self.__cols = 0
        self.__cells = dict()


    @property
    def rows(self):
        return max(row for row, col in self.__cells.keys()) + 1

    
    @property
    def cols(self):
        return max(col for row, col in self.__cells.keys()) + 1


    def add_data(self, row: int, col: int, data: any):
        self.__cells[(row, col)] = Cell(data)


    def remove_data(self, row: int, col:int):
        if (row, col) not in self.__cells:
            raise IndexError('ячейка с указанными индексами не существует')
        del self.__cells[(row, col)]


    def __getitem__(self, keys: tuple):
        if keys not in self.__cells:
            raise ValueError('данные по указанным индексам отсутствуют')
        return self.__cells[keys].value


    def __setitem__(self, keys: tuple, value: any):
        self.__cells[keys] = Cell(value)


st = SparseTable()
st.add_data(2, 5, Cell(25))
st.add_data(1, 1, Cell(11))
assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"

try:
    v = st[3, 2]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

st[3, 2] = 100
assert st[3, 2] == 100, "неверно отработал оператор присваивания нового значения в ячейку таблицы"
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"

st.remove_data(1, 1)
try:
    v = st[1, 1]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"
    
try:
    st.remove_data(1, 1)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

d = Cell('5')
assert d.value == '5', "неверное значение атрибута value в объекте класса Cell, возможно, некорректно работает инициализатор класса"
        




