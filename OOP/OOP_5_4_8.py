class CellException(Exception):
    pass


class CellIntegerException(CellException):
    pass


class CellFloatException(CellException):
    pass


class CellStringException(CellException):
    pass


class Cell:
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._is_valid(value)
        self._value = value

    def __repr__(self):
        return str(self._value)


class CellInteger(Cell):
    def _is_valid(self, value):
        if type(value) != int or value < self._min_value or value > self._max_value:
            raise CellIntegerException('значение выходит за допустимый диапазон')
    

class CellFloat(Cell):
    def _is_valid(self, value):
        if type(value) != float or value < self._min_value or value > self._max_value:
            raise CellFloatException('значение выходит за допустимый диапазон')
    


class CellString(Cell):
    def __init__(self, min_length, max_length):
        self._min_length = min_length
        self._max_length = max_length

    def _is_valid(self, value):
        if type(value) != str or len(value) < self._min_length or len(value) > self._max_length:
            raise CellStringException('длина строки выходит за допустимый диапазон')


class TupleData:
    def __init__(self, *args):
        if not all(isinstance(i, Cell) for i in args):
            raise TypeError
        self._lst = list(args)

    def __getitem__(self, idx):
        return self._lst[idx]

    def __setitem__(self, idx, value):
        self._lst[idx].value = value

    def __iter__(self):
        for i in self._lst:
            yield i.value

    def __len__(self):
        return len(self._lst)


ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))


try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.5
    ld[3] = "asf"
    print(ld._lst)
    for i in ld:
        print(i)
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")


