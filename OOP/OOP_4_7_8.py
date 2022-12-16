class Star:
    __slots__ = ('_name', '_massa', '_temp')

    def __init__(self, name, massa, temp):
        self._name = name
        self._massa = massa
        self._temp = temp


class SlotsMixin(Star):
    __slots__ = ('_type_star', '_radius')

    def __init__(self, name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius

    def __repr__(self):
        return f"{self._name} | {self._type_star}"


class WhiteDwarf(SlotsMixin, Star):
    __slots__ = tuple()

class YellowDwarf(SlotsMixin, Star):
    __slots__ = tuple()

class RedGiant(SlotsMixin, Star):
    __slots__ = tuple()

class Pulsar(SlotsMixin, Star):
    __slots__ = tuple()


d = {'RedGiant':RedGiant, 'WhiteDwarf':WhiteDwarf, 'YellowDwarf':YellowDwarf}
s = '''RedGiant: Альдебаран; 5; 3600; красный гигант; 45
WhiteDwarf: Сириус А; 2,1; 9250; белый карлик; 2
WhiteDwarf: Сириус B; 1; 8200; белый карлик; 0,01
YellowDwarf: Солнце; 1; 6000; желтый карлик; 1'''

stars = [d[i.split(': ')[0]](*i.split(': ')[1].split('; ')) for i in s.splitlines()]
white_dwarfs = list(filter(lambda x: isinstance(x, WhiteDwarf), stars))
stars[0]._a = 5
print(white_dwarfs)
        
