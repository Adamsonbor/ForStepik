class Validator:
    def _is_valid(self, data):
        raise NotImplementedError('в классе не переопределен метод _is_valid')

    def __call__(self, data):
        return self._is_valid(data)


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.__min_value = min_value
        self.__max_value = max_value

    def _is_valid(self, data):
        return type(data) is float and self.__min_value <= data <= self.__max_value
    
float_validator = FloatValidator(0, 10.5)
res_1 = float_validator(1)  # False (целое число, а не вещественное)
res_2 = float_validator(1.0)  # True
res_3 = float_validator(-1.0)  # False (выход за диапазон [0; 10.5])
print(res_3, res_2, res_1)
