class Food:
    __attrs = ['_name', '_weight', '_calories']

    def __init__(self, *args):
        self.attrs = self.__attrs[:]
        if hasattr(self, '_attrs'):
            self.attrs.extend(self._attrs)

        for i, attr in enumerate(self.attrs):
            setattr(self, attr, args[i])
        delattr(self, 'attrs')


class BreadFood(Food):
    _attrs = ['_white']


class SoupFood(Food):
    _attrs = ['_dietary']


class FishFood(Food):
    _attrs = ['_fish']


bf = BreadFood("Бородинский хлеб", 34.5, 512, False)
sf = SoupFood("Черепаший суп", 520, 890.5, False)
ff = FishFood("Консерва рыбная", 340, 1200, "семга")

a = Food('apple', 100, 200)
print(a.__dict__)
b = BreadFood('orange', 100, 300, True)
print(b.__dict__)
sf = SoupFood("Черепаший суп", 520, 890.5, False)
