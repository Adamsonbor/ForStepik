class Validator:

    def __call__(self, data):
        return self._is_valid(data)
        

class IntegerValidator(Validator):

    def __init__(self, min_value, max_value):
        self.__min_value = min_value
        self.__max_value = max_value


    def _is_valid(self, data):
        if type(data) != int or data < self.__min_value or data > self.__max_value:
            raise ValueError('данные не прошли валидацию')
        return True



class FloatValidator(Validator):

    def __init__(self, min_value, max_value):
        self.__min_value = min_value
        self.__max_value = max_value


    def _is_valid(self, data):
        if type(data) != float or data < self.__min_value or data > self.__max_value:
            raise ValueError('данные не прошли валидацию')
        return True

integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)
res1 = integer_validator(10)  # True
res2 = float_validator(10)    # исключение ValueError
