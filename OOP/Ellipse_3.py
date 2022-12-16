class Ellipse:
    def __init__(self, *args):
        if len(args):
            self.x1, self.y1, self.x2, self.y2 = args

    
    def get_coords(self):
        if self:
            return self.x1, self.y1, self.x2, self.y2
        else:
            raise AttributeError('нет координат для извлечения')


    def __bool__(self):
        return hasattr(self, x1) and hasattr(self, x2) and hasattr(self, y1) and hasattr(self, y2)


    def __repr__(self):
        return ' '.join(map(str, self.__dict__.values()))


lst_geom = [Ellipse() if i < 2 else Ellipse(1, 1, 1, 1) for i in range(4)]
print(lst_geom)

