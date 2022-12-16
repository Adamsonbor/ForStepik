class Point:
    def __init__(self, x=0, y=0):
        # self._x, self._y = self.validate(x, y)
        self._x = x
        self._y = y

    def __repr__(self):
        return f"Point: x = {self._x}, y = {self._y}"

    def validate(self, *args):
        for i in args:
            try:
                yield int(i)
            except:
                try:
                    yield float(i)
                except:
                    raise ValueError("hello")


try:
    x, y = '1', '1.1'
    x = int(x)
    y = int(y)
    res = Point(x, y)
except Exception as e:
    try:
        x = float(x)
        y = float(y)
        res = Point(x, y)
    except:
        res = Point()
finally:
    print(res)
