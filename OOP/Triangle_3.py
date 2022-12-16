class Side:
    def __set_name__(self, owner, name):
        self.name = f"__{name}"


    def __get__(self, instance, owner):
        return getattr(instance, self.name)


    def __set__(self, instance, var):
        if type(var) not in (int, float) or var < 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        setattr(instance, self.name, var)


class Triangle:
    a = Side()
    b = Side()
    c = Side()

    def __init__(self, a, b, c):
        if a < b + c and b < a + c and c < b + a:
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError("с указанными длинами нельзя образовать треугольник")


    def __len__(self):
        return int(self.a + self.b + self.c)


    def __repr__(self):
        return f"{self.a} {self.b} {self.c}"


    def tr(self):
        p = len(self)
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


a = Triangle(5, 4, 3)
print(a)
print(len(a))
print(a.tr())
