class Track:
    def __init__(self, *args):
        if all(type(i) in (int, float) for i in args):
            self.__points = [PointTrack(args[0], args[1])]

        if all(type(i) is PointTrack for i in args):
            self.__points = list(args)

    @staticmethod
    def is_Point(func):
        def wrapper(self, value):
            if type(value) != PointTrack:
                raise ValueError
            return func(self, value)
        return wrapper

    @is_Point
    def add_back(self, obj):
        self.__points.append(obj)

    @is_Point
    def add_front(self, obj):
        self.__points = [obj].extend(self.__points)

    def pop_back(self):
        out = self.__points[-1]
        del self.__points[-1]
        return out

    def pop_front(self):
        out = self.__points[0]
        del self.__points[0]
        return out

    @property
    def points(self):
        return self.__points



class PointTrack:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __setattr__(self, key, value):
        if type(value) not in (int, float):
            raise TypeError('координаты должны быть числами')
        object.__setattr__(self, key, value)

    
    def __str__(self):
        return f"PointTrack: {self._x}, {self._y}"


a = Track(1, 2)

tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)
