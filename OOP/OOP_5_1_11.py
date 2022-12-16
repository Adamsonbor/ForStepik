class Validator:
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value

    def __call__(self, value):
        raise NotImplementedError('hello')


class FloatValidator(Validator):
    def __call__(self, value):
        if type(value) != float or value < self._min_value or value > self._max_value:
            raise ValueError('значение не прошло валидацию')


class IntegerValidator(Validator):
    def __call__(self, value):
        if type(value) != int or value < self._min_value or value > self._max_value:
            raise ValueError('значение не прошло валидацию')


def is_valid(lst, validators):
    out = []
    for i in lst:
        for v in validators:
            try:
                v(i)
                out.append(i)
            except:
                pass
    return out

fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])   # [1, 4.5]
print(lst_out)

