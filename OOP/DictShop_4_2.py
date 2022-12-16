class Thing:

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight



class DictShop(dict):
    
    def __init__(self, things=dict()):
        self._is_valid(things)
        super().__init__(things)


    def _is_valid(self, things):
        if type(things) != dict:
            raise TypeError('аргумент должен быть словарем')
        if not all(type(i) is Thing for i in things):
            raise TypeError('ключами могут быть только объекты класса Thing')

    
    def _is_thing(self, key):
        if not isinstance(key, Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')

    
    
    def __setitem__(self, key, value):
        self._is_thing(key)
        super().__setitem__(key, value)



a = DictShop()
b = Thing('hello', 2123, 100)
a[(1,2)] = b
print(b)
