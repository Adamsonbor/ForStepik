class Triangle:
    def __init__(self, a, b, c):
        self._is_valid(a, b, c)
        self._a = float(a)
        self._b = float(b)
        self._c = float(c)

    def _is_valid(self, *args):
        if not all(type(i) in (int, float) for i in args) or not all(i > 0 for i in args):
            raise TypeError('стороны треугольника должны быть положительными числами')
        if args[0] > args[1] + args[2] or args[1] > args[0] + args[2] or args[2] > args[0] + args[1]:
            raise ValueError('из указанных длин сторон нельзя составить треугольник')

    def __repr__(self):
        r = 5
        out = []
        out.append(self.__class__.__name__)
        out.append(f"{' ' * r} *")
        for n in range(r):
            if n == r // 2 - 1:
                out.append(f"{self._a}{' ' * (r - n - len(str(self._a)))}* {' ' * n * 2}*  {self._b}")
            else:
                out.append(f"{' ' * (r - n)}* {' ' * n * 2}*")
        out.append(f"{'* ' * (r + 2)}")
        out.append(f"{' ' * r} {self._c}\n")
        return '\n'.join(out)


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
lst_tr = []
for i in input_data:
    try:
        lst_tr.append(Triangle(*i))
    except:
        pass
print(lst_tr)
