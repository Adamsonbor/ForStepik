class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        self.V = self.volume()


    @classmethod
    def is_valid(cls, var):
        return type(var) in (int, float) and cls.MIN_DIMENSION <= var <= cls.MAX_DIMENSION


    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, var):
        if self.is_valid(var):
            self.__a = var
            self.V = self.volume()


    @property
    def b(self):
        return self.__b

    @a.setter
    def b(self, var):
        if self.is_valid(var):
            self.__b = var
            self.V = self.volume()


    @property
    def c(self):
        return self.__c

    @a.setter
    def c(self, var):
        if self.is_valid(var):
            self.__c = var
            self.V = self.volume()


    def volume(self):
        return self.__a * self.__b * self.__c


    def __eq__(self, other):
        return self.V == other.V


    def __lt__(self, other):
        return self.V < other.V


    def __le__(self, other):
        return self.V <= other.V


    def __repr__(self):
        return str(self.V)


class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price 
        self.dim = dim
    
    def __repr__(self):
        return str(self.dim.V)


trainers = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
umbrella = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
fridge = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
chair = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
lst_shop = (trainers, umbrella, fridge, chair)
lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)
print(lst_shop_sorted)


