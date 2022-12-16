class ListMath:
    def __init__(self, lst=[]):
        self.lst_math = self.validate(lst)        

    @classmethod
    def validate(cls, lst):
        return [i for i in lst if cls.is_valid(i)]

    @classmethod
    def is_valid(cls, var):
        return type(var) in (int, float)

    def __add__(self, var):
        if self.is_valid(var):
            return ListMath(i + var for i in self.lst_math)

    def __radd__(self, var):
        return self + var

    def __iadd__(self, var):
        self.lst_math = [i + var for i in self.lst_math]
        return self

    def __sub__(self, var):
        if self.is_valid(var):
            return ListMath(i - var for i in self.lst_math)

    def __rsub__(self, var):
        return ListMath(var - i for i in self.lst_math)

    def __isub__(self, var):
        self.lst_math = [i - var for i in self.lst_math]
        return self

    def __mul__(self, var):
        if self.is_valid(var):
            return ListMath(i * var for i in self.lst_math)
   
    def __rmul__(self, var):
        return self * var

    def __imul__(self, var):
        self.lst_math = [i * var for i in self.lst_math]
        return self

    def __truediv__(self, var):
        if self.is_valid(var):
            return ListMath(round(i / var, 2) for i in self.lst_math)

    def __rtruediv__(self, var):
        return self / var

    def __itruediv__(self, var):
        self.lst_math = [round(i / var, 2) for i in self.lst_math]
        return self

    def __repr__(self):
        return ', '.join(str(i) for i in self.lst_math)


lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]
lst = lst + 76 # сложение каждого числа списка с определенным числом
print(lst)
lst = 6.5 + lst # сложение каждого числа списка с определенным числом
lst += 76.7  # сложение каждого числа списка с определенным числом
lst = lst - 76 # вычитание из каждого числа списка определенного числа
lst = 7.0 - lst # вычитание из числа каждого числа списка
lst -= 76.3
lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
lst *= 5.54
lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
lst = 3 / lst # деление числа на каждый элемент списка
lst /= 13.0
