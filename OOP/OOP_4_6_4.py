class Digit:
    def __init__(self, value):
        print("DIGIT")
        if type(value) not in (int, float):
            raise TypeError('значение не соответствует типу объекта')

class Integer(Digit):
    def __init__(self, value):
        print("INTEGER")
        super().__init__(value)
        if type(value) != int:
            raise TypeError('значение не соответствует типу объекта')

class Float(Digit):
    def __init__(self, value):
        print("FLOAT")
        super().__init__(value)
        if type(value) != float:
            raise TypeError('значение не соответствует типу объекта')

class Positive(Digit):
    def __init__(self, value):
        print("POSITIVE")
        super().__init__(value)
        if value < 0:
            raise TypeError('значение не соответствует типу объекта')

class Negative(Digit):
    def __init__(self, value):
        print("NEGATIVE")
        super().__init__(value)
        if value >= 0:
            raise TypeError('значение не соответствует типу объекта')


class PrimeNumber(Integer, Positive):
    pass

class FloatPositive(Float, Positive):
    pass

a = PrimeNumber(10)
b = FloatPositive(12.2)

# digits = [PrimeNumber(10) if i < 3 else FloatPositive(10.2) for i in range(8)]
# lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
# lst_float = [i for i in digits if isinstance(i, Float)]
# print(lst_float)
