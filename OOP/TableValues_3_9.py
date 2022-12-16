class Cell:

    def __init__(self, data=0):
        self.__data = data


    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data



class TableValues:

    def __init__(self, rows, cols, data_type=int):
        self.__rows = rows
        self.__cols = cols
        self.__data_type = data_type
        self.__lst = [[Cell() for col in range(cols)] for row in range(rows)]


    def __is_valid_idxs(self, idxs):
        if idxs[0] > self.__rows or idxs[1] > self.__cols:
            raise IndexError('неверный индекс')


    def __is_valid_value(self, value):
        if type(value) != self.__data_type:
            raise TypeError('неверный тип присваиваемых данных')


    def __getitem__(self, idxs):
        self.__is_valid_idxs(idxs)

        return self.__lst[idxs[0]][idxs[1]].data


    def __setitem__(self, idxs, value):
        self.__is_valid_idxs(idxs)
        self.__is_valid_value(value)

        self.__lst[idxs[0]][idxs[1]].data = value


    def __iter__(self):
        for row in self.__lst:
            yield (i.data for i in row)


a = TableValues(3, 3)
a[1, 1] = 4
print(a[1,1])

for row in a:
    print()
    for col in row:
        print(col, end=' ')


