class Integer:
    def __init__(self, value=0):
        self.__value = value


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__is_valid(value)
        self.__value = value


    def __is_valid(self, value):
        if type(value) != int:
            raise ValueError('должно быть целое число')


    def __repr__(self):
        return str(self.__value)



class Array:
    def __init__(self, max_length, cell):
        self.max_length = max_length
        self.cell = cell
        self.arr  = [Integer() for _ in range(max_length)]


    def __is_valid_key(self, key):
        if type(key) != int or key >= self.max_length or key < 0:
            raise IndexError('неверный индекс для доступа к элементам массива')


    def __getitem__(self, key):
        self.__is_valid_key(key)
        return self.arr[key].value


    def __setitem__(self, key, value):
        self.__is_valid_key(key)
        self.arr[key].value = value


    def __repr__(self):
        return ' '.join(map(str, self.arr))


ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10
print(ar_int)
ar_int[1] = 10.5 # должно генерироваться исключение ValueError
# ar_int[10] = 1 # должно генерироваться исключение IndexError
