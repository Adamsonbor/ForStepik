class Rect:
    def __init__(self, x, y, width, height):
        self._x, self._y, self._width, self._height = self.validate(x, y, width, height)
        self._right = self._x + self._width
        self._bottom = self._y + self._height


    def validate(self, x, y, width, height):
        x, y, width, height = self._to_digit(x, y, width, height)
        if width <= 0 or height <= 0:
            raise ValueError('некорректные координаты и параметры прямоугольника')
        return x, y, width, height
            
    def _to_digit(self, *args):
        for i in args:
            try:
                yield int(i)
            except:
                try:
                    yield float(i)
                except:
                    raise ValueError('некорректные координаты и параметры прямоугольника')

    def is_collision(self, rect):
        if not (self._right < rect._x or rect._right < self._x or self._bottom < rect._y or rect._bottom < self._y):
            raise TypeError('прямоугольники пересекаются')

    def __repr__(self):
        return " ".join(map(str, self.__dict__.values()))


s = '''0; 0; 5; 3
6; 0; 3; 5
3; 2; 4; 4
0; 8; 8; 1'''

s = s.split('\n')
lst_rect = [Rect(*i.split('; ')) for i in s]
lst_not_collision = []

for i in lst_rect:
    try:
        for j in lst_rect:
            if i != j:
                i.is_collision(j)
        lst_not_collision.append(i)
    except:
        pass

print(lst_not_collision)

r = Rect(1, 2, 10, 20)
assert r._x == 1 and r._y == 2 and r._width == 10 and r._height == 20, "неверные значения атрибутов объекта класса Rect"

r2 = Rect(1.0, 2, 10.5, 20)

try:
    r2 = Rect(0, 2, 0, 20)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при создании объекта Rect(0, 2, 0, 20)"


assert len(lst_rect) == 4, "список lst_rect содержит не 4 элемента"
assert len(lst_not_collision) == 1, "неверное число элементов в списке lst_not_collision"

def not_collision(rect):
    for x in lst_rect:
        try:
            if x != rect:
                rect.is_collision(x)
        except TypeError:
            return False
    return True

f = list(filter(not_collision, lst_rect))
assert lst_not_collision == f, "неверно выделены не пересекающиеся прямоугольники, возможно, некорректно работает метод is_collision"

r = Rect(3, 2, 2, 5)
rr = Rect(1, 4, 6, 2)

try:
    r.is_collision(rr)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове метода is_collision() для прямоугольников Rect(3, 2, 2, 5) и Rect(1, 4, 6, 2)"
