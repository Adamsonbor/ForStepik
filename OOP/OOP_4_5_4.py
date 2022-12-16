class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    def __init__(self, name, weight, price):
        self.__id = id(self)
        self._name = name
        self._weight = weight
        self._price = price

    def get_id(self):
        return self.__id
