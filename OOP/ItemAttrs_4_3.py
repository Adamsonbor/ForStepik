class ItemAttr:
    def __getitem__(self, idx):
        values = list(self.__dict__.values())
        return values[idx]

    def __setitem__(self, idx, value):
        keys = list(self.__dict__.keys())
        self.__dict__[keys[idx]] = value
        
class Point(ItemAttr):
    def __init__(self, x, y):
        self.x = x
        self.y = y


a = Point(1, 2)
a[1] = 100
print(a[1])
# a = list(zip(['x', 'y', 'z'], [2,3,5]))
# print(a)
# print(list(zip(*a)))

