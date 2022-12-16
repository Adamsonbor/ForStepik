class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        pass


    @classmethod
    def register(cls, obj):
        obj.cb = cls

    @classmethod
    def __rates(cls, rates):
        cls.rates = "hello"


class Money:
    __EPS = 0.1

    def __init__(self, volume, name):
        self.__cb = None
        self.__volume = volume
        self.__name = name


    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, obj):
        if obj is CentralBank:
            self.__cb = obj


    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        if type(volume) in (int, float):
            self.__volume = volume


    @property
    def name(self):
        return self.__name

    
    def __is__valid(self, other):
        if not other.cb and not self.cb:
            raise ValueError("Неизвестен курс валют.")
        else:
            return True

    
    def ru_equivalent(self):
        if self.name == 'rub':
            return self.volume
        return self.volume * self.cb.rates[self.name] * self.cb.rates['rub']


    def __eq__(self, other):
        self.__is__valid(other)
        return abs(self.ru_equivalent() - other.ru_equivalent()) < self.__EPS
    

    def __lt__(self, other):
        self.__is__valid(other)
        return self.ru_equivalent() < other.ru_equivalent()


    def __le__(self, other):
        self.__is__valid(other)
        v1 = self.ru_equivalent()
        v2 = other.ru_equivalent()
        return v1 < v2 or abs(v1 - v2) < self.__EPS



class MoneyR(Money):
    def __init__(self, volume=0):
        super().__init__(volume, 'rub')


class MoneyD(Money):
    def __init__(self, volume=0):
        super().__init__(volume, 'dollar')
        

class MoneyE(Money):
    def __init__(self, volume=0):
        super().__init__(volume, 'euro')

CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(100)
e = MoneyE(100)

CentralBank.register(r)
CentralBank.register(d)
CentralBank.register(e)
print(r.ru_equivalent())
print(d.ru_equivalent())
print(e.ru_equivalent())

if r > d:
    print("неплохо")
else:
    print("нужно поднажать")

